from gase_stove import GaseBurner, Burner
from vessel import Vessel, VesselPlacing, VesselUpdate, Kettle


gase_burner = Burner()
kettle = Kettle()


#gase_burner.get_burners_info()
#kettle.get_vessel_info()

kettle_operate = VesselPlacing()
kettle_update = VesselUpdate()

a = 1
while a == 1:
    choice = input("Please, enter number a command.\n 1.Get burnerns info.\n 2.Get vessel info\n 3.Placing vessel.\n 4.Update water and put on a burner.\n")
    if choice == "1":
        gase_burner.get_burners_info()
    elif choice == "2":
        kettle.get_vessel_info()
    elif choice == "3":
        kettle_operate.fill_vessel()
        kettle_operate.put_on()
        kettle_operate.set_fire()
    elif choice == "4":
        kettle_update.pour_out()
        kettle_operate.fill_vessel()
        kettle_operate.put_on()
        kettle_operate.set_fire()
    else:
        print("Invalid command.")

