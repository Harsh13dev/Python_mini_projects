import pandas as pd

# Series

x = ['a', 'b', 'c', 'd', 'e']
y = [1, 2, 3, 4, 5]
z = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

print(pd.Series(data=x, index=y))
print(pd.Series(z))

x2 = ['a', 'b', 'c', 'd', 'f']

a = pd.Series(y, x)
b = pd.Series(y, x2)
print(a + b)

# Dataframes

A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = [9, 10, 11, 12]
D = [13, 14, 15, 16]
E = [17, 18, 19, 20]

df = pd.DataFrame([A,B,C,D,E], ['a','b','c','d','e'], ['w','x','y','z'])
print(df)
print("\n")

df['P'] = df['y'] + df['z']                 # Adding a column P
print(df)
print("\n")

print(df.drop('e'))                         # Temporary remove the row e
print("\n")

df.drop('d', inplace=True)                  # permanentlu removing the row
print(df)
print("\n")

df.drop('P', axis=1)                        # Temporary remove the column
df.drop('P', axis=1, inplace=True)          # permanentlu removing the column
print(df)
print("\n")

print(df['y'])                              # Accessing a column
print(df.loc['a'])                          # Accessing a row
print(df.loc['a','y'])                      # Accessing a particular element by row and column

# pd.concat(data, index)
# pd.merge(df1,df2)                           # To merge to dataframe

x = pd.DataFrame({'a':(1, 2, 3, 4, 5), 'b':(20, 40, 10, 20, 30)})
print(x)
# x.index                                      # Gives all index/ how many index are there
# x.column                                     # Gives all column
# .sum
# .apply(function)
'''eg- def add(a):
            a = a + 100
            return a
       x['b'].apply(add)'''
# x.sort_values('b')                 >>> [10,20,20,30,40]
# x['b'].unique()                   >>> [10,20,30,40]
# x['b'].nunique()                  >>> 4
# x['b'].value_count()

