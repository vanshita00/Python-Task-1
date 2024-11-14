import json
file_path = r"data_set_python_training.json"
def count_unit_source(file_path):
    count_inter=0
    count_intra=0
    count_not_defined=0
    with open(file_path, mode='r') as file:
        data = json.load(file)
        for item in data:
            unit_source=item.get("unit_source")
            if unit_source=="INTER":
                count_inter+=1
            elif unit_source=="INTRA":
                count_intra+=1
            else:
                count_not_defined += 1
    print("INTER-", count_inter)
    print("INTRA-", count_intra)
    print("Not Defined-", count_not_defined)
count_unit_source(file_path)
