# Mengambil data guru secara uniqe yang terdapat pada list_mape
def filter_guru(data):
    list_guru = []
    for i in data['List_Mapel']:
        for j in i['Guru']:
            for k in i['Guru'][j]:
                if k not in list_guru:
                    list_guru.append(k)

    data['Guru'] = list_guru
