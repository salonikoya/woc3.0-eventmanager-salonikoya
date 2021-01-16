class Participant:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


par=[]
parChoice='y'
c='y'
while parChoice=='y':
    print("Enter name")
    name=input()
    contact = []
    print("Enter contact")
    ct=input()
    contact.append(ct)
    print("Do you want to enter contact number?(y/Y")
    c = input()
    while c=='Y' or c=='y':
            print("Enter contact")
            ct = input()
            contact.append(ct)
            print("Do you want to enter contact number?(y/Y")
            c = input()
    p = Participant(name, contact)
    par.append(p)
    print("Do you want to enter participant?(y/Y)")
    parChoice = input()

par.sort(key=lambda x: x.name)
for x in par:
     print(x.name)
     for y in x.contact:
      print(y)

autocomplete=[]
print("Search by name")
print("Enter name")
sn=input()


for x in par:
    if sn in x.name:
        print(x.name)
    if sn==x.name:
        print(x.contact)




