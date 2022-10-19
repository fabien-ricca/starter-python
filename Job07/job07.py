# On crée une variable 'a', puis une boucle while qui va incrémenter a à chaque tour jusquà ce que a atteigne 100
a = 0

while a < 100:
    a += 1
    # Si le modulo de 'a' par 3 et par 5 et égal à zero alors on affiche "FizzBuzz"
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    # Sinon, si le modulo de 'a' par 5 et égal à zero alors on affiche "Buzz"
    elif a % 5 == 0:
        print("Buzz")
    # Sinon, si le modulo de 'a' par 5 et égal à zero alors on affiche "Fizz"
    elif a % 3 == 0:
        print("Fizz")
    # Sinon on affiche 'a'
    else:
        print(a)

        