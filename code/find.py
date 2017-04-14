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
# space
Find(r'\d\s+\d\s','1 2 3')
Find(r'\d\s\d\d\d\d+\s+\w....n','2016 2015 python 3.0')#here '+' is greedy
#Non-white-space
Find(r'\S+',"blahblah 1234,blah blahblah1")
Find(r'\w+@\w+.+\s','xyz@gmail.com xvtyu@yahoo.com')#here '+' is greedy
Find(r'[\w]+@\w+.+\s','xyz@gmail.com xvtyu.123@yahoo.com')
r=Find(r'([\w]+)+@([\w.]+)','xyz@gmail.com xvtyu.123@yahoo.com')
y=re.search(r'([\w]+)+@([\w.]+)','xyz@gmail.com xvtyu.123@yahoo.com')
y1=print(y.group(1))
y1
y2=print(y.group(2))
y2
#re.Findall
o=re.findall(r'([\w]+)+@([\w.]+)','xyz@gmail.com xvtyu.123@yahoo.com alex@python.org')
print(o,type(o))

