# Flight table data
flight_data = [
    {"P_ID": "P1", "VSCode": 100, "Priority": "MID", "MID": "Eclipse"},
    {"P_ID": "P23", "VSCode": 234, "Priority": "MID", "MID": "Chrome"},
    {"P_ID": "P93", "VSCode": 189, "Priority": "High", "MID": "JDK"},
    {"P_ID": "P42", "VSCode": 9, "Priority": "High", "MID": "CMD"},
    {"P_ID": "P9", "VSCode": 7, "Priority": "High", "MID": "NotePad"},
    {"P_ID": "P87", "VSCode": 23, "Priority": "Low", "MID": "Write"}
]

def sort_flight_data(data, sorting_parameter):
    if sorting_parameter == 1:
        return sorted(data, key=lambda x: x["P_ID"])
    elif sorting_parameter == 2:
        return sorted(data, key=lambda x: x["VSCode"])
    elif sorting_parameter == 3:
        return sorted(data, key=lambda x: x["Priority"])
    else:
        return data

def print_flight_data(data):
    for entry in data:
        print(f"P_ID: {entry['P_ID']}, VSCode: {entry['VSCode']}, Priority: {entry['Priority']}, MID: {entry['MID']}")

if __name__ == "__main__":
    sorting_parameter = int(input("Choose a sorting parameter:\n1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n"))
    
    sorted_flight_data = sort_flight_data(flight_data, sorting_parameter)
    print("\nSorted Flight Table:")
    print_flight_data(sorted_flight_data)
