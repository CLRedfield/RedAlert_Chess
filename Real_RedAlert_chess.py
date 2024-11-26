import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Red Alert Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps=60
run = True
end = False
player1_pieces=[]
player1_locations=[]
captured_pieces_player1=[]
player1_pieces_1=['S_2','S_4','S_3','S_5','S_6','S_3','S_4','S_2',
                  'S_1','S_1','S_1','S_1','S_1','S_1','S_1','S_1',
                  'S_1','S_1']
player1_locations_1=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                     (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),
                     (0,2),(7,2)]
player1_pieces_2=['A_3','A_5','A_4','A_6','A_7','A_4','A_5','A_3',
                  'A_1','A_1','A_2','A_2','A_2','A_2','A_1','A_1']
player1_locations_2=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                     (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
player1_pieces_3=['E_4','E_2','E_3','E_5','E_6','E_3','E_2','E_4',
                  'E_1','E_1','E_1','E_1','E_1','E_1','E_1','E_1']
player1_locations_3=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                     (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
player1_pieces_4=['F_13','F_12','F_14','F_6','F_8','F_7','F_5','F_4',
                  'F_1','F_2','F_10','F_10','F_2','F_1']
player1_locations_4=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                     (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),]

player2_pieces=[]
player2_locations=[]
captured_pieces_player2=[]
player2_pieces_1=['S_2','S_4','S_3','S_5','S_6','S_3','S_4','S_2',
                  'S_1','S_1','S_1','S_1','S_1','S_1','S_1','S_1',
                  'S_1','S_1']
player2_locations_1=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                     (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),
                     (0,5),(7,5)]
player2_pieces_2=['A_3','A_5','A_4','A_6','A_7','A_4','A_5','A_3',
                  'A_1','A_1','A_2','A_2','A_2','A_2','A_1','A_1']
