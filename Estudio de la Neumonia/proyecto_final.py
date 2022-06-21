import os 
os.system('clear')
print("")
print("┌───────────────────────────────────────────────────────────────┐")
print("│ 🏥 Bienvenidos al sistema de historias clínicas del hospital 🏥 │")
print("└───────────────────────────────────────────────────────────────┘")
print("")
print("")

# **********************
# * VARIABLES GLOBALES *
# **********************
running = True
#database = list()
database = [{'nombre': 'Juan', 'historia': 'resfrio'}, {'nombre': 'pedro', 'historia': 'dolor de muela'}]




# **********************
# *     FUNCIONES      *
# **********************

def show_menu():
    print("")
    print("")
    print("\t\t🛑  1 - Cargar paciente")
    print("\t\t🛑  2 - Buscar paciente")
    print("\t\t🛑  3 - Listar pacientes")
    print("\t\t🛑  4 - Salir")
    print("")
    res = input("INGRESE UNA OPCION ▶ ")
    os.system('clear')
    return res


def response_validate(r):
    validated = False
    num_res = 0
    
    if response.isdigit():
        num_res = int(response)
        if num_res >= 1 and num_res <= 4:
            msg = "esta en rango"
            validated = True
        else:
            msg = "fuera de rango"
    else:
        msg ="Entrada incorrecta"

    return validated,num_res,msg


# **********************
# *  LOOP PRINCIPAL    *
# **********************
while running:
    response = show_menu()
    validated,num_res,msg = response_validate(response)
    if validated:
        if num_res == 1:
            name = input("Ingrese el nombre del paciente ▶ ")
            history = input("Ingrese la historia clínica del paciente ▶ ")
            paciente = {"nombre":name, "historia":history}
            database.append(paciente)
            print(database)

        elif num_res == 2:
            name = input("Ingrese el nombre del paciente  ▶ ")

            finded = True
            for x in range(len(database)):
                if  database[x]["nombre"].lower() == name.lower():
                    print("")
                    print("Paciente encontrado!")
                    print("PACIENTE ENCONTADO | H. CLINICA ▶ ",database[x]["historia"])
                    print("")
                else:
                    finded = False
            
            if not finded:
                print("Paciente no encontrado :( ")

        elif num_res == 3:
            print("")
            print("┌─────────────────────────────┐")
            print("│   LISTADO DE PACIENTES      │")
            print("└─────────────────────────────┘")
            print("")
            for x in range(len(database)):
                print("Nombre ▶ ".ljust(10),database[x]["nombre"], "\t Historia C ▶ ".ljust(10),database[x]["historia"])
            
            print ("FIN DE LISTA")
            
        else:
           running = False
    else:
        print(msg)
        

print("")
print("Aplicación finalizada")
print("")

    