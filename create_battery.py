from Battery import battery


def create(metals):
    print("\n###############################################################")
    print("AQUI VOCE IRÁ CRIAR SUA PROPRIA BATERIA")
    print("###############################################################\n")
    print("Escolha os metais que irão compor sua bateria: ")
    List_battery = []
    List_metals = []
    for metal in metals:
        List_metals.append(metals[metal]["name"])
        print(metals[metal]["name"])
    while(True):
        metal1 = (input("\nSelecione um metal dentre os disponíveis: "))
        if (metal1 in List_metals):
            break
        print("\nMetal não disponível, selecione um da lista abaixo:")
        for metal in metals:
            print(metals[metal]["name"])
    metal1 = metals[metal1]
    metal1_mass = float(input("Qual é a massa do primeiro metal (em grama)? \n"))
    metal1_solution = float(
        input("Qual é a concentração da solução para primeiro metal (em mol/L)? \n"))

    List_battery.append(metal1)
    List_battery.append(metal1_mass)
    List_battery.append(metal1_solution)

    while(True):
        metal2 = (input("\nSelecione outro metal dentre os disponíveis: \n"))
        if (metal2 in List_metals):
            break
        print("\nMetal não disponível, selecione um da lista abaixo:\n")
        for metal in metals:
            print(metals[metal]["name"])
    metal2 = metals[metal2]
    metal2_mass = float(input("Qual é a massa do segundo metal (em grama)? "))
    metal2_solution = float(
        input("Qual é a concentração da solução para segundo metal (em mol/L)? "))
    List_battery.append(metal2)
    List_battery.append(metal2_mass)
    List_battery.append(metal2_solution)
    temp = float(input("Em qual temperatura a bateria vai operar (em Celsius)? "))
    List_battery.append(temp)

    bateria = battery(List_battery)
    return bateria