player2_locations_2=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                     (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
player2_pieces_3=['E_4','E_2','E_3','E_5','E_6','E_3','E_2','E_4',
                  'E_1','E_1','E_1','E_1','E_1','E_1','E_1','E_1']
player2_locations_3=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                     (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
player2_pieces_4=['F_13','F_12','F_14','F_6','F_8','F_7','F_5','F_4',
                  'F_1','F_2','F_10','F_10','F_2','F_1']
player2_locations_4=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                     (1,6),(2,6),(3,6),(4,6),(5,6),(6,6)]

turn_step=4
selection=100
valid_moves=[]


player1_images=[]
player1_small_images=[]
player2_images=[]
player2_small_images=[]
S_1_1 = pygame.image.load('images/S1.png')
S_1_1 = pygame.transform.scale(S_1_1,(80,64))
S_1_1_small = pygame.transform.scale(S_1_1,(40,32))
S_2_1 = pygame.image.load('images/S2.png')
S_2_1 = pygame.transform.scale(S_2_1,(80,64))
S_2_1_small = pygame.transform.scale(S_2_1,(40,32))
S_3_1 = pygame.image.load('images/S3.png')
S_3_1 = pygame.transform.scale(S_3_1,(80,64))
S_3_1_small = pygame.transform.scale(S_3_1,(40,32))
S_4_1 = pygame.image.load('images/S4.png')
S_4_1 = pygame.transform.scale(S_4_1,(80,64))
S_4_1_small = pygame.transform.scale(S_4_1,(40,32))
S_5_1 = pygame.image.load('images/S5.png')
S_5_1 = pygame.transform.scale(S_5_1,(80,64))
S_5_1_small = pygame.transform.scale(S_5_1,(40,32))
S_6_1 = pygame.image.load('images/S6.png')
S_6_1 = pygame.transform.scale(S_6_1,(80,64))
S_6_1_small = pygame.transform.scale(S_6_1,(40,32))



A_1_1 = pygame.image.load('images/A1.png')
A_1_1 = pygame.transform.scale(A_1_1,(80,64))
A_1_1_small = pygame.transform.scale(A_1_1,(40,32))
A_2_1 = pygame.image.load('images/A2.png')
A_2_1 = pygame.transform.scale(A_2_1,(80,64))
A_2_1_small = pygame.transform.scale(A_2_1,(40,32))
A_3_1 = pygame.image.load('images/A3.png')
A_3_1 = pygame.transform.scale(A_3_1,(80,64))
A_3_1_small = pygame.transform.scale(A_3_1,(40,32))
A_4_1 = pygame.image.load('images/A4.png')
A_4_1 = pygame.transform.scale(A_4_1,(80,64))
A_4_1_small = pygame.transform.scale(A_4_1,(40,32))
A_5_1 = pygame.image.load('images/A5.png')
A_5_1 = pygame.transform.scale(A_5_1,(80,64))
A_5_1_small = pygame.transform.scale(A_5_1,(40,32))
A_6_1 = pygame.image.load('images/A6.png')
A_6_1 = pygame.transform.scale(A_6_1,(80,64))
A_6_1_small = pygame.transform.scale(A_6_1,(40,32))
A_7_1 = pygame.image.load('images/A7.png')
A_7_1 = pygame.transform.scale(A_7_1,(80,64))
A_7_1_small = pygame.transform.scale(A_7_1,(40,32))


E_1_1 = pygame.image.load('images/E1.png')
E_1_1 = pygame.transform.scale(E_1_1,(80,64))
E_1_1_small = pygame.transform.scale(E_1_1,(40,32))
E_2_1 = pygame.image.load('images/E2.png')
E_2_1 = pygame.transform.scale(E_2_1,(80,64))
E_2_1_small = pygame.transform.scale(E_2_1,(40,32))
E_3_1 = pygame.image.load('images/E3.png')
E_3_1 = pygame.transform.scale(E_3_1,(80,64))
E_3_1_small = pygame.transform.scale(E_3_1,(40,32))
E_4_1 = pygame.image.load('images/E4.png')
E_4_1 = pygame.transform.scale(E_4_1,(80,64))
E_4_1_small = pygame.transform.scale(E_4_1,(40,32))
E_5_1 = pygame.image.load('images/E5.png')
E_5_1 = pygame.transform.scale(E_5_1,(80,64))
E_5_1_small = pygame.transform.scale(E_5_1,(40,32))
E_6_1 = pygame.image.load('images/E6.png')
E_6_1 = pygame.transform.scale(E_6_1,(80,64))
E_6_1_small = pygame.transform.scale(E_6_1,(40,32))
E_7_1 = pygame.image.load('images/E7.png')
E_7_1 = pygame.transform.scale(E_7_1,(80,64))
E_7_1_small = pygame.transform.scale(E_7_1,(40,32))

F_1_1 = pygame.image.load('images/F1.png')
F_1_1 = pygame.transform.scale(F_1_1,(80,64))
F_1_1_small = pygame.transform.scale(F_1_1,(40,32))
F_2_1 = pygame.image.load('images/F2.png')
F_2_1 = pygame.transform.scale(F_2_1,(80,64))
F_2_1_small = pygame.transform.scale(F_2_1,(40,32))
F_3_1 = pygame.image.load('images/F3.png')
F_3_1 = pygame.transform.scale(F_3_1,(80,64))
F_3_1_small = pygame.transform.scale(F_3_1,(40,32))
F_4_1 = pygame.image.load('images/F4.png')
F_4_1 = pygame.transform.scale(F_4_1,(80,64))
F_4_1_small = pygame.transform.scale(F_4_1,(40,32))
F_5_1 = pygame.image.load('images/F5.png')
F_5_1 = pygame.transform.scale(F_5_1,(80,64))
F_5_1_small = pygame.transform.scale(F_5_1,(40,32))
F_6_1 = pygame.image.load('images/F6.png')
F_6_1 = pygame.transform.scale(F_6_1,(80,64))
F_6_1_small = pygame.transform.scale(F_6_1,(40,32))
F_7_1 = pygame.image.load('images/F7.png')
F_7_1 = pygame.transform.scale(F_7_1,(80,64))
F_7_1_small = pygame.transform.scale(F_7_1,(40,32))
F_8_1 = pygame.image.load('images/F8.png')
F_8_1 = pygame.transform.scale(F_8_1,(80,64))
F_8_1_small = pygame.transform.scale(F_8_1,(40,32))
F_9_1 = pygame.image.load('images/F9.png')
F_9_1 = pygame.transform.scale(F_9_1,(80,64))
F_9_1_small = pygame.transform.scale(F_9_1,(40,32))
F_10_1 = pygame.image.load('images/F10.png')
F_10_1 = pygame.transform.scale(F_10_1,(80,64))
F_10_1_small = pygame.transform.scale(F_10_1,(40,32))
F_11_1 = pygame.image.load('images/F11.png')
F_11_1 = pygame.transform.scale(F_11_1,(80,64))
F_11_1_small = pygame.transform.scale(F_11_1,(40,32))
F_12_1 = pygame.image.load('images/F12.png')
F_12_1 = pygame.transform.scale(F_12_1,(80,64))
F_12_1_small = pygame.transform.scale(F_12_1,(40,32))
F_13_1 = pygame.image.load('images/F13.png')
F_13_1 = pygame.transform.scale(F_13_1,(80,64))
F_13_1_small = pygame.transform.scale(F_13_1,(40,32))
F_14_1 = pygame.image.load('images/F14.png')
F_14_1 = pygame.transform.scale(F_14_1,(80,64))
F_14_1_small = pygame.transform.scale(F_14_1,(40,32))


soviet= pygame.image.load('images/soviet.png')
allied= pygame.image.load('images/allied.png')
epsilon= pygame.image.load('images/epsilon.png')
foehn= pygame.image.load('images/foehn.png')
p1forces=[soviet,allied,epsilon,foehn]
p2forces=[soviet,allied,epsilon,foehn]
desc=("Soviet army has the strongest power",
    "to crush the enermies.",
    "However, the slow speed is the biggest weakness",
    "Combining advanced technology and high speed armies,",
    "the Allied force always control",
    "the initiative in the battle field ",
    "Broke out from the Soviet,",
    "Yuri led his own army.",
    "He has the world's most mystrious power",
    "Since the world was almost destroyed",
    "by Yuri, the last people who pursue",
    "freedom built this last fortress")


images=[S_1_1,S_2_1,S_3_1,S_4_1,S_5_1,S_6_1,A_1_1,A_2_1,A_3_1,A_4_1,A_5_1,A_6_1,A_7_1,E_1_1,E_2_1,E_3_1,E_4_1,E_5_1,E_6_1,F_1_1,\
        F_2_1,F_3_1,F_4_1,F_5_1,F_6_1,F_7_1,F_8_1,F_9_1,F_10_1,F_11_1,F_12_1,F_13_1,F_14_1]
piece_list=['S_1','S_2','S_3','S_4','S_5','S_6','A_1','A_2','A_3','A_4','A_5','A_6','A_7','E_1','E_2','E_3','E_4','E_5','E_6','F_1',\
            'F_2','F_3','F_4','F_5','F_6','F_7','F_8','F_9','F_10','F_11','F_12','F_13','F_14']
small_images=[S_1_1_small,S_2_1_small,S_3_1_small,S_4_1_small,S_5_1_small,S_6_1_small,A_1_1_small,A_2_1_small,A_3_1_small,A_4_1_small,A_5_1_small,A_6_1_small,A_7_1_small,\
              E_1_1_small,E_2_1_small,E_3_1_small,E_4_1_small,E_5_1_small,E_6_1_small,F_1_1_small,F_2_1_small,F_3_1_small,F_4_1_small\
                ,F_5_1_small,F_6_1_small,F_7_1_small,F_8_1_small,F_9_1_small,F_10_1_small,F_11_1_small,F_12_1_small,F_13_1_small,F_14_1_small]


def draw_board():
    for i in range(32):
        a=i%4
        b=i//4
        if b % 2 == 0:
            pygame.draw.rect(screen,(130,130,130),[600-(a*200),b*100,100,100])
        else:
            pygame.draw.rect(screen,(130,130,130),[700-(a*200),b*100,100,100])
        pygame.draw.rect(screen,'gray',[0,800,WIDTH,100])
        pygame.draw.rect(screen,(20,200,200),[0,800,WIDTH,100],5)
        pygame.draw.rect(screen,(20,200,200),[800,0,200,HEIGHT],5)
    status_text=["Player1's turn to select a piece!","Player1: select a destination!",
                     "Player2's turn to select a piece!","Player2: select a destination!","Choose your forces now!"]
    if not end:
        screen.blit(big_font.render(status_text[turn_step],True,'black'),(20,820))
    for i in range(9):
        pygame.draw.line(screen,(10,10,10),(0,100*i),(800,100*i),2)
        pygame.draw.line(screen,(10,10,10),(100*i,0),(100*i,800),2)

def draw_pieces():
    for i in range(len(player1_pieces)):
        index = piece_list.index(player1_pieces[i])
        screen.blit(images[index],(player1_locations[i][0]*100+10,player1_locations[i][1]*100+18))
        for j in player1_locations:
            pygame.draw.rect(screen,(170,0,0),[j[0]*100,j[1]*100,100,100],2)
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen,(255,0,0),[player1_locations[i][0]*100,player1_locations[i][1]*100,100,100],5)
    for i in range(len(player2_pieces)):
        index = piece_list.index(player2_pieces[i])
        screen.blit(images[index],(player2_locations[i][0]*100+10,player2_locations[i][1]*100+18))
        for j in player2_locations:
            pygame.draw.rect(screen,(0,0,170),[j[0]*100,j[1]*100,100,100],2)
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen,(0,0,255),[player2_locations[i][0]*100+1,player2_locations[i][1]*100+1,100,100],5)


