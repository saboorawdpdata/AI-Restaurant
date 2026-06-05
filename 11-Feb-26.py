
print("********Welcome to AI Restaurant*******")

person=int(input("How many person you are? \n1. 8 to 15 \n2. 6 to 8 \n3. 4 to 6 \n4. 2 to 4 \nSelect any of the above?:"))
person2=int(input("Whats the Count of Person you have:"))

if person==1:
    #budget=int(input("Enter you budget:"))
    if person2>=8 and person2<=15:
        version=int(input("What do you want us to do for you?: \n1. Something Special? \n2. Something in Mind? \nSelect any one?: "))
        print("\n*====================================*")
        if version==1:
            fav=int(input("what you eat commonly? \n1.biryani \n2.Karahi \n3.bbq: \nSelect any one:"))
            print("\n*====================================*")
            if fav==1:
                time=int(input("How often Do you eat Biryani \n1.regularly? \n2.weekly  \n3.monthly?"))
                print("\n*====================================*")
                if time==1:
                    variant=int(input("Do you want: \n1. Chicken \n2. Mutton (Most Recommended) \n3. (Type anything for) Beef (Most Recommended)"))
                    print("\n*====================================*")
                    if variant==1:
                        typ=int(input("Do you want to eat \n1. Bombay Biryaani \n2. Sindhi Biryaani \n3. Hyderabadi Biryani \n4.Type anything something Special in Rice \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Bombay Biryaani Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            sajji_per=2000 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            special_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(sajji_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani \n2. Fresh Live {quantity} Sajji \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Bombay Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Sajji Rs.{sajji_per*quantity}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                        elif typ==2:
                            print("*************Moving for Sindhi Biryaani Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            tikka_per=1500 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(tikka_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Sindhi Biryaani \n2. Fresh Live {quantity} Lahori Tikka \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Sindhi Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Lahori Tikka Rs.{tikka_per*quantity}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                     
                        elif typ==3:
                            print("*************Moving for Hyderabaadi Biryaani Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            qeema_per=1500 #15000
                            rabri=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(qeema_per*quantity)+(rabri*person2)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Hyderabaadi Biryaani \n2. Fresh Live {quantity}Kg Dum Qeema \n3. {quantity}kg Rabri \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Hyderabaadi Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Kg Dum qeema Rs.{qeema_per*quantity}/- \n***********\n3. {quantity} Rabri Rs.{rabri*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                      
                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice*********")
                            madbi_plat=6000 #for Regularly chicken biryaani lover #16500
                            dumpukht=2500 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(madbi_plat*platter)+(dumpukht*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter} Fresh Afghaani Special Platter \n2. Fresh Live {quantity} KG Dumpukht  \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter} Fresh Afghaani Special Platter Rs.{madbi_plat*platter}/-  \n***********\n2. Fresh Live {quantity} KG Dumpukht Rs.{dumpukht*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                    elif variant==2:
                        typ=int(input("Do you want to eat \n1. Moroccan Lamb Rice \n2. Classic Dumpukht mutton biryaani \n3. Mutton Kabbuli Pulao \n4.Type anything something Special in Rice \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Moroccan Lamb Rice Lover*********")
                            lamb_rice=3000 #for Regularly lamb rice lover #16500
                            saalam_lamb=3000 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            special_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(lamb_rice*platter_kg)+(saalam_lamb*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10

                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter_kg}KG Fresh Live Morrocon Lamb rice \n2. Fresh Live {platter_kg} Lamb \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter_kg} KG Fresh Live Morrocon Lamb rice Rs.{lamb_rice*platter_kg}/-  \n***********\n2. Fresh Live {Platter_kg} Saalam Lamb Rs.{saalam_lamb*platter_kg}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                        elif typ==2:
                            print("*************Moving for Classic Dumpukht Mutton Biryaani Lover*********")
                            mutton_bir=4500 #for Regularly chicken biryaani lover #16500
                            mutton_rosh=3500 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            mutton_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(mutton_bir*mutton_kg)+(mutton_rosh*mutton_kg)+(kunaffa*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {mutton_kg}KG Fresh Live Classic Dumpukht Mutton Biryaani \n2. Fresh Live {mutton_kg} Mutton Rosh \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {mutton_kg} KG Fresh Live Classic Dumpukht Mutton Biryaani Rs.{mutton_bir*mutton_kg}/-  \n***********\n2. Fresh Live {mutton_kg} kg Mutton Rosh Rs.{mutton_rosh*mutton_kg}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                     
                        elif typ==3:
                            print("*************Moving for Mutton Kabbuli Pulao Lover*********")
                            kabuli_pulao=3000 #for Regularly chicken biryaani lover #16500
                            mutton_peti_kabab=2000 #15000
                            rabri=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            kabuli_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(kabuli_pulao*kabuli_kg)+(mutton_peti_kabab*quantity)+(rabri*person2)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {kabuli_kg}KG Fresh Live Chicken Hyderabaadi Biryaani \n2. Fresh Live {person2} Petti Kabaab  \n3. {quantity}kg Rabri \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {kabuli_kg} KG Fresh Live Chicken Hyderabaadi Biryaani Rs.{kabuli_pulao*kabuli_kg}/-  \n***********\n2. Fresh Live {person2} Petti Kabaab Rs.{mutton_peti_kabab*person2}/- \n***********\n3. {quantity} Rabri Rs.{rabri*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")

                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice*********")
                            b_plat=6000 #for Regularly badshahi platter lover #16500
                            salim_dumba=4500 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(b_plat*platter)+(salim_dumba*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter} Fresh Afghaani Special Platter \n2. Fresh Live {quantity} Salim Dumba \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter} Fresh Baadshahi Platter Rs.{b_plat*platter}/-  \n***********\n2. Fresh Live {quantity} KG Salim Dumba Rs.{salim_dumba*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
#                     elif variant==3:
#                         print("")
                    else:
                        #print("")
                        typ=int(input("Do you want to eat \n1. Classic Beef Special Daigh Biryaani \n2.Type anything something Special in Rice with beef \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Classic Beef Special Daigh Biryaani Lover*********")
                            classic_daig=1947 #for Regularly lamb rice lover #16500
                            bihaari_kabaab=1408 #15000
                            kunaffa=1499 #11250
                            gulabj=78 #3000
                            special_dr=547 #9000 
                            meetha_p=73 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(classic_daig*daigh_kg)+(bihaari_kabaab*person2*2)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill//14
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Classic Beef Special Daigh Biryaani rice \n2. Fresh Live {person2*2} Bihaari Kabaab \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Classic Beef Special Daigh Biryaani rice Rs.{classic_daig*daigh_kg}/-  \n***********\n2. Fresh Live {person2*2} Bihaari Kabaab Rs.{bihaari_kabaab*(person2*2)}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                    
                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice with beef*********")
                            beef_hyder_daigh=4359 #for Regularly badshahi platter lover #16500
                            beef_balochi_tikka=2569 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            beef_daigh=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(beef_hyder_daigh*beef_daigh)+(beef_balochi_tikka*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {beef_daigh} KG Live Fresh Special Beef Hyderabaadi Daighi Biryaani \n2. Fresh Live {quantity} Beef Balochi Tikka \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {beef_daigh} KG Live Fresh Special Beef Hyderabaadi Daighi Biryaani Rs.{beef_hyder_daigh*beef_daigh}/-  \n***********\n2. Fresh Live {quantity} Beef Balochi Tikka Rs.{beef_balochi_tikka*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                    
                elif time==2: #weekly
                    #print("")
                    variant=int(input("Do you want: \n1. Chicken \n2. Mutton (Most Recommended) \n3. (Type anything for) Beef (Most Recommended)"))
                    print("\n*====================================*")
                    if variant==1:
                        typ=int(input("Do you want to eat \n1. Biryaani \n2. Chinese \n3. Fast food \n4.Type anything something Special \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Biryaani Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            sajji_per=2000 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            special_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(sajji_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani \n2. Fresh Live {quantity} Sajji \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Bombay Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Sajji Rs.{sajji_per*quantity}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                        elif typ==2: #user input chinese
                            print("*************Moving for Chinese Food Lover*********")
                            chinese_plat=2200 #for Regularly chicken biryaani lover #16500
                            Chinese_bowl=1500 #15000
                            lotus_tofu=1500 #11250 #meetha for chinese lover
                            dumplings=200 #3000
                            bubble_tea=600 #9000 
                            moon_cake=100 #1500 #
                            dumplings_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            chinese_per=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(chinese_plat*chinese_per)+(Chinese_bowl*person2)+(lotus_tofu*person2)+(dumplings*dumplings_per)+(bubble_tea*person2)+(moon_cake*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {chinese_per} Live Jumbo Platter of Chinese Cuisine \n2. Fresh Live {person2} Chinese Bowl of Chowmein \n3. {person2} Lotus Tofu \n4.{dumplings_per} Dumplings \n5.{person2} Bubble Tea \n6. {person2} Moon cake")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {chinese_per} Live Jumbo Platter of Chinese Cuisine Rs.{chinese_per*chinese_plat}/-  \n***********\n2. Fresh Live {person2} Chinese Bowl of Chowmein Rs.{Chinese_bowl*person2}/- \n***********\n3. {person2} Lotus Tofu Rs.{lotus_tofu*person2}/- \n***********\n4.{dumplings_per} Dumplings Rs {dumplings_per*person2}/- \n***********\n5.{person2} Bubble Tea Rs {bubble_tea*person2}/- \n***********\n6. {person2} Moon cake Rs {moon_cake*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                     
                        elif typ==3: #fast food
                            print("*************Moving for Fast Food Lover*********")
                            burger=1500 #for Regularly chicken biryaani lover #16500
                            broast=2000 #15000
                            wings=200 #11250
                            fries_buk=400 #3000
                            soft_dr=120 #9000 
                            dips=100 #1500
                            Choco_bar=400
                            #burger_per=person2 #for the purspose to calculate 2 gulab jamun per person
                            #broast_per=person2//2
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(burger*person2)+(broast*quantity)+(wings*person2*2)+(fries_buk*quantity)+(soft_dr*person2)+(Choco_bar*person2)+(dips*quantity) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Fast Food is here confirmed and here \n1. {person2} Crispy Chicken Chipotle Burger \n2.  {quantity}Arabic Cripy Chicken Broast \n3. {person2*2} Korean Wings \n4.{quantity} Cripy Mayo Garlic Fries \n5.{person2} Soft Drink \n6. {person2} Special Choco Bar \n7. {quantity} Dips") 
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {person2} Crispy Chicken Chipotle Burger Rs.{person2*burger}/-  \n***********\n2. Arabic Cripy {quantity} Chicken Broast Rs.{broast*quantity}/- \n***********\n3. {person2*2} Korean Wings Rs.{wings*(person2*2)}/- \n***********\n4..{quantity} Cripy Mayo Garlic Fries Rs.{fries_buk*quantity}/- \n***********\n5.{person2} Soft Drink Rs {soft_dr*person2}/- \n***********\n6. {person2} Special Choco Bar Rs {Choco_bar*person2}/- \n************\n7. {quantity} Dips Rs.{dips*quantity}\- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                      
                        else:
                            print("*************Moving Towards Our Special Suggestion*********")
                            broast=2000 #for Regularly chicken biryaani lover #16500
                            matka_biry=2500 #15000
                            icecream_falooda=1200 #11250
                            wings=200 #3000
                            chinese=1000 #9000 
                            choco_bar=400 #1500
                            dips=100
                            #gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            #platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(broast*quantity)+(matka_biry*quantity)+(icecream_falooda*person2)+(wings*person2*2)+(chinese*quantity)+(choco_bar*person2)+(dips*quantity) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {quantity} Fresh Arabic Broast Bucket \n2. Fresh Live {quantity} Special Matka Biryaani \n3. {person2} Bowl Ice Cream Falooda \n4.{person2*2} Special Korean Wings \n5.{quantity} Platter of Chinese Cuisine \n6. {person2} Special Choco Bar \n7. {quantity} Special Dips for Broast")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {quantity} Fresh Arabic Broast Bucket Rs.{broast*quantity}/-  \n***********\n2. Fresh Live {quantity} Special Matka Biryaani Rs.{matka_biry*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{person2*2} Special Korean Wings  Rs.{wings*(person2*2)}/- \n***********\n5.{quantity} Platter of Chinese Cuisine Rs.{chinese*quantity}/- \n***********\n6. {person2} Special Choco Bar Rs.{choco_bar*person2}/- \n7. {quantity} Special Dips for Broast Rs.{broast*quantity}\- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                            
                    elif variant==2:
                        typ=int(input("Do you want to eat \n1. Special Mutton Fusion Platter  \n2. Classic Jumbo Mutton Paaya and Nihari Deal  \n3. Special Mutton BBQ and Mutton Kabbuli Pulao Platter \n4.Type anything something Special in Rice \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Special Mutton Fusion Platter*********")
                            mutton_kar=3000 #for Regularly lamb rice lover #16500
                            mutton_chaanp=800 #15000
                            fried_rice_kg=250 #11250
                            r_naan=100 #3000
                            chatni_per=100

                            soft_dr=150 #9000 
                            gulab_j=100 #1500
                            kheer_rabri=300
                            mutton_yakhni=300
            
                            #gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            #platter_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(mutton_kar*quantity)+(mutton_chaanp*(person2*3))+(fried_rice_kg*quantity)+(r_naan*person2)+(chatni_per*person2)+(soft_dr*person2)+(gulab_j*person2*2)+(kheer_rabri*quantity//2)+(mutton_yakhni*person2) #calculation for bill
                            tax=bill/10

                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {quantity}KG Fresh Live Mutton Shinwaari Karahi \n2. {person2*3} Sizzling Mutton Chaaamp \n3. {quantity}KG Fried Rice \n4.{person2} Sesame Roghni Kulcha \n5.{person2} Special Spicy red piping hot chatni \n6. {person2} Soft Drinks \n7. {person2*2} Hot sheeray wala Gulab jamun \n8. {quantity//2}KG Special Badshaahi Kheer Rabri \n9. {person2} Special Mutton Yakhni")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {quantity}KG Fresh Live Mutton Shinwaari Karahi Rs.{mutton_kar*quantity}/-  \n***********\n2. {person2*3} Sizzling Mutton Chaaamp Rs.{mutton_chaanp*(person2*3)}/- \n***********\n3. {quantity}KG Fried Rice Rs.{fried_rice_kg*quantity}/- \n***********\n4.{person2} Sesame Roghni Kulcha Rs.{r_naan*person2}/- \n***********\n5.{person2} Special Spicy red piping hot chatni Rs.{chatni_per*person2}/- \n***********\n6. {person2} Soft Drink Rs {soft_dr*person2}/- \n7. {person2*2} Gulaab Jamun Rs.{gulab_j*(person2*2)} \n8. {quantity//2} Kg Special Badshaahi Kheer Rabri Rs.{kheer_rabri*(quantity//2)} \n9. {person2} Special Mutton Yakhni Rs.{mutton_yakhni*person2}   \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                        elif typ==2:
                            print("*************Moving for Classic Jumbo Mutton Paaya and Nihari Deal*********")
                            mutton_paaya=1500 #for Regularly chicken biryaani lover #16500
                            mutton_nihari=3500 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500
                            zeera_rice=150
                            r_naan=150
                            raita=80
                            salad=300
                            #gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            #mutton_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(mutton_paaya*quantity)+(mutton_nihari*quantity)+(kunaffa*quantity)+(gulabj*person2*2)+(limca_dr*person2)+(meetha_p*person2)+(zeera_rice*quantity)+(r_naan*person2)+(raita*person2)+(salad*quantity) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {quantity}KG Fresh Live Special Mutton Paaya  \n2. {quantity} Fresh Live Special Dehli Mutton Nihaari \n3. {quantity}Kunafah \n4.{person2*2} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan \n7. {quantity//2} KG Zeera Rice \n8. {person2} Roghni Naan \n9. {person2} Green Raita \n10. {quantity} Special Green Salad")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n*********** \n1. {quantity}KG Fresh Live Special Mutton Paaya Rs.{mutton_paaya*quantity}/-  \n***********\n2. {quantity} Fresh Live Special Dehli Mutton Nihaari Rs.{mutton_nihari*quantity}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{person2*2} Gulaab Jamun Rs{gulabj*person2*2}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs.{meetha_p*person2}/- \n7. {quantity//2} KG Zeera Rice Rs.{zeera_rice*(quantity//2)}/- \n8. {person2} Roghni Naan Rs.{r_naan*person2}/- \n9. {person2} Green Raita Rs.{raita*person2}/- \n10. {quantity} Special Green Salad Rs.{salad*quantity}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                     
                        elif typ==3:
                            print("*************Moving for Special Mutton BBQ and Mutton Kabbuli Pulao Platter*********")
                            kabuli_pulao=3000 #for Regularly chicken biryaani lover #16500
                            mutton_chaamp=1000 #15000
                            kheer=300 #11250
                            barfi=100 #3000
                            limca_dr=600 #9000 
                            kaju_katli=100 #1500
                            ice_cream=300
                            
                            #gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            #kabuli_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(kabuli_pulao*quantity)+(mutton_chaamp*person2*2)+(kheer*person2)+(barfi*person2*2)+(limca_dr*person2)+(kaju_katli*person2*2)+(ice_cream*person2)
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {quantity}KG Fresh Live Mutton kaabuli Pulao \n2. Fresh Live {person2*2} Mutton Chaamp  \n3. {person2} Kheer \n4.{person2*2} Barfi \n5.{person2} Limca Drink \n6. {person2*2} Kaaju Katli \n7. {person2} Ice Cream")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {quantity}KG Fresh Live Mutton kaabuli Pulao Rs.{kabuli_pulao*quantity}/-  \n***********\n2. Fresh Live {person2*2} Mutton Chaamp Rs.{mutton_chaamp*person2*2}/- \n***********\n3. {person2} Kheer Rs.{kheer*person2}/- \n***********\n4.{person2*2} Barfi Rs.{barfi*person2*2}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2*2} Kaaju Katli Rs {kaju_katli*person2*2}/- \n***********\n \n7. {person2} Ice Cream Rs.{ice_cream*person2}  \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")

                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice*********")
                            b_plat=6000 #for Regularly badshahi platter lover #16500
                            salim_dumba=4500 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(b_plat*platter)+(salim_dumba*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter} Fresh Afghaani Special Platter \n2. Fresh Live {quantity} Salim Dumba \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter} Fresh Baadshahi Platter Rs.{b_plat*platter}/-  \n***********\n2. Fresh Live {quantity} KG Salim Dumba Rs.{salim_dumba*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
#                     elif variant==3:
#                         print("")
                    else:
                        #print("")
                        typ=int(input("Do you want to eat \n1. Special Beef Rice and BBQ Platter \n2.Type anything something Special in Rice with beef \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Special Beef Rice and BBQ Platter *********")
                            bbq_karahi=2000 #for Regularly lamb rice lover #16500
                            beef_rice=1200 #15000
                            kunaffa=1499 #11250
                            gulabj=78 #3000
                            special_dr=547 #9000 
                            naan=73 #1500
                            doodh_jalebi=300
#                             gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
#                             daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bbq_karahi*quantity)+(beef_rice*quantity)+(kunaffa*quantity)+(gulabj*person2)+(special_dr*person2)+(naan*person2*2)+(doodh_jalebi*person2) #calculation for bill
                            tax=bill//14
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {quantity}KG Fresh Live Beef BBQ Karahi \n2. Fresh Live {quantity} Beef Rice \n3. {quantity}Kunafah \n4.{person2} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2*2} Special Naan \n7. {person2} Live Doodh Jalebi")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {quantity}Kg Fresh Live BBQ Karahi Rs.{bbq_karahi*quantity}/-  \n***********\n2. Fresh Live {quantity} Beef Rice Rs.{beef_rice*quantity}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{person2} Gulaab Jamun Rs {gulabj*person2}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2*2} Special Naan Rs {naan*person2*2}/-\n**********\n7. {person2} Live Doodh Jalebi Rs. {doodh_jalebi*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                    
                        else:
                            print("*************Moving Towards Our Special Suggestion for you in beef Recommendation*********")
                            beef_steak=3000 #for Regularly badshahi platter lover #16500
                            beef_rosh=2500 #15000
                            beef_naali_biryani=1500 #11250
                            gulabj=100 #3000
                            lemonade=400 #9000
                            paratha=200
                            beef_boti=500
                            khowa=400
#                             fire_meetha_pan=150 #1500 
#                             gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
#                             beef_daigh=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(beef_steak*quantity)+(beef_rosh*quantity)+(beef_naali_biryani*quantity)+(gulabj*person2)+(lemonade*person2)+(paratha*person2)+(beef_boti*quantity)+(khowa*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {quantity}  Platter of Beef Steak  \n2. {quantity} Namkeen Beef Rosh \n3. {quantity} Nalli Beef Biryani \n4. {quantity} Plate of Beef Boti \n5.{person2} Gulaab Jamun \n6.{person2} Special Mint Lemonda \n7. {person2} Mughlai Paratha \n8. {person2} Bowl Khowa")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {quantity} Platter of Beef Steak Rs.(beef_steak*quantity)/-  \n***********\n2. {quantity} Namkeen Beef Rosh Rs.{beef_rosh*quantity}/- \n***********\n3. {quantity} Nalli Beef Biryani Rs.{beef_naali_biryani*quantity}/- \n**********\n4. {quantity} Plate of Beef Boti Rs.{beef_boti*quantity}/-\n***********\n5.{person2} Gulaab Jamun Rs {gulabj*person2}/- \n***********\n6.{person2} Special Mint Lemonda Rs.{lemonade*person2}/- \n***********\n7. {person2} Mughlai Paratha Rs {paratha*person2}/- \n*******\n8. {person2} Bowl Khowa Rs. {khowa*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                    
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
        
#     elif budget>=10000 and budget<20000: #
#         print("")
#         
#     elif budget>=5000 and budget<10000:
#         print("")
#         
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
        
elif person2==2:
    print("")
elif person2==3:
    print("")
elif person2==4:
    print("")
else:
    print("")
