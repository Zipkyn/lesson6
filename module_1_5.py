immutable_var = 1,2,'a','b'
print('Immutable tuple:',immutable_var)
# immutable_var[0] = 200 # кортеж относится к неизменяемому типу данных. Его используют, как хранилище и он занимет мало места
mutable_list =[1,2,'a','b']
mutable_list.append('Modified')
print('Mutable list:',mutable_list)