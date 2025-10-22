import random

numero_secreto = random.randint(1,50);
print(numero_secreto)
intento = 0 
adivinado = 0 

#Ciclo repetitivo 
while adivinado != numero_secreto:
     #Intentos (Incrementos y decrementos)
     intento += 1 
     print(F"Este es tu intento {intento}, adivina el numero entre 1 y 50")
     adivinado = int(input("Ingrese el numero "))
     if intento == 5: 
        print("LENTEJAS, demasiados intentos amigo")
        print ("A perdido")
        break
     
   print("Lo he logrado")