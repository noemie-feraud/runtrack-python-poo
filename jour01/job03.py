class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def addition(self):
        return self.nombre1 + self.nombre2
mon_operation = Operation(12, 34)
print(f"Le résultat de {mon_operation.nombre1} + {mon_operation.nombre2} est : {mon_operation.addition()}")