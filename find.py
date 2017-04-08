import re
#help(re)

for i in dir(re):
    print(i)
#help(re.match)
#But we use mymatch
#mymatch=re.search('iig','called piig')
def Find(pat,text):
    mymatch=re.search(pat,text)
    if mymatch:
        print(mymatch.group())
    else:
        print("Not Found")
print(" ")
Find("Hello!","text Hello!World") 
#special characters
# for find any char we can use .(dot)
print(" ")
Find('...g',"called piiig")
print(" ")
#This .(dot ) fails  in case pat='...g' and text="called piiig   much better:xyz"
#Find('...g',"called piiig   much better:xyz")
#To find special characters
Find(r'...\$',"Bash$ is in Windows")
print(" ")
# Now we move to word char "\w "  and \d .it match word or  number 
Find(r'\w\w\d \w\w\w\w','blah :cat blah blah more than 100 times')