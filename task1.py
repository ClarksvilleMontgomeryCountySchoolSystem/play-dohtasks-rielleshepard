color1 = "purple"

    print(f"1) Use {color1} to roll a medium-sized ball.\n")
    choice1 = input("big or small? ")
    # == Is used to test for equality.
    if choice1 == "big":
        print(f"2) Flatten the ball into a wide disc.\n")
    else:
        print(f"2) Keep it as a ball.\n")
    print(f"3) Roll four small pieces into short ropes.\n")
    print(f"4) Attach them to the bottom.\n")
    print(f"5) Use {color1} to roll a small ball.\n")
    print(f"6) Attach it to one side.\n")
    #Go to user - Include a space after the ? in your prompt.
    choice2 = input("option 1 or option 2? ")
    # Use == to check the User's choice.
    # Remember you are checking equality to a string. You must use quotes.
    if choice2 == "option 1":
        print(f"7) Pinch the small ball to make it pointy.\n")
    else:
        print(f"7) Keep the small ball round.\n")
    print(f"8) Poke two tiny holes in the small ball for eyes.\n")
    print(f'9) Write "Turtle" on the name card.')
