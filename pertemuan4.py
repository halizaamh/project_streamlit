#Kode Sepatu ABC
print("==== TOKO SEPATU ICHA IMUT ====")
print("AD = adidas")
print("PM = puma")
print("NK = nike")

kodeSepatu = input("Masukkan Kode Sepatu\t: ").upper()
sizeSepatu = int(input("Masukkan Size Sepatu(36-44)\t: "))

if kodeSepatu == "AD":
   merk = "adidas"
   if sizeSepatu >= 36 and sizeSepatu <= 41: 
      harga = 700000
   elif sizeSepatu >=42 and sizeSepatu <=44:
         harga = 750000
   else:
      harga = 0

elif kodeSepatu == "PM":   
   merk = "puma"
   if sizeSepatu >= 36 and sizeSepatu <=41:
      harga = 600000
   elif sizeSepatu >=42 and sizeSepatu <=44:
      harga = 650000
   else:
    harga = 0
elif kodeSepatu == "NK":
    merk = "nike"
    if sizeSepatu >= 36 and sizeSepatu <=41:
       harga = 500000
    elif sizeSepatu >=42 and sizeSepatu <=44:
       harga = 550000
    else:
       harga = 0
else:
   merk = "Kode Tidak Sesuai"

print("\n === STRUK PEMBELIAN SEPATU ===")
print(f"Merk\t: {merk}")
print(f'Harga\t: {harga}')