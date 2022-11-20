# Cost Function
def cost_function(gen, data):
    cost_cons1 = 0
    cost_cons2 = 0
    
    # Kerangka penampungan slot waktu guru
    guru = {data['Guru'][i]: {'Slot_waktu': []} for i in range(0, len(data['Guru']))}
    for i in guru:
        guru[i]['Slot_waktu'] = {}
        for j in data['Waktu']:
            guru[i]['Slot_waktu'][j] = []

    # Menelusuri gen
    for angkatan in gen:
        for kelas in gen[angkatan]:
            for hari in gen[angkatan][kelas]:
                mapel_sehari = {}
                mapel_sehari['Mapel'] = []
                for Id in gen[angkatan][kelas][hari]:
                    # Masukkan slot waktu tiap guru
                    for slot in gen[angkatan][kelas][hari][Id]['Slot_waktu']:
                        guru[gen[angkatan][kelas][hari][Id]['Guru']]['Slot_waktu'][hari].append(slot)
                    # Mapel sehari ada apa aja ngitung total Id mapel
                    mapel_sehari['Mapel'].append(gen[angkatan][kelas][hari][Id]['Mapel'])
                # (Soft Constraint) Jika ada mata pelajaran yang sama yang dibagi 2 berada di satu hari yang sama (+1)
                result = dict((i, mapel_sehari['Mapel'].count(i)) for i in mapel_sehari['Mapel'])
                if len(result) < len(mapel_sehari['Mapel']):
                    cost_cons1 += 1

    # (Soft Constraint) Jika ada Guru yang sama di slot waktu yang sama disetiap 1 hari pada kelas yang terkait (irisan) (+1)
    for j in guru:
        guru[j]['result'] = []
        for k in guru[j]['Slot_waktu']:
            result = dict((i, guru[j]['Slot_waktu'][k].count(i))for i in guru[j]['Slot_waktu'][k])
            if len(result) < len(guru[j]['Slot_waktu'][k]):
                cost_cons2 += 1
            guru[j]['result'].append(result)
        
    return cost_cons1 + cost_cons2, cost_cons1, cost_cons2, guru
