loop = 1

while (loop < 10):

    
    nombre = input("Selecciona un sustantivo: ")
    plurarlnon = input("Selecciona un sustantivo en plural: ")
    nombre2 = input("Selecciona un sustantivo: ")
    lugar = input("Nombra un lugar: ")
    adjetivo = input("Selecciona un adjetivo (Describe una palabra): ")
    nombre3 = input("Selecciona un sustantivo: ")

   
    print ("------------------------------------------")
    print ("Hola mi nombre es",nombre,"y tengo muchos", plurarlnon)
    print ("Por suerte existe", nombre2,",")
    print ("Que tiene la formula para ",plurarlnon,"en un lugar de",lugar)
    print ("De todas manera",nombre,"siempre fue" ,adjetivo,".")
    print ()
    print ("A pesar de todo su colega",nombre3,"siempre esta con",nombre,".")
    print ("Eso es todo")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1