def touch(x1,y1,x2,y2):
    if pygame.mouse.get_pos()[0] > x1 and pygame.mouse.get_pos()[0] < x2 and pygame.mouse.get_pos()[1] > y1 and pygame.mouse.get_pos()[1] < y2:
        return True
    else:
        return False
    



def check_options(pieces,locations,turn):
    moves_list=[]
    all_moves_list=[]
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece =='S_1':
            moves_list = check_S_1(location, turn)
        elif piece == 'S_2':
            moves_list = check_S_2(location, turn)
        elif piece == 'S_3':
            moves_list = check_S_3(location, turn)
        elif piece == 'S_4':
            moves_list = check_S_4(location, turn)
        elif piece == 'S_5':
            moves_list = check_S_5(location, turn)
        elif piece == 'S_6':
            moves_list = check_S_6(location, turn)
        elif piece == 'A_1':
            moves_list = check_A_1(location, turn)
        elif piece == 'A_2':
            moves_list = check_A_2(location, turn)
        elif piece == 'A_3':
            moves_list = check_A_3(location, turn)
        elif piece == 'A_4':
            moves_list = check_A_4(location, turn)
        elif piece == 'A_5':
            moves_list = check_A_5(location, turn)
        elif piece == 'A_6':
            moves_list = check_A_6(location, turn)
        elif piece == 'A_7':
            moves_list = check_A_7(location, turn)
        elif piece == 'E_1':
            moves_list = check_E_1(location, turn)
        elif piece == 'E_2':
            moves_list = check_E_2(location, turn)
        elif piece == 'E_3':
            moves_list = check_E_3(location, turn)
        elif piece == 'E_4':
            moves_list = check_E_4(location, turn)
        elif piece == 'E_5':
            moves_list = check_E_5(location, turn)
        elif piece == 'E_6':
            moves_list = check_E_6(location, turn)
        elif piece == 'F_1':
            moves_list = check_F_1(location, turn)
        elif piece == 'F_2':
            moves_list = check_F_2(location, turn)
        elif piece == 'F_4':
            moves_list = check_F_4(location, turn)
        elif piece == 'F_5':
            moves_list = check_F_5(location, turn)
        elif piece == 'F_6':
            moves_list = check_F_6(location, turn)
        elif piece == 'F_7':
            moves_list = check_F_7(location, turn)
        elif piece == 'F_8':
            moves_list = check_F_8(location, turn)
        elif piece == 'F_10':
            moves_list = check_F_10(location, turn)
        elif piece == 'F_12':
            moves_list = check_F_12(location, turn)
        elif piece == 'F_13':
            moves_list = check_F_13(location, turn)
        elif piece == 'F_14':
            moves_list = check_F_14(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_S_1(position, turn):
    moves_list=[]
    if turn == 'p1':
        if (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations \
            and position[1] < 7:
            moves_list.append((position[0],position[1]+1))
        if (position[0],position[1]+2) not in player1_locations and (position[0],position[1]+2) not in player2_locations \
           and (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations and position[1] == 1 and position[0] in (3,4):
            moves_list.append((position[0],position[1]+2))
        if (position[0] + 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]+1,position[1]+1))
        if (position[0] - 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]-1,position[1]+1))
    if turn == 'p2':
        if (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
        if (position[0],position[1]-2) not in player1_locations and (position[0],position[1]-2) not in player2_locations \
            and (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations and position[1] == 6 and position[0] in (3,4):
            moves_list.append((position[0],position[1]-2))
        if (position[0] + 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]+1,position[1]-1))
        if (position[0] - 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]-1,position[1]-1))
    return moves_list

