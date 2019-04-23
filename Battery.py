from math import *


class battery():
    def __init__(self, listbattery):
        self.metal1 = listbattery[0]
        self.metal2 = listbattery[3]
        self.metal1_mass = listbattery[1]
        self.metal2_mass = listbattery[4]
        self.metal1_solution = listbattery[2]
        self.metal2_solution = listbattery[5]
        # cada solucao possui 100ml e densidade 1g/ml
        self.total_mass = (self.metal1_mass + self.metal2_mass + 2 * (100))
        self.temp = listbattery[6]
        self.ddp = self.calc_ddp()
        self.charge_capacity = self.calc_charge_capacity()
        self.charge_density = self.calc_chargedensity()
        self.energy_density = self.calc_energydensity()
        self.cost = self.calc_cost()

    def calc_ddp(self):
        if (self.metal2["E0"] > self.metal1["E0"]):
            E0 = self.metal2["E0"] - self.metal1["E0"]
            cathode = self.metal2  # +
            anode = self.metal1  # -
            cat_sol = self.metal2_solution
            an_sol = self.metal1_solution
        else:
            E0 = self.metal1["E0"] - self.metal2["E0"]
            cathode = self.metal1  # +
            anode = self.metal2  # -
            cat_sol = self.metal1_solution
            an_sol = self.metal2_solution
        e1 = self.metal1["charge"]
        e2 = self.metal2["charge"]
        if(e1 % e2 == 0):
            if (e1 == e2):
                n = e1  # Poderia ser o e2
            else:
                if(e1 > e2):
                    n = e1/e2
                else:
                    n = e2/e1
        else:
            n = e1*e2
        ddp = E0 - ((8.314*(self.temp + 273.15))/(n*96485))*log(
            (an_sol)/(cat_sol))
        return ddp

    def calc_charge_capacity(self):
        F = 96485.3329

        limit = self.metal1_mass
        metal = self.metal1
        counter_metal = self.metal2
        electrode1 = self.metal1_mass*self.metal2["charge"]
        electrode2 = self.metal2_mass*self.metal1["charge"]
        if ((electrode1/electrode2)/(self.metal1_mass/self.metal2_mass)):
            limit = self.metal2_mass
            metal = self.metal2
            counter_metal = self.metal1

        e_total = (metal["charge"] * limit *
                   counter_metal["charge"]) / (metal["metal_M"])

        return F * e_total / 3600

    def calc_chargedensity(self):
        return self.charge_capacity/self.total_mass

    def calc_energydensity(self):
        pot_hour = self.ddp*self.total_mass
        return pot_hour/self.total_mass

    def calc_pot(self):
        pot = self.ddp * self.charge_capacity
        return pot/1000

    def calc_cost(self):
        cell1_cost = (self.metal1_mass)*self.metal1["metal_price"]/1000  \
            + self.metal1["solution_price"] * \
            (self.metal1["solution_M"]*self.metal1_solution*0.1)
        cell2_cost = (self.metal2_mass)*self.metal2["metal_price"]/1000  \
            + self.metal2["solution_price"] * \
            (self.metal2["solution_M"]*self.metal2_solution*0.1)
        return cell1_cost + cell2_cost
