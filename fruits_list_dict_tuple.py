import pandas as pd

#tuple ()
fruits = ('apple', 'red')
print('fruits:', fruits, 'is', type(fruits))

#list []
fruits_list = ['strawberry','apple','orange']
print('fruits_list:', fruits_list, 'is', type(fruits_list))

#dict{}
fruits_dict = {'strawberry':'red','apple':'red','orange':'orange'}
print('fruits_dict:', fruits_dict, 'is', type(fruits_dict))

#tuple of list
t1 = ('strawberry', 'red')
t2 = ('apple', 'red')
t3 = ('orange','orange')

print(type(t1))

fruits_tuples_of_list = [t1,t2,t3]

print('fruits_tuples_of_list:', fruits_tuples_of_list, 'is', type(fruits_tuples_of_list))

#tuple of list
fruits_list_of_tuples = (['strawberry', 'red'],['apple', 'red'],['orange', 'orange'])
print('fruits_list_of_tuples: ', fruits_list_of_tuples, 'is', type(fruits_list_of_tuples))

#DataFrame
fruits_df = pd.DataFrame({'Fruits': ('strawberry','apple','red')})
print('fruits_df:\n', fruits_df, '\nis',' \n', type(fruits_df))