def check_S_2(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=0
            y=1
        elif i == 1:
            x=0
            y=-1
        elif i == 2:
            x=1
            y=0
        elif i == 3:
            x=-1
            y=0
        while path and chain <= 6:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    if (position[0] + 1,position[1] - 1) not in friends_list and position[0] < 7 and position[1] > 0:
        moves_list.append((position[0]+1,position[1]-1))
    if (position[0] - 1,position[1] - 1) not in friends_list and position[0] > 0 and position[1] > 0:
        moves_list.append((position[0]-1,position[1]-1))
    if (position[0] + 1,position[1] + 1) not in friends_list and position[0] < 7 and position[1] < 7:
        moves_list.append((position[0]+1,position[1]+1))
    if (position[0] - 1,position[1] + 1) not in friends_list and position[0] > 0 and position[1] < 7:
        moves_list.append((position[0]-1,position[1]+1))
    return moves_list

def check_S_3(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=1
            y=1
        elif i == 1:
            x=-1
            y=-1
        elif i == 2:
            x=1
            y=-1
        elif i == 3:
            x=-1
            y=1
        while path and chain <= 6:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    if (position[0],position[1]+1) not in friends_list\
        and position[1] < 7:
        moves_list.append((position[0],position[1]+1))
    if (position[0],position[1]-1) not in friends_list\
        and position[1] > 0:
        moves_list.append((position[0],position[1]-1))
    return moves_list

def check_S_4(position, turn):
    moves_list=[]
    if turn == 'p1':
        if (position[0]+1,position[1]+2) not in player1_locations\
            and position[1] < 6 and position[0] < 7:
            moves_list.append((position[0]+1,position[1]+2))
        if (position[0],position[1]+2) not in player1_locations\
            and position[1] < 6:
            moves_list.append((position[0],position[1]+2))
        if (position[0]-1,position[1]+2) not in player1_locations\
            and position[1] < 6 and position[0] > 0:
            moves_list.append((position[0]-1,position[1]+2))
        if (position[0]+2,position[1]+1) not in player1_locations\
            and position[1] < 7 and position[0] < 6:
            moves_list.append((position[0]+2,position[1]+1))
        if (position[0]-2,position[1]+1) not in player1_locations\
            and position[1] < 7 and position[0] > 1:
            moves_list.append((position[0]-2,position[1]+1))
        if (position[0]+2,position[1]-1) not in player1_locations\
            and position[1] > 0 and position[0] < 6:
            moves_list.append((position[0]+2,position[1]-1))
        if (position[0]-2,position[1]-1) not in player1_locations\
            and position[1] > 0 and position[0] > 1:
            moves_list.append((position[0]-2,position[1]-1))
        if (position[0],position[1]-2) not in player1_locations\
            and position[1] > 1:
            moves_list.append((position[0],position[1]-2))
    if turn == 'p2':
        if (position[0]+1,position[1]-2) not in player2_locations\
            and position[1] > 1 and position[0] < 7:
            moves_list.append((position[0]+1,position[1]-2))
        if (position[0],position[1]+2) not in player2_locations\
            and position[1] < 6:
            moves_list.append((position[0],position[1]+2))
        if (position[0]-1,position[1]-2) not in player2_locations\
            and position[1] > 1 and position[0] > 0:
            moves_list.append((position[0]-1,position[1]-2))
        if (position[0]+2,position[1]+1) not in player2_locations\
            and position[1] < 7 and position[0] < 6:
            moves_list.append((position[0]+2,position[1]+1))
        if (position[0]-2,position[1]+1) not in player2_locations\
            and position[1] < 7 and position[0] > 1:
            moves_list.append((position[0]-2,position[1]+1))
        if (position[0]+2,position[1]-1) not in player2_locations\
            and position[1] > 0 and position[0] < 6:
            moves_list.append((position[0]+2,position[1]-1))
        if (position[0]-2,position[1]-1) not in player2_locations\
            and position[1] > 0 and position[0] > 1:
            moves_list.append((position[0]-2,position[1]-1))
        if (position[0],position[1]-2) not in player2_locations\
            and position[1] > 1:
            moves_list.append((position[0],position[1]-2))
    return moves_list

def check_S_5(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(8):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_S_6(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,2),(0,-2),(2,0),(-2,0)]
    for i in range(12):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0<=target[0]<=7 and 0<=target[1]<=7:
            moves_list.append(target)
    return moves_list

def check_A_1(position, turn):
    moves_list=[]
    if turn == 'p1':
        if (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations \
            and position[1] < 7:
            moves_list.append((position[0],position[1]+1))
        if (position[0],position[1]+2) not in player1_locations and (position[0],position[1]+2) not in player2_locations \
            and (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations and position[1] == 1:
            moves_list.append((position[0],position[1]+2))
        if (position[0] + 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]+1,position[1]+1))
        if (position[0] - 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]-1,position[1]+1))
    if turn == 'p2':
        if (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
        if (position[0],position[1]-2) not in player1_locations and (position[0],position[1]-2) not in player2_locations \
            and (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations and position[1] == 6:
            moves_list.append((position[0],position[1]-2))
        if (position[0] + 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]+1,position[1]-1))
        if (position[0] - 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]-1,position[1]-1))
    return moves_list

