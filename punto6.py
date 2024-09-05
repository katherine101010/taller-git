print ("¡Bienvenido a la pizzería Bella Napoli!")
pizza =  int(input("¿Desea una pizza vegetariana?: 1. Sí  2. No: "))

if pizza == 1:
    print("Usted eligió la opción vegetariana")
    ingrediente1 = int(input("Por favor elija los siguientes ingredientes, recuerde que su pizza ya lleva incluidos la mozzarela y el tomate: 3. pimiento  4. tofu: "))
    if ingrediente1 == 3:
        print("Los ingredientes de su pizza vegetariana serán: mozzarella, tomate y pimiento")
    else:
        print("Los ingredientes de su pizza vegetariana serán: mozzarella, tomate y tofu")
else:
    print("Usted eligió la opción no vegetariana")
    ingrediente2 = int(input("Por favor elija los siguientes ingredientes, recuerde que su pizza ya lleva incluidos la mozzarela y el tomate: 5. Peperoni  6. Jamón  7. Salmón: "))
    if ingrediente2 == 5:
        print("Los ingredientes de su pizza no vegetariana serán: mozzarella, tomate y peperoni")
    elif ingrediente2 == 6:
        print("Los ingredientes de su pizza no vegetariana serán: mozzarella, tomate y jamón")
    else:
        print("Los ingredientes de su pizza no vegetariana serán: mozzarella, tomate y salmón")
        
    