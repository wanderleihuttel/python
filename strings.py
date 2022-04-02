from datetime import datetime
# Exemplos de uso e formatações de strings
# https://docs.python.org/3/library/string.html#format-specification-mini-language

# Live Dunossauro
# https://youtu.be/fkGFNOOmXsY

#########################################################################################################
# Exemplos utilizando format
print(f"{'':*>80}")
print("O {} foi à {}! Parabéns {}!".format('João', 'escola', 'João'))
print("O {0} foi à {1}! Parabéns {0}!".format('João', 'escola'))
print("O {1} foi à {0}! Parabéns {0}!".format('João', 'escola'))
print("O {nome} foi à {lugar}! Parabéns {nome}!".format(lugar='escola', nome='João'))

#########################################################################################################
# Exemplo utilizando um dicionário e desempacotando
print(f"{'':*>80}")
pessoa = {
    'nome' : 'João',
    'idade': 25,
    'apelido': 'JJ',
    'time' : 'Flamengo',
    'cidade' : 'Rio de Janeiro'
}
s ='Olá {nome}, vi que você tem {idade} anos de idade, o seu apelido é {apelido} e você torce para o {time}.'
print(s.format(**pessoa))


#########################################################################################################
# Exemplo usando conversões
# Three conversion flags are currently supported: '!s' which calls str() on the value, '!r' which calls repr() and '!a' which calls ascii().
print(f"{'':*>80}")   
print('{!s}'.format('Ração'))   # s = string
print('{!r}'.format('Ração'))   # r = objeto string
print('{!a}'.format('Ração'))   # a = array bytes


#########################################################################################################
print(f"{'':*>80}")
string = 'Melão'
print(f'{string}')              # Melão
print(f'{string.upper()}')      # MELÃO
print(f'{string[-1]}')          # O
print(f'{string=}')             # Melão
print(f'{string!a}')            # Mel\\xe3o
print(f'{string.upper()=!a}')   # MEL\\xc3O


#########################################################################################################
# Exemplo usando f-strings
print(f"{'':*>80}")
nome='João'
print(f'{nome.upper()}')
lista = [1,2,3,4]
print(f'{lista[0]} {lista[1:]}')


#########################################################################################################
print(f"{'':*>80}")
# PEP3101 (depois dos :)
#{:[caracter][alinhamento][tamanho]}
# < alinhamento à esquerda
# > alinhamento à direita
# ^ alinhamento no centro
nome = ['João', 'Pedro', 'Maria']
idade = [39, 9, 300]
for nome, idade in zip(nome, idade):
    print(f'{nome:<20} {idade:^5}')       # Tamanho mínimo

# Repetir caracter =, alinhar ao centro com tamanho 50
print(f'{"Menu":=^50}')

#########################################################################################################
# Formatação de número
print(f"{'':*>80}")
# {:[sinal][.precisao][tipo]}
print(f"{15:b}") # Binário          1111
print(f"{15:o}") # Octal            17
print(f"{15:d}") # Decimal          15
print(f"{15:x}") # Hexadecimal      f (minúsculo)
print(f"{15:X}") # Hexadecimal      F (maiúsculo)
print(f"{15:f}") # Float            15.000000
print(f"{15:e}") # Exponencial      15.000000e+01
print(f"{15:.2%}") # Exponencial    15.000000%
print(f"{15:-^20.2f}") # Float      -------15.00-------- 

# = no começo coloca o sinal no início da string
print(f"{-15.3245:=+.2f}")       # -15.00
print(f"{-15.3245:=+14.2f}")     # -        15.00
print(f"{-15.3245:+14.2f}")      #         -15.00
# Com separador de milhar, sinal e alinhado à direita
print(f"{1515.3245:=+14,.2f}")   # +     1,515.32

#########################################################################################################
# Exemplo de formatação de datas
print(f"{'':*>80}")
agora = datetime.now()
print(f'{agora:%d/%m/%Y - %H:%M:%S}')


#########################################################################################################
# Exemplo pegando partes da string
print(f"{'':*>80}")
# String Padrão
msg='Welcome to Python 101: Strings'

# Gerar outra string com letras das string anterior
# 1 Welcome Ring To Tyler
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title())

# Inverter a string 
print(msg1.title()[::-1])

# Passo, pegar de 2 em 2 caracteres
print(msg1[0::2])

# Primeiro 8 caracteres
print(msg[:8])

# Últimos 5 caracteres
print(msg[-5:])


#########################################################################################################
# Enumerar Strings
print(f"{'':*>80}")
for k,v in enumerate('Banana'):
    print(k,v)


#########################################################################################################
# Imprimir index
print(f"{'':*>80}")
friends = ['John','Terry','Eric','Michael','George']
for index in range(len(friends)):
   print(index)

# Imprimir nome
print(f"{'':*>80}")
friends = ['John','Terry','Eric','Michael','George']
for index in friends:
   print(index)
