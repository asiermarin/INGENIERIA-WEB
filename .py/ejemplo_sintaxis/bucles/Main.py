class Main(object):
    """description of class"""

    contador = 7

    while(contador < 15):
        contador += 1
        print(contador)

    print("Fin")
    
    un_string = ""
    conjunto_string = ["aitor", "mikel", "asier", "otro"]
    for un_string in conjunto_string:
        if(un_string == "mikel"):
            break
        print(un_string)

    for i in range(len(conjunto_string)):
        print(conjunto_string[i])

    print("--------------------------------------------------")
    print(conjunto_string[3])

    # Recorre en sentido contrario
    print(conjunto_string[-3])

    # Recorrer varios elementos [desde : hasta], no incluye la ultima 
    print(conjunto_string[1:3])