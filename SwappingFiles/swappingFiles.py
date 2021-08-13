def swapFiles():
    filename1 = input("enter files name:- ")
    filename2 = input("enter files name:- ")

    with open(filename1, 'r') as a:
        dataA = a.read()

    with open(filename2, 'r') as b:
        dataB = b.read()

    with open(filename1, 'w') as a:
        a.write(dataB)

    with open(filename2, 'w') as b:
        b.write(dataA)

swapFiles()