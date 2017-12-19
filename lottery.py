#I simulated a simple lottery game. Just to see the possible opportunity win 5of6 or 6of6. #What i found is that the lottery not an investment thing.

import collections from random import randint from datetime import datetime from tkinter import *

print(str(datetime.now())) dublike=0 allz=[] sans=[] oyun=[] deneme=0 skor=[] talih= [] oyun_say=0

#create a 6 different number in between 1-49 while len(sans)<6: b=randint(1,49) if b not in sans: sans.append(int(b)) sans.sort()

#check the score of a random plat. if it has a match of 5 or six, put them in a list.

def kar(): global deneme global skor global talih global allz global dublike

deneme=deneme+1 xx=[] #print ("çekili: ",sans) if oyun not in allz: allz.append(oyun) else: dublike=dublike+1 for x in oyun: if x in sans: xx.append(x) #print(xx) #print(deneme, " : ", len(xx))
skor.append(len(xx)) if len(xx)>4: talih.append(oyun) #print(skor)

#print some of the varaibles on the screen def say(): global dublike global sans global talih global skor global oyun_say

print("oyun sayısı:", oyun_say ) print ("aynı kolon saısı: ", dublike ) print ("cekilis :", sans) counter=collections.Counter(skor) print (counter) print("talihli numaralar", talih) print(str(datetime.now()))

#play a 10000 game. you can change it by changing the i value

def says(): global oyun global oyun_say i=1

while i<10000: a=[] while len(a)<6: b=randint(1,49) if b not in a: a.append(int(b))

a.sort() 
i=i+1 oyun= a

#print ("ürün",oyun) oyun_say=i-1
if i%10000 == 0: print(i) print(str(datetime.now()))
kar()

#create a button to play many times.

def sayhello(): says()
say() master =Tk() button= Button(master,text="tıkla", command=sayhello) button.pack() mainloop()

