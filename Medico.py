import os
import json
import time
import random
import discord
import datetime
import wikipedia
import inspirobot
import youtube_search as ytbs
from discord import Embed
from discord.ext import commands, tasks
from discord.utils import get
from discord.voice_client import VoiceClient

client = commands.Bot(command_prefix="§")

versione = "1.0.3"

ciao_words = ["ciao", "buongiorno", "hello", "salve"]
bad_words = ["cazzo", "merda", "figa", "vaffanculo", "coglione", "puttana", "troia"]

sold = ["https://static.wikia.nocookie.net/goodgameempire/images/9/93/Maceman.png/revision/latest/scale-to-width-down/105?cb=20160810070326",
        "https://static.wikia.nocookie.net/goodgameempire/images/5/5a/Crossbowman.png/revision/latest/scale-to-width-down/104?cb=20160810071532",
        "https://static.wikia.nocookie.net/goodgameempire/images/5/5a/Swordsman.png/revision/latest/scale-to-width-down/103?cb=20171029141143",
        "https://static.wikia.nocookie.net/goodgameempire/images/a/a2/Two-handed_sword.jpg/revision/latest/scale-to-width-down/122?cb=20121016160519",
        "https://static.wikia.nocookie.net/goodgameempire/images/b/b7/Heavy_Crossbowman.png/revision/latest/scale-to-width-down/100?cb=20190606220715",
        "https://static.wikia.nocookie.net/goodgameempire/images/f/f0/Veteran_Crossbowman-0.png/revision/latest/scale-to-width-down/114?cb=20190606205047",
        "https://static.wikia.nocookie.net/goodgameempire/images/6/65/Veteran_Swordsman.png/revision/latest/scale-to-width-down/100?cb=20191108084657",
        "https://static.wikia.nocookie.net/goodgameempire/images/d/df/Two-Handed_Swordsman_%28Veteran%29.png/revision/latest/scale-to-width-down/100?cb=20190630083001",
        "https://static.wikia.nocookie.net/goodgameempire/images/8/85/Vet_Heavy_Crossbow.png/revision/latest/scale-to-width-down/124?cb=20140903011405",
        "https://static.wikia.nocookie.net/goodgameempire/images/f/fc/Relic_Axeman.png/revision/latest/scale-to-width-down/98?cb=20190517045146",
        "https://static.wikia.nocookie.net/goodgameempire/images/e/e8/Relic_Shortbowman.png/revision/latest/scale-to-width-down/100?cb=20190517055554",
        "https://static.wikia.nocookie.net/goodgameempire/images/3/30/Bowman.png/revision/latest/scale-to-width-down/104?cb=20160810063433",
        "https://static.wikia.nocookie.net/goodgameempire/images/7/77/Halberdier.png/revision/latest/scale-to-width-down/107?cb=20171010203657",
        "https://static.wikia.nocookie.net/goodgameempire/images/a/a8/Longbowman.png/revision/latest/scale-to-width-down/107?cb=20171008204733",
        "https://static.wikia.nocookie.net/goodgameempire/images/3/3c/IMG_0547.PNG/revision/latest/scale-to-width-down/107?cb=20170518162614",
        "https://static.wikia.nocookie.net/goodgameempire/images/e/ea/Relic_Hammerman.png/revision/latest/scale-to-width-down/100?cb=20190517061130",
        "https://static.wikia.nocookie.net/goodgameempire/images/5/5a/Relic_Longbowman.png/revision/latest/scale-to-width-down/100?cb=20190517061944"]

#EVENTS=========================================================================
@client.event
async def on_connect():
    print(f"{client.user} si è connesso a Discord")

@client.event
async def on_disconnect():
    print(f"{client.user} si è disconnesso da Discord")

@client.event
async def on_ready():
    print("Medico della Peste è Online!")
    await client.change_presence(activity=discord.Game(f"by Zoldie#4848 - Versione {versione}"))
#===============================================================================

#MESSAGE========================================================================
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif any(word in message.content.lower() for word in bad_words):
        await message.delete(message)
    elif any(word in message.content.lower() for word in ciao_words):
        await message.channel.send("Ciao!")
    elif message.content.startswith("https://"):
        await message.delete(message)
        await message.channel.send("È vietato inviare link di qualsiasi tipo!")
    await client.process_commands(message)
#===============================================================================

