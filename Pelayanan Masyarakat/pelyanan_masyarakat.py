# import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# menyiapkan himpunan fuzzy 
kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 101), 'ketersediaan_sarpras')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401), 'kepuasan_pelayanan')  

# kejelasan informasi
kejelasan_informasi['tidak_memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [0, 60, 75])
kejelasan_informasi['cukup_memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi['memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [75, 90, 100])

# kejelasan persyaratan
kejelasan_persyaratan['tidak_memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [0, 60, 75])
kejelasan_persyaratan['cukup_memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan['memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [75, 90, 100])

# kemampuan petugas
kemampuan_petugas['tidak_memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [0, 60, 75])
kemampuan_petugas['cukup_memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas['memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [75, 90, 100])

# ketersediaan sarana dan prasarana
ketersediaan_sarpras['tidak_memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [0, 60, 75])
ketersediaan_sarpras['cukup_memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [60, 75, 90])
ketersediaan_sarpras['memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [75, 90, 100])

#kepuasan pelayanan
kepuasan_pelayanan['tidak_memuaskan'] = fuzz.trimf(kepuasan_pelayanan.universe, [0, 50, 75])
kepuasan_pelayanan['kurang_memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100, 150])
kepuasan_pelayanan['cukup_memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan['memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan['sangat_memuaskan'] = fuzz.trimf(kepuasan_pelayanan.universe, [325, 350, 400])

aturan1 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['tidak_memuaskan'])
aturan2 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['tidak_memuaskan'])
aturan3 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['tidak_memuaskan'])
aturan4 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['tidak_memuaskan'])
aturan5 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['tidak_memuaskan'])
aturan6 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan7 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['tidak_memuaskan'])
aturan8 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan9 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan10 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan11 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan12 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan13 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9, aturan10, aturan11, aturan12, aturan13])
system = ctrl.ControlSystemSimulation(engine)

system.input['kejelasan_informasi'] = 80
system.input['kejelasan_persyaratan'] = 60
system.input['kemampuan_petugas'] = 50
system.input['ketersediaan_sarpras'] = 90

system.compute()
print(system.output['kepuasan_pelayanan'])

kepuasan_pelayanan.view(sim=system)
input('Tekan Enter untuk keluar...')