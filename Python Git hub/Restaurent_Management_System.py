def create_order():
    from datetime import datetime
    m=list(Menu)
    ch=int(input("\nEnter Item Number of The Choice from The Menu: "))
    ch=ch-1
    q=int(input("Enter The Quantity: "))
    if q<=0:
        print("Please Enter A Valid Quantity!")
    else:
        available=input(f"Is {m[ch]} Available ? ").strip().lower()
        if available in ["yes","y",""]:
            date=datetime.today().strftime("Date: %d-%m-%y")
            order.append(f"{date} Item: {m[ch]} & Price: {Menu[m[ch]]} X Quantity: {q}")
            payment_amount.append(Menu[m[ch]]*q)
        else:
            print(f"Sorry! {m[ch]} is not Available Right Now...")
if __name__=="__main__":
    import sys
    import os
    import time
    Menu={
        "Chicken Biriyani":150,
        "Mutton Biriyani":250,
    }
    j=1
    order=[]
    payment_amount=[]
    for i in Menu:
        print(f"Item-{j}: {i} = {Menu[i]}Rs")
        j+=1
    create_order()
    while True:
        more=input("\nDo You Want to Enter More Choices? ").strip().lower()
        if more in ["yes","y",""]:
            create_order()
        elif more=="x":
            break
        else:
            break
    summery=""
    for i in order:
        summery=summery+i+";"
    print("\nOrder Summery:\n",summery)
    print("Payable Amount:",sum(payment_amount))
    print("\nProceed To Pay => [PRESS: 'y' or TYPE: 'yes' or PRESS: Enter Key]\nCancel Order => [PRESS: 'x']")
    proceed=input("\nEnter Your Operation: ").strip().lower()
    if proceed in ["yes","y",""]:
        customer_name=input("Enter Customer Name: ")
        customer_ph=input("Enter Customer Contact Number: ")
        pay=input("Payment Done? (yes/no)").strip().lower()
        if pay in ["yes","y",""]:
            print(f"Order Placed for \n{summery} & Payment of Rs: {sum(payment_amount)} is Done!")
            with open("orders.txt","a") as file:
                file.write(f"Customer Name: {customer_name}; Items: {summery} Contact No: {customer_ph}; Payment Amount: {sum(payment_amount)}; Payment Status: Success\n")
            time.sleep(3)
            order.clear()
            payment_amount.clear()
            os.system("cls")
            sys.exit()
        else:
            print("Order Cancelled!")
            time.sleep(3)
            order.clear()
            payment_amount.clear()
            os.system("cls")
            sys.exit()
    elif proceed=="x":
        print("Order Cancelled!")
        time.sleep(3)
        order.clear()
        payment_amount.clear()
        os.system("cls")
        sys.exit()
    else:
        print("Invalid Input!")
        time.sleep(3)
        os.system("cls")
        sys.exit()