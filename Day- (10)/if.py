sales = int(input("Enter the sales: "))
if sales>1000:
    print("Best seller")

eli_account = eval(input("Eleigible account: "))
ver_account = eval(input("meta verified subscription: "))

if eli_account and ver_account:
    print("verified badge granted")