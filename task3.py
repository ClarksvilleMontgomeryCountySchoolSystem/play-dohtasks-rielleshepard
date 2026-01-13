 color1 = "gray"
    color2 = "pink"
    print(f"1) Roll a ball using {color1}.")
    choice1 = input("long body or round body? ")
    # CAUTION: You must include the word "body" when checking!
    if choice1 == "long body":
        print(f"2) Roll the ball into an egg shape.")
    else:
        print(f"2) Keep it as a ball.")
    print(f"3) Roll a smaller ball using {color1} for the head.")
    print(f"4) Attach the head to one end of the body.")
    choice2 = input("long tail or short tail? ")
    if choice2 == "long tail":
        print(f"5) Roll a thin rope using {color2} and attach to the back.")
    else:
        print(f"5) Add a small bump using {color2} to the back.")
    print(f"6) Add four small legs to the bottom using {color1}.")
    print(f"6) Add four small legs to the bottom using {color1}.")
    print("Name this creation: \"Mouse\"")
