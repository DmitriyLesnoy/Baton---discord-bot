from ntpath import join
from os import read
from random import random
from cv2 import split
from discord import channel, guild, mentions, message, role, voice_client,VoiceChannel
from discord.ext import commands
from discord.ext.commands.core import command
from discord.user import ClientUser
from discord.utils import get
import discord
import random
import time
from matplotlib import offsetbox
from matplotlib.pyplot import figimage

from sklearn import random_projection
from torch import square

client = commands.Bot(command_prefix='>')

fishs=['пажилая рыба', 'пажилой иглобрюх', 'пажилой кальмар', 'пажилой осьминог', 'пажилой гомункул', 'пажилой кит', 'пажилая акулОчка', 'пажилая черепаха', 'пажилой дельфин', 'пажилой краб', 'пажилая ракушка', 'пажилая морская звёздочка', 'пажилой ламантин', 'пажилая медузка', 'пажилая морская свинка', 'пажилой морской огурчик', 'пажилая акулка', 'пожилая акула', 'пажилой скат', 'пажилой дельфинчик', 'пажилая рыбка', 'пажилая устрица', 'пажилой рачок', 'пажилой рак (пресноводный)', 'пажилая креветочка', 'пажилой китёнок', 'пажилая косаточка', 'пажилая фуга', 'пажилая рыба-капля', 'пажилая зелёная водоросль', 'пажилая ламинария']
black_list=[817670520685199370,711069979457486909,711069079653318759,711069431375200298]

#:white_large_square:  ':black_large_square:':white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square:
#:black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:
#:white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square:
#:black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:
#:white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square:
#:black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:
#:white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square:
#:black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:


offset='      '

board_clear=[['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□'],
            ['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□'],
            ['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□'],
            ['□      ','■      ','□      ','■      ','□      ','■      ','□      ','■'],
            ['■      ','□      ','■      ','□      ','■      ','□      ','■      ','□']]

board_first=board_clear


figures=[['○      ','♘    ','♗    ','♖    ','♕    ','♔    '],
         ['●      ','♞    ','♝    ','♜    ','♛    ','♚    ']]   
# [['♙','♘','♗','♖','♕','♔'],['♟','♞','♝','♜','♛','♚']]   
squares=['□','■']

board_first[0]=[figures[1][3],figures[1][1],figures[1][2],figures[1][4],figures[1][5],figures[1][2],figures[1][1],figures[1][3]]
board_first[1]=[figures[1][0],figures[1][0],figures[1][0],figures[1][0],figures[1][0],figures[1][0],figures[1][0],figures[1][0]]

board_first[7]=[figures[0][3],figures[0][1],figures[0][2],figures[0][4],figures[0][5],figures[0][2],figures[0][1],figures[0][3]]
board_first[6]=[figures[0][0],figures[0][0],figures[0][0],figures[0][0],figures[0][0],figures[0][0],figures[0][0],figures[0][0]]


global player2,player1,dir,score1,score2

player1=None
player2=None
dir==None
score1=[]
score2=[]
	

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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
        exit()

def print_board(board):
    toprint=[]

    toprint.append(plus_list(['`'+offset,'A      ','B      ','C      ','D      ','E      ','F      ','G      ','H']))
    for i in range(8):
        toprint.append(str(i+1)+'      '+plus_list(board[i]))

    toprint.append(plus_list(['. '+offset,'A      ','B      ','C      ','D      ','E      ','F      ','G      ','H']))

    toprint.append(f'Фигуры ■{player1.mention}: '+plus_list(score1))
    toprint.append(f'Фигуры □{player2.mention}: '+plus_list(score2))

    return toprint

def plus_list(list):
    plus=''
    for i in list:
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

    
    board_game=board_first


    await ctx.send('\n'.join(print_board(board_first)))


    return player1,player2,dir,board_game

@client.command()
async def chess_go(ctx, go1=None, go2=None):
    abc2num={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,}
    global board_game
    if go1==None and go2==None:
        if dir==1:
            await ctx.send(f'Сечайс ходит  ■{player1.mention}')
        else:
            await ctx.send(f'Сечайс ходит  □{player2.mention}')
    else:
        go1=list(go1)
        go2=list(go2)

        go1[1]=int(go1[1])     
        go2[1]=int(go2[1])

        go1[0]=abc2num[go1[0]]
        go2[0]=abc2num[go2[0]]

        print(go1,go2)
        






client.run('ODk2NzExNjY2MjE2MDkxNjUw.YWLF0Q.G4IJ2RRjSONyXsHf65LuP5Q0Wbw')