#INFO===========================================================================
@client.command(help="Mostra le informazioni tecniche del server")
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    embed = discord.Embed(title=f"Informazioni del server \"{name}\"", description=description, color=discord.Color.dark_green())
    embed.set_thumbnail(url=icon)
    embed.set_author(name="Medico della peste", icon_url="https://cdn.discordapp.com/app-icons/817397996454150144/934735c613c69ba324f5877ed990a901.png?size=256")
    embed.add_field(name="Proprietario", value=owner, inline=True)
    embed.add_field(name="ID Server", value=id, inline=True)
    embed.add_field(name="Regione", value=region, inline=True)
    embed.add_field(name="Numero Membri", value=memberCount, inline=True)
    await ctx.send(embed=embed)

@client.command(help="Invia le informazioni sul bot", aliases=["presenta", "introduce","presentati"])
async def info(ctx):
    await ctx.message.delete()
    embed.set_author(name="Medico della peste", icon_url="https://cdn.discordapp.com/app-icons/817397996454150144/934735c613c69ba324f5877ed990a901.png?size=256")
    embed = discord.Embed(title=f"Medico della Peste", description="Bot Discord\nCoded by Zoldie#4848", color=discord.Color.dark_green())
    embed.add_field(name="Comandi", value="Scrivi in chat §help per ricevere una lista di tutti i comandi disponibili.", inline=False)
    embed.add_field(name="Prestigio", value="Il Medico della Peste ha un sistema di prestigio/onore integrato, che ha un funzionamento simile all'XP.\nPuoi donare prestigio agli altri utenti con il comando \"§onora @nome_dell'utente\".\nQuesto sistema è ancora un **WIP**", inline=False)
    await ctx.send(embed=embed)
#===============================================================================

#STATUS=========================================================================
@client.command(help="Imposta lo status offline")
async def offline(ctx):
    if str(ctx.author) == "Zoldie#4848":
        await client.change_presence(status=discord.Status.offline)
        print("Status cambiato ad Offline")
    else:
        await ctx.send("Solo l'host può usare questo comando!")

@client.command(help="Imposta lo status online")
async def online(ctx):
    if str(ctx.author) == "Zoldie#4848":
        await client.change_presence(status=discord.Status.online)
        print("Status cambiato ad Online")
    else:
        await ctx.send("Solo l'host può usare questo comando!")
#===============================================================================

#ADMIN==========================================================================
@client.command(help="Controlla la latenza del bot")
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(help="Mostra l'avatar di un membro")
@commands.guild_only()
async def avatar(ctx, *, user:discord.Member=None):
    user = user or ctx.author
    await ctx.send(f"Avatar di **{user.name}**\n{user.avatar_url_as(size=1024)}")
        
@client.command(help="Gestisci la slowmode del canale testuale in cui ti trovi")
@commands.guild_only()
async def slowmode(ctx, sec: int):
    if str(ctx.author) == "Zoldie#4848" or str(ctx.author) == "Collium#0412" or str(ctx.author) == "Collium#7709":
        await ctx.channel.edit(slowmode_delay=sec)
        await ctx.send(f"Impostata la slowmode del canale \"#{ctx.channel.name}\" a {sec} secondi!")
    else:
        await ctx.send("Non hai il permesso di utilizzare questo comando!")
#===============================================================================


#FUN============================================================================
@client.command(help="Invia un soldato casuale di Goodgame Empire", aliases=["soldato", "soldati", "guerriero", "guerrieri"])
async def soldier(ctx):
    chosen_img=random.choice(sold)
    embed=discord.Embed(
    color=discord.Color.dark_green()
    )
    embed.set_image(url=chosen_img)
    await ctx.send(embed=embed)

