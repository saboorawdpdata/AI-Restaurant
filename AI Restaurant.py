print("*****Welcome to AI Restaurant*****")

name=input("Enter your Name:")
budget=eval(input("Enter your Budget:"))


csne=int(input(f"Dear {name}\nSelect Any One From Below! \n1. Pakistani \n2. Chinese \n3. Italian \n4. Korean \n5. Thai \n6. Dont Know, Suggest Something Special"))

if csne==1:
    print("Welcome to Pakistani Cuisine")
    if budget>=15000:
        fav=int(input(f"Dear {name}, \nWhat you like the most in normal days? \n1. Biryaani \n2. Karahi \n3. Creamy Handi \n4. BBQ \n5. All of the above?"))
        if fav==1:
            bill=8500
            print(f"Dear {name}, \nHave Your Special Mandi Platter with Shamas special dumpukt! along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad \nYour Total Bill is {bill} Rs:8500/- (including tax)")
            r_amount=budget-bill
            meetha=int(input(f"Dear {name}, Do you want sweet? as the remaining amount is {budget-bill} \n1. Kunafah \n2. Chocolate Tart \n3. Suggest Something"))
            if meetha==1:
                bill2=500R
                print(f"Here is Your Sweet (Kunafah) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount-bill2}") 
        elif meetha==2:
            bill2=1000
            print(f"Here is Your Sweet (Chocolate Tart) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
        elif meetha==3:
            bill2=850
            print(f"Here is Your recommended Sweet (Kunafah Chocolate) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount}")   
        else:
            print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
            
    elif fav==2:
        bill=9000
        print(f"Dear {name}, \nHave Your Special shinwari karachi Platter with Aziz special Brain Masala! along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad \nYour Total Bill is {bill} Rs:8500/- (including tax)")
            r_amount=budget-bill
            meetha=int(input(f"Dear {name}, Do you want sweet? as the remaining amount is {budget-bill} \n1. lava chocolate with premium \n2. brownie cake \n3. Suggest Something"))
            if meetha==1:
                bill2=1200
                print(f"Here is Your Sweet (lava chocolate with premium) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount-bill2}") 
        elif meetha==2:
            bill2=1500
            print(f"Here is Your Sweet (brownie cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
        elif meetha==3:
            bill2=2000
            print(f"Here is Your recommended Sweet (Chocolate dream cake) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount}")   
        else:
            print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
            
     elif fav==3:
        bill=9500
        print(f"Dear {name}, \nHave Your Special white karachi Platter with Aziz special Niharri! along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad \nYour Total Bill is {bill} Rs:8500/- (including tax)")
            r_amount=budget-bill
            meetha=int(input(f"Dear {name}, Do you want sweet? as the remaining amount is {budget-bill} \n1. ice cake \n2. Three milk cake \n3. Cheese cake"))
            if meetha==1:
                bill2=1500
                print(f"Here is Your Sweet (ice cake) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount-bill2}") 
        elif meetha==2:
            bill2=2000
            print(f"Here is Your Sweet (Three milk cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
        elif meetha==3:
            bill2=3000
            print(f"Here is Your recommended Sweet (Cheese cake) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount}")   
        else:
            print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
            
     elif fav==4:
        bill=7000
        print(f"Dear {name}, \nHave Your Special BBQ Platter with Aziz special mutton chaamp! along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad \nYour Total Bill is {bill} Rs:8500/- (including tax)")
            r_amount=budget-bill
            meetha=int(input(f"Dear {name}, Do you want sweet? as the remaining amount is {budget-bill} \n1. Rabri kheer \n2. meethy Dahi Bhalay \n3. Cheese cake"))
            if meetha==1:
                bill2=1000
                print(f"Here is Your Sweet (Rabri kheer) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount-bill2}") 
        elif meetha==2:
            bill2=700
            print(f"Here is Your Sweet (meethy Dahi Bhalay) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
        elif meetha==3:
            bill2=1500
            print(f"Here is Your recommended Sweet (Gulaab jamun with rasmali fusioned with Ice cream) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount}")   
        else:
            print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")

     elif fav==5:
        bill=20000
        print(f"Dear {name}, \nHave Your Special Family Platter with special mutton dumpukht and BBQ Platter! along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad \nYour Total Bill is {bill} Rs:8500/- (including tax)")
            r_amount=budget-bill
            meetha=int(input(f"Dear {name}, Do you want sweet? as the remaining amount is {budget-bill} \n1. Rabri kheer \n2. meethy Dahi Bhalay \n3. Cheese cake"))
            if meetha==1:
                bill2=1000
                print(f"Here is Your Sweet (Rabri kheer) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount-bill2}") 
        elif meetha==2:
            bill2=700
            print(f"Here is Your Sweet (meethy Dahi Bhalay) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
        elif meetha==3:
            bill2=1500
            print(f"Here is Your recommended Sweet (Gulaab jamun with rasmali fusioned with Ice cream) \nYour Total Bill is {bill2+bill} \nHere is Your Remaining Amount{r_amount}")   
        else:
            print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")          
           