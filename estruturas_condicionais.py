maior_idade = 18
idade_especial = 17

idade = int(input("Informe a sua idade: "))


if idade >= maior_idade:
    print("Pode tirar a CNH.")

else:
    print("Ainda não pode tirar a CNH.")



if idade >= maior_idade:
    print("Pode tirar a CNH.")
elif idade == idade_especial:
    print("Não pode tirar carteira, mas pode assistir as aulas teóricas.")


else:
    print("Ainda não pode tirar a CNH.")




