import sys
from thermofluid import ThermoTable

def run_lookup():
    print("==============================================")
    print("    THERMOFLUID PROPERTIES LOOKUP ENGINE      ")
    print("==============================================")
    print("Available Tables:")
    print(" 1. Saturated Water   (water_sat_T.csv)")
    print(" 2. Air Ideal Gas      (air_ideal_gas.csv)")
    print(" 3. Nitrogen (N2)      (n2_ideal_gas.csv)")
    print(" 4. Oxygen (O2)        (o2_ideal_gas.csv)")
    print(" 5. Carbon Dioxide     (co2_ideal_gas.csv)")
    print(" 6. Carbon Monoxide    (co_ideal_gas.csv)")
    print(" 7. Hydrogen (H2)      (h2_ideal_gas.csv)")
    print(" 8. Water Vapor (H2O)  (h2o_ideal_gas.csv)")
    print(" 9. Monatomic Oxygen   (o_atom_ideal_gas.csv)")
    print("10. Hydroxyl (OH)      (oh_ideal_gas.csv)")
    print("----------------------------------------------")
    
    # Selection Mapping Matrix for all target textbook appendices
    table_map = {
        "1": ("water_sat_T.csv", "°C"),
        "2": ("air_ideal_gas.csv", "K"),
        "3": ("n2_ideal_gas.csv", "K"),
        "4": ("o2_ideal_gas.csv", "K"),
        "5": ("co2_ideal_gas.csv", "K"),
        "6": ("co_ideal_gas.csv", "K"),
        "7": ("h2_ideal_gas.csv", "K"),
        "8": ("h2o_ideal_gas.csv", "K"),
        "9": ("o_atom_ideal_gas.csv", "K"),
        "10": ("oh_ideal_gas.csv", "K")
    }
    
    choice = input("Select a table number (1-10): ").strip()
    if choice not in table_map:
        print("[-] Invalid choice. Exiting.")
        return

    file_name, unit = table_map[choice]
    
    try:
        table = ThermoTable(file_name)
        val_str = input(f"Enter target temperature ({unit}): ")
        target_val = float(val_str)
        
        # Calculate properties using the unified engine core
        results = table.query(target_val)
        
        print("\n[+] Calculation Complete! Interpolated Properties:")
        print("----------------------------------------------")
        for key, value in results.items():
            print(f"  {key:<15}: {value:.4f}")
        print("----------------------------------------------")
        
    except ValueError as e:
        print(f"\n[-] Input Error: {e}")
    except FileNotFoundError as e:
        print(f"\n[-] File Error: {e}")
        print("    Please verify the corresponding CSV is populated in your data/ directory.")

if __name__ == "__main__":
    run_lookup()