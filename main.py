from smart_battery import smart_Battery
from Battery import battery
from comercial_batteries import commercial_battery
from create_battery import create
from select_battery import select
import sys
import json

with open('metais.json', 'r') as metals:
    metals = json.load(metals)
with open('batteries.json', 'r') as batteries:
    batteries = json.load(batteries)


while(True):
    user_action = int(input('\n(Você pode criar sua propria pilha ou inserir os dados da sua aplicação para selecionarmos uma pilha adequada. \
            \nDigite: \n(1) para criar sua própria pilha\n(2) para selecionarmos uma para voce\n--> '))

    if (user_action == 1) or (user_action == 2):
        break
    else:
        print("comando inexistente!")


while(True):
    if user_action == 1:
        battery = create(metals)
        print("\n##################################")
        print("RESULTADOS DA SUA BATERIA: ")
        print("####################################\n")
        print("DDP: %.2f Volts" % battery.ddp)
        print("\nCapacidade de carga: %.2f mAh " % battery.charge_capacity)
        print("\nDensidade de carga: %.2f mAh/g " % battery.charge_density)
        print("\nDensidade de energia: %.2f Wh/g" % battery.energy_density)
        print("\nCusto: %.2f Reais" % battery.cost)
    if user_action == 2:
        batteries = select(batteries)
        print("\n##################################")
        print("RESULTADOS DA SUA BATERIA: ")
        print("####################################\n")
        print("Os resultado estão ordenados em ordem crescente de preço: \n")
        # FIltrando a lista de baterias pelo preço
        batteries.sort(key=lambda battery: battery.totalcost)

        count = 1
        for i in batteries:
            if(i.totalbatteries != 0):
                print("\n-------------- Opção {} --------------".format(count))
                count += 1
                print(
                    "Nosso software determinou que uma possível pilha para seu caso será a: ", i.name)
                print("Você irá associar {} delas em série, e {} dessas associações em paralelo".format(
                    i.serie, i.parallel))
                print("Como serão utilizadas {} pilhas no total e o preço unitário é R$ {}".format(
                    i.totalbatteries, i.unitcost))
                print("O custo total será: R$", i.totalcost)
            if(count == 1):
                print("Nao conseguimos selecionar uma pilha com base nos valores inseridos.\n \
                    Tente novamente")

    a = input("\nDigite enter para fechar o programa")
    break
