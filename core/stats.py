import json

def lost_stats():
    police_db_file = open("core/police_db.json","r")
    police_db = json.load(police_db_file)
    police_db_file.close()

    lost_count_at_places=dict()
    
    lost_and_found_file = open("core/lost_and_found_db","r")
    
    lost_and_found_data = lost_and_found_file.readlines()
    for data in lost_and_found_data:
        tmp_data=data.strip().split("/")
        try:
            lost_count_at_places[police_db[tmp_data[1]]] += 1
        except KeyError:
            lost_count_at_places[police_db[tmp_data[1]]] = 1
    
    return lost_count_at_places

def found_stats():
    police_db_file = open("core/police_db.json","r")
    police_db = json.load(police_db_file)
    police_db_file.close()

    found_count_at_places=dict()
    
    lost_and_found_file = open("core/lost_and_found_db","r")
    
    lost_and_found_data = lost_and_found_file.readlines()
    for data in lost_and_found_data:
        tmp_data=data.strip().split("/")
        try:
            found_count_at_places[police_db[tmp_data[2]]] += 1
        except KeyError:
            found_count_at_places[police_db[tmp_data[2]]] = 1
    
    return found_count_at_places

def lost_and_found_relation():
    """
    return dict structure
    { 
        found_place_1 : { lost_place_1 : count_1 , lost_place_2 : count_2  ... },
        found_place_2 : { lost_place_1 : count_1 , lost_place_2 : count_2  ... },
        ...
        ...
    } 
    """
    police_db_file = open("core/police_db.json","r")
    police_db = json.load(police_db_file)
    police_db_file.close()

    relation_dict=dict()

    lost_and_found_file = open("core/lost_and_found_db","r")

    lost_and_found_data = lost_and_found_file.readlines()

    for data in lost_and_found_data:
        tmp_data = data.strip().split("/") 
        relation_dict[police_db[tmp_data[2]]] = dict()

    for data in lost_and_found_data:
        tmp_data = data.strip().split("/") 
        try:
            relation_dict[police_db[tmp_data[2]]][police_db[tmp_data[1]]] += 1
        except KeyError:
            relation_dict[police_db[tmp_data[2]]][police_db[tmp_data[1]]] = 1
        
    return relation_dict

    

if __name__=='__main__':
    print(lost_stats())
    print(found_stats())
    print(lost_and_found_relation())