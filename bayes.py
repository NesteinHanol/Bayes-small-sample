#Python 3.6.5
dosya=open("train.txt") #train dosyasinin okunmasi
x=dosya.readlines()
t=len(x)
liste=[]
for i in range(1,t):    
    liste.append(x[i].split(","))

for i in range(0,t-1): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=liste[i][len(liste[0])-1].split()
    liste[i][len(liste[0])-1]=x[0]


badtoplam=0
goodtoplam=0
for i in range(0,len(liste)):
    if(liste[i][8] == "good"):
        goodtoplam=goodtoplam+1
    elif(liste[i][8] == "bad"):
        badtoplam=badtoplam+1
        
classsTablo=[["bad",badtoplam/800.0],["good",goodtoplam/800.0]]

credit_history = ['critical/other existing credit', 'delayed previously', 'existing paid', 'no credits/all paid', 'all paid']
purpose = ['furniture/equipment', 'repairs', 'new car', 'radio/tv', 'business', 'other', 'used car', 'education']
employment = ['1<=X<4', '>=7', '<1', '4<=X<7', 'unemployed']
personal_status = ['male div/sep', 'male mar/wid', 'male single', 'female div/dep/mar']
property_magnitude = ['real estate', 'life insurance', 'no known property', 'car']
housing=['rent', 'own', 'for free']
job=['high qualif/self emp/mgmt', 'skilled', 'unskilled resident', 'unemp/unskilled non res']
own_telephone=['yes', 'none']
classs = ['bad', 'good']

# ---------------Bayes Agina Gore Tablolarin Olusturulmasi-------------------------

#purposeTablo =>> classs,housing,purpose,DEGER
purposeTablo=[]
for i in range(0,len(classs)):
    for k in range(0,len(housing)):
        for j in range(0,len(purpose)):
            purposeTablo.append([classs[i],housing[k],purpose[j],"DEGER"])
    
#housingTablo =>> class,property_magnitude,housing,DEGER
housingTablo=[]
for i in range(0,len(classs)):
    for k in range(0,len(property_magnitude)):
        for j in range(0,len(housing)):
            housingTablo.append([classs[i],property_magnitude[k],housing[j],"DEGER"])

#personal_statusTablo =>> class,housing,personal_status,DEGER
personal_statusTablo=[]
for i in range(0,len(classs)):
    for k in range(0,len(housing)):
        for j in range(0,len(personal_status)):
            personal_statusTablo.append([classs[i],housing[k],personal_status[j],"DEGER"])

#property_magnitudeTablo =>> class,property_magnitude,DEGER
property_magnitudeTablo=[]
for i in range(0,len(classs)):
    for k in range(0,len(property_magnitude)):
            property_magnitudeTablo.append([classs[i],property_magnitude[k],"DEGER"])


#employmentTablo =>> class,job,employment,DEGER
employmentTablo=[]
for i in range(0,len(classs)):
    for k in range(0,len(job)):
        for j in range(0,len(employment)):
            employmentTablo.append([classs[i],job[k],employment[j],"DEGER"])


#jobTablo =>> class,property_magnitude,job,DEGER
jobTablo=[]
for i in range(0,len(classs)):
    for k in range(0,len(property_magnitude)):
        for j in range(0,len(job)):
            jobTablo.append([classs[i],property_magnitude[k],job[j],"DEGER"])


#own_telephoneTablo =>> calss,job,own_telephone,DEGER
own_telephoneTablo=[]
for i in range(0,len(classs)):
    for k in range(0,len(job)):
        for j in range(0,len(own_telephone)):
            own_telephoneTablo.append([classs[i],job[k],own_telephone[j],"DEGER"])


#credit_historyTablo =>> class,own_telephone,credit_history,DEGER
credit_historyTablo=[]
for i in range(0,len(classs)):
    for k in range(0,len(own_telephone)):
        for j in range(0,len(credit_history)):
            credit_historyTablo.append([classs[i],own_telephone[k],credit_history[j],"DEGER"])

