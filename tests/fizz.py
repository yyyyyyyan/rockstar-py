def Midnight(your_heart, your_soul):
    while your_heart >= your_soul: #this is a comment
        your_heart = your_heart - your_soul
    return your_heart
Desire = 100
my_world = False
Fire = 3 #i love comments
Hate = 5
while not my_world == Desire:
    my_world += 1
    if Midnight(my_world, Fire) == False and Midnight(my_world, Hate) == False:
        print("FizzBuzz!")
        continue
    if Midnight(my_world, Fire) == False:
        print("Fizz!")
        continue
    if Midnight(my_world, Hate) == False:
        print("Buzz!")
        continue
    print(my_world)
