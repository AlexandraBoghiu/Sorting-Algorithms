from time import time
import random

#Bubble Sort
def bubble_sort(v):
    L = len(v)

    for i in range(L - 1):
        for j in range(i + 1, L):
            if v[i] > v[j]:
                v[j], v[i] = v[i], v[j]

#Insertion Sort
def insertion_sort(v):
    L = len(v)

    for i in range(L):
        j = i - 1
        aux = v[i]
        while j >= 0 and v[j] > aux:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = aux
    return v

#Count Sort
def count_sort(v, maxim):
    L = len(v)
    count = [0] * (maxim + 1)
    rez = [0] * L

    for i in range(L):
        count[v[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    nr = L - 1
    while nr >= 0:
        rez[count[v[nr]] - 1] = v[nr]
        count[v[nr]] -= 1
        nr -= 1

    for i in range(L):
        v[i] = rez[i]

#Radix Sort in baza 10
def count_radix_baza10(v, cifra):
    L = len(v)
    count = [0] * 10
    rez = [0] * L

    for i in v:
        aux = (i // cifra) % 10
        count[aux] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = L - 1
    while i >= 0:
        aux = (v[i] // cifra) % 10
        rez[count[aux] - 1] = v[i]
        count[aux] -= 1
        i -= 1

    for i in range(L):
        v[i] = rez[i]

def radix_sort_baza10(v):
    maxim = elementMaxim(v)
    rez = v.copy()

    poz_cifra = 1
    while maxim / poz_cifra:
        count_radix_baza10(rez, poz_cifra)
        poz_cifra *= 10
    return rez

#Radix Sort in baza 16
def count_radix_baza16(v, bit):
    L = len(v)
    count = [0] * 16
    rez = [0] * L

    for i in v:
        count[15 & (i >> bit)] += 1

    for i in range(1, 16):
        count[i] += count[i - 1]

    i = L - 1
    while i >= 0:
        aux = 15 & (v[i] >> bit)
        rez[count[aux] - 1] = v[i]
        count[aux] -= 1
        i -= 1

    for i in range(L):
        v[i] = rez[i]


def radix_sort_baza16(v):
    maxim = elementMaxim(v)
    rez = v.copy()
    bit = 0

    while maxim >> bit:
        count_radix_baza16(rez, bit)
        bit += 4
    return rez

#Merge Sort
def interclasare_merge(st, dr):
    i = 0
    j = 0
    rez = list()

    while i < len(st) and j < len(dr):
        if st[i] < dr[j]:
            rez.append(st[i])
            i += 1
        else:
            rez.append(dr[j])
            j += 1

    while i < len(st):
        rez.append(st[i])
        i += 1

    while j < len(dr):
        rez.append(dr[j])
        j += 1

    return rez

def merge_sort(v):
    L = len(v)
    if L <= 1:
        return v
    else:
        mij = L // 2
        st = merge_sort(v[:mij])
        dr = merge_sort(v[mij:])
        return interclasare_merge(st, dr)

#Quick sort cu mediana din 3
def mediana_din_3(v):
    L = len(v)
    st = 0
    dr = L - 1
    mij = (st + dr) // 2

    if v[st] > v[dr]:
        v[st], v[dr] = v[dr], v[st]
    if v[st] > v[mij]:
        v[st], v[mij] = v[mij], v[st]
    if v[mij] > v[dr]:
        v[mij], v[dr] = v[dr], v[mij]
    return v[mij]

def quick_sort(v):
    L = len(v)
    if L <= 1:
        return v
    pivot = mediana_din_3(v)
    st = list()
    mij = list()
    dr = list()

    for element in v:
        if element < pivot:
            st.append(element)
        elif element == pivot:
            mij.append(element)
        elif element > pivot:
            dr.append(element)

    return quick_sort(st) + mij + quick_sort(dr)

def elementMaxim(v):
    maxim = v[0]
    L = len(v)

    for i in range(L):
        if v[i] > maxim:
            maxim = v[i]
    return maxim



print("Introduceti numarul de teste care vor fi efectuate: ")
nr_teste = int(input())

while(nr_teste > 0):
    print("Alegeti tipul de vector: ")
    print("1. Vector complet random")
    print("2. Vector aproape sortat")
    print("3. Vector sortat descrescator")
    print("4. Vector constant")
    alegere = int(input())

    if(alegere < 1 or alegere > 4):
        print("Alegere invalida!")

    else:
        print("Alegeti tipul elementelor:")
        print("1. int")
        print("2. float")

        alegere_element = int(input())

        if alegere_element < 1 or alegere_element > 2:
            print("Alegere invalida!")
        else:
            print("Introduceti numarul de elemente ale vectorului (de preferat, maxim 1000000):")
            nrElementeVector = int(input())

            print("Introduceti intervalul in care se vor afla elementele")
            capatInf = input("Capatul inferior: ")
            capatSup = input("Capatul superior: ")

            if alegere == 4 and alegere_element == 1:
                numar = random.randint(int(capatInf), int(capatSup))
                lista = [numar for i in range(nrElementeVector)]

            elif alegere_element == 2:
                    lista = [random.uniform(float(capatInf), float(capatSup)) for i in range(nrElementeVector)]
            else:
                    lista = random.sample(range(int(capatInf), int(capatSup)), nrElementeVector)

            if alegere == 2:
                lista[0: len(lista) - len(lista) // 5] = sorted(lista[0: len(lista) - len(lista) // 5])

            if alegere == 3 and alegere_element == 1:
                lista = random.sample(range(int(capatInf), int(capatSup)), nrElementeVector)
                lista.sort(reverse = True)

            if alegere == 3 and alegere_element == 2:
                lista = [random.uniform(float(capatInf), float(capatSup)) for i in range(nrElementeVector)]
                lista.sort(reverse = True)

            print("Doriti afisarea vectorului? Introduceti 1 daca da, 0 daca nu.")
            ok = int(input())

            if ok == 1:
                print("Vectorul initial este: ", lista)
            print("Timpul de executie pentru BubbleSort este: ")
            lista1 = lista.copy()
            if(len(lista)) > 10000:
                print("Eroare! Vectorul este prea mare.")
            else:
                startTime = time()
                bubble_sort(lista1)
                endTime = time()
                print(round(endTime-startTime, 3))
            if (len(lista)) > 10000 and (alegere != 4 or alegere_element == 2):
                print("Timpul de executie pentru InsertionSort este: ")
                print("Eroare! Vectorul este prea mare.")

            else:
                print("Timpul de executie pentru InsertionSort este: ")
                lista2 = lista.copy()
                nrMax = elementMaxim(lista2)
                startTime = time()
                lista2 = insertion_sort(lista2)
                endTime = time()
                print(round(endTime-startTime, 3))

            if alegere_element == 1 and len(lista) < 1000000:
                print("Timpul de executie pentru CountSort este: ")
                lista3 = lista.copy()
                nrMax = elementMaxim(lista3)
                startTime = time()
                count_sort(lista3, nrMax)
                endTime = time()
                print(round(endTime-startTime , 3))
            elif alegere_element == 1:
                print("Timpul de executie pentru CountSort este: ")
                print("Eroare! Vectorul este prea mare.")

            if ((len(lista)) > 10000 and alegere_element == 1 and alegere != 4) or ((len(lista)) > 10000 and alegere_element == 1and int(capatSup) > 100000):
                print("Timpul de executie pentru RadixSort, baza 10 este: ")
                print("Eroare! Vectorul este prea mare.")
            elif alegere_element == 1:
                print("Timpul de executie pentru RadixSort, baza 10 este: ")
                lista4 = lista.copy()
                startTime = time()
                lista4 = radix_sort_baza10(lista4)
                endTime = time()
                print(round(endTime-startTime, 3))

            if alegere_element == 1:
                print("Timpul de executie pentru RadixSort, baza 16 este: ")
                lista5 = lista.copy()
                startTime = time()
                lista5 = radix_sort_baza16(lista5)
                endTime = time()
                print(round(endTime-startTime, 3))

            print("Timpul de executie pentru MergeSort este:")
            lista6 = lista.copy()
            startTime = time()
            lista6 = merge_sort(lista6)
            endTime = time()
            print(round(endTime-startTime, 3))

            print("Timpul de executie pentru QuickSort cu mediana din 3 este: ")
            lista7 = lista.copy()
            startTime = time()
            lista7 = quick_sort(lista7)
            endTime = time()
            print(round(endTime-startTime, 3))


            print("Timpul de executie pentru .sort() este:")
            lista8 = lista.copy()
            startTime = time()
            lista8.sort()
            endTime = time()
            print(round(endTime-startTime, 3))

            print("Timpul de executie pentru sorted este: ")
            lista9 = lista.copy()
            startTime = time()
            lista9 = sorted(lista9)
            endTime = time()
            print(round(endTime-startTime, 3))

    nr_teste -= 1