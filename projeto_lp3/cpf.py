from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("841.490.735-03"))
print(cpf.validate("84149073503"))
print(cpf.validate("844905"))

cpfs = [
    "841.490.735-03",
    "84149073503",
    "844905"
]

print(cpf.validate_list(cpfs))