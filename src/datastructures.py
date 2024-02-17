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
        # defino los miembros iniciales


        # example list of members
        self._members = [{'first_name': 'John',
                          'last_name': self.last_name,
                          'age': 33,
                          'lucky_numbers': [7, 13, 22],
                          'id': self._generate_id()},
                        {'first_name': 'Jane',
                          'last_name': self.last_name,
                          'age': 35,
                          'lucky_numbers': [10, 14, 3],
                          'id': self._generate_id()},
                        {'first_name': 'Jimmy',
                          'last_name': self.last_name,
                          'age': 5,
                          'lucky_numbers': [1],
                          'id': self._generate_id()}]
    

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        #agrego las claves las name al dic member que recibi
        member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        # agregar member a la lista self.members
        self._members.append(member)
        return self._members
        # fill this method and update the return
        pass

    def delete_member(self, id):
        # fill this method and update the return
        self._members = [item for item in self.members if id != item['id']]
        return self._members

    def get_member(self, id):
        # fill this method and update the return
        # recorrer la lista bsucando el ID, y devolver el miembri que encontramos 
        # OPCION1
        """for item in self._members:
            if id == item['id']:
                return {'result': item}
            return {'message':'no encontrado'}"""
        # OPCION2 list comprension  (----  preferencia a utilizar----)
        # variables = objetivo recorriendo una lista y filtrado por una condicion

        result = [item for item in self._members if id == item['id']]
        return result
           

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
