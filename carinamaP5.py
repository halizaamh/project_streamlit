cariNama = ['Bram', 'Fauzi', 'Iput', 'Jonathan', 'Icha', 'Rohyatul']
for i in range(len(cariNama)):    
    if cariNama[i]=='Jonathan':
        continue
    print('ini adalah', cariNama[i])
print('-'*20)

#Break
cariNama = ['Bram', 'Fauzi', 'Iput', 'Jonathan', 'Icha', 'Rohyatul']
for i in range(len(cariNama)):
    print('Ini Adalah', cariNama[i])
    if cariNama[i] == 'Jonathan':
        print('Yeay jonathan sudah hadir')
        break
print('-'*20)

#Perulangan While
i = 1
while i > 10 :
    print('No Urut', i)
    i+=1
else:
    print('No Urut Tidak Valid')