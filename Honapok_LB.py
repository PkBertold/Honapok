honapok = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus","Szeptember", "Október", "November", "December"]
napok=[31,29,31,30,31,30,31,31,30,31,30,31]
napokSz=[31,28,31,30,31,30,31,31,30,31,30,31]

e=int(input("Év: "))
h=input("Hónap: ")
n=int(input("Nap: "))

index1 = honapok.index(h)


def honapNev():
    if h in honapok:  
        return h
    else:
        return "Hibás adatmegadás"
    
def napValaszto():
    napmax= napok[index1]
    if n<=napmax and n>0:
        return "{}.".format(n)
    else:
        return "Hibás adatmegadás!"


def napValasztoSz():
    napmax2= napokSz[index1]
    if n<=napmax2 and n>0:
        return "{}.".format(n)
    else:
        return "Hibás adatmegadás!"
   
def simaEvek():
    if napValaszto()=="Hibás adatmegadás!":
        return "Hibás adatmegadás!"
    else:
        return (honapNev(),napValaszto())
    
def szokoEvek():
    if napValaszto()=="Hibás adatmegadás!":
        return "Hibás adatmegadás!"
    else:
        return (honapNev(),napValasztoSz())


def milyenEv():
    if e%4==0:
        return szokoEvek()
    elif e%4==1:
        return simaEvek()
    else:
        return "Hibás adatmegadás!"

    
if napValaszto()=="Hibás adatmegadás!":
    print("Hibás adatmegadás!")
elif napValasztoSz()=="Hibás adatmegadás!":
    print("Hibás adatmegadás!")
else:
    print ("{} {} {}.".format(e,h,n))

    
