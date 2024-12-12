if (__name__=="__main__"):
    def change_to_be_given(change,i):
        denominations=[2000,500,200,100,50,20,10,5,2,1]
        if(i<len(denominations)-2):
            n=int(change/denominations[i])
            if(n!=0):
                change=change-(n*denominations[i])
                if(n==1):
                    print(f"give 1 change of Rs.{denominations[i]}")
                else:
                    print(f"give {n} changes of Rs.{denominations[i]}")
            i=i+1
            change_to_be_given(change,i)
        elif(i==len(denominations)-2):
            if(change>1 or change==1):
                print(f"give a Rs.1 coin")
                change=change-1
        elif(i==len(denominations)-1):
            if(change==0):
                print("No change Left")
            else:
                print(f"Remaining change is {change}")
    a=0
    b=1
    c="y"
    def ask_for_input():
        global a 
        global b
        a=input("Enter the amount given by the customer: ")
        while(a.isdigit()==False):
            print("Enter a valid input")
            a=input("Enter the amount given by the customer: ")
        b=input("Enter the amount of order: ")
        while(b.isdigit()==False):
            print("Enter a valid input")
            b=input("Enter the amount of order: ")
    change="Placeholder"
    if(change=="Placeholder"):
        ask_for_input()
        change=float(a)-float(b)
        while(change<0):
            print("Order is not possible")
            d=0
            while(d==0):
                c=input("Do you want to order again?(y/n): ")
                if(c=="y"):
                    ask_for_input()
                    change=float(a)-float(b)
                    d=1
                elif(c=="n"):
                    d=1
                    change=0
                    break
                else:
                    print("Enter a valid input")
    if(c=="y"):
        change_to_be_given(change,0)
    print("Thank you from shopping from us. Have a good day :)")
    input()