def check_A_2(position, turn):
    moves_list=[]
    if turn == 'p1':
        if (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations \
            and position[1] < 7:
            moves_list.append((position[0],position[1]+1))
        if (position[0],position[1]+2) not in player1_locations and (position[0],position[1]+2) not in player2_locations \
            and (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations and position[1] == 1:
            moves_list.append((position[0],position[1]+2))
        if (position[0] + 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]+1,position[1]+1))
        if (position[0] - 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]-1,position[1]+1))
        if (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
    if turn == 'p2':
        if (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
        if (position[0],position[1]-2) not in player1_locations and (position[0],position[1]-2) not in player2_locations \
            and (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations and position[1] == 6:
            moves_list.append((position[0],position[1]-2))
        if (position[0] + 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]+1,position[1]-1))
        if (position[0] - 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]-1,position[1]-1))
        if (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations \
            and position[1] < 7:
            moves_list.append((position[0],position[1]+1))
    return moves_list

def check_A_3(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=0
            y=1
        elif i == 1:
            x=0
            y=-1
        elif i == 2:
            x=1
            y=0
        elif i == 3:
            x=-1
            y=0
        while path and chain <= 7:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_A_4(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=1
            y=1
        elif i == 1:
            x=-1
            y=-1
        elif i == 2:
            x=1
            y=-1
        elif i == 3:
            x=-1
            y=1
        while path and chain <= 7:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                if chain >= 2:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    if (position[0],position[1]+1) not in friends_list\
        and position[1] < 7:
        moves_list.append((position[0],position[1]+1))
    if (position[0],position[1]+2) not in friends_list and (position[0],position[1]+1) not in friends_list\
        and (position[0],position[1]+1) not in enemies_list and position[1] < 6:
        moves_list.append((position[0],position[1]+2))
    if (position[0],position[1]-1) not in friends_list\
        and position[1] > 0:
        moves_list.append((position[0],position[1]-1))
    if (position[0],position[1]-2) not in friends_list and (position[0],position[1]-1) not in friends_list\
        and (position[0],position[1]-1) not in enemies_list and position[1] > 1:
        moves_list.append((position[0],position[1]-2))
    return moves_list

def check_A_5(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    if turn == 'p1':
        targets.append((0,-2))
    else:
        targets.append((0,2))
    for i in range(9):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0<=target[0]<=7 and 0<=target[1]<=7:
            moves_list.append(target)
    return moves_list

def check_A_6(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(8):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_A_7(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    for i in range(8):
        path = True
        chain = 1
        if i == 0:
            x=0
            y=1
        elif i == 1:
            x=0
            y=-1
        elif i == 2:
            x=1
            y=0
        elif i == 3:
            x=-1
            y=0
        elif i == 4:
            x=1
            y=1
        elif i == 5:
            x=-1
            y=-1
        elif i == 6:
            x=1
            y=-1
        elif i == 7:
            x=-1
            y=1
        while path and chain <= 7:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_E_1(position, turn):
    moves_list=[]
    if turn == 'p1':
        if (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations \
            and position[1] < 7:
            moves_list.append((position[0],position[1]+1))
        if ((position[0] + 1,position[1] + 1) in player2_locations) or position[0] < 4\
            and not (position[0]+1,position[1]+1) in player1_locations:
            moves_list.append((position[0]+1,position[1]+1))
        if ((position[0] - 1,position[1] + 1) in player2_locations) or position[0] > 3\
            and not (position[0]-1,position[1]+1) in player1_locations:
            moves_list.append((position[0]-1,position[1]+1))
    if turn == 'p2':
        if (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
        if ((position[0] + 1,position[1] - 1) in player1_locations) or position[0] < 4\
            and not (position[0]+1,position[1]-1) in player2_locations:
            moves_list.append((position[0]+1,position[1]-1))
        if ((position[0] - 1,position[1] - 1) in player1_locations) or position[0] > 3\
            and not (position[0]-1,position[1]-1) in player2_locations:
            moves_list.append((position[0]-1,position[1]-1))
    return moves_list

def check_E_2(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(1,2),(1,-2),(-1,2),(-1,-2),(1,1),(1,-1),(-1,1),(-1,-1)]
    if turn == 'p1':
        targets.append((0,-1))
    else:
        targets.append((0,1))
    for i in range(9):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0<=target[0]<=7 and 0<=target[1]<=7:
            moves_list.append(target)
    return moves_list

def check_E_3(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=1
            y=1
        elif i == 1:
            x=-1
            y=-1
        elif i == 2:
            x=1
            y=-1
        elif i == 3:
            x=-1
            y=1
        while path and chain <= 6:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    if (position[0]+1,position[1]) not in friends_list\
        and position[0] < 7:
        moves_list.append((position[0]+1,position[1]))
    if (position[0]-1,position[1]) not in friends_list\
        and position[0] > 0:
        moves_list.append((position[0]-1,position[1]))
    return moves_list

def check_E_4(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
        for i in range(2):
            path = True
            chain = 1
            if i == 0:
                x=1
                y=0
            elif i == 1:
                x=-1
                y=0
            while path and chain <= 7:
                if (position[0] + (chain*x), position[1]+1) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + 1 <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + 1))
                    if (position[0] + (chain*x),position[1] + 1) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
        for i in range(2):
            path = True
            chain = 1
            if i == 0:
                x=1
                y=0
            elif i == 1:
                x=-1
                y=0
            while path and chain <= 7:
                if (position[0] + (chain*x), position[1]-1) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] - 1 <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] -1))
                    if (position[0] + (chain*x),position[1] - 1) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
    for i in range(2):
        path = True
        chain = 1
        if i == 0:
            x=0
            y=1
        elif i == 1:
            x=0
            y=-1
        while path and chain <= 7:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    
    return moves_list

def check_E_5(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(8):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_E_6(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,3),(0,-3),(3,0),(-3,0),(0,2),(0,-2),(2,0),(-2,0)]
    for i in range(8):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and target in enemies_list:
            moves_list.append(target)
    targets2 = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(4):
        target2=(position[0]+targets2[i][0],position[1]+targets2[i][1])
        if target2 not in friends_list and 0<=position[0]+targets2[i][0]<=7 and 0<=position[1]+targets2[i][1]<=7:
            moves_list.append(target2)
    return moves_list

def check_F_1(position, turn):
    moves_list=[]
    if turn == 'p1':
        if (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations \
            and position[1] < 7:
            moves_list.append((position[0],position[1]+1))
        if (position[0]+1,position[1]) not in player1_locations and (position[0]+1,position[1]) not in player2_locations \
            and position[0] < 7:
            moves_list.append((position[0]+1,position[1]))
        if (position[0]-1,position[1]) not in player1_locations and (position[0]-1,position[1]) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0]-1,position[1]))
        if (position[0] + 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]+1,position[1]+1))
        if (position[0] - 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]-1,position[1]+1))
    if turn == 'p2':
        if (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
        if (position[0]+1,position[1]) not in player1_locations and (position[0]+1,position[1]) not in player2_locations \
            and position[0] < 7:
            moves_list.append((position[0]+1,position[1]))
        if (position[0]-1,position[1]) not in player1_locations and (position[0]-1,position[1]) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0]-1,position[1]))
        if (position[0] + 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]+1,position[1]-1))
        if (position[0] - 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]-1,position[1]-1))
    return moves_list

