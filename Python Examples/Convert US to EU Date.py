'''
You and your friends are going to Europe! You have made plans to travel around Europe with your friends, but one thing you need to take into account so that everything goes according to play, is that the format of their date is different than from what is used in the United States. Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY.

Task: 
Create a function that takes in a string containing a date that is in US format, and return a string of the same date converted to EU.

Input Format: 
A string that contains a date formatting 11/19/2019 or November 19, 2019.

Output Format: 
A string of the same date but in a different format: 19/11/2019.

Sample Input: 
7/26/2019

Sample Output: 
26/7/2019
Note, that the input can be in two different formats, 11/19/2019 or November 19, 2019.



'''
'''
# Month conversion dictionary
dic = {'January':'1','February':"2","March":"3","April":"4","May":"5","June":"6",
        "July":"7","August":"8", "September":"9","October":"10","November":"11",
        "December":"12"}
# Date input
a = str(input())
if len(a) == 10:
    a = a.split('/')    
    x = a[1]
    y = a[0]
    z = a[2]
else:
    a = a.split()
    x = a[1].replace(',','')
    y = dic.get(a[0])
    z = a[2]
print('{}/{}/{}'.format(x, y, z))

# With this code you can define any other format of date formatting, defining the values of x,y and z.

'''



c=input()
if len(c)<=10:
    d=c.split("/")
    print(d[1]+"/"+d[0]+"/"+d[2])
else:
    e=c.split(",")
    h=e[1]
    i=h.split(" ")
    f=e[0]
    g=f.split(" ")
    if g[0]=="January":
        x=g[0].replace('January','1')
    elif g[0]=="February":
        x=g[0].replace('February','2')
    elif g[0]=="March":
        x=g[0].replace('March','3')
    elif g[0]=="April":
        x=g[0].replace('April','4')
    elif g[0]=="May":
        x=g[0].replace('May','5')
    elif g[0]=="June":
        x=g[0].replace('June','6')
    elif g[0]=="July":
        x=g[0].replace('July','7')
    elif g[0]=="August":
        x=g[0].replace('August','8')
    elif g[0]=="September":
        x=g[0].replace('September','9')
    elif g[0]=="October":
        x=g[0].replace('October','10')
    elif g[0]=="November":
        x=g[0].replace('November','11')
    elif g[0]=="December":
        x=g[0].replace('December','12')
    print(g[1]+"/"+x+"/"+i[1])