##-----------OLASILIK DEGERLERİ DOLDURMA -----------------Olusturulan Tablolara Olasilik Degerlerinin Atanmasi
            
##purposeTablo =>> classs,housing,purpose,DEGER  -- 8 , 5 , 1 ,deger -- (index degerileri)
toplam=0
toplamdeger=0
for i in range(0,len(purposeTablo)):
    
    for k in range(0,len(liste)):
        if (purposeTablo[i][0] == liste[k][8]) and (purposeTablo[i][1] == liste[k][5]):
            toplam=toplam+1
            
    for k in range(0,len(liste)):
        if (purposeTablo[i][0] == liste[k][8]) and (purposeTablo[i][1] == liste[k][5]) and (purposeTablo[i][2]==liste[k][1]):
            toplamdeger=toplamdeger+1
    purposeTablo[i][3]=toplamdeger/float(toplam)
    toplamdeger=0
    toplam=0

#housingTablo =>> class,property_magnitude,housing,DEGER -- 8 , 4 , 5 ,deger -- (index degerileri)
toplam=0
toplamdeger=0
for i in range(0,len(housingTablo)):
    
    for k in range(0,len(liste)):
        if (housingTablo[i][0] == liste[k][8]) and (housingTablo[i][1] == liste[k][4]):
            toplam=toplam+1
            
    for k in range(0,len(liste)):
        if (housingTablo[i][0] == liste[k][8]) and (housingTablo[i][1] == liste[k][4]) and (housingTablo[i][2]==liste[k][5]):
            toplamdeger=toplamdeger+1
    housingTablo[i][3]=toplamdeger/float(toplam)
    toplamdeger=0
    toplam=0

#personal_statusTablo =>> class,housing,personal_status,DEGER -- 8 , 5 , 3 deger -- (index degerileri)
toplam=0
toplamdeger=0
for i in range(0,len(personal_statusTablo)):
    
    for k in range(0,len(liste)):
        if (personal_statusTablo[i][0] == liste[k][8]) and (personal_statusTablo[i][1] == liste[k][5]):
            toplam=toplam+1
            
    for k in range(0,len(liste)):
        if (personal_statusTablo[i][0] == liste[k][8]) and (personal_statusTablo[i][1] == liste[k][5]) and (personal_statusTablo[i][2]==liste[k][3]):
            toplamdeger=toplamdeger+1
    personal_statusTablo[i][3]=toplamdeger/float(toplam)
    toplamdeger=0
    toplam=0

#property_magnitudeTablo =>> class,property_magnitude,DEGER -- 8 , 4 , deger -- (index degerileri)
toplam=0
toplamdeger=0
for i in range(0,len(property_magnitudeTablo)):
    
    for k in range(0,len(liste)):
        if (property_magnitudeTablo[i][0] == liste[k][8]) :
            toplam=toplam+1
            
    for k in range(0,len(liste)):
        if (property_magnitudeTablo[i][0] == liste[k][8]) and (property_magnitudeTablo[i][1] == liste[k][4]) :
            toplamdeger=toplamdeger+1
    property_magnitudeTablo[i][2]=toplamdeger/float(toplam)
    toplamdeger=0
    toplam=0
    
#employmentTablo =>> class,job,employment,DEGER -- 8 , 6 , 2 ,deger -- (index degerileri)
toplam=0
toplamdeger=0
for i in range(0,len(employmentTablo)):
    
    for k in range(0,len(liste)):
        if (employmentTablo[i][0] == liste[k][8]) and (employmentTablo[i][1] == liste[k][6]):
            toplam=toplam+1
            
    for k in range(0,len(liste)):
        if (employmentTablo[i][0] == liste[k][8]) and (employmentTablo[i][1] == liste[k][6]) and (employmentTablo[i][2]==liste[k][2]):
            toplamdeger=toplamdeger+1
    employmentTablo[i][3]=toplamdeger/float(toplam)
    toplamdeger=0
    toplam=0
    
