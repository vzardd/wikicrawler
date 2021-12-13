import urllib.request,urllib.parse,urllib.error
import re
#function to filter sentences
def trim(line):
    sublst=re.findall("<.+?>",line)
    for sub in sublst:
        line=line.replace(sub,"")
    sublst=re.findall("[&]\S+",line)
    for sub in sublst:
        line=line.replace(sub,"")
    sublst=re.findall("/.+;",line)
    for sub in sublst:
        line=line.replace(sub,"")
    sublst=re.findall("\S+[a-z][0-9]\S+?",line)
    for sub in sublst:
        line=line.replace(sub,"")
    return line
print(118*"-"+"\n"+55*" "+"WIKICRAWLER"+"\n"+118*"-")
while True:
    #enter something to search
    name=str(input("\nEnter Something to know about - "))
    print()
    name=name.split()
    for i,x in enumerate(name):
        name[i]=x.capitalize()
    name="_".join(name)
    url="https://en.wikipedia.org/wiki/"+name
    try:
        uh=str(urllib.request.urlopen(url).read())
    except:
        url="https://en.wikipedia.org/wiki/Cls"
        uh=str(urllib.request.urlopen(url).read())
    strlst=re.findall("<p>(.+?)</p>",uh)
    if len(strlst)<2:
        print("\nNo results found! Check your input...")
        continue
    for i,p in enumerate(strlst):
        print(trim(p),end=" ")
        if i==1:
            break
    print()
input()

