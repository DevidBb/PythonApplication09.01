#gender=input("Kas te olete mees või naine?")
#if gender.lower()=="naine":
#    print("Kahjuks meile vaja ainult mehed")
#else:
#    age=int(input("Palun kirjutage oma vanus"))
#    if age>16 and age <=18:
#        print("Sa sobid meie meeskonda")
#    else:
#        print("Kahjuks teie ei sobite meie keskonna")



#def new_func():
#    hind = float(input("Sisetage toode hinne"))
#    return hind

#hind = new_func()
#if hind <=10:
#    soodustus = hind * 0.1
#else:
#    soodustus = hind * 0.2
#okonnelik_hind = hind - soodustus
#print("Lõplik hind on", okonnelik_hind, "€")











#h1 = input("чило 1 ")
#h2 = input("число 2 ")
#o = input("dыберите действие")
#if o=="+":
#    otvet = h1 + h2
#elif o=="-":
#    otvet = h1 - h2
#elif o=="*":
#    otvet = h1 * h2
#elif o=="/":
#    otvet = h1 / h2
#else: 
#    print("не знаю таких симболов, могу только -,+,/,*")
#print("tvoi otvet")



#from random import * 
#from datetime import *
#a=10
#b=2.3
#c="programma"
#d="1.1"
#print(b.is_integer())
#print(c.isalpha())
#print(d.isalpha())
#print(d.isnumeric())
#print(d.isdigit())
#print(c.isdecimal())

#try:
#    gender=input("sugu: ")
#    if gender.isalpha() and (gender.lower()=="naine" or gender.lower()=="mees"):
#        if gender.lower()=="naine":
#            print("ei sobi")
#        else:
#            try:
#                age=int(input("Vanus"))
#                if 16<=age<=18:
#                    print("oled meeskonnas!")
#                else:
#                    print("Vanus ei sobi")
#            except:
#                print("Vale vanus! Viga andmetüübiga")
#    else:
#        print("siseta õige tekst")
#except:
#    print("viga andmetüübiga!")



try:
    print("Tere! Olen sinu uus sõber - Python!")
    
    nimi = input("Sisesta oma nimi: ")
    
    
    print(nimi + ", oi kui ilus nimi!")
    
    
    vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    
    if vastus == 1:
        try:
         
            pikkus = int(input("Sisesta pikkus (cm): "))
            
            
            mass = float(input("Sisesta kaal (kg): "))
            
            
            indeks = mass / (0.01 * pikkus) ** 2
            
            
            print(nimi + "! Sinu keha indeks on: {:.1f}".format(indeks))
            
            
            if indeks < 16:
                print("Tervisele ohtlik alakaal")
            elif 16 <= indeks < 19:
                print("Alakaal")
            elif 19 <= indeks < 25:
                print("Normaalkaal")
            elif 25 <= indeks < 30:
                print("Ülekaal")
            elif 30 <= indeks < 35:
                print("Rasvumine")
            elif 35 <= indeks < 40:
                print("Tugev rasvumine")
            else:
                print("Tervisele ohtlik rasvumine")
        
        except ValueError:
            print("Viga! Palun sisestage sobivad numbrid.")
    
    else:
        print("Kahju! See on väga kasulik info!")
        print()

    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

except ValueError:
    print("Viga! Palun sisestage sobivad numbrid.")
