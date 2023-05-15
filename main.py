número = input('Digite um número: ')
número = int(número)
if número < 0:
   print('Impossível!')
if número < 18:
   print('Não precisa se alistar.')
elif número > 18 and número < 65:
   print('Não esqueça de votar na próxima eleição.')
elif número > 65: 
   print('Vá descansar.')
else:
    print('Eita!')
