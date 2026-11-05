daftarKaryawan = []
gapok = 5000000
totalgajiPerusahaan = 0
jumlahKaryawan = int(input('Masukkan Jumlah Karyawan\t: '))
for i in range (jumlahKaryawan):
    print(f'Input Karyawan Ke-{i+1}')
    nama = input('Masukkan Nama\t: ')
    golongan = int(input('Masukkan Golongan  (1/2/3)\t: '))
    pendidikan = input('Masukkan Pendidikan (SMA/S1)\t: ').upper()
    jamKerja = float(input('Masukkan Jumlah Jam Kerja\t: '))

    if golongan==1:
        tjGolongan = 0.25/100*gapok
    elif golongan==2: 
        tjGolongan = 5/100*gapok
    elif golongan==3:
        tjGolongan = 10/100*gapok
    else: 
        tjGolongan = 0

    if pendidikan=='SMA':
        tjPendidikan = 12/100*gapok
    elif pendidikan=='S1':
        tjPendidikan = 20/100*gapok
    else: 
        tjPendidikan = 0
    if jamKerja > 160:
        honorLembur = (jamKerja - 160)*35000
    else:
        honorLembur = 0

    totalGaji = gapok + tjGolongan + tjPendidikan + honorLembur
    totalgajiPerusahaan += totalGaji

    daftarKaryawan.append({        
        'nama': nama,
        'golongan': tjGolongan,
        'pendidikan': tjPendidikan,
        'lembur': honorLembur,
        'gaji': totalGaji,
    }) 

print('='*90)
print(f"{'No':<5} | {'Nama':<12} | {'tjGolongan':<13} | {'tjPendidikan':<14} | {'honorLembur':<12} | {'totalGaji':<13}")
print('='*88)
for i in range (len(daftarKaryawan)):
    dk=daftarKaryawan[i]
    print(f"{i+1:<5} | {dk['nama']:<12} | Rp.{dk['golongan']:>10,.0f} | Rp.{dk['pendidikan']:>11,.0f} | Rp.{dk['lembur']:>9,.0f} | Rp.{dk['total']:>10,.0f}")
    print('='*88) 
    print(f"{'Total gaji yang dibayarkan perusahaan' :<70} : Rp.{totalgajiPerusahaan:>10,.0f}")
    print('='*88)