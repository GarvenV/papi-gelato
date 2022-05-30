def PapiGelato():
    print ('Welkom bij Papi Gelato.')
    Gelatomarkt = input('Bent u particulier of zakelijk?')
    if Gelatomarkt == 'particulier':
        particulierbolletjes()
    if Gelatomarkt == 'zakelijk':
        zakelijkLiter()


slagroom = 0
sprinkels = 0
caramelsaushoortnje = 0 
caramelsausbakje = 0

#------soortbolletjes--------
def soortbolletjes (aantal):
    v = 1
    for x in range (1,aantal=1):
        soort = input('Welke smaak wilt u voor bolletje nummer' + str(x) + '? A) Aardbei, C) Chocolade of V) Vanille?')
        if soort == "V" or "M" or "C" or "A":
            x += 1
        else:
            print('Sorry dat is geen optie die we aanbieden..')
            soortbolletjes()

#-----aantalbolletjes------
def aantalbolletjes():
    aantal = int(input('Hoeveel bolletjes wilt u?'))
    if aantal >= 1 and aantal <= 3:
        soortbolletjes(aantal)
        bakjehoorntjes(aantal)
        
    elif aantal >= 4 and aantal <= 8:
        print('Dan krijgt u van mij een bakje met ' + str(aantal) + ' bolletjes')
        soortbolletjes(aantal)
    elif aantal > 8:
        print('Sorry, zulke grote bakken hebben we niet')
    else:
        print('Sorry dat is geen optie die we aanbieden..')


#------bakjehoorntjes------
def bakjehoorntjes(aantal):
    bakjehoorntje = input('Wilt u deze ' + str(aantal) + ' bolletje(s) in A) een hoorntje of B) een bakje?')
    if bakjehoorntje == "A":
        
        totaal = prijs(aantal, 1, 0, 0)
        hoorntje = input('Hier is uw hoorntje met ' + str(aantal) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if hoorntje == 'Y':
            aantalbolletjes()
            
        elif hoorntje == 'N':
            
            print('Bedankt en tot ziens')


    elif bakjehoorntje == "B":
        totaal = prijs(aantal, 0, 1, 1)
        bakje = input('Hier is uw bakje met ' + str(aantal) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if bakje == 'Y':
            aantalbolletjes()
        elif bakje == 'N':
            totaal()
            print('Bedankt en tot ziens')
    else:
        print('Sorry dat is geen optie die we aanbieden..')

#-------toppings------    
def topping(bolletjes,hoorntjebakje,hoorntje,bakje):
    toppings = input('Wat voor topping wilt u: Slagroom,  Sprinkels of  CaramelSaus?')
    if toppings == 'Slagroom':
        slagroom == 0.50
        print ('Dat wordt Slagroom op je Bolletjes.')
    if toppings == 'Sprinkels':
        sprinkels == 0.30
        print ('Dat worden Sprinkles op je Bolletjes.')
    if toppings == 'CaramelSaus' and hoorntje == 1:
        CaramelsausHoorntje == 0.60
        print ('Dat wordt CaramelSaus met je Hoorntje.')
    if toppings == 'CaramelSaus' and bakje == 1:
        Caramelsausbakje == 0.90
        print ('Dat wordt CaramelSaus met je Bakje.')

    particulierresultaat(toppings,bolletjes,hoorntje,bakje,slagroom,sprinkels,CaramelsausHoorntje,Caramelsausbakje)


#-------prijs-------
def prijs (aantal,hoorntje,bol,top):
    top = toppings(top) 
    totaalprijs = 0 
    bolletje = round(1.10, 2)
    hoorn = 1.25
    bakje = 0.75
    if hoorntje == 1:
        totaalprijs += hoorntje
    elif bol == 1:
        totaalprijs =+ bakje
        bolletjeprijs = bolletje * aantal
        totaalprijs = totaalprijs + bolletjeprijs
        totaalprijs = totaalprijs + top

    print ("--------[Papi Gelato]--------")
    print("Bolletjes        " + str(aantal) + " x €0.70 = €" + str(aantal * 1.10))
    print("Hoorntje         " + str(hoorntje) + " x €1.10 = €" + str(hoorntje * 1.25))
    print("Bakje            " + str(bol) + " x €0.75 = €" + str(bol * 0.55))
    print("Toppings                   = €" + str(round(top,2)) )
    print("Totaal                     = €" + str(round(totaalprijs,2)))


    return totaalprijs 