@client.command(help="Invia un'immagine \"ispirazionale\" dal sito inspirobot.me", aliases=["inspireme", "inspire", "ispirare", "ispirami"])
async def inspirobot(ctx):
    try:
        cuote = inspirobot.generate()
        quote = cuote.url
        embed = discord.Embed(
        color=discord.Color.dark_green()
        )
        embed.set_author(name="InspiroBot", icon_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Finspirobot.me%2Fwebsite%2Fimages%2Finspirobot-dark-green.png&f=1&nofb=1")
        embed.set_image(url=quote)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Impossibile raggiungere il sito inspirobot.me")

@client.command(help="Ripete il messaggio che segue", aliases=["repeat", "ripeti", "say"])
async def echo(ctx, *, message=None):
    message = message or "Per favore inserire il messaggio da ripetere."
    await ctx.message.delete()
    await ctx.send(message)
#===============================================================================

#RANDOM=========================================================================
@client.command(help="Lancia una moneta", aliases=["coin", "moneta", "testacroce"])
async def flip(ctx):
    testacroce = ["Testa!", "Croce!"]
    await ctx.send(random.choice(testacroce))

@client.command(help="Lancia un dado", aliases=["dice"])
async def dado(ctx, max=6):
    n = random.randrange(1, max)
    await ctx.send(str(n))
#===============================================================================

#PRESTIGIO======================================================================
async def open_money(user):
    users = await get_money_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
    with open("Money.json", "w") as f:
        users = json.dump(users,f)
        return True

async def get_money_data():
    with open("Money.json", "r") as f:
        users = json.load(f)
    return users

@client.command(help="Aggiungi del prestigio alla persona taggata", aliases=["+", "onora"])
async def add(ctx, tag:discord.Member, acoin=1):
    await open_money(tag)
    users = await get_money_data()
    if acoin == 0:
        await ctx.send(f"{ctx.author}, credi di essere spiritoso/a?")
    elif acoin < 0:
        if str(ctx.author) == "Zoldie#4848":
            user = tag
            earnings = acoin
            await ctx.send(f"Congratulazioni {tag} hai ottenuto {acoin} punti prestigio!")
            users[str(user.id)]["wallet"] += earnings
            with open("Money.json", "w") as f:
                json.dump(users,f)
        else:
            await ctx.send(f"{ctx.author}, credi di essere spiritoso/a?")
    else:
        user = tag
        earnings = acoin
        await ctx.send(f"Congratulazioni {tag} hai ottenuto {acoin} punti prestigio!")
        users[str(user.id)]["wallet"] += earnings
        with open("Money.json", "w") as f:
            json.dump(users,f)

@client.command(help="Controlla quanti punti prestigio possiedi", aliases=["onore"])
async def prestigio(ctx, target:discord.Member=None):
    if target is None:
        await open_money(ctx.author)
        user = ctx.author
        users = await get_money_data()
        money_amt = users[str(user.id)]["wallet"]
        embed = discord.Embed(title = f"Prestigio di {ctx.author.name}", color = discord.Color.dark_green())
        embed.add_field(name="Punti Prestigio:", value = money_amt)
        await ctx.send(embed=embed)
    else:
        await open_money(target)
        user = target
        users = await get_money_data()
        money_amt = users[str(user.id)]["wallet"]
        embed = discord.Embed(title = f"Prestigio di {user.name}", color = discord.Color.dark_green())
        embed.add_field(name="Punti Prestigio", value = money_amt)
        await ctx.send(embed=embed)

@client.command(help="Mostra la classifica dei membri con più prestigio", aliases=["leaderboard"])
async def classifica(ctx, x=3):
    users = await get_money_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"]
        leader_board[total_amount] = name
        total.append(total_amount)
    total = sorted(total, reverse=True)
    em = discord.Embed(title=f"Top {x} Utenti con più Prestigio", color=discord.Color.gold())
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        name = await client.fetch_user(id_)
        em.add_field(name = f"{index}. {name}", value = f"<==**{amt}**==>", inline=False)
        if index == x:
            break
        else:
            index += 1
        await ctx.send(embed=em)
#===============================================================================

#RICERCHE=======================================================================
@client.command(help="Cerca un video su YouTube", aliases=["youtube", "yt"])
async def youtube_search(ctx, *, search):
    results = ytbs.YoutubeSearch(search, max_results=3).to_dict()
    try:
        tit1 = results[0]["title"]
        rurl1 = results[0]["url_suffix"]
        url1 = "https://www.youtube.com" + rurl1
        img1 = results[0]["thumbnails"][0]
        view1 = results[0]["views"]
        cha1 = results[0]["channel"]
        dur1 = results[0]["duration"]#>>
        tit2 = results[1]["title"]
        rurl2 = results[1]["url_suffix"]
        url2 = "https://www.youtube.com" + rurl2
        img2 = results[1]["thumbnails"][0]
        view2 = results[1]["views"]
        cha2 = results[1]["channel"]
        dur2 = results[1]["duration"]#>>
        tit3 = results[2]["title"]
        rurl3 = results[2]["url_suffix"]
        url3 = "https://www.youtube.com" + rurl3
        img3 = results[2]["thumbnails"][0]
        view3 = results[2]["views"]
        cha3 = results[2]["channel"]
        dur3 = results[2]["duration"]#>>

        embed1=discord.Embed(title="[1] " + tit1, description=url1, url=url1, color=0xff0000)
        embed1.set_thumbnail(url=img1)
        embed1.add_field(name="Visualizzazioni:", value=view1.rstrip(" visualizzazioni"), inline=True)
        embed1.add_field(name="Canale:", value=cha1, inline=True)
        embed1.add_field(name="Durata:", value=dur1, inline=True)
        embed2=discord.Embed(title="[2] " + tit2, description=url2, url=url2, color=0xff0000)
        embed2.set_thumbnail(url=img2)
        embed2.add_field(name="Visualizzazioni:", value=view2.rstrip(" visualizzazioni"), inline=True)
        embed2.add_field(name="Canale:", value=cha2, inline=True)
        embed2.add_field(name="Durata:", value=dur2, inline=True)
        embed3=discord.Embed(title="[3] " + tit3, description=url3, url=url3, color=0xff0000)
        embed3.set_thumbnail(url=img3)
        embed3.add_field(name="Visualizzazioni:", value=view3.rstrip(" visualizzazioni"), inline=True)
        embed3.add_field(name="Canale:", value=cha3, inline=True)
        embed3.add_field(name="Durata:", value=dur3, inline=True)

        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
    except:
        await ctx.send("La ricerca richiesta ha portato ad un errore.")

@client.command(help="Effettua una ricerca su Wikipedia", aliases=["wikipedia"])
async def wiki(ctx, *, search:str):
    try:
        wikipedia.set_lang("it")
        ws=wikipedia.page(search)
        embed=discord.Embed(title=ws.title, url=ws.url, description=ws.summary, color=0xfffffe)
        embed.set_author(name="Wikipedia", icon_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fpngimg.com%2Fuploads%2Fwikipedia%2Fwikipedia_PNG35.png&f=1&nofb=1")
        embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F7%2F77%2FWikipedia_svg_logo.svg%2F1200px-Wikipedia_svg_logo.svg.png&f=1&nofb=1")
        embed.set_image(url=ws.images[0])
        embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    except wikipedia.exceptions.DisambiguationError as e:
        await ctx.send(f"Sembra che la ricerca \"*{search}*\" si riferisca a più pagine di Wikipedia:\n{e.options}")
    except wikipedia.exceptions.PageError:
        await ctx.send(f"Sembra che non esista una pagina Wikipedia per \"*{search}*\".")
    except discord.errors.HTTPException:
        await ctx.send(f"Sembra che questa pagina abbia troppe informazioni per essere inserita in un embed.\nLascio qui il link per raggiungere la pagina:\n{ws.url}")
#===============================================================================

#VOICE==========================================================================
@client.command(help="Sposta o connette il bot al tuo canale vocale", aliases=["joinme"])
async def join(ctx):
        global voice
        try:
            channel = ctx.author.voice.channel
        except:
            return await ctx.send("Prima devi connetterti ad un canale vocale!")
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

@client.command(help="Disconnette il bot da un canale vocale")
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Non sono connesso ad un canale vocale!")

@client.command(help="Riproduce l'audio di un video di Youtube")
async def play(ctx, *url:str):
    if url:
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Aspetta che il brano in riproduzione finisca o usa il comando $stop.")
            return
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if not voice.is_connected():
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Generale')
            await voiceChannel.connect()
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': "./song.mp3",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        song_search = " ".join(url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{song_search}"])
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    else:
        await ctx.send("Assicurati di aver inserito il nome della canzone o un url di youtube!")

@client.command(help="Mette in pausa l'audio in riproduzione")
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    elif not voice.is_connected():
        await ctx.send("Non sono in un canale vocale al momento!")
    else:
        await ctx.send("Non sto riproducendo audio al momento!")

@client.command(help="Riprende la riproduzione di un audio precedentemente messo in pausa")
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    elif not voice.is_connected():
        await ctx.send("Non sono in un canale vocale al momento!")
    else:
        await ctx.send("L'audio non è in pausa!")

@client.command(help="Ferma la riproduzione di un brano, eliminandolo dalla coda di riproduzione")
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        voice.stop()
    else:
        await ctx.send("Non sono in un canale vocale al momento!")
#===============================================================================

@client.command(help="Disconnette il bot da Discord")
async def logout(ctx):
    if str(ctx.author) == "Zoldie#4848":
        qexit = input("Disconnect from Discord? y/n")
        if qexit == "y":
            await ctx.send("Vi saluto feudatari, addio!")
            await client.logout()
            print(f'{client.user} has logout from Discord!')
        elif qexit == "n":
            pass
        else:
            print(qexit)
            print("Invalid Input!")
    else:
        await ctx.send("Solo l'host può disconnettermi da Discord")

client.run('ODE3Mzk3OTk2NDU0MTUwMTQ0.YEI7NA.XUExf0Z4aWhFW71yIS-sy-pNl_A')
#@client.command
#async def play(ctx, url:str):
