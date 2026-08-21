#fa=eval(input("Follows account:"))
#if fa:
#    cf=eval(input("close frnd:"))
#     if cf:
#        print("story visible")
#    else:
#        print("not in close friend list")
#else:
#   print("follow the accountfirst") 



#reg=eval(input("registered"))
#if reg:
#    fee = eval(input("fee paid"))
#    if fee:
#        print("tournment entry confirmed")
#    else:
#        printff("Enter fee pending")    
#else:
#    printf("registeratuion required")

data={
    'lohitha':{'status':True,'python':90,'mysql':95,'flask':98},
    'dipak':{'status':False,'python':None,'mysql':None,'flask':None},    
    'teja':{'status':True,'python':20,'mysql':35,'flask':38},
    'dinesh':{'status':True,'python':60,'mysql':75,'flask':78},
    'usharani':{'status':True,'python':80,'mysql':75,'flask':88},
    }
name=input("enter the name:")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f"hello{name}!!!")
        print(f"your average score is {avg}")
        if avg>=90:
            print("out standing performance")
        elif avg>=80:
            print("very good")
        elif avg>=70:
            print("good, work hard")
        elif avg>=40:
            print("weak , work hard")
