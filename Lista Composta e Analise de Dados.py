temp = []
princ = []
b = l = 0
while True:
    temp.append(str(input('Nome:  ')))
    temp.append(float(input('Peso:  ')))
    if len(princ) == 0:
        b = l = temp[1]
    else:
        if temp[1] > b:
            b = temp[1]
        if temp[1] < l:
            l = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo, foram marcadas {len(princ)} pessoas.')
print(f'O maior peso marcado foi de {b}Kg.')
for p in princ:
    if p[1] == b:
        print(f'O/A mais pesado(a) foi {p[0]}.')
print(f'O menor peso foi de {l}Kg.')

