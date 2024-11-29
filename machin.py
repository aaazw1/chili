from regex import *
from PyPDF2 import *
name1=[]
textT=""
text=""
reader = PdfReader("nomina-ppt.pdf")
nbpage=4
for nbpage in range(len(reader.pages)):
#for nbpage in range(1):
    page = reader.pages[nbpage]
    text=page.extract_text()
    textT=textT+page.extract_text()
#print(text)
    words_pattern = '[a-zA-ZÁíéúñóá]+'
    output = findall(words_pattern, text)
    name1=name1+output
print("1")
K = "K"
while(K in name1):
    name1.remove(K)
print("2")
#while(RUN in name1):
    #name1.remove(RUN)
for loop in range(10):
    name1.remove(name1[0])
for loop in range(10):
    name1.remove(name1[-1])
print(name1)
RUN='RUN'
nameF=[]
loop=0
merge=''
for loop in range(len(name1)):
    cond=1
    if name1[loop]==RUN:
        cond=0
    else:
        merge=merge+' '+name1[loop]
    if cond==0:
        nameF.append(merge)
        merge=""
        
print(nameF)
for loop in range(len(namef)):
    namenow=nameF[loop]
    sleep(5)