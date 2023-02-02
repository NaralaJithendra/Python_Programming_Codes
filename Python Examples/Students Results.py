'''
Students Results
ABS School wants good SSLC results in the next upcoming year. So they wanted to prepare students who passed the 9th standard final exam. The education department of the school decided to give free SSLC coaching to students. Headmaster told the class teacher to shortlist the students who passed and failed in the final exam of the 9th standard. Now she wants to create new students list who passed and failed the final exam.
     
Help her to create new student lists. If the student mark is less than 40 then he is failed otherwise he is passed.

Problem Constraints:
Use Nested Dictionary store students details like d = { "pass" : {Roll No: mark } , "fail" : {Roll No: mark }} .


Input format:
1st input indicates a number of students.
Next lines of input indicate marks of students(Marks entered according to Roll No, Roll  No starts from 1).

Output format:
The output indicates Roll No and marks of students who failed and passed (Refer sample input-output format).
All text in bold corresponds to the input and the rest corresponds to output.

Sample Input and Output 1:
5
78
39
45
35
89
Students who failed in Final Exam
Roll No: 2 - Mark: 39
Roll No: 4 - Mark: 35
Students who passed in Final Exam
Roll No: 1 - Mark: 78
Roll No: 3 - Mark: 45
Roll No: 5 - Mark: 89

Sample Input and Output 2:
6
41
67
45
80
89
67
All are passed

Sample Input and Output 3:
6
39
37
35
30
29
17
All are failed
'''
a=int(input())
l=[]
df={}
dp={}
for i in range(a):
    l.append(int(input()))
for i in range(len(l)):
    if(l[i]<40):
        d1={i:l[i]}
        df.update(d1)
    else:
        d2={i:l[i]}
        dp.update(d2)
print(dp)
print(df)
print(len(df))
print(len(dp))
if(len(df)==a):
    print("All are failed")
elif(len(dp)==a):
    print("All are passed")
else:
    print("Students who failed in Final Exam")
    for i in df:
        print("Roll No: "+str(i+1)+" - Mark: "+str(df[i]))
    print("Students who passed in  Final Exam")
    for i in dp:
        print("Roll No: "+str(i+1)+" - Mark: "+str(dp[i]))