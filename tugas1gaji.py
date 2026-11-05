print(" === PENGGAJIAN PT. DINGIN DAMAI ===")
karyawan = input ("masukkan nama karyawan:")
pendidikan = input("masukkan data pendidikan:")
jam_kerja = int (input ("masukkan total jam lembur:"))
jabatan = int(input ("masukkan golongan jabatan:"))

gaji_pokok = 5000000
lembur = jam_kerja *35000

Bonus_lembur = max(0, jam_kerja - 8) * 35000

if pendidikan == "smk" :
    bonus_pendidikan = 2.5 / 100
elif pendidikan == "D1":
    bonus_pendidikan = 5/100
elif pendidikan == "d3":
    bonus_pendidikan = 20/100
elif pendidikan == "S1":
    bonus_pendidikan = 30/100 * 30000
else:
    bonus_pendidikan = 0

if jabatan == 1:
    bonus_jabatan = 5/100
elif jabatan == 2:
    bonus_jabatan = 10/100
elif jabatan == 3:
    bonus_jabatan = 15/100
else :
    bonus_jabatan = 0

total_gaji = gaji_pokok + lembur + bonus_pendidikan + bonus_jabatan

print("-" * 35)
print(f"Nama karyawan             : {karyawan}")
print(f"Gaji pokok                :Rp {gaji_pokok:,.0f}".replace(",", "."))
print(f"lembur                    :Rp {lembur:,.0f}".replace(",", "."))
print(f"Bonus pendidikan          :Rp {bonus_pendidikan:,.0f}".replace(",", "."))
print(f"Bonus jabatan             :Rp {bonus_jabatan:,.0f}".replace(",", "."))
print(f"Total gaji                :Rp {total_gaji:,.0f}".replace(",", ".")) 