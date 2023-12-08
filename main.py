
import discord
from discord.ext import commands
import os, random
import requests
import random
intents = discord.Intents.default()
intents.message_content = True
from model import get_class
bot = commands.Bot(command_prefix='$', intents=intents)

pop=['https://open.spotify.com/track/1ado6H8nwj0izGVinobwuP?si=9d8bd82e7e5547c1' , 'https://open.spotify.com/track/7uwo3VQxUlRtKudAjluuTr?si=acae93c3aa994095' ,'https://open.spotify.com/track/26aNjbOgTVrFZEx7was69A?si=394084bd09be440f']
e=['https://open.spotify.com/track/4P4i1b7cg9xH3iz5eX3Q6W?si=35115a6262f04e65' ,'https://open.spotify.com/track/0JiVRyTJcJnmlwCZ854K4p?si=4b2190817aaa416b' , 'https://open.spotify.com/track/0QjpQP1w7apeMXzioL8sqN?si=b44acca8030344c5']
r=['https://open.spotify.com/track/5T8EDUDqKcs6OSOwEsfqG7?si=f755e80eda894de9' ,'https://open.spotify.com/track/7snQQk1zcKl8gZ92AnueZW?si=3ebe43b449934c2c' ,'https://open.spotify.com/track/5AEOqLsRJFAoSS4ay4Jzao?si=1883371e60e7466c']
j=['https://open.spotify.com/track/78MI7mu1LV1k4IA2HzKmHe?si=1b2d30197be24529' ,'https://open.spotify.com/track/5w4tCdeCq74xLodAc8uZMQ?si=1b8804e330b44f46' , 'https://open.spotify.com/track/2u3aQ9fMrUaC5vcxRb853x?si=2d57555165304378']
rn=['https://open.spotify.com/track/2fXwCWkh6YG5zU1IyvQrbs?si=692f50c37acc4203' , 'https://open.spotify.com/track/7MYmo0JJJDmu4MZTSAF9y3?si=f9223bc28a8046e8'  ,'https://open.spotify.com/track/1IhURnZpLfkVO7fKxBGL0a?si=b2c1b0980c244593']
pr=['https://open.spotify.com/track/0ufRKgpHvlP0676HyqSpKb?si=f3b21e97bdee4e4a' , 'https://open.spotify.com/track/74X2u8JMVooG2QbjRxXwR8?si=5e96e23f04394334'  ,'https://open.spotify.com/track/5uraJqtCBvLpwt3VeomZdq?si=f7c8383f662b4516'  ,'https://open.spotify.com/track/0Z54rUZ81Vn0qphFR3jXUb?si=b10895fb13eb49d0' ,'https://open.spotify.com/track/7MXVkk9YMctZqd1Srtv4MB?si=dcc5f5e6535c42cd']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def halo(ctx):
    await ctx.send(f'Halo! aku bot yang bisa membantu kamu! ')

@bot.command()
async def info(ctx):
    await ctx.send(f'Aku bisa membantu kamu mengenai Musik!Kamu bisa mengetik $musik untuk Music dan juga $bantuan jika kamu perlu bantuan!')

@bot.command()
async def bantuan(ctx):
    await ctx.send(f'Berikut command yang bisa membantumu! \n1. $musik : Apa yang bisa kamu cari di bagian musik \n2. $Pengertian_Musik : Pengertian dari musik yang dapat kamu ketahui \n3. $Genre_Musik : Genre-Genre yang populer di dunia mu! \n4. $Pop : Informasi mengenai genre musik pop \n5. $pilihpop : Salah satu lagu Pop  \n6. $Rock : Informasi mengenai genre musik rock  \n7. $pilihrock : Salah satu lagu rock n\8. $Jazz : Informasi mengenai genre musik Jazz \n9. $pilihjazz : Salah satu lagu jazz \n10. $EDM : Informasi mengenai genre musik EDM \n11. $pilihedm : Salah satu lagu EDM \n12. $RNB : Informasi mengenai genre musik RNB \n13. $pilihedm : Salah satu lagu RNB \n14. $pilihrandom : Salah satu lagu acak dari genre yang berbeda \n15. $telecaster_stratocaster : Aku bisa membantumu menebak apakah itu gitar Stratocaster atau Telecaster ')
@bot.command()
async def musik(ctx):
    await ctx.send('Apa yang ingin kamu ketahui? \n-Pengertian_Musik  \n-Genre_Musik')

