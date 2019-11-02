def separa_pessoas_altas_e_baixas(pessoas):
    """ altos >= 1.70 """
    pessoas_altas = []
    pessoas_baixas = []
    
    for altura in pessoas:
        if(altura > 1.70):
            pessoas_altas.append(altura)
        else:
            pessoas_baixas.append(altura)
    return pessoas_altas, pessoas_baixas