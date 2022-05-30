print ('Welkom bij Papi Gelato')
print  ("je mag alle smaken kiezen zolang het maar vanille ijs is")
   


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
def toppings(bakje):
    top = input('wat voor topping wilt u: A) Geen B) Slagroom, C) Sprinkels of D) Caramel Saus?')
    if top == "A":
        totaal_topping = 0
        return totaal_topping
    elif top == "B":
        totaal_topping = 0.40
        return totaal_topping

    elif top == "C":
        totaal_topping = 0.60
        return totaal_topping
        
    elif top == "D":
        if bakje == 0:
            totaal_topping = 0.70
            return totaal_topping
           
        elif bakje == 1:
            totaal_topping = 0.95
            return totaal_topping
        
            
    else:
        print("Sorry dat begrijp ik niet.")


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

