# Welcome to AI Restaurant!
# 
# 1: How many Person you are? greater than 8 and less than 15 - 1
# greater than 6 and less than 8 - 2
# greater than 4 and less than 6 - 3
# greater than 2 and less than 4 - 4
# equal equal to 1 - 5
# 
# 2: Whats your Budget range today ?
# greater than 20000 and less than 40000
# greater than 10000 and less than 20000
# greater than 5000 and less than 10000
# less than 5000
# 
# 2:Are you Happy to Eat something special from us?
# or do you have something in your mind? (mood) if else
# 
# something special: - AI Version
# something in mind : - Traditional Restaurant Version
# 
# AI-Version:
#     fav: what you eat commonly? (biryani, Karahi, bbq)
#     biryani - Have you eat is regularly? or weekly or monthly?
#     karahi - Have you eat is regularly? or weekly or monthly?
#     bbq - Have you eat is regularly? or weekly or monthly?
#    
#     regularly -
#     do want to eat - bombay biryani ? sindhi biryani ? hyderabadi biryani ?
#     or something different in rice?
#     if bombay biryani.. special daigh biryaani / plate
#         if daigh ? == above (10 persons / 2.5) * 1 daigh
#         if plate ? == above (8, 6, 4, 2 person) * plate biryani
#             remaining_amt=budget-bill
#            
#         --- if remaining_amt>=1000 and remaining_amt<=5000:
#             meetha= kunafah (2500) , brownie, (1100), threemilk cake(3500)
#             if remaining_amt<1000 and remaining_amt>=500:
#             meetha = gulaab jamun with ice-cream (650), chocolate icream (900)
#            
#     or something different in rice?
#     else:
#         input = do you like mutton or chicken ?
#         if mutton = mandi platter with dumpukht for you -
#         (1, 2 if budget is between 20000 to 40000)
#         if chicken = madbi platter with chicken sajji for you
#         (1,2,3 if budget is between 5000 - 40000)
#          --- if remaining_amt>=1000 and remaining_amt<=5000:
#             meetha= kunafah (2500) , brownie, (1100), threemilk cake(3500)
#             if remaining_amt<1000 and remaining_amt>=500:
#             meetha = gulaab jamun with ice-cream (650), chocolate icream (900)







print("********Welcome to AI Restaurant*******")

person=int(input("How many person you are? \n1. 8 to 15 \n2. 6 to 8 \n3. 4 to 6 \n4. 2 to 4 \nSelect any of the above?:"))
person2=int(input("Whats the Count of Person you have:"))

if person==1:
    budget=int(input("Enter you budget:"))
    if budget>=20000 and budget<=90000 and (person2>=8 and person<=15):
        
        version=int(input("What do you want us to do for you?: \n1. Something Special? \n2. Something in Mind? \nSelect any one?: "))
        if version==1:
            fav=int(input("what you eat commonly? \n1.biryani \n2.Karahi \n3.bbq: \nSelect any one:"))
            if fav==1:
                time=int(input("How often Do you eat Biryani \n1.regularly? \n2.weekly  \n3.monthly?"))
                if time==1:
                    variant=int(input("Do you want: \n1. Chicken \n2. Mutton (Most Recommended) \n3. Beef (Most Recommended)"))
                    if variant==1:
                        typ=int(input("Do you want to eat \n1. Bombay Biryaani \n2. Sindhi Biryaani \n3. Hyderabadi Biryani \n4.Type anything something Special in Rice \nSelect any specific from above: "))
                        if typ==1:
                            bir_daigh=2200 #for Regularly chicken biryaani lover 
                            sajji_per=2000
                            kunaffa=2500
                            gulabj=100
                            special_dr=1200
                            meetha_p=250
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2/3
                            quantity=person2/2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(sajji_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani \n2. Fresh Live {quantity} Sajji \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani Rs.{bir_daigh*daigh_kg}  \n2. Fresh Live {quantity} Sajji Rs {sajji_per*quantity} \n3. {quantity}Kunafah Rs {kunaffa*quantity} \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per} \n5.{person2} Special Drink Rs {special_dr*person2} \n6. {person2} Special Meetha Paan Rs {meetha_p*person2} \nTotal Bill: Rs{bill} + Tax {bill/10} \nGrand Total: {bill} ")
                            
                        elif typ==2:
                            print("")
                        elif typ==3:
                            print("")
                        else:
                            print("")
                    elif variant==2:
                        print("")
                    elif variant==3:
                        print("")
                    else:
                        print("")
                    
                elif time==2:
                    print("")
                elif time==3:
                    print("")
                else:
                    print("")
            elif fav==2:
                print("")
            elif fav==3:
                print("")
            else:
                print("Wrong input, Please Try Again! Last Chance:") 
        else:
            print("")
        
    elif budget>=10000 and budget<20000:
        print("")
        
    elif budget>=5000 and budget<10000:
        print("")
        
    else:
        print("Please Increase your budget as your count of person is huge!")
        budget2=int(input("Do you want to increase your budget? (\n1.Yes \n2. No):"))
        if budget2==1:
            budget_repeat=int(input("Enter your budget?:"))
            if budget_repeat>=20000:
                print("")
            elif budget_repeat>=10000 and budget_repeat<20000:
                print("")
            elif budget_repeat>=5000 and budget_repeat<10000:
                print("")
            else:
                print("Still You have'nt increased! Thank you for visiting us!")
        else:
            print("Thank you for visiting us!")
        
elif person==2:
    print("")
elif person==3:
    print("")
elif person==4:
    print("")
else:
    print("")