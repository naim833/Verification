#!/usr/bin/python3
str1=input("Input word : ")
print("Lettre  Valeur ck1 ck2")
ck1=0
ck2=0
for i in range(len(str1)):   
    ck1 = ck1 + ord(str1[i])
    ck2 = ck2 + ck1
    print("   "+str1[i]+"     "+str(ord(str1[i]))+ "   "+str(ck1)+"  "+str(ck2) )   
    

