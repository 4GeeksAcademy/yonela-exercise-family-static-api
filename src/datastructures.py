
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
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    # Agregar miembro a la familia
    def add_member(self, member):
        # Si no se proporciona un ID, se genera uno automáticamente
        if "id" not in member:
            member["id"] = self._generateId()
        # Añadir el apellido por defecto
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    # Eliminar miembro de la familia
    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done": True}
        return {"done": False}

    # Obtener un miembro de la familia
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # Actualizar la información de un miembro
    def update_member(self, id, updated_member):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members[i].update(updated_member)
                return self._members[i]
        return None

    # Obtener todos los miembros de la familia
    def get_all_members(self):
        return self._members