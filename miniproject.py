m = {"hard candy":  {"chocolate": 5,  "vanilla": 5, "coffee": 5, "strawberries": 5, "orange": 5},
     "chewy candy": {"chocolate": 5,  "lychee": 5,   "lemon": 5,  "orange": 5, "strawberries": 5},
     "soft candy":  {"chocolate": 20, "vanilla": 20, "strawberries": 15, "mixed fruit": 10}
     }
def password():
    usr = []
    pwd = []
    print("***Please apply account***")
    print("Create a new account")
    usr.append(input("please youre username:"))
    pwd.append(input("please youre password:"))
    print("." * 50)
    print("***welcome***")
    loop = 'true'
    while(loop == 'true'):
        username = input("Please User: ")
        password = input("Please Pass: ")
        if(username == usr[0] and password == pwd[0]):
            print ('Successful login  ' + username)
            def catalog():
                print("***welcome to the candyshop***")
                print("{:20} {}".format("Category", "The taste and Price"))
                for a, b in m.items():
                    print("{:20}".format(a), end="")
                    print(b)
                print("." * 50)
                print("Promotion")
                print("buy 40 up baht Discount 10%")
                print("." * 50)
            catalog()
            def buy():
                p1 = []
                p2 = []
                p3 = []
                p4 = []
                p5 = []
                total = 0
                key = 1
                while key == 1:
                    key2 = 1
                    while key2 == 1:
                        a = input("Select your Candy type :").lower().strip()
                        b = input("Select your Candy taste :").lower().strip()
                        if a not in ["hard candy", "chewy candy",'soft candy']:
                            print('Please make the list correctly.')
                        elif b not in ['chocolate', 'vanilla','coffee','lychee', 'lemon','orange','strawberries',
                                    'mixed fruit']:
                            print('Please make the list correctly.')
                        else:
                            key2 = 2
                    j = input("How many pieces do you need ? :")
                    n = m[a][b]
                    k = int(n)*int(j)
                    p1.append(a)
                    p2.append(b)
                    p3.append(n)
                    p4.append(j)
                    p5.append(k)
                    total += int(n)*int(j)
                    c = input("Choose to continue? (y/n) :")
                    if c.upper() == "N":
                        key = 2
                if total >= 40:
                    d = (10/100*total)
                    e = total - d
                    print("-" * 50)
                    print('CP ALL Candyshop Mae Ka(M.Phayao)')
                    print('***Receipt / Tax Invoice Summary***')
                    print('****Category \t The taste \t Price****')
                    for i in range(len(p1)):
                        print("\t{} \t {} \t  {}".format(p1[i],p2[i],p5[i]))
                    print("Discount = {}".format(d))
                    print("Total = {}".format(e))
                    c = input("Want to receive plastic bags ? (y/n)")
                    if c == "y":
                        print("All products are in plastic bags.")
                    else:
                        print("Thank you for not accepting plastic bags.")
                    key1 = 1
                    while key1 == 1:
                        Pay = int(input("receive money : "))
                        if Pay < total:
                            print("Please enter the correct amount")
                        else:
                            key1 = 2
                    x = Pay - e
                    print("change = ", x, "Baht")
                    print("-" * 50)
                else:
                    print("-" * 50)
                    print('CP ALL Candyshop Mae Ka(M.Phayao)')
                    print('***Receipt / Tax Invoice Summary***')
                    print('****Category \t The taste \t Price****')
                    for i in range(len(p1)):
                        print("\t{} \t {} \t  {}".format(p1[i],p2[i],p5[i]))
                    print("Total = {} Baht".format(total))
                    c = input("Want to receive plastic bags ? (y/n)")
                    if c == "y":
                        print("All products are in plastic bags.")
                    else:
                        print("Thank you for not accepting plastic bags.")
                    key1 = 1
                    while key1 == 1:
                        Pay = int(input("receive money : "))
                        if Pay < total:
                            print("Please enter the correct amount")
                        else:
                            key1 = 2
                    x = Pay - total
                    print("change = ", x, "Baht")
                    print("-" * 50)
            buy()
            loop = 'false'
            loop1 = 'true'
            while (loop1 == 'true'):
                command = input(username + ">> ")
                if (command == "exit"):
                    print('Log out successfully')
                    print('Thank you for Use of service')
                    break
                else:
                    print("'" + command + "' คำสั่งผิด!")
        else:
            print('Wrong password')
password()
