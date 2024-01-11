class Customer:
    def __init__(self, name, units_consumed):
        self.name = name
        self.units_consumed = units_consumed

    def calculateBill(self):
        rate_per_unit = 0.1
        return self.units_consumed * rate_per_unit

    def displayBill(self):
        bill_amount = self.calculateBill()
        print(f"Customer: {self.name}\nUnits Consumed: {self.units_consumed}\nBill Amount: ${bill_amount:.2f}\n")


class ResidentialCustomer(Customer):
    def __init__(self, name, units_consumed, family_members):
        super().__init__(name, units_consumed)
        self.family_members = family_members

    def calculateBill(self):
        base_rate = 0.08
        discount_per_member = 0.02
        discounted_rate = base_rate - (self.family_members * discount_per_member)
        return self.units_consumed * discounted_rate


class CommercialCustomer(Customer):
    def __init__(self, name, units_consumed, business_type):
        super().__init__(name, units_consumed)
        self.business_type = business_type

    def calculateBill(self):
        base_rate = 0.12
        if self.business_type == "Small":
            base_rate *= 0.9  
        elif self.business_type == "Large":
            base_rate *= 1.1  
        return self.units_consumed * base_rate


residentialCustomer = ResidentialCustomer("John Doe", 200, 3)
commercialCustomer = CommercialCustomer("ABC Corp", 500, "Large")

residentialCustomer.displayBill()
commercialCustomer.displayBill()