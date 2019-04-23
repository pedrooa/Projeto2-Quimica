from comercial_batteries import commercial_battery


class smart_Battery():
    def __init__(self, inputs_list):
        self.ddp = inputs_list[0]["value"]
        self.pot = inputs_list[1]["value"]
        self.time = inputs_list[2]["value"]
        self.charge_capacity = inputs_list[3]["value"]
        self.tolerance = inputs_list[4]["value"]

    def selection(self, batteries):
        parallels = 0
        in_serie = 0
        lowest_price = 100000000000
        List_batteries = []

        for i in batteries:

            in_serie = self.serie(i["ddp"])
            parallels = self.parallel(i["charge_capacity"], i["ddp"]*in_serie)
            total = in_serie*parallels
            price = total*i["price"]
            if(lowest_price > price and price > 0):
                lowest_price = price
            new_battery = commercial_battery(
                i["name"], in_serie, parallels, total, i["price"], price)
            List_batteries.append(new_battery)

        return List_batteries

    def serie(self, ddp_battery):
        if(ddp_battery >= (self.ddp - self.tolerance) and ddp_battery <= (self.ddp + self.tolerance)):
            return 1
        elif(ddp_battery < (self.ddp - self.tolerance)):
            test = float(self.ddp/ddp_battery)
            count = int(self.ddp/ddp_battery)
            if (test > count):
                count += 1
                if (count*ddp_battery > (self.ddp + self.tolerance)):
                    return 0
                return count + 1
            else:
                if (count*ddp_battery > (self.ddp + self.tolerance)):
                    return 0
                return count
        else:
            return 0

    def parallel(self, battery_charge_capacity, ddp_battery):
        time_battery = (battery_charge_capacity*ddp_battery)/self.pot
        if time_battery >= self.time:
            return 1
        else:
            if (time_battery != 0):
                return int(self.time/time_battery) + 1
            return 0