def check_F_2(position, turn):
    moves_list=[]
    if turn == 'p1':
        if (position[0],position[1]+1) not in player1_locations and position[1] < 7:
            moves_list.append((position[0],position[1]+1))
        if (position[0] + 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]+1,position[1]+1))
        if (position[0] - 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]-1,position[1]+1))
    if turn == 'p2':
        if (position[0],position[1]-1) not in player2_locations and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
        if (position[0] + 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]+1,position[1]-1))
        if (position[0] - 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]-1,position[1]-1))
    return moves_list

def check_F_4(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
        for i in range(3):
            path = True
            chain = 1
            if i == 0:
                x=1
                y=0
            elif i == 1:
                x=-1
                y=0
            elif i == 2:
                x=0
                y=1
            while path and chain <= 6:
                if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                    if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        for i in range(2):
            path = True
            chain = 1
            if i == 0:
                x=1
                y=-1
            elif i == 1:
                x=-1
                y=-1
            while path and chain <= 3:
                if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                    if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
        for i in range(3):
            path = True
            chain = 1
            if i == 0:
                x=1
                y=0
            elif i == 1:
                x=-1
                y=0
            elif i == 2:
                x=0
                y=-1
            while path and chain <= 6:
                if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                    if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        for i in range(2):
            path = True
            chain = 1
            if i == 0:
                x=1
                y=1
            elif i == 1:
                x=-1
                y=1
            while path and chain <= 3:
                if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                    if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
    return moves_list

def check_F_5(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,1),(0,-1),(1,2),(-1,2),(1,-2),(-1,-2),(2,0),(-2,0)]
    for i in range(8):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_F_6(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(8):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_F_7(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
        for i in range(2):
            path = True
            chain = 1
            if i == 0:
                x=1
                y=1
            elif i == 1:
                x=-1
                y=1
            while path and chain <= 6:
                if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                    if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        targets = [(0,-1),(1,0),(-1,0),(2,0),(-2,0),(0,-2)]
        for i in range(6):
            target=(position[0]+targets[i][0],position[1]+targets[i][1])
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
        for i in range(2):
            path = True
            chain = 1
            if i == 0:
                x=1
                y=-1
            elif i == 1:
                x=-1
                y=-1
            while path and chain <= 6:
                if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                    if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        targets = [(0,1),(1,0),(-1,0),(2,0),(-2,0),(0,2)]
        for i in range(6):
            target=(position[0]+targets[i][0],position[1]+targets[i][1])
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)
    return moves_list

def check_F_8(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,1),(0,-1),(1,0),(-1,0),(0,3),(0,-3),(3,0),(-3,0),(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for i in range(16):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_F_10(position, turn):
    moves_list=[]
    if turn == 'p1':
        if (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations \
            and position[1] < 7:
            moves_list.append((position[0],position[1]+1))
        if (position[0],position[1]+2) not in player1_locations and (position[0],position[1]+2) not in player2_locations \
            and (position[0],position[1]+1) not in player1_locations and (position[0],position[1]+1) not in player2_locations and position[1] < 6:
            moves_list.append((position[0],position[1]+2))
        if (position[0] + 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]+1,position[1]+1))
        if (position[0] - 1,position[1] + 1) in player2_locations:
            moves_list.append((position[0]-1,position[1]+1))
    if turn == 'p2':
        if (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations \
            and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
        if (position[0],position[1]-2) not in player1_locations and (position[0],position[1]-2) not in player2_locations \
            and (position[0],position[1]-1) not in player1_locations and (position[0],position[1]-1) not in player2_locations and position[1] > 1:
            moves_list.append((position[0],position[1]-2))
        if (position[0] + 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]+1,position[1]-1))
        if (position[0] - 1,position[1] - 1) in player1_locations:
            moves_list.append((position[0]-1,position[1]-1))
    return moves_list

