#STAGE 1
num_people = int(input("enter the number of friends joining (including you):\n"))
print("")
if num_people <= 0:
    print ("no one is joining for the party")
else:
    dictionary = {}
    print("\nenter the name of every friend (including you), each on anew line:")
    for i in range (num_people):
        name = input()
        dictionary[name] = 0
        print ()
        print (dictionary)



#STAGE 2
def thebills():
final_bill = float(input("enter the total bill value :\n"))
split_amount = round(final_bill / num_people, 2)
for name in dictionary:
  dictionary[name] = split_amount
  print (dictionary)

  num_people = int(input("enter the number of friends joining (including you):\n"))
  print ("")

  if num_people <= 0:
      print("no one is joining for the party")
  else:
      print("enter the name of every friend (including you), each on a new line:\n")
      dictionary = ()
      for i in range (num_people):
          name = input()
          dictionary[name] = 0
          print()
          thebills()


#STAGE 3
def thebills():
    final_bill = float(input("enter the total bill value:\n"))
    split_amount = round(final_bill / num_people, 2)
    for name in dictionary :
        dictionary[name] = split_amount


    num_people = int(input("enter the number of friends joining(including you):\n"))
    print("")

    if num_people <= 0:
        print("no one is joining for the party")
    else:
        print("enter the name of every friend  (including you), each one on a new line:\n")
        dictionary = {}
        for i in range(num_people):
            name = input()
            dictionary [name] = 0
            print ()
            thebills()
            print()
            use_lucky_feature = input("do you want to use the 'who is lucky?' feature? (yes/no): \n")
            if use_lucky_feature == "yes":
                lucky_friend = random.choice(list(dictionary.keys()))
                print("")
                print (f"{lucky_friend} is the lucky one!")
            else :
                print("")
                print("no one is going to be lucky")



#STAGE 4
number_friends = int(input("enter the number of friends joining (including you):\n"))
print("")
if number_friends <= 0:
    print("no one is joining for the party") 
else:
    print("\nenter the name of every friend (including you), each on anew line:")
    dictionary = {}
    for _ in range(number_friends):
        name_friend = input()
        dictionary[name_friend] = 0
        print ("")
        total_bill = float(input("enter the total bill value :\n"))
        split_bill = round(total_bill / number_friends, 2)
        for name in dictionary:
            dictionary [name] = split_bill
            print("")

            lucky_feature = input("do you want to use the 'who is lucky?' feature? (yes/no): \n")  
            if lucky_feature == "yes":
                lucky_one = random.choice(list(dictionary.keys())) 
                print("") 
                print(f"(lucky_one) is the lucky one!")
                print ("") 
                dictionary[lucky_one] = 0
                total_friends = number_friends - 1
                split_value = round(total_bill / total_friends, 2) 
                for name in dictionary:
                    if name != lucky_one:
                        dictionary[name] = split_value
                    else:
                        print("no one is going to be lucky")
                        print()

                        print(dictionary)   
