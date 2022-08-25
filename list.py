from ast import Continue
import json
import os.path

def main():
    os.system('clear')
    # if json db does not exist create one
    if os.path.exists('stores.json') == False: 
        file = open("stores.json", "w")
        file.write('[]')
        file.close()
    
    options = input("Welcome to the Main Menu!\n0 : Create an efficient grocery list\n1 : Register a store\n0/1 : ")
    if(options == '0'):
        makeList()
    else:
        registerStore()
        
def registerStore():
    os.system('clear')
    store_name = input("Enter the name of the store: ")
    new_store = {"store_name": store_name}
    
    os.system('clear')
    print("Enter the aisle names and their row number\n")

    file = open("stores.json", "r")
    content = file.read()
    stores = json.loads(content)
    
    aisle_name = ''
    while(True):
        aisle_name = input("Category: ")
        number = input("Row: ")
        new_store[number] = aisle_name
        if input("Continue? y/n: ") == "n":
            break
        print("\n")

    stores.append(new_store)
    
    json_obj = json.dumps(stores, indent=4)

    file = open("stores.json", "w")
    file.write(json_obj)

    file.close()
    main()

def makeList():
    os.system('clear')
    file = open("stores.json", "r")

    content = file.read()
    stores = json.loads(content)
    for idx,store in enumerate(stores):
        print(idx , ":" , store['store_name'])
    choice = input("Choose a Store: ")

    os.system('clear')
    store = stores[int(choice)]
    
    print("\n" + store['store_name'] + " has aisles: ")
    aisles = ""
    for aisle in sorted(store.keys()):
        num = store[aisle]
        if(aisle != "store_name"):
            aisles += aisle + ": "+ num + "\n"
    print(aisles)
    print("Enter your items and it's category\n")
    shopping_list = {}
    while(True):
        item_name = input("Item: ")
        number = input("Row: ")
        if number in shopping_list:
            shopping_list[number].append(item_name)
        else:
            shopping_list[number] = [item_name]
        
        if input("Continue? y/n: ") == "n":
            break
        print("\n")
    
    # Making the list 
    orderedList = ""
    for row in sorted(shopping_list.keys()):
        for item in shopping_list[row]:
            orderedList += item + "\n"
    
    os.system('clear')

    file_name = input("Name your file: ") + ".txt"
    file = open(file_name, "w")
    file.write(orderedList)
    file.close()

if __name__ == "__main__":
    main()




