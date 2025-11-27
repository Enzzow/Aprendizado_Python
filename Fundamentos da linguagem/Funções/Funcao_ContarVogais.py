def cont_vogais(palavra):
    vogais = [
    'a','e','i','o','u',
    'â','ã','á','à','ê',
    'ẽ','é','è','î','ĩ',
    'í','ì','ô','õ','ó',
    'ò','û','ũ','ù','ú'
    ]
    qntd = 0 

    for i in range(len(palavra)):
        for ii in range(len(vogais)):
            if vogais[ii]==palavra[i]:
             qntd+=1
    
    return qntd


palavra = input(" \nInforme uma palavra e descubra o número de vogais q ela possuí: ").lower()
print(f"\n {palavra} possuí {cont_vogais(palavra)} \n")