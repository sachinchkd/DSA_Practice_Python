player_begin = input("Enter the number (1,2) which player to start? ")
player_next = 1 if (player_begin=='2') else 2 
sign = input("Which one do you like to choose (O,X) :")

moves = 8

x1 =[]
x2 =[]
y1 =[]
y2 =[]

for i in range(moves):
    if(i % 2 == 0):
        a1,b1 = map(int,input(f"Turn Player {player_begin} : Tell me the place to put your {sign} in (x1,y1) position: ").split(","))
        x1.append(a1)
        y1.append(b1)
        if(i>=4):
            if(x1[0]==x1[2]==x1[4]):
                print(player_begin, "won!!")
            elif (x1[0]==0 & x1[1]==1 and x1[2]==2):   
                print(player_begin, "won!!")
            elif (x1[0])





        
    else:
        a2,b2 = map(int,input(f"Turn Player {player_next} : Tell me the place to put your {'X' if (sign==0) else 'O'} in (x1,y1) position: ").split(","))
        x1.append(a2)
        y1.append(b2)


for j in range(moves):
    print(x1[j],y1[j])
    print(x2[j],y2[j])