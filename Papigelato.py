print ("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")
def soortbolletjes (aantal):
    v = 1
    for x in range (1,aantal=1):
        soort = input('Welke smaak wilt u voor bolletje nummer' + str(x) + '? A) Aardbei, C) Chocolade of V) Vanille?')
        if soort == "V" or "M" or "C" or "A":
            x += 1
        else:
            print('Sorry dat is geen optie die we aanbieden..')
            soortbolletjes()

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

def bakjehoorntjes(aantal):
    bakje_hoorntje = input('Wilt u deze ' + str(aantal) + ' bolletje(s) in A) een hoorntje of B) een bakje?')
    if bakje_hoorntje == "A":
        
        totaal = prijs(aantal, 1, 0, 0)
        hoorntje = input('Hier is uw hoorntje met ' + str(aantal) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if hoorntje == 'Y':
            aantalbolletjes()
            
        elif hoorntje == 'N':
            
            print('Bedankt en tot ziens')

    elif bakje_hoorntje == "B":
        totaal = prijs(aantal, 0, 1, 1)
        bakje = input('Hier is uw bakje met ' + str(aantal) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if bakje == 'Y':
            aantalbolletjes()
        elif bakje == 'N':
            totaal()
            print('Bedankt en tot ziens')
    else:
        print('Sorry dat is geen optie die we aanbieden..')

