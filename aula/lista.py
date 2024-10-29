numeros = [1,2,3,4,5]

print(numeros)

#Exibir o primeiro item da lista 
print(numeros[0])

#Exibir o ultimo item da lista 
print(numeros[-1])

#removendo um elemento da lista 
numeros.remove(3)

print(numeros)


#exibir elementos 
print("Exibindo todos esses valores")
for numero in numeros:
    print("Proximo num")
    print(numero + 1 )


#Verificando se o valor 2 está na Lista 
if 2 in numeros: 
    print("o numero 2 está na lista")
else: 
    print("o numero 2 não está na lista ")