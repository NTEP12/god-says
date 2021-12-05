import random
f = open('g0dsays/godswords', 'r')
gods_words = f.read()
x = ''
for i in range(0,23): x = x + (random.choice(gods_words.split(' '))) + ' '
    
print(f'God says... {x}')