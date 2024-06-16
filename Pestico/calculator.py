# Pricing is estimated for 2 family houses with a basement, any additional property or
#  floors added on will be an additional charge. Not included are Termites, Bed Bugs and 
# Rodent jobs where the structural damage is over $50.00
def structural_damage():
   

    type_of_pests = {'rodents':['rats','squirrels']}


    damage_amount = input("Is the damage amount over $50 ? ")

    if int(damage_amount) > 50:
        print(type_of_pests)
        which_kind_of_pest = input("Which kind of pest has caused thd damage ?")
        if which_kind_of_pest in type_of_pests:
            print('yes')


structural_damage()



