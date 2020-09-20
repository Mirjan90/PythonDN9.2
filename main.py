#Fizzbuzz program, če je deljivo z 3 potem izpiše fizz, če pa z 5 potem pa buzz

numberinput = int(input("Write an range number between 1-100: "))

for num in range(1, numberinput):

    if num % 3 == 0 and num % 5 == 0:
        print( "fizzbuzz" )
    elif num % 5 == 0:
        print( "buzz" )
    elif num % 3 == 0:
        print( "fizz" )
    else:
        print(num)


