# Need to create a class to work with my functions from assignment 1 (dspt7_utilities)
class Business():
    def __init__(self, name, number, street, city):
        self.name = name
        self.number = number
        self.street = street
        self.city = city

    @property
    def name_number(self):
        return f"{self.name}'s phone number is {self.number}"

    @property
    def name_address(self):
        return f"{self.name} is located on {self.street} in {self.city}"

if __name__ == "__main__":

    businesses = [
        {"name":"Subway", "number":"386-555-5555", 'street':'Any St', 'city':'Jasper'},
        {"name":"Mcdonalds", "number":"386-555-1111", 'street':'Main St', 'city':'Live Oak'},
        {"name":"Wendys", "number":"386-555-3333", 'street':'Co Rd 129', 'city':'Lee'}
    ]

    for v in businesses:
        business = Business(v['name'], v['number'], v['street'], v['city'])
        print(business.name_number)
        print(business.name_address)
