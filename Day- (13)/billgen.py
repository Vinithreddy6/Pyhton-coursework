data={
    'sugar': 20,
    'milk': 30, 
    'bread': 15,
    'eggs': 10,
    'rice': 50,
    'butter': 25,
    'peanuts': 100
}
for i in data:
    print(i.ljust(20),data[i]) 
prod=list(map(str,input("Enter items you want to buy:").split()))
print("---------------bill----------------")
bill=0
for i in prod:
    print(i.ljust(20),data[i]) 
    bill+=data[i]
print("Total bill:",bill)