#jobTablo =>> class,property_magnitude,job,DEGER -- 8 , 4 , 6 ,deger -- (index degerileri)
toplam=0
toplamdeger=0
for i in range(0,len(jobTablo)):
    
    for k in range(0,len(liste)):
        if (jobTablo[i][0] == liste[k][8]) and (jobTablo[i][1] == liste[k][4]):
            toplam=toplam+1
            
    for k in range(0,len(liste)):
        if (jobTablo[i][0] == liste[k][8]) and (jobTablo[i][1] == liste[k][4]) and (jobTablo[i][2]==liste[k][6]):
            toplamdeger=toplamdeger+1
    jobTablo[i][3]=toplamdeger/float(toplam)
    toplamdeger=0
    toplam=0

#own_telephoneTablo =>> calss,job,own_telephone,DEGER -- 8 , 6 , 7 ,deger -- (index degerileri)
toplam=0
toplamdeger=0
for i in range(0,len(own_telephoneTablo)):
    
    for k in range(0,len(liste)):
        if (own_telephoneTablo[i][0] == liste[k][8]) and (own_telephoneTablo[i][1] == liste[k][6]):
            toplam=toplam+1
            
    for k in range(0,len(liste)):
        if (own_telephoneTablo[i][0] == liste[k][8]) and (own_telephoneTablo[i][1] == liste[k][6]) and (own_telephoneTablo[i][2]==liste[k][7]):
            toplamdeger=toplamdeger+1
    own_telephoneTablo[i][3]=toplamdeger/float(toplam)
    toplamdeger=0
    toplam=0

#credit_historyTablo =>> class,own_telephone,credit_history,DEGER -- 8 , 7 , 0 ,deger -- (index degerileri)
toplam=0
toplamdeger=0
for i in range(0,len(credit_historyTablo)):
    
    for k in range(0,len(liste)):
        if (credit_historyTablo[i][0] == liste[k][8]) and (credit_historyTablo[i][1] == liste[k][7]):
            toplam=toplam+1
            
    for k in range(0,len(liste)):
        if (credit_historyTablo[i][0] == liste[k][8]) and (credit_historyTablo[i][1] == liste[k][7]) and (credit_historyTablo[i][2]==liste[k][0]):
            toplamdeger=toplamdeger+1
    credit_historyTablo[i][3]=toplamdeger/float(toplam)
    toplamdeger=0
    toplam=0  


##fark=[]
##var=0
##for i in range(0,len(liste)):
##    for s in range(0,len(fark)):
##        if liste[i][8]==fark[s]:
##            var=1
##    if var==0:
##        fark.append(liste[i][8])
##    var=0

####### H E S A P L A M A -------------------------Bayes Agi Test Kaydi Olasilik Hesaplamalari

dosya=open("test.txt") #test tablosunun okunmasi
x=dosya.readlines()
t=len(x)
liste2=[]
for i in range(1,t):    
    liste2.append(x[i].split(","))

for i in range(0,t-1): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=liste2[i][len(liste2[0])-1].split()
    liste2[i][len(liste2[0])-1]=x[0]

#credit_history,purpose,employment,personal_status,property_magnitude,housing,job,own_telephone,class

