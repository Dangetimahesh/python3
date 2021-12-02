def status(marks):
    if marks>=35:
        s='p'
    else:
        s="F"
    return s
def find_grade(marks):
    if marks>=75:
        g="A+"
    elif marks >=60:
        g="A"
    elif marks>=50:
        g="B"
    else :
        if status(marks)=='F':
          g='F'
        else :
         g='C'
    return g
def b1_count(s1,s2,s3,s4,s5,s6):
    c=0
    if stastus(s1)=='F':
        c+=1
    if stastus(s1)=='F':
        c+=1
    if stastus(s1)=='F':
        c+=1
    if stastus(s1)=='F':
        c+=1
    if stastus(s1)=='F':
        c+=1
    if stastus(s1)=='F':
        c+=1
    return c
def find_per(s1,s2,s3,s4,s5,s6):
    res=s1+s2+s3+s4+s5+s6
    return res
def find_per(total):
    return total//6
s1,s2,s3,s4,s5,s6=map(int(input().split())
print("english",s1,100,status(s1),find_grade(s1))
print("telugu",s2,100,status(s2),find_grade(s2))
print("hindi",s3,100,status(s3),find_grade(s3))
print("maths",s4,100,status(s4),find_grade(s4))
print("science",s5,100,status(s5),find_grade(s5))
print("social",s6,100,status(s6),find_grade(s6))
total=find_total(s1,s2,s3,s4,s5,s6)
per=find_per(total)
print(b1_count(s1,s2,s3,s4,s,s6),total,per)                      
