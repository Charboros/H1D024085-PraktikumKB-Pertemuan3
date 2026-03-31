# import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# menyiapkan himpunan fuzzy 
barang_terjual = ctrl.Antecedent(np.arange(0, 101), 'barang_terjual')
permintaaan = ctrl.Antecedent(np.arange(0, 301), 'permintaaan')
harga_per_item = ctrl.Antecedent(np.arange(0, 100001), 'harga_per_item')
profit = ctrl.Antecedent(np.arange(0, 4000001), 'profit')  
stok_makanan = ctrl.Consequent(np.arange(0, 1001), 'stok_makanan')

# jumlah barang terjual
barang_terjual['rendah'] = fuzz.trimf(barang_terjual.universe, [0, 20, 40])
barang_terjual['sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['tinggi'] = fuzz.trimf(barang_terjual.universe, [60, 80, 100])

# permintaan
permintaaan['rendah'] = fuzz.trimf(permintaaan.universe, [0, 50, 100])
permintaaan['sedang'] = fuzz.trimf(permintaaan.universe, [50, 150, 250])
permintaaan['tinggi'] = fuzz.trimf(permintaaan.universe, [200, 250, 300])

# harga per item
harga_per_item['murah'] = fuzz.trimf(harga_per_item.universe, [0, 20000, 40000])
harga_per_item['sedang'] = fuzz.trimf(harga_per_item.universe, [30000, 50000, 80000])
harga_per_item['mahal'] = fuzz.trimf(harga_per_item.universe, [60000, 80000, 100000])

# profit
profit['rendah'] = fuzz.trimf(profit.universe, [0, 500000, 1000000])
profit['sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000])
profit['tinggi'] = fuzz.trimf(profit.universe, [1500000, 2500000, 4000000])

# stok makanan
stok_makanan['sedang'] = fuzz.trimf(stok_makanan.universe, [100, 500, 900])
stok_makanan['banyak'] = fuzz.trimf(stok_makanan.universe, [600, 800, 1000])

aturan1 = ctrl.Rule(barang_terjual['tinggi'] & permintaaan['tinggi'] & harga_per_item['murah'] & profit['tinggi'], stok_makanan['banyak'])
aturan2 = ctrl.Rule(barang_terjual['tinggi'] & permintaaan['tinggi'] & harga_per_item['murah'] & profit['sedang'], stok_makanan['sedang'])
aturan3 = ctrl.Rule(barang_terjual['tinggi'] & permintaaan['sedang'] & harga_per_item['murah'] & profit['sedang'], stok_makanan['sedang'])
aturan4 = ctrl.Rule(barang_terjual['sedang'] & permintaaan['tinggi'] & harga_per_item['murah'] & profit['sedang'], stok_makanan['sedang'])
aturan5 = ctrl.Rule(barang_terjual['sedang'] & permintaaan['tinggi'] & harga_per_item['murah'] & profit['tinggi'], stok_makanan['banyak'])
aturan6 = ctrl.Rule(barang_terjual['rendah'] & permintaaan['rendah'] & harga_per_item['sedang'] & profit['sedang'], stok_makanan['sedang'])


engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6])
system = ctrl.ControlSystemSimulation(engine)

system.input['barang_terjual'] = 80
system.input['permintaaan'] = 255
system.input['harga_per_item'] = 25000
system.input['profit'] = 3500000

system.compute()
print(system.output['stok_makanan'])

stok_makanan.view(sim=system)
input('Tekan Enter untuk keluar...')