@bot.command()
async def Pengertian_Musik(ctx):
    await ctx.send(f'Musik termasuk sejenis fenomena intuisi, untuk mencipta, memperbaiki, dan mempersembahkannya dalam suatu bentuk seni. Musik adalah sebuah fenomena unik yang dihasilkan oleh beberapa alat musik. Namun, seni musik tidak hanya sebatas bunyi/suara yang dihasilkan dari alat musik, apa pun yang bisa menghasilkan bunyi/suara itu bisa dianggap sebagai musik; istilahnya disebut dengan musik alam.  \nSource:https://id.wikipedia.org/wiki/Musik')

@bot.command()
async def Genre_Musik(ctx):
    await ctx.send(f'Genre musik adalah pengelompokan musik sesuai dengan kemiripannya satu sama lain. Di dunia mu ada banyak genre musik! yang umumnya diketahui oleh manusia ada genre Pop, Electron Dance Music(EDM),Rock,Jazz,,Rhythm and Blues,dan masih banyak lagi!')

@bot.command()
async def Pop(ctx) :
    await ctx.send(f'Musik pop adalah sebuah genre musik populer yang berasal dari bentuk modernnya di Amerika Serikat dan Inggris pada pertengahan 1950-an. Istilah "musik populer" dan "musik pop" sering digunakan secara bergantian, meskipun yang pertama menggambarkan semua musik yang populer dan mencakup banyak gaya yang beragam.  \nSource:https://id.wikipedia.org/wiki/Musik_pop')

@bot.command()
async def Rock(ctx) :
    await ctx.send(f'Musik rok atau musik cadas adalah genre yang luas dari musik populer yang berasal dari rock and roll di Amerika Serikat pada akhir 1940-an dan awal 1950-an, berkembang menjadi berbagai gaya yang berbeda pada pertengahan 1960-an hingga seterusnya, terutama di Amerika Serikat dan Inggris  \nSource:https://id.wikipedia.org/wiki/Musik_rok')

@bot.command()
async def EDM(ctx) :
    await ctx.send(f'Musik dansa elektronik atau electronic dance music adalah berbagai genre musik elektronik perkusif yang dibuat sebagian besar untuk klub malam, rave, dan festival-festival \nSource:https://id.wikipedia.org/wiki/Musik_dansa_elektronik')

@bot.command()
async def Jazz(ctx) :
    await ctx.send(f'Jaz adalah aliran musik yang berasal dari Amerika Serikat pada awal abad ke-20 dengan akar-akar dari musik Afrika dan Eropa. Musik jaz banyak menggunakan gitar, trombon, piano, trompet, dan saksofon. Elemen penting dalam jaz adalah blue notes, improvisasi, polyrhythms, sinkopasi, dan shuffle note. \nSource:https://id.wikipedia.org/wiki/Musik_jaz')

@bot.command()
async def RNB(ctx) :
    await ctx.send(f'R&B adalah genre musik populer yang menggabungkan jazz, gospel, dan blues, aliran jenis ini pertama kali diperkenalkan oleh pemusik Afrika-Amerika. Istilah ini pertama kali dipakai sebagai istilah pemasaran dalam musik di Amerika Serikat pada tahun 1947 oleh Jerry Wexler yang bekerja pada majalah Billboard  \nSource:https://id.wikipedia.org/wiki/R%26B')

@bot.command()
async def pilihpop(ctx) :
    pilih = random.choice(pop)
    await ctx.send(f'Silahkan buka lagu dengan link berikut {pilih}')

@bot.command()
async def pilihrock(ctx) :
    pilih = random.choice(r)
    await ctx.send(f'Silahkan buka lagu dengan link berikut {pilih}')

@bot.command()
async def pilihjazz(ctx) :
    pilih = random.choice(j)
    await ctx.send(f'Silahkan buka lagu dengan link berikut {pilih}')

@bot.command()
async def pilihrnb(ctx) :
    pilih = random.choice(r)
    await ctx.send(f'Silahkan buka lagu dengan link berikut {pilih}')

@bot.command()
async def pilihedm(ctx) :
    pilih = random.choice(e)
    await ctx.send(f'Silahkan buka lagu dengan link berikut {pilih}')

@bot.command()
async def pilihrandom(ctx) :
    pilih = random.choice(pr)
    await ctx.send(f'Silahkan buka lagu dengan link berikut {pilih}')
@bot.command()
async def telecaster_stratocaster(ctx):
    await ctx.send(f'Kamu bisa mengunggah foto gitar Stratocaster/Telecaster dan aku akan menebaknya! unggah foto dan gunakan command $check')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Anda lupa mengunggah gambar :(")


bot.run("")