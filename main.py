import random
from discord import channel, guild, mentions, message, role, voice_client,VoiceChannel
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
import discord
from psutil import net_connections

client = commands.Bot(command_prefix='>')

fishs=['пажилая рыба', 'пажилой иглобрюх', 'пажилой кальмар', 'пажилой осьминог', 'пажилой гомункул', 'пажилой кит', 'пажилая акулОчка', 'пажилая черепаха', 'пажилой дельфин', 'пажилой краб', 'пажилая ракушка', 'пажилая морская звёздочка', 'пажилой ламантин', 'пажилая медузка', 'пажилая морская свинка', 'пажилой морской огурчик', 'пажилая акулка', 'пожилая акула', 'пажилой скат', 'пажилой дельфинчик', 'пажилая рыбка', 'пажилая устрица', 'пажилой рачок', 'пажилой рак (пресноводный)', 'пажилая креветочка', 'пажилой китёнок', 'пажилая косаточка', 'пажилая фуга', 'пажилая рыба-капля', 'пажилая зелёная водоросль', 'пажилая ламинария']
black_list=[817670520685199370,711069979457486909,711069079653318759,711069431375200298,944915898555326484]

# global player2,player1,dir,score1,score2,board_clear,board_game,offset


# https://tenor.com/view/valakas-glad-gif-21423993

score1=[]
score2=[]
dir=1


offset='      '

board_clear=[['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□'],
            ['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□'],
            ['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□'],
            ['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□']]

board_game=[['♜    ','♞    ','♝     ','♛    ','♚     ','♝     ','♞    ','♜    '],
            ['●      ','●      ','●      ','●      ','●      ','●      ','●      ','●'],
            ['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□'],
            ['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□'],
            ['○      ','○      ','○      ','○      ','○      ','○      ','○      ','○      '],
            ['♖    ','♘    ','♗    ','♕    ','♔    ','♗    ','♘    ','♖    ']]

figures=[['○      ','♘    ','♗    ','♖    ','♕    ','♔    ','□      '],
         ['●      ','♞    ','♝    ','♜    ','♛    ','♚    ','■      '],]   
# [['♙','♘','♗','♖','♕','♔'],['♟','♞','♝','♜','♛','♚']]
   
# squares=['□      ','■      ']

# board_game[0]=[figures[1][3],figures[1][1],figures[1][2],figures[1][4],figures[1][5],figures[1][2],figures[1][1],figures[1][3]]
# board_game[1]=[figures[1][0],figures[1][0],figures[1][0],figures[1][0],figures[1][0],figures[1][0],figures[1][0],figures[1][0]]

# board_game[7]=[figures[0][3],figures[0][1],figures[0][2],figures[0][4],figures[0][5],figures[0][2],figures[0][1],figures[0][3]]
# board_game[6]=[figures[0][0],figures[0][0],figures[0][0],figures[0][0],figures[0][0],figures[0][0],figures[0][0],figures[0][0]]


dir==1
score1=[]
score2=[]
	

@client.event
async def on_ready():
    print('Бот {0.user} был авторизирован'.format(client))

@client.command()
async def info(ctx):
    i=open('help.txt')
    p=i.read()
    await ctx.send(p)

@client.command()
async def addrole(ctx, role: discord.Role, user: guild.Member):
    if role.id in black_list :
        await ctx.send(f" Роль {role.mention} не может быть выдана {user.mention} ")
    else:
        await user.add_roles(role)
        await ctx.send(f" Роль {role.mention} выдана {user.mention} ")

@client.command()
async def remove(ctx, role: discord.Role, user: guild.Member):
    if role.id in black_list:
        await ctx.send(f" Роль {role.mention} не может быть убрана {user.mention} ")
    else:
        await user.remove_roles(role)
        await ctx.send(f" Роль {role.mention} убрана  {user.mention} ")
    
@client.command()
async def fish(ctx,user:guild.Member):
    await ctx.message.delete()
    await user.edit(nick = fishs[random.randint(0,32)])

@client.command()
async def rand(ctx,one,two):
    number=random.randint(int(one),int(two))
    await ctx.send(f"Я выбираю число.....  "+str(number))

