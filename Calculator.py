#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:
    print('1 Addition')
    print('2 Subtraction')
    print('3 Multiplication')
    print('4 Division')
    print('5 Floor division')
    print('6 Modulo')
    print('Enter x to Exit')

    choice = input('Enter your choice: ')
    
    if choice == 'x':
        break

    num1 = float(input('Enter number 1 : '))
    num2 = float(input('Enter number 2 : '))

    if choice == '1':
        print(num1, '+', num2, '=', (num1+num2))
    elif choice == '2':
        print(num1, '-', num2, '=', (num1-num2))
    elif choice == '3':
        print(num1, '*', num2, '=', (num1*num2))
    elif choice == '4':
        if num2 == 0.0:
            print('Divide by 0 Error')
        else:
            print(num1, '/', num2, '=', (num1/num2))
    elif choice == '5':
        if num2 == 0.0:
            print('Divide by 0 Error')
        else:
            print(num1, '//', num2, '=', (num1//num2))
    elif choice == '6':
        if num2 == 0.0:
            print('Divide by 0 Error')
        else:
            print(num1, '%', num2, '=', (num1%num2))
    else:
        print('invalid choice')


# In[ ]:




