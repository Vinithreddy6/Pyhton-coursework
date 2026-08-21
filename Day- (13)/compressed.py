s="aaaaaaaaaasssssssssssdddddccctttaaaa"
n =len(s)-1
count=1
result=''
for i in range(n):
    if s[i]==s[i+1]:
        count+=1
    else:
        result+=s[i]+str(count)
        count=1
result+=s[i]+str(count)
print(result)           






