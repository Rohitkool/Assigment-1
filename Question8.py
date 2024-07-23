# Program to print numbers from 1 to 10, skipping numbers divisible by 3

for n in range(1, 11):

    if n % 3 == 0:
        continue
    print(n)
