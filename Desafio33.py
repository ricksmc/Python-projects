n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if (n3 > n1) and (n3 > n2) and (n2 > n1):
    print(f'O maior número é {n3} e o menor número é {n1}')
if (n3 > n1) and (n3 > n2) and (n1 > n2):
    print(f'O maior número é {n3} e o menor número é {n2}')
if (n2 > n1) and (n2 > n3) and (n3 > n1):
    print(f'O maior número é {n2} e o menor número é {n1}')
if (n2 > n1) and (n2 > n3) and (n1 > n3):
    print(f'O maior número é {n2} e o menor número é {n3}')
if (n1 > n2) and (n1 > n3) and (n2 > n3):
    print(f'O maior número é {n1} e o menor número é {n3}')
if (n1 > n2) and (n1 > n3) and (n3 > n2):
    print(f'O maior número é {n1} e o menor número é {n2}')