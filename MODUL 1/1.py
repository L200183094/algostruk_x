#dd = {'nama':'joko', 'umur':21, 'asal':'surakarta'}
#for kunci in dd:
#    print(kunci, '<--->', dd[kunci])

#Number 1
string = ''
bar = 1

x = int(input("cetakSiku : "))
#looping Baris
while bar <= x:
    kol = bar

    #Looping Kolom
    while kol > 0:
        string = string + " * "
        kol = kol -1

    string = string + "\n"
    bar = bar +1
print (string)


    
    
