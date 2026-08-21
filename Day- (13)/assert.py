email=''
password=''
amount=-2000
assert amount>0, "Amount cannot be negative"
assert email!='' and password!='', "Email and password cannot be empty"
#assert statement is used to check if a condition is true or not. If the condition is true, the program continues to execute. If the condition is false, an AssertionError is raised with an optional error message. It is commonly used for debugging and testing purposes to catch errors early in the development process.