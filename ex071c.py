print('='*30)
print('BANCO DO PYTHON')
print('='*30)
sq=int(input('Qual o valor a ser sacado: R$ '))
total=sq
ced=50
totced=0
while True:
    if total >= ced:
        total=total-ced
        totced=totced+1
    else:
        if totced > 0:
            print(f'O total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced=1
        totced=0
        if total == 0:
            break