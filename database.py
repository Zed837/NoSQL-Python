#!/usr/bin/python3.7.1
import time
import datetime
import sys
import base64
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
from os import path
x = datetime.datetime.now()
print(x)
time.sleep(1)
print(bcolors.WARNING +  "Loading the DataBase....")
time.sleep(2)
print("Welcome...")
welcome = input("Ai un cont? da/nu: ")
if welcome == "nu":
    while True:
        username  = input("Introdu numele:")
        password  = input("Introdu parola:")
        password1 = input("Reintrodu parola:")
        if password == password1:
            file = open(username+".txt", "w")
            file.write(username+":"+password)

            file.close()
            welcome = "y"
            break
        print("Parolele nu se POTRIVESC!")
 
if welcome == "da":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        file = open(login1+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("Welcome")
            break
        print("Nume incorect sau parola incorecta")
         
print ("--------------------------------------------------------------------------------------------------------")
print ("---------------------------Control the code, control the world--------------------------")
print ("--------------------------------------------------------------------------------------------------------")
time.sleep(4)

raspuns = ( "----Now you can write in the database------")
print (raspuns)
while True:
   answer = input('Doresti sa vezi baza de date?\n')
   if answer.lower().startswith("da"):
     f = open("informatiistocate.txt", "r")
     print(f.read())


   elif answer.lower().startswith("nu"):
      print("ok, acum poti scrie in Baza de Date!  ")
      break

def calcul_baza(numeF ,prenumeF ,telefonF ,localizatF ,telefonpF ,cnpF ,fumatorF, dnasteriF  ,numetF ,numemF ):
  print ("\n [1]Nume Elev= " + numeF + ", \n [2]Prenume Elev= " + prenumeF + ", \n [3]Telefon = " + telefonF +  " \n [4]Localizat= " + localizatF +  ",\n [5]Telefon Parinte " + telefonpF + ",\n [6]CNP-UL " + cnpF + ",\n [7]Fumator= " + fumatorF +  ",\n [8]Data Nasteri = " + dnasteriF + ",\n [9]Numele Tata= " + numetF + ",\n [10]Numele Mama = " + numemF + ".")

nume = input( "[1]Scrie numele elevului= ")
prenume = input("[2]Scrie prenumele elevului= ")
telefon = input("[3]Numarul de telefon al elevului= ")
localizat = input("[4]Localizat pe= ")
telefonp = input("[5]Numarul de telefon al parintilor= ")
cnp = input("[6]CNP-UL= ")
fumator = input("[7]Fumator?= ")
dnasteri = input("[8]Data nasterii= ")
numet = input("[9]Numele tatalui= ") 
numem = input("[10]Numele mamei= ")
while True:
   answer = input('Informatile sunt corecte?:da sau nu?\n')
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
raspuns = ("Victim in databae")
print (raspuns)

calcul_baza(nume ,prenume ,telefon ,localizat ,telefonp ,cnp ,fumator ,dnasteri  ,numet ,numem )
sys.stdout.close()




