class MhsTIF(object):
    def __init__(self, nama, umur, kota, NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.nim = NIM

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

a0 = MhsTIF('Hafidz', 19, 'Batang', 'L200170134')
a1 = MhsTIF('ocha', 15, 'Klaten', 'L200170135')
a2 = MhsTIF('Bambang', 12, 'Surakarta', 'L200170187')
a3 = MhsTIF('Supar', 21, 'Wonogiri', 'L200170106')
a4 = MhsTIF('Ningsih', 20, 'Salatiga', 'L200170042')
a5 = MhsTIF('Silvi', 17, 'Purworejo', 'L200170061')
a6 = MhsTIF('Arga', 11, 'Bandung', 'L200170095')
a7 = MhsTIF('Surati', 42, 'Surabaya', 'L200170049')
a8 = MhsTIF('Sukirman', 26, 'Purwodadi', 'L200170079')
a9 = MhsTIF('Danis', 16, 'Salatiga', 'L200170040')
a10 = MhsTIF('Dinsa', 15, 'Purwodadi', 'L200170055')

Daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]


def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)
        
insertionSort(Daftar)
cetakDaftar(Daftar)
