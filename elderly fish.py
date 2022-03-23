from os import read
from random import random
from discord import guild, mentions, message, role
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
import discord
import random

client = commands.Bot(command_prefix='>')

fishs=['пажилая рыба', 'пажилой иглобрюх', 'пажилой кальмар', 'пажилой осьминог', 'пажилой гомункул', 'пажилой кит', 'пажилая акулОчка', 'пажилая черепаха', 'пажилой дельфин', 'пажилой краб', 'пажилая ракушка', 'пажилая морская звёздочка', 'пажилой ламантин', 'пажилая медузка', 'пажилая морская свинка', 'пажилой морской огурчик', 'пажилая акулка', 'пожилая акула', 'пажилой скат', 'пажилой дельфинчик', 'пажилая рыбка', 'пажилая устрица', 'пажилой рачок', 'пажилой рак (пресноводный)', 'пажилая креветочка', 'пажилой китёнок', 'пажилая косаточка', 'пажилая фуга', 'пажилая рыба-капля', 'пажилая зелёная водоросль', 'пажилая ламинария']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# @client.on_message()

while True:
    channel=906796493451714581
    members=channel.members

client.run('OTI5MjMzMjQzODQ3NDA1NjI4.YdkV5Q.dDiCu3aXBE-WA34FiFcDhW2gRoY')