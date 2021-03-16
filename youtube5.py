# Dedi Yanto_71200593
# Universita Kristen Duta Wacana
# Prodi Teknik Informatika
# Struktur Kontrol Kompleks

'''
Kimi ingin mengetahui apa saja bilangan prima yang terdapat pada bilangan bulat 
positif yang diberikan, karena kimi malas dan sangat merepotkan untuk mencari 
bilangan prima pada bilangan bulat positif jika angka yang diberikan besar, 
oleh sebab itu kimi meminta untuk dibuatkan sebuah program yang dapat menampilkan
bilangan prima yang terdapat dalam bilangan positif yang diberikan. Kimi
memberitahukan jika dia ingin mencari bilangan prima apa saja yang terdapat
pada angka 1 – 30 maka program dapat menampilakan bilangan prima yang
terdapat pada jarak 1 – 30, namun jika dia ingin mencari bilangan prima
pada angka 5 – 10, maka program dapat menampilkan bilangan prima yang
terdapat pada jarak 5 – 10. Dan Kimi menginginkan jika output ditampilkan
dari huruf yang terbesar.
'''

'''
Input:
2-10
batas awal = 2
batas akhir = 10
Proses:
2-10
2   3     4        10
1,2 1,2,3 1,2,3,4  1-10

4
1,2,4

Output:

7 5 3 2
'''
# Source Code
lispr = []
prima = []
b = 0

batas_awal = int(input("Masukkan batas awal: "))
batas_akhir = int(input("Masukkan batas akhir: "))

for i in range(batas_awal,batas_akhir+1):
    for j in range(1,i+1):
        if i%j == 0:
            lispr.append(j)
        else:
            continue
    if len(lispr) == 2:
        prima.append(i)
        lispr.clear()
    else:
        lispr.clear()
    
prima.reverse()

for i in range(len(prima)):
    if prima[i] <= 9:
        print(" "+str(prima[i]),end=" ")
    else:
        print(prima[i],end=" ")
    b += 1
    if b%5 == 0:
        print()
    else:
        continue


