#times = input("How many times do I need to tell you?")
#times= int(times)

#for times  in range(times):
 #   print(f"times {times+1} :CLEAN UP YOUR ROOM")

for num in range(1,21):
    if num==14 or num==3 or num==7:
        state = "UNLUCKY!"
    elif num % 2 ==1:
        state = "odd"
    else:
        state = "even"
    print(f"{num} is {state}")