def check_F_12(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    targets = [(0,1),(0,-1),(1,2),(-1,2),(1,-2),(-1,-2),(1,0),(-1,0)]
    for i in range(8):
        target=(position[0]+targets[i][0],position[1]+targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_F_13(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=0
            y=1
        elif i == 1:
            x=0
            y=-1
        elif i == 2:
            x=1
            y=0
        elif i == 3:
            x=-1
            y=0
        while path and chain <= 6:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=1
            y=1
        elif i == 1:
            x=1
            y=-1
        elif i == 2:
            x=-1
            y=1
        elif i == 3:
            x=-1
            y=-1
        while path and chain <= 2:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                if chain > 1:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    
    return moves_list

def check_F_14(position, turn):
    moves_list=[]
    if turn == 'p1':
        enemies_list = player2_locations
        friends_list = player1_locations
    else:
        enemies_list = player1_locations
        friends_list = player2_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=1
            y=1
        elif i == 1:
            x=-1
            y=-1
        elif i == 2:
            x=1
            y=-1
        elif i == 3:
            x=-1
            y=1
        while path and chain <= 7:
            if (position[0] + (chain*x), position[1] + (chain*y)) not in friends_list and\
                0 <= position[0] + (chain*x) <= 7 and 0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain*x),position[1] + (chain*y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_valid_moves():
    if turn_step < 2:
        options_list = options1
    else:
        options_list = options2 
    valid_options = options_list[selection]
    return valid_options

def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0]*100+50,moves[i][1]*100+50),8)

def check_win():
    loselist=['S_5','A_6','E_5','F_6']
    if all(lose not in player1_pieces for lose in loselist):
        end = True
        screen.blit(big_font.render('Player2 wins the game!',True,'blue'),(120,380))
    if all(lose not in player2_pieces for lose in loselist):
        end = True
        screen.blit(big_font.render('Player2 wins the game!',True,'red'),(120,380))

def draw_captured():
    for i in range(len(captured_pieces_player1)):
        captured_piece = captured_pieces_player1[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_images[index],(825,5+35*i))
    for i in range(len(captured_pieces_player2)):
        captured_piece = captured_pieces_player2[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_images[index],(925,5+35*i))


p1choose=False
p2choose=False
started=False

