from smart_battery import smart_Battery


def select(batteries):
    print("\n############################################################################")
    print("AQUI VAMOS SELECIONAR A PILHA MAIS ADEQUADA COM BASE NOS SEUS PARAMETROS")
    print("############################################################################\n")
    inputs_List = [{"name": "a ddp", "unity": "Volts"}, {"name": "a potência", "unity": "Watts"},
                   {"name": "o tempo de uso", "unity": "horas"}, {"name": "a capacidade de carga", "unity": "mAh"}]

    for i in inputs_List:
        i["value"] = input(
            "Qual {} da pilha que você precisa (em {})?".format(i["name"], i["unity"]))
        while (True):
            try:
                i["value"] = float(i["value"])
                break
            except:
                print("O valor inserido nao é um numero, tente novamente")
                i["value"] = input(
                    "Qual {} da pilha que você precisa (em {})?".format(i["name"], i["unity"]))

    tolerance = input(
        "Qual tolerância devemos considerar para a ddp, caso não pudermos chegar a ddp exata (em Volts)?")
    while (True):
        try:
            tolerance = float(tolerance)
            inputs_List.append({"value": tolerance})
            break
        except:
            print("O valor inserido nao é um numero, tente novamente")
            tolerance = input(
                "Qual tolerância devemos considerar para a ddp, caso não seja possível chegar a ddp exata (em Volts)?")

    battery = smart_Battery(inputs_List)
    return (battery.selection(batteries))
