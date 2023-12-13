#Kush Patel
#9/27/2023
#Contact List




def add_contact(contacts : dict,id="65432345",first_name="James",last_name="Horn"):
    try:
        if id not in contacts:
            contacts[id] = ([first_name, last_name])
            return contacts
        else:
            return "error"
    except Exception:
         return contacts

    




def modify_contact(contacts : dict,id="25436464",first_name="Ethan",last_name="Avalos"):
    try:
        if id not in contacts:
            return "error"

        else:
            contacts[id] = ([first_name, last_name])
            return contacts[id]
    
    except Exception:
        return contacts

        
    


def delete_contact(contacts : dict, id="81222111"):
    try:
        if id not in contacts:
            return "error"
        else:
            contacts.pop(id)
            return contacts
    except Exception:
        return contacts    



def sort_contacts(contacts : dict):
    try:
         contacts.sort(key = lambda x : x[1])
         contacts.sort(key = lambda x : x[0])
         return contacts
    except Exception:
         return contacts



def find_contact(contacts,find):
    try:
        diction = dict()
        if find.isnumeric():
            find = int(find)
            if find in contacts:
                diction[find] = contacts[find]
                return diction
        
        else:
            lower_find = find.lower()
            for keys, values in contacts.items():
                if len(values):
                    if lower_find == values[0].lower() or lower_find == values[1].lower():
                        diction[keys] = values

            return diction
    

    except Exception:
        return diction

    
    
    
    
    
    
    
    
    
    
    
    



        


    













