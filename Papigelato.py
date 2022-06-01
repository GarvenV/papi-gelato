def PapiGelato():
    print ('Welkom bij Papi Gelato.')
    Gelatomarkt = input('Bent u particulier of zakelijk?')
    if Gelatomarkt == 'particulier':
        particulierbolletjes()
    if Gelatomarkt == 'zakelijk':
        zakelijkLiter()


slagroom = 0
sprinkels = 0
caramelsaushoorntje = 0 
caramelsausbakje = 0

#------particulierbolletjes--------
def particulierbolletjes(aantal):
    bolletjes = int(input('Hoeveel bolletjes wilt u? \n'))  
    if bolletjes > 8:
        print ('Sorry, zulke grote bakken hebben we niet.')
        particulierbolletjes()
    elif bolletjes  <= 3:
        print ('Dus,' , bolletjes , 'bolletjes.')
    elif bolletjes > 3:
        print ('Dan krijgt u van mij een bakje met' , bolletjes , 'bolletjes')

    particuliersmaak(bolletjes)
    return bolletjes
    

#-----smaak------

def particuliersmaak(bolletjes):
    if  (bolletjes > 3) or (bolletjes <= 3) == True:
        Smaakbol = bolletjes   
        while Smaakbol > 0:
            Smaakbol = Smaakbol - 1
            smaak = input(print('Welke smaak wilt u voor bolletje nummer', Smaakbol ,'?',' Aardbei, Chocolade of Vanille? \n'))

        if smaak == 'Aardbei' or smaak == 'Chocolade' or  smaak == 'Vanille':
            print ('bolletje{s}.', bolletjes, 'heeft het smaak,' , smaak)

        else:
            print ('Sorry dat is geen optie die we aanbieden...')
            particuliersmaak(bolletjes)
    hoorntje(bolletjes)


#------hoorntjes------
def hoorntje(bolletjes):
    hoorntjebakje = input('Wilt u deze bolletje(s). in een hoorntje of een bakje? \n')
    hoorntje = 'hoorntje' and 0
    bakje = 'bakje' and 0

    if hoorntjebakje == 'bakje':
        bakje = 1
        print ('Dat wordt 1 Bakje.')
    elif hoorntjebakje == 'hoorntje':
        hoorntje = 1
        print ('Dat wordt 1 Hoorntje.')
    else:
        print('Sorry dat is geen optie die we aanbieden..')
        hoorntje()
    topping(bolletjes,hoorntjebakje,hoorntje,bakje)


      

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
        caramelsaushoorntje == 0.60
        print ('Dat wordt CaramelSaus met je Hoorntje.')
    if toppings == 'CaramelSaus' and bakje == 1:
        caramelsausbakje == 0.90
        print ('Dat wordt CaramelSaus met je Bakje.')

    particulierresultaat(toppings,bolletjes,hoorntje,bakje,slagroom,sprinkels,caramelsaushoorntje, caramelsausbakje)


#-------prijs-------
def particulierresultaat  (aantal,hoorntje,bol,top):
    top = topping(top) 
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

#----------zakelijkijs----------
def zakelijkLiter():
    Liter = int(input('Hoeveel Liter wilt u? \n'))
    zakelijksmaak(Liter)



#----------zakelijkijs----------
def zakelijkLiter():
    Liter = int(input('Hoeveel Liter wilt u? \n'))
    zakelijksmaak(Liter)


#----------zakelijksmaak----------
def zakelijksmaak(Liter):
    smaakAardbei = int(input('Hoeveel Liter Aardbei wilt u? \n'))
    Totaalliter = Liter - smaakAardbei 
    print(Totaalliter)
    if Totaalliter > 0:
        smaakChocolade = int(input('Hoeveel Liter Chocolade wilt u? \n'))
        Totaalliter = Totaalliter - smaakChocolade
        print(Totaalliter)
    if Totaalliter > 0:
        smaakVanille = int(input('Hoeveel Vanille Chocolade wilt u? \n'))
        Totaalliter = Totaalliter - smaakVanille
        print(Totaalliter)

    zakelijkresultaat(Liter)


def zakelijkresultaat(Liter):
    print ("---------[Papi Gelato]---------")
    print ('Liter'  , Liter , 'x 9.80  = ', Liter*9.80)
    print ("-------------------------------")
    print ('Totaal                         = ', Liter*9.80 )
    print ('BTW(9%)                        = ', (Liter*9.80) / 100 * 6)

PapiGelato()