N=int(input("Introduzca la dimensión de la matriz cuadrada: "));
i=1;
Num=2;
Numeros_primos=[];

while (i<=(N*N)):
    if (not(Num%2==0) and not (Num%3==0) and not (Num%5==0) and not (Num%7==0)):
        Numeros_primos.append(Num);
        i+=1;
    if ((Num==2 or Num==3 or Num==5 or Num==7)):
        Numeros_primos.append(Num);
        i+=1
    Num+=1
suma=0;
filas="";
print("La matriz de números primos consecutivos es:");
for j in range (0,N):
    p=j*N
    for h in range (p,N*(j+1)):
            print("\t", Numeros_primos[h], end=" ");
    print();
print("La diagonal de la matriz es:");
for j in range (0,N):
    p=j*N
    for h in range (p,N*(j+1)):
        if (j==0 or (h>=p+j)):
            print("\t", Numeros_primos[h], end=" ");
        else:
            print("\t","-", end=" ");
    print();
for j in range (0,N):
    p=j*N
    for h in range (p,N*(j+1)):
        if (j==0 or (h>=p+j)):
            suma+=Numeros_primos[h]
print ("La suma de los elementos en la matriz diagonal superior es:", suma);