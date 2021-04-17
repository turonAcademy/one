car1={'moodel':'BMW','rang':'qora'}
car2={'moodel':'ferrari','rang':'qizil'}
car3={'moodel':'bugattiy','rang':'oq'}
car4={'moodel':'Mersedes','rang':'qora'}
car5={'moodel':'ferrari','rang':'saroq'}
cars=[car1,car3,car2,car4,car5]
for car in cars:
    print(
    f"{car['moodel'].title()} model ,"
    f"{car['rang'].title()}, rangi"
)
