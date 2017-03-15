# import
from random import randint
from time import time

def operations():

    print("")
    print("Seattle 2017")
    print("Bonjour Elouan")
    print("Bienvenue dans ton jeu de Math")
    print("Ton Papa")
    print("")

    start_t = time()
    i = 0
    j = 0
    c = ''
    bool = True

    while bool == True:
        j +=1
        x = randint(1,4)

        if x == 1:

            z = 10
            a = randint(1, z)
            b = randint(1, z)
            e = a * b
            operator = ' x '

        elif x == 2:

            z = 200
            a = randint(1, z)
            b = randint(1, z)
            if b >= a:
                a,b = b,a
            e = a - b
            operator = ' - '

        elif x == 3:

            z = 100
            a = randint(1, z)
            b = randint(1, z)
            if b >= a:
                a,b = b,a
            e = int(a / b)
            operator = ' / '

        else:

            z = 200
            a = randint(1, z)
            b = randint(1, z)
            e = a + b
            operator = ' + '

        d = str(a) + operator + str(b)  + " = ? "
        print(d)

        c = input(' reponse ?  ')

        if c == 'x':
            j -= 1
            final_t = time() - start_t
            time_per_op = round(final_t/ j,2)
            final_t= ' en ' + str(round(final_t,0)) + ' secondes'
            time_per_op= str(time_per_op) + ' secondes par operation'

            print("")
            print('Ton est score ' + str(i) + " sur " + str(j) + final_t)
            print('soit environ ' + time_per_op)
            print("Au revoir Elouan !")
            print("")
            bool = False

        elif c != 'x':
            c = int(c)
            if c == e:
                print("")
                print ("Bravo Ton score + 1")
                print("")
                i += 1

            else:

                print( "C'est faux !")
                print("la Bonne reponse est :" + str(e))
                print("")

if __name__ == "__main__":
    operations()