#purposeTablo =>> classs,housing,purpose,DEGER  -- 8 , 5 , 1 ,deger -- (index degerileri)
#housingTablo =>> class,property_magnitude,housing,DEGER -- 8 , 4 , 5 ,deger -- (index degerileri)
#personal_statusTablo =>> class,housing,personal_status,DEGER -- 8 , 5 , 3 deger -- (index degerileri)
#property_magnitudeTablo =>> class,property_magnitude,DEGER -- 8 , 4 , deger -- (index degerileri)
#employmentTablo =>> class,job,employment,DEGER -- 8 , 6 , 2 ,deger -- (index degerileri)
#jobTablo =>> class,property_magnitude,job,DEGER -- 8 , 4 , 6 ,deger -- (index degerileri)
#own_telephoneTablo =>> calss,job,own_telephone,DEGER -- 8 , 6 , 7 ,deger -- (index degerileri)
#credit_historyTablo =>> class,own_telephone,credit_history,DEGER -- 8 , 7 , 0 ,deger -- (index degerileri)
dogrupozitif=0
dogrunegatif=0
yanlispozitif=0
yanlisnegatif=0
#-------PAY ------------------------   Pay Kisminin Hesaplanmasi 
for i in range(0,len(liste2)):
    sonucclass = "bad"
    
    for c in range(0,len(credit_historyTablo)):
        if (credit_historyTablo[c][0] == sonucclass) and (credit_historyTablo[c][1] == liste2[i][7]) and (credit_historyTablo[c][2]==liste2[i][0]):
            
            P_credit_history = credit_historyTablo[c][3]

    for c in range(0,len(purposeTablo)):
        if (purposeTablo[c][0] == sonucclass) and (purposeTablo[c][1] == liste2[i][5]) and (purposeTablo[c][2]==liste2[i][1]):
            
            P_purposeTablo = purposeTablo[c][3]


    for c in range(0,len(employmentTablo)):
        if (employmentTablo[c][0] == sonucclass) and (employmentTablo[c][1] == liste2[i][6]) and (employmentTablo[c][2]==liste2[i][2]):
            
            P_employmentTablo = employmentTablo[c][3]
            

    for c in range(0,len(personal_statusTablo)):
        if (personal_statusTablo[c][0] == sonucclass) and (personal_statusTablo[c][1] == liste2[i][5]) and (personal_statusTablo[c][2]==liste2[i][3]):
            
            P_personal_statusTablo = personal_statusTablo[c][3]  


    for c in range(0,len(property_magnitudeTablo)):
        if (property_magnitudeTablo[c][0] == sonucclass) and (property_magnitudeTablo[c][1] == liste2[i][4]) :
            
            P_property_magnitudeTablo = property_magnitudeTablo[c][2]  


    for c in range(0,len(housingTablo)):
        if (housingTablo[c][0] == sonucclass) and (housingTablo[c][1] == liste2[i][4]) and (housingTablo[c][2]==liste2[i][5]):
            
            P_housingTablo = housingTablo[c][3]  


    for c in range(0,len(jobTablo)):
        if (jobTablo[c][0] == sonucclass) and (jobTablo[c][1] == liste2[i][4]) and (jobTablo[c][2]==liste2[i][6]):
            
            P_jobTablo = jobTablo[c][3]

    for c in range(0,len(own_telephoneTablo)):
        if (own_telephoneTablo[c][0] == sonucclass) and (own_telephoneTablo[c][1] == liste2[i][6]) and (own_telephoneTablo[c][2]==liste2[i][7]):
            
            P_own_telephoneTablo = own_telephoneTablo[c][3]

    for c in range(0,len(classsTablo)):
        if (classsTablo[c][0]==sonucclass):
            P_classTablo=classsTablo[c][1]
    
    
    paydegeri=P_credit_history*P_purposeTablo*P_employmentTablo*P_personal_statusTablo*P_property_magnitudeTablo*P_housingTablo*P_jobTablo*P_own_telephoneTablo*P_classTablo

