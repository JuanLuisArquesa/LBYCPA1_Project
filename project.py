def appliance_info():
    print("\n" + "=== Appliance Information ===".center(50))
    name = input("Enter the name of the appliance: ")
    wattage = input("Enter the wattage (W): ")
    duration = input("Enter usage duration per day (hours): ")
    frequency = input("Enter frequency of use (days per week): ")
    
    print("\n" + "Appliance Information Recorded:".center(50))
    print(f"Name: {name}".center(50))
    print(f"Wattage: {wattage} W".center(50))
    print(f"Usage Duration: {duration} hours/day".center(50))
    print(f"Frequency: {frequency} days/week".center(50))

def main():
    while True:
        print("\n" + "========== Energy Consumption Calculator =========".center(50))
        print("1. Enter Applicance Info".center(50))
        print("2. ".center(50))
        print("3. ".center(50))
        print("4. ".center(50))
        print("5. Exit".center(50))
        print("=" * 50)
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            appliance_info()
        elif choice == '2':
            continue
        elif choice == '3':
            continue
        elif choice == '4':
            continue
        elif choice == '5':
            print("\n" + "Goodbye!".center(50))
            break
        else:
            print("\n" + "Invalid choice. Please select a valid option.".center(50))

if __name__ == "__main__":
    main()
