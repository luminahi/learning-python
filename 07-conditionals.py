
userReply = input("Do you need to ship a package? (Enter 'yes' or 'no') ")

if userReply == "yes":
    print("we can help you ship that package!")
    count = input("how many things? ")
    if int(count) > 0:
        print(f"nicezera, {count} items right?")
    else:
        print("I don't get it...")
elif userReply == "no":
    print("Please come back when you need to ship a package. Thank you.")
else:
    print("hum?!")