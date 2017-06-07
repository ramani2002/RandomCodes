# Problem: Determine the largest of three number where this largest number is odd

print('Enter values of x, y, and z. After each number insert a space')
x,y,z = input(), input(), input() # enter three numbers

# Sort the numbers in descending order and determine the oddity of the largest
# number in the triad. The logic can be broken up into three cases.

#Case1
if x > y and x > z and y > z:
    print('The sorted numbers from largest to smallest are:', x, y, z)
#Test for odd to get the largest odd number in the triad
    if int(x)%2 != 0:
            print('The largest odd number in the triad is:', x)
    elif int(y) %2 != 0:
            print('The largest odd number in the triad is:', y)
    elif int(z)%2 != 0:
            print('The largest odd number in the triad is:', z)
    else:
            print('The triad does not have any odd numbers')
elif z > y:
    print('The sorted numbers from largest to smallest are:', x, z, y)   
# Now test for odd or even to get the largest odd number in the triad
    if int(x)%2 != 0:
            print('The largest odd number in the triad is:', x)
    elif int(z) %2 != 0:
            print('The largest odd number in the triad is:', y)
    elif int(y)%2 != 0:
            print('The largest odd number in the triad is:', z)
    else:
            print('The triad does not have any odd numbers')
            
#Case2
if y > x and y > z and x > z:
    print('The sorted numbers from largest to smallest are:', y, x, z)
#Test for odd to get the largest odd number in the triad
    if int(x)%2 != 0:
            print('The largest odd number in the triad is:', x)
    elif int(x) %2 != 0:
            priny('The largest odd number in the triad is:', y)
    elif int(z)%2 != 0:
            print('The largest odd number in the triad is:', z)
    else:
            print('The triad does not have any odd numbers')
elif z > x:
    print('The sorted numbers from largest to smallest are:', y, z, x)   
# Now test for odd or even to get the largest odd number in the triad
    if int(y)%2 != 0:
            print('The largest odd number in the triad is:', x)
    elif int(z) %2 != 0:
            print('The largest odd number in the triad is:', y)
    elif int(x)%2 != 0:
            print('The largest odd number in the triad is:', z)
    else:
            print('The triad does not have any odd numbers')
            
#Case3
if z > x and z >  yand x > y:
    print('The sorted numbers from largest to smallest are:', z, x, y)
#Test for odd to get the largest odd number in the triad
    if int(z)%2 != 0:
            print('The largest odd number in the triad is:', x)
    elif int(x) %2 != 0:
            print('The largest odd number in the triad is:', y)
    elif int(y)%2 != 0:
            print('The largest odd number in the triad is:', z)
    else:
            print('The triad does not have any odd numbers')
elif y > x:
    print('The sorted numbers from largest to smallest are:', z, y, x)   
# Now test for odd or even to get the largest odd number in the triad
    if int(x)%2 != 0:
            print('The largest odd number in the triad is:', x)
    elif int(z) %2 != 0:
            print('The largest odd number in the triad is:', y)
    elif int(y)%2 != 0:
            print('The largest odd number in the triad is:', z)
    else:
            print('The triad does not have any odd numbers')