while run:
    timer.tick(fps)
    screen.fill((208,208,208))
    draw_board()
    
    if started:
        draw_pieces()
        check_win()
        draw_captured()

    if not started:
        if not p1choose:
            screen.blit(p1forces[0],(50,100))
            screen.blit(p1forces[1],(280,100))
            screen.blit(p1forces[2],(570,100))
            screen.blit(p1forces[3],(800,100))
        if not p2choose:
            screen.blit(p2forces[0],(50,500))
            screen.blit(p2forces[1],(280,500))
            screen.blit(p2forces[2],(570,500))
            screen.blit(p1forces[3],(800,500))
        if not p1choose:
            if touch(50,100,250,300):
                for i in range(3):
                    screen.blit(font.render(desc[i],True,(0,0,0)),(40,285+20*i))
                if pygame.mouse.get_pressed()[0]:
                    player1_pieces=player1_pieces_1[:]
                    player1_locations=player1_locations_1[:]
                    p1choose=True
            if touch(280,100,550,300):
                for i in range(3):
                    screen.blit(font.render(desc[i+3],True,(0,0,0)),(250,285+20*i))
                if pygame.mouse.get_pressed()[0]:
                    player1_pieces=player1_pieces_2[:]
                    player1_locations=player1_locations_2[:]
                    p1choose=True
            if touch(570,100,740,300):
                for i in range(3):
                    screen.blit(font.render(desc[i+6],True,(0,0,0)),(530,285+20*i))
                if pygame.mouse.get_pressed()[0]:
                    player1_pieces=player1_pieces_3[:]
                    player1_locations=player1_locations_3[:]
                    p1choose=True
            if touch(800,100,950,300):
                for i in range(3):
                    screen.blit(font.render(desc[i+9],True,(0,0,0)),(630,285+20*i))
                if pygame.mouse.get_pressed()[0]:
                    player1_pieces=player1_pieces_4[:]
                    player1_locations=player1_locations_4[:]
                    p1choose=True
        if not p2choose:
            if touch(50,500,250,700):
                for i in range(3):
                    screen.blit(font.render(desc[i],True,(0,0,0)),(40,685+20*i))
                if pygame.mouse.get_pressed()[0]:
                    player2_pieces=player2_pieces_1[:]
                    player2_locations=player2_locations_1[:]
                    p2choose=True
            if touch(280,500,550,700):
                for i in range(3):
                    screen.blit(font.render(desc[i+3],True,(0,0,0)),(250,685+20*i))
                if pygame.mouse.get_pressed()[0]:
                    player2_pieces=player2_pieces_2[:]
                    player2_locations=player2_locations_2[:]
                    p2choose=True
            if touch(570,500,740,700):
                for i in range(3):
                    screen.blit(font.render(desc[i+6],True,(0,0,0)),(530,685+20*i))
                if pygame.mouse.get_pressed()[0]:
                    player2_pieces=player2_pieces_3[:]
                    player2_locations=player2_locations_3[:]
                    p2choose=True
            if touch(800,500,950,700):
                for i in range(3):
                    screen.blit(font.render(desc[i+9],True,(0,0,0)),(630,685+20*i))
                if pygame.mouse.get_pressed()[0]:
                    player2_pieces=player2_pieces_4[:]
                    player2_locations=player2_locations_4[:]
                    p2choose=True
        if p1choose and p2choose:
            options1 = check_options(player1_pieces,player1_locations,'p1')
            options2 = check_options(player2_pieces,player2_locations,'p2')
            started = True
            turn_step = 0
    
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not end:
            x_coord = event.pos[0] //100
            y_coord = event.pos[1] //100
            click_coords=(x_coord,y_coord)
            if turn_step <= 1:
                if click_coords in player1_locations:
                    selection = player1_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    if click_coords in player2_locations:
                        if player1_pieces[selection] != 'E_6':
                            p2_piece = player2_locations.index(click_coords)
                            captured_pieces_player2.append(player2_pieces[p2_piece])
                            player2_pieces.pop(p2_piece)
                            player2_locations.pop(p2_piece)
                        else:
                            p2_piece = player2_locations.index(click_coords)
                            pie=player2_pieces.pop(p2_piece)
                            loc=player2_locations.pop(p2_piece)
                            player1_pieces.append(pie)
                            player1_locations.append(loc)
                        if  player1_pieces[selection] != 'S_6' and player1_pieces[selection] != 'E_6':
                            player1_locations[selection] = click_coords
                    else:    
                        player1_locations[selection] = click_coords
                    if player1_pieces[selection] in ('A_1','A_2','S_1','E_1','F_1','F_2','F_10') and player1_locations[selection][1] == 7:
                        if player1_pieces[selection] == 'A_1':
                            player1_pieces[selection] = 'A_7'
                        elif player1_pieces[selection] == 'A_2':
                            player1_pieces[selection] = 'A_7'
                        elif player1_pieces[selection] == 'S_1':
                            player1_pieces[selection] = 'S_6'
                        elif player1_pieces[selection] == 'E_1':
                            player1_pieces[selection] = 'E_6'
                        elif player1_pieces[selection] in ('F_1','F_2','F_10'):
                            player1_pieces[selection] = 'F_8'
                    options1 = check_options(player1_pieces,player1_locations,'p1')
                    options2 = check_options(player2_pieces,player2_locations,'p2')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in player2_locations:
                    selection = player2_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    
                    if click_coords in player1_locations:
                        if player2_pieces[selection] != 'E_6':
                            p1_piece = player1_locations.index(click_coords)
                            captured_pieces_player1.append(player1_pieces[p1_piece])
                            player1_pieces.pop(p1_piece)
                            player1_locations.pop(p1_piece)
                        else:
                            p1_piece = player1_locations.index(click_coords)
                            pie=player1_pieces.pop(p1_piece)
                            loc=player1_locations.pop(p1_piece)
                            player2_pieces.append(pie)
                            player2_locations.append(loc)
                        if player2_pieces[selection] != 'S_6' and player2_pieces[selection] != 'E_6':
                            player2_locations[selection] = click_coords
                    else:
                        player2_locations[selection] = click_coords
                    if player2_pieces[selection] in ('A_1','A_2','S_1','E_1','F_1','F_2','F_10') and player2_locations[selection][1] == 0:
                        if player2_pieces[selection] == 'A_1':
                            player2_pieces[selection] = 'A_7'
                        elif player2_pieces[selection] == 'A_2':
                            player2_pieces[selection] = 'A_7'
                        elif player2_pieces[selection] == 'S_1':
                            player2_pieces[selection] = 'S_6'
                        elif player2_pieces[selection] == 'E_1':
                            player2_pieces[selection] = 'E_6'
                        elif player2_pieces[selection] in ('F_1','F_2','F_10'):
                            player2_pieces[selection] = 'F_8'
                    options1 = check_options(player1_pieces,player1_locations,'p1')
                    options2 = check_options(player2_pieces,player2_locations,'p2')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
    pygame.display.flip()
pygame.quit()