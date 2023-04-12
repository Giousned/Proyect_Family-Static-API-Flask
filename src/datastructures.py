
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name


        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return

        try:
            claves_member = member.keys()

            if not "first_name" in claves_member or not "age" in claves_member or not "lucky_numbers" in claves_member:               # member.get("first_name") and member.get("age")
                return {"code": 400, "mensaje": "Falta el nombre, edad o los números favoritos"}
            
            new_member = {     
            "id": member.get("id",self._generateId()),
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
            }

            self._members.append(new_member)

            return {"code": 200, "mensaje": "Todo ha ido bien", "members": self._members}

        except:
            return {"code": 500}  


    def delete_member(self, id):
        # fill this method and update the return

        try:
            # if type(id) != "int":
            #     return {"code": 400, "mensaje": "La ID tiene que ser un número entero"}
            
            if id == None:
                return {"code": 400, "mensaje": "Falta la ID, ID no proporcionada"}

            # if not self._members["id"] in self._members:
            #     return {"code": 404, "mensaje": "Ningún miembro tiene esa ID"}

            self._members = list(filter(lambda member: member["id"] != id, self._members))

            return {"code": 200, "mensaje": "Todo ha ido bien", "members": self._members}

        except:
            return {"code": 500}
            

    def get_member(self, id):
        # fill this method and update the return

        try:
            # if type(id) != "int":
            #     return {"code": 400, "mensaje": "La ID tiene que ser un número entero"}
            
            if id == None:
                return {"code": 400, "mensaje": "Falta la ID, ID no proporcionada"}

            # if not self._members["id"] in self._members:
            #     return {"code": 404, "mensaje": "Ningún miembro tiene esa ID"}

            selected_member = [member for member in self._members if member["id"] == id]
            
            return {"code": 200, "mensaje": "Todo ha ido bien", "member": selected_member[0]}

        except:
            return {"code": 500}  


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        try:
            return {"code": 200, "members": self._members}
        except:
            return {"code": 500}      # Diccionario con el texto y el error


    # OTRA FORMA DE HACER LA FUNCION DELETE
    # def delete_member(self, id):
    #     # fill this method and update the return
    #     selected_member = [member for member in self._members if member["id"] != id]
        
    #     return selected_member