#--------------PAYDA------------------------------------ payda kisminin hesaplanmasi 
    sonucclass = "good"
    
    for c in range(0,len(credit_historyTablo)):
        if (credit_historyTablo[c][0] == sonucclass) and (credit_historyTablo[c][1] == liste2[i][7]) and (credit_historyTablo[c][2]==liste2[i][0]):
            
            P_credit_history = credit_historyTablo[c][3]

    for c in range(0,len(purposeTablo)):
        if (purposeTablo[c][0] == sonucclass) and (purposeTablo[c][1] == liste2[i][5]) and (purposeTablo[c][2]==liste2[i][1]):
            
            P_purposeTablo = purposeTablo[c][3]


    for c in range(0,len(employmentTablo)):
        if (employmentTablo[c][0] == sonucclass) and (employmentTablo[c][1] == liste2[i][6]) and (employmentTablo[c][2]==liste2[i][2]):

            P_employmentTablo = employmentTablo[c][3]
            

    for c in range(0,len(personal_statusTablo)):
        if (personal_statusTablo[c][0] == sonucclass) and (personal_statusTablo[c][1] == liste2[i][5]) and (personal_statusTablo[c][2]==liste2[i][3]):
            
            P_personal_statusTablo = personal_statusTablo[c][3]  


    for c in range(0,len(property_magnitudeTablo)):
        if (property_magnitudeTablo[c][0] == sonucclass) and (property_magnitudeTablo[c][1] == liste2[i][4]) :
            
            P_property_magnitudeTablo = property_magnitudeTablo[c][2]  


    for c in range(0,len(housingTablo)):
        if (housingTablo[c][0] == sonucclass) and (housingTablo[c][1] == liste2[i][4]) and (housingTablo[c][2]==liste2[i][5]):
            
            P_housingTablo = housingTablo[c][3]  


    for c in range(0,len(jobTablo)):
        if (jobTablo[c][0] == sonucclass) and (jobTablo[c][1] == liste2[i][4]) and (jobTablo[c][2]==liste2[i][6]):
            
            P_jobTablo = jobTablo[c][3]

    for c in range(0,len(own_telephoneTablo)):
        if (own_telephoneTablo[c][0] == sonucclass) and (own_telephoneTablo[c][1] == liste2[i][6]) and (own_telephoneTablo[c][2]==liste2[i][7]):
            
            P_own_telephoneTablo = own_telephoneTablo[c][3]

    for c in range(0,len(classsTablo)):
        if (classsTablo[c][0]==sonucclass):
            P_classTablo=classsTablo[c][1]
    
    paydaikincikisimdegeri=P_credit_history*P_purposeTablo*P_employmentTablo*P_personal_statusTablo*P_property_magnitudeTablo*P_housingTablo*P_jobTablo*P_own_telephoneTablo*P_classTablo


    if ( paydegeri==0 and paydaikincikisimdegeri==0):
        #print ("i degeri = ",i)
        pass
    else:
        
        PSONUC = paydegeri/(paydegeri+paydaikincikisimdegeri)
        
    sonucclass=liste2[i][8]
    if  PSONUC>0.5 :
        ff="class bad"
        #print("bad")
    else:
        ff="class good"
        #print("good")
        
    if ff=="class bad" and sonucclass=="bad":
        #dogru pozitif
        dogrupozitif = dogrupozitif+1
        dd="dogru clasa atanmis"
        
    if ff=="class bad" and sonucclass=="good":
        #yanlis pozitif
        yanlispozitif=yanlispozitif+1
        dd="farkli clasa atanmis"
        
    if ff=="class good" and sonucclass=="good":
        #dogru negatif
        dogrunegatif=dogrunegatif+1
        dd="dogru clasa atanmis"
        
    if ff=="class good" and sonucclass=="bad":
        #yanlis negatif
        yanlisnegatif=yanlisnegatif+1
        dd="farkli clasa atanmis"

dogrupozitiforani=dogrupozitif/(dogrupozitif+yanlisnegatif)
#yanlispozitiforani=yanlispozitif/(yanlispozitif+dogrunegatif)
dogrunegatiforani=dogrunegatif/(dogrunegatif+yanlispozitif)
#yanlisnegatiforani=yanlisnegatif/(yanlisnegatif+dogrupozitif)
dogruluk=(dogrupozitif+dogrunegatif)/(dogrupozitif+dogrunegatif+yanlispozitif+yanlisnegatif)

print ("Dogru Pozitif Sayisi = " ,dogrupozitif)
print ("Dogru Negatif Sayisi = ",dogrunegatif)
##print ("Yanlis Pozitif Sayisi = ",yanlispozitif)
##print ("Yanlis Negatif Sayisi = ",yanlisnegatif)
print ("--------------------------------------------------")
print ("Dogru Pozitif Orani = ",dogrupozitiforani)
print ("Dogru Negatif Orani = ",dogrunegatiforani)
##print ("Yanlis Pozitif Orani = ",yanlispozitiforani)
##print ("Yanlis Negatif Orani = ",yanlisnegatiforani)
print ("Dogruluk = ",dogruluk)
