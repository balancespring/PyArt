import turtle

running = True

while running:
    print("Enter triangle, square, circle, or exit: ")
    entered = input()

    if entered == "triangle":
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
    elif entered == "square":
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif entered == "circle":
        turtle.circle(50)
    elif entered == "exit":
        running = False
        print("exiting...")
    else:
        print("Not a command")
        print("Bye...")