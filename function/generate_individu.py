# Generate sebuah gen/kromosom/individu yaitu satu timetable
from copy import deepcopy
from function import randomizer_list

def generate_individu(data):
    space = {}
    for angkatan in data['Kelas']:
        kelas_temp = {}
        for kelas in data['Kelas'][angkatan]:
            hari_temp = {}
            # (Hard Constraint) Tiap kelas harus mendapatkan semua Mapel
            list_mapel = deepcopy(data['List_Mapel'])
            for hari in data['Waktu']:
                alokasi_waktu = 0
                mapel_temp = {}
                i = 0
                for jam in data['Waktu'][hari]:
                    # (Hard Constraint) Tidak ada Mapel yang hanya 1 jam pelajaran di suatu hari
                    if i < 6 and hari != "Jumat":
                        batas = 3
                    else:
                        batas = 2
                    # (Hard Constraint) Alokasi waktu harus sesuai dengan slot waktu yang diberikan
                    if (alokasi_waktu == 0):
                        temp_id = {}
                        temp_mapel, index_mapel = randomizer_list.randomizer(list_mapel)
                        while int(temp_mapel['Alokasi_Jam']) != batas:
                            temp_mapel, index_mapel = randomizer_list.randomizer(list_mapel)
                        # Jika jumlah guru per mapel 2, bagi 2 angkatan tersebut
                        if len(temp_mapel['Guru'][angkatan]) > 1:
                            if kelas < 'F':
                                num = 1
                            else:
                                num = 0
                        else:
                            num = 0
                        # Hilangkan mapel yang telah diberikan kepada kelas
                        list_mapel.pop(index_mapel)
                        # Ambil guru dari list mapel berdasarkan index num
                        temp_guru = temp_mapel['Guru'][angkatan][num]
                        # Kerangka Mapel yang akan diberikan ke kelas pada hari, kelas, dan angkatannya
                        temp_id['Mapel'] = temp_mapel['Mapel']
                        temp_id['ID'] = temp_mapel['ID']
                        temp_id['Guru'] = temp_guru
                        # Mapel berserta Kerangka slot Waktunya
                        mapel_temp[temp_mapel['ID']] = temp_id
                        mapel_temp[temp_mapel['ID']]['Slot_waktu'] = []
                        # counter
                        alokasi_waktu = int(temp_mapel['Alokasi_Jam'])
                    # masukkan slot waktu ke kerangka slot waktu milik mapel
                    mapel_temp[temp_mapel['ID']]['Slot_waktu'].append(jam)
                    alokasi_waktu = alokasi_waktu - 1
                    i = i+1
                hari_temp[hari] = mapel_temp
            kelas_temp[kelas] = hari_temp
        space[angkatan] = kelas_temp

    return space
