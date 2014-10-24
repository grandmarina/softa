luku1=int(input("Anna ensimmäinen luku: "))
luku2=int(input("Anna toinen luku: "))
print("Nelilaskin osaa seuraavat toiminnot:")
print("1) Summa")
print("2) Erotus")
print("3) Tulo")
print("4) Osamäärä")
print("5) Potenssi")
print("Antamasi luvut ovat",luku1,"ja",luku2)
x=int(input("Valitse toiminto (1-5): "))

if x == 1:
    val="Summa"
    m="+"
    vast=luku1+luku1
elif x==2:
    val="Erotus"
    m="-"
    vast=luku1-luku2
elif x==3:
    val="Tulo"
    m="*"
    vast=luku1*luku2
elif x==4:
    val="Osamäärä"
    m="/"
    if luku2==0:
        print("Nollalla ei voi jakaa.")         
    else:
        vast=round(luku1/luku2, 2)   
elif x==5:
    val="Potenssi"
    m="^"
    vast=luku1**luku2
elif (x not in [1,2,3,4,5]):
    print("Toimintoa ei tunnistettu.")

if luku2==0 or (x not in [1,2,3,4,5]):
    print("")
else:

    print(val, luku1, m, luku2, "=", vast,)


