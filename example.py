from googletrans import Translator
import fileinput
import time

dict = {}

try:
    translator = Translator()
    print(translator.translate("Hello",src='en',dest='fr').text)
    f = open('french.txt','a')
    for line in fileinput.input('find_words.txt'):
        if(line != '\n'):
            word = line.strip()
            dict[word] = translator.translate(word,dest='fr').text
            print(word+' - '+dict[word])
            f.write(word+'-'+dict[word]+'\n')
            time.sleep(0.5)
    f.close()
except:
    print("This is VS Code") 