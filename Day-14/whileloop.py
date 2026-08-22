
'''s='wile loop'

i=len(s)-1
while i>=0:
    print(s[i])
    i-=1

l=[5,4,6,7]
i=0
while i<len(l):
    print(l[i])
    i+=1
    
#Sum and Product of digits of a number:
n=8765
sum=0
prod=1
while n>0:
    sum=sum+n%10
    prod*=n%10
    n//=10
print("Sum of digits:", sum)
print("Product of digits:", prod)

#Reverse of digits:
n=3456
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print("Reverse of digits:", rev)


  


n=3456
res=0
while n>0:
    rem=n%10
    if rem%2==0:
        res+=rem
    n//=10
print("Sum of even digits:", res)   


l=[4,5,6,7,0,0,4,0,6]
while 0 in l:
    l.remove(0)
print(l)'''


l=[2,3,4,56,77]
sum=[]
i=0
j=len(l)-1
while i<j:
    print(l[i]+l[j])   
    i+=1
    j-=1
    if i==j:
        print(l[i])   

      

 





