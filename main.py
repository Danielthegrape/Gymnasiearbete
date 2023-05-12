from bs4 import BeautifulSoup
from done import Mall
from done import arbet




rapport = open('spel.txt', 'w')

Betsmart = Mall("Betsmart.html",'div','ml__row bg-main-100', "span", "", "span",
               "ml__odd bg-main-200")

gång = 0
betsave = {}


#Detta stycket skapar ett lexikon(betsave) med en ordning. Detta gör den med att nyckeln blir till att nummer som ska vara med i en viss order och värderna blir Lagen som finns i matchen samt oddsen till den matchen. Det kommer göra att en nyckel och ett värde ser ut så här:  {order(nyckeln):((namn på lagen),(odds1,odds2,odds3))}
for name in Betsmart:
  bestbet = [name] #tar namnet och lägger den till listan bestbet
  gång += 1
  bets = Betsmart[name]

  bestbet.append(bets)#lägger till oddsen till listan bestbet

  
  tuplebet = tuple(bestbet)
  betsave[gång] = tuplebet  #betsave är den saken som har med alla bets och namnen
  #sparar betsen till ett lexikon med nummmber ordning {1:((namenet pålagen)(1.32,21,5.4))}
  #slut delen på programmet
endrange = next(
  reversed(betsave.keys())
) + 1  #tar hur upp hur många bets det finns och adderar den med ett för att de gör att en for-loop ska kunna fungerar

#här är exemplet i sitt fulla verk:
#print(betsave)











#De här är satt på noll men kommer öka vid nästa stycket. Antal_val betyder antal spel som programmet har gått igenom. Vinst betyder antal arbitrage den har hittat. 
antal_val = 0
vinst = 0





#här så går den igenom lexikonen betsave och kollar om det är ett arbitrage eller inte. Om det är det så publicerar den i filen spel.txt. den lägger till också hur många matcher som den har gått igenom och hur många arbitrage den har hittat.  
for number in range(1, endrange):  # går igenom alla bets och kollar om om betsen oddesen är på spelarans sida.
  
  
  antal_val += 1
  
  tab = betsave[number]  #får tuple med informationen: ((lag),(bet,bet,bet),namn)
  list = betsave[number]
  print("\n",list)
  
  arblist = list[
    1]  # dett a gör att jag år en lista med alla oddsen på det laget
  värde = arbet(arblist)  #här koller den om oddsen är på din sida
  
  if värde[0] == 1:  #om det är det så gå till att berättat hur mycket man ska betta på var sida. om det inte är det fortsätt med nästa lag.
    vinst += 1
    print(tab, "bet number", number)

    värde = arbet(arblist, 150, 1)
    rapport.write(str(tab) + " spelnummer " + str(number) + "\n")
    rapport.write("bets = " + str(värde[1]) + " vinst = " + str(värde[2]) +
                  "\n\n")

print("\n","antal spel =", antal_val, "antal arbitrage =", vinst)

rapport.close()

