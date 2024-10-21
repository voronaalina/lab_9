regions = dict()
regions['Київська'] = 28131
regions['Полтавська'] = 228748
regions['Чернігівська']= 31865
regions['Львівська'] = 21833
regions['Одеська'] = 33310

print("Словник з областями та їхніми площами:")
for key in regions:
    print(key + ": " + str(regions[key]) + " км²")

while True:
    print("\n1. додати область")
    print("2. пошук площі області")
    print("3. видалити область")

    choice = input("оберіть дію 1-3:")

    if choice == "1":
        name = input("введіть назву області: ")
        area=int(input("введіть її площу:"))
        regions[name] = area
        print("область успішно додано")
    elif choice == "2":
        name = input("введіть назву області: ").strip()
        if name in regions:
            print("площа області " + name +":" + str(regions[name])+ "км**2")
        else:
            print("область не знайдено")
    elif choice == "3":
        name = input("введіть назву області для видалення:")
        if name in regions:
            del regions[name]
            print("область успішно видалено")
        else:
            print("область не знайдено")
    else:
        print("щось пішло не так.спробуйте ще раз")