@client.command()
async def choose(ctx,one,two):
    i=random.randint(0,1)
    if i:
        await ctx.send(f"Я выбираю.....  "+one)
    else:
        await ctx.send(f"Я выбираю.....  "+two)

@client.command()
async def off(ctx):
    if ctx.message.author.id==657906035675365387:
        await ctx.send('Завершение работы')
        exit()

def print_board(board,play1,play2):
    global score1,score2
    toprint=[]

    toprint.append(plus_list(['`'+offset,'A      ','B      ','C      ','D      ','E      ','F      ','G      ','H']))
    for i in range(8):
        toprint.append(str(i+1)+'      '+plus_list(board[i]))

    toprint.append(plus_list(['. '+offset,'A      ','B      ','C      ','D      ','E      ','F      ','G      ','H']))

    toprint.append(' ')
    toprint.append(f'Фигуры ■{player1.mention}: '+plus_list(score1))
    toprint.append(f'Фигуры □{player2.mention}: '+plus_list(score2))
    toprint.append(' ')
    if dir==1:
        toprint.append(f'Сейчас ходит {player1.mention}')
    else:
        toprint.append(f'Сейчас ходит {player2.mention}')

    return toprint

def plus_list(list_):
    plus=''
    for i in list_:
        for j in i:
            plus+=j
    return plus

@client.command()
async def chess_start(ctx,p1:guild.Member,p2:guild.Member):
    global player1,player2,dir,board_game
    player1=p1
    player2=p2
    dir=1
    print(player1,player2)

    await ctx.send('\n'.join(print_board(board_game,player1,player2)))

    return player1,player2

@client.command()
async def chess_go(ctx, go1_=None, go2_=None):
    global dir,board_game,board_clear

    abc2num={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    if go1_==None and go2_==None:
        if dir==1:
            await ctx.send(f'Сечайс ходит  ■{player1.mention}')
        else:
            await ctx.send(f'Сечайс ходит  □{player2.mention}')
    else:
        if (dir==1 and ctx.author==player1) or (dir==-1 and ctx.author==player2):

            dir=dir*(-1)

            go1=list(go1_)
            go2=list(go2_)

            go1[1]=int(go1[1])-1     
            go2[1]=int(go2[1])-1

            go1[0]=int(abc2num[go1[0]])
            go2[0]=int(abc2num[go2[0]])

            flag_error=False
                
            if board_game[go1[1]][go1[0]]==figures[1][6] or board_game[go1[1]][go1[0]]==figures[0][6]:
                flag_error=True
                await ctx.send('клеточка')

            if board_game[go1[1]][go1[0]]==figures[0][0]:
                if not(go1[0]==go2[0]) or not(go1[1]!=go2[1]) or not(go1[1]<go2[1]):
                    if not(go1[1]==1 and (go2[1]-go1[1])<=2) or not(go1!=1 and (go2[1]-go1[1])>1):
                        flag_error=True
                        await ctx.send('пешка')
            if board_game[go1[1]][go1[0]]==figures[1][0]:
                if not(go1[0]==go2[0]) or not(go1[1]!=go2[1]) or not(go1[1]>go2[1]):
                    if not(go1[1]==6 and (go1[1]-go2[1])<=2) or not(go1[1]!=6 and (go1[1]-go2[1])>1):
                        flag_error=True
                        await ctx.send('пешка')
            

            if flag_error:
                await ctx.send("Неверный ход "+str(go1_)+" - "+str(go2_))
            else:
                board_game[go2[1]][go2[0]]=board_game[go1[1]][go1[0]]    

                board_game[go1[1]][go1[0]]=board_clear[go1[1]][go1[0]]
                
                await ctx.send('\n'.join(print_board(board_game,player1,player2)))        
        else:
            if dir==1:
                await ctx.send(f'{ctx.author.mention} сейчас ходит {player1.mention}')
            else:
                await ctx.send(f'{ctx.author.mention} сейчас ходит {player2.mention}')


@client.command()
async def chess_finish(ctx):
    await ctx.send(f'Игра завершена игроком {ctx.author.mention}')




client.run('ODk2NzExNjY2MjE2MDkxNjUw.YWLF0Q.G4IJ2RRjSONyXsHf65LuP5Q0Wbw')