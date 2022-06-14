
#Mary is planning a party on Sunday, so on Monday, she started to create a list of things she needed to do.
#First, she thought of the food she wanted to have and she created a list named ‘food” and added the following items:

partyList = list =["pizza", "soda", "chips", "carrots", "celery", "cheese" ]
print("---------------------party list----------------------")
print("")
print(partyList)

#Then, she thought of the decorations she wanted to buy and added to the list:

addList1=list=("balloons", "helium", "cake")
partyList.extend(addList1)
print("")
print("---------------------party list + decorations----------------------")
print("")
print(partyList)

#She then decided that it would be a good idea to sort the list in alphabetical order, so she did.

partyList.sort()
print("")
print("---------------------party list alphabetical----------------------")
print("")
print(partyList)

#On Tuesday, she realized that she needed to get some nice clothes for her party, so she added to the list a dress, a purse and shoes.

addList2 = list = ("dress", "purse", "shoes")
partyList.extend(addList2)
print("")
print("---------------------party list + clothes----------------------")
print("")
print(partyList)

#On Wednesday, she thought that she should organized the list by places that she needed to go to get all the things, so the put
#everything that she could buy in a grocery store first, then everything she needed to get from the party store, and last,
#everything she could get at a department store.

print("")
print("---------------------party list ordered----------------------")
print("")
partyList.pop(0)
partyList.pop(5)
partyList.pop(-4)
partyList.insert(6, "helium")
partyList.insert(7, "balloons")
partyList.insert(3, "soda")

print(partyList)

#She decided that she was going to split the shopping into 2 days, because it was too much to do all every day, so she made two new lists.
#One named: “Thursday” and one named “Friday”.
#On Thursday she was going to buy everything that was food, and on Friday she was going to get everything that wasn’t food.

print("")
print("----------------------thursday---------------------")
print("")
Thursday = partyList.copy()
del Thursday [7:12]
print(Thursday)
Friday = partyList.copy()
print("")
print("----------------------friday---------------------")
print("")
del Friday [0:7]
print(Friday)

#Then, her friend Ana called her and said she found out she is allergic to cheese, so Mary decided to change the menu. 
#Instead of Pizza and Cheese she replaced them with Soup and Breadsticks.

print("")
print("---------------------dairy-free Thursday----------------------")
print("")
Thursday.pop(-1)
Thursday.pop(-2)
Thursday.insert(3, "soup")
Thursday.insert(4, "breadsticks")
print(Thursday)


#She went shopping on Thursday and found eveything but carrots, soda and cake.
#So, she deleted all other items from the Thursday list,

print("")
print("---------------------shopped Thursday----------------------")
print("")
Thursday.pop(2)
Thursday.pop(3)
Thursday.pop(4)
Thursday.pop(-1)
print(Thursday)

#added the Thursday list to the Friday list,

Friday.extend(Thursday)
print("")
print("---------------------combined Thursday and Friday----------------------")
print("")
print(Friday)

#and deleted the Thursday list.

del Thursday

#On Friday she bought everything else, so her list ended up being empty.

Friday.clear()
print("")
print("---------------------cleared friday----------------------")
print("")
print(Friday)

#The party was EPIC!