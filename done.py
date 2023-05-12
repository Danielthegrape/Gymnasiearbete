from bs4 import BeautifulSoup

#Denna funktion alstrar den viktiga information från Html-koden Betsmart.html, och ger ut den information i ett lexikon. Där i ett lexikon korrisponderar en nyckel till ett värde. Detta fall är nyckeln(lagnamnet) och värdet(oddsen)
def Mall(name_html,
         tab_tag,
         tab_class,
         name_tag,
         name_class,
         bet_tag,
         bet_class,
         n=0):

  with open(name_html, 'r') as html_file:
    #öppnar filen med HTML scirpten
    contentHtml = html_file.read()

#ger en variable HTML scripten
  soup = BeautifulSoup(contentHtml, 'lxml')
  #Omvandlar Html-koden till en form som pogrammet kan arbeta med
  tabs = soup.find_all(tab_tag, class_=tab_class)
  #letar upp alla tabbar. En tabb är en match som innehåller informatione om oddsen och lagnamnet på lagen som möter vrandra.
    #find all gör att den tar med alla tabbar. 
    
  

  lexikon = {}
  #den här gör att den tar en tabb i taget från tabs för att en python klara bara av det 
  for tab in tabs:
    
    #för varje match
    versus = []
    betsin = []
    #gör listor för att spara informationenen
    versus.clear()
    betsin.clear()

    #rensar listan för de kommande matcherna med de kommande lagens namn och odds.
    names = tab.find_all(name_tag, class_=name_class)
   #detta tar namnet från alla tabbar och lägger det i en sorts lista. 
    
    #Samma sak är det här där den alstrar namne från tabben och sätter det i en lista.
    for name in names:
     
     #namnen är inte riktigt klara i med att de fortfarande innehåller onödiga tecken/ mellanslag. 
      show = name.text
      
      #lägger till namnen i en lista med detta kommandot 
      versus.append(show)
      
    #omvandlar listan till ett format som kan vara i ett lexikon. Lexikon är en lista som består av nycklar och värden. nycklarna korresponderar till ett värde. Nycklarna i vårat fall är namnen och värderna är oddsen. 
    saveversus = tuple(versus)
    #det här för senare anvädning 
    

    #den här upprepas samma saker fast för bets
    bets = tab.find_all(bet_tag, class_=bet_class)
    for bet in bets:


      showbet = str(bet.text).strip()

      #detta är för att programmet itne ska  krasha om tabben har ett odds som saknas 
      try:
        number = float(showbet)
        betsin.append(number)
      except:
        betsin.append(0)
    #det finns en möjlighet där det finns i tabben nummer som inte är oddsen. Detta tar bort det. 
    if len(betsin) > 3:
      while len(betsin) > 3:
        betsin.pop(-1)

    #konverterar detta till en form som lexikon kan ta 
    savebets = tuple(betsin)
    #print(savebets)

    #Här händer detta som jag berätta om att man lägger nyckeln(namnet på laget) med värdet(oddsen til den matchen)
    lexikon[saveversus] = savebets
  #text = name_html
  #name = str(text).replace('.html', '')
  #lexikon[name] = 0

  return lexikon























#Detta är en funktion som räknar ut om det är ett aribtrage eller inte. Värderna korrisponderar till utbetalning från betting sidan(saldo), Determintor, extra funktion som bestämmer om den ska visa och publicera arbitrage om den hittar en. Koden i main gör att determinator blir till 1 när den hittar ett. 
def arbet(
  odds,
  saldo=100,
  determinator=0
):  #fixa så att det inte finns något antal,men bara värde, så att värde är en lista
  

  #listor som ska vara med för att programmet ska kunna fungera
  term = []  # är för att spara alla addera sanolikheterna från betsen
  dethela = []
  sequellist = []
  prequellist = []
  
  p = 0 #omställer obalansen i sannolikheten 
  
  for n in odds:  #här så omvandlas oddsen till indirektat sannolikheter
    try:
      p += 1 / n  # här så adderas sannolikheterna för att kolla om de är mindre än 1
      tarm = 1 / n
      term.append(tarm)
    except:  #det som som finns här är om programmet har gått snett
      #print("saknas ett bett")
      print(odds)  #
  Sannolik = round(
    p, 3)  # avrundar sannolikheter till de tre närmaste decimalerna
  
  risktest = 1  #checka om koden fungerar. Den tittar om sannolikheten är under den
  #checkar om oddsen är indre än risktest
  
  #Detta gör för att se om oblansen är på din sida eller inte. Om den är över 1 så är den inte på din sida. Om den är under ett så är den på din sida och du kan starta tjäna pengar.
  if p > risktest:
    pass
    print('SVAR: oddsen är inte på din sida', Sannolik)
    värde = [0]

    return värde

  #Den här funktion kommer vid nästa varv. I main koden där det här funktionen har givit ett värde till determinator till 1. 
  elif determinator == 1:  #det är för en screen när du har fått ett aribratage
    # ger information ionen om determinator är = 1
    for n in term:  #gångrar alla oddsen med Utbetalning(slad)o för att kunna ta reda på  hur mycket man kan Utbetalningen blir.
      summan = saldo * n  #ta reda hur cyket kostnade blir från var bet
      summan = round(summan, 2)  #av rundara kosntaden till två decilmaler
      dethela.append(
        summan)  # sparar kostanerna till en lista som heter det hela

    for n in dethela:

      siffra = dethela.index(
        n)  # brättar vilkne ordning och hur mycket du ska betta på var bet
      siffra += 1

      print(str(siffra) + ". betta =", int(round(n, 0)), "eller", n)
      prequellist.append(round(n, 0))

    sum = 0
    for n in dethela:
      sum -= n
    throw1 = 0

    for n in dethela:  #tar reda pu hur mycket man går i vinst med och berättar det för persoenen
      siffra = dethela.index(n)
      siffra += 1
      svar = odds[throw1] * n + sum
      svar = round(svar, 2)
      throw1 += 1

      print("vinst på " + str(siffra) + " = " + str(int(round(svar, 0))),
            "eller", svar)
      sequellist.append(svar)
      #rapport.write("vinst på " + str(siffra) + " = " + str(int(round(svar, 0))),"eller",svar,"\n")
    värde = [
      1, prequellist, sequellist
    ]  # sparar hur mycket som man ska betta och hur mycket man kommer vinna

    return värde

  else:  # den här
    #print(Sannolik)
    värde = [1]  #är här för atkvira determinator .
    return värde


