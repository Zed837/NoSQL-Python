#!/usr/bin/python3.7.1
import time
import sys

from os import path
time.sleep(2)
print( "Loading the DataBase....")
time.sleep(6)


print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(2)
print ("--------------------------DONE---------------------\n")
time.sleep(1)
raspuns = ( "----Now you can write in the database------")
print (raspuns)
def calcul_baza(numeF ,prenumeF ,telefonF ,localizatF ,telefonpF ,cnpF ,dnasteriF  ,numetF ,numemF ):
 print ("[1]Nume Elev= " + numeF + ", [2]Prenume Elev= " + prenumeF + ", [3]Telefon = "
  + telefonF +  " [4]Localizat= " + localizatF +  ", [5]Telefon Parinte " + telefonpF + ", [6]CNP-UL "
   + cnpF + ", [7]Data Nasteri = " + dnasteriF + ", [8]Numele Tata= " + numetF + ", [9]Numele Mama = " + numeF + ". \n")

nume = input( "[1]Scrie numele elevului= ")
prenume = input("[2]Scrie prenumele elevului= ")
telefon = input("[3]Numarul de telefon al elevului= ")
localizat = input("[4]Localizat pe= ")
telefonp = input("[5]Numarul de telefon al parintilor= ")
cnp = input("[6]CNP-UL= ")
dnasteri = input("[7]Data nasterii= ")
numet = input("[8]Numele tatalui= ") 
numem = input("[9]Numele mamei= ")
while True:
   answer = input('Informatile sunt corecte?:da sau nu?')
   if answer.lower().startswith("da"):
       break
      
   elif answer.lower().startswith("nu"):
      print("ok, aparent informatile sunt gresite,REVINO!  ")
      exit()

info = input("[--]Informatile sunt pregatite sa se salveze ,press ENTER!")

time.sleep(2)
print ( "----------------Succesful--------------")
sys.stdout = open("informatiistocate.txt", "a")
print ("-------------------------")
calcul_baza(nume ,prenume ,telefon ,localizat ,telefonp ,cnp ,dnasteri  ,numet ,numem )
sys.stdout.close()

