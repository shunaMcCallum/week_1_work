# PET SHOP FUNCTIONS

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, num):
    pet_shop["admin"]["total_cash"] += num

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num

def get_stock_count(pet_shop):
    stock_count = []
    for pet in pet_shop["pets"]:
        stock_count.append(pet)
    return len(stock_count)

def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return breed_list

def find_pet_by_name(pet_shop, name):
    index = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet_shop["pets"][index]
        index += 1

def remove_pet_by_name(pet_shop, name):
    index = 0
    new_pet_list = []
    for pet in pet_shop["pets"]:
        if pet["name"] != name:
            new_pet_list.append(pet)
            break
        index += 1
    pet_shop["pets"] = new_pet_list

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer_cash = customer["cash"]
    customer["cash"] = customer_cash - amount
    return customer["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    can_buy_pet = False
    if customer["cash"] >= pet["price"]:
        can_buy_pet = True
    return can_buy_pet

def sell_pet_to_customer(pet_shop, pet, customer):
    for pets in pet_shop["pets"]:
        if pet is None:
            break
        elif pets["name"] == pet["name"] and customer["cash"] >= pet["price"]:
            add_pet_to_customer(customer, pet)
            remove_pet_by_name(pet_shop, pet)
            increase_pets_sold(pet_shop, 1)

            amount = pet["price"]
            remove_customer_cash(customer,amount)
            get_customer_cash(customer)
            add_or_remove_cash(pet_shop, amount)
            get_total_cash(pet_shop)
