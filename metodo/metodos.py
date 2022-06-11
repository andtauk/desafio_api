import random


def separar_lista_em_n_colunas(lista, n_colunas):
    lista_colunas = []
    for i in range(0, len(lista), n_colunas):
        lista_colunas.append(lista[i : i + n_colunas])
    return lista_colunas

def generate_random_mac_address():
    mac = [0x00, 0x16, 0x3e, random.randrange(0x00, 0x7f), random.randrange(0x00, 0xff), random.randrange(0x00, 0xff)]
    return ":".join(map(lambda x: "%02x" % x, mac))
    