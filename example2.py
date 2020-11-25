import goslate
gs=goslate.Goslate()
f1=open(r"find_words.txt","r+")
f2=open(r"french.txt","w+")
for x in f1:
    newtext=gs.translate(x,'fr')
    f2.write(newtext+"\n")
print("Done")