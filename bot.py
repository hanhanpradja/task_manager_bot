import discord
from discord.ext import commands
from command import Command
from database import create_database

TOKEN = "INPUT YOUR OWN TOKEN"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
name = 'tugas.db'
create_database(name)
db_act = Command(name)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} sudah online.")

@bot.command()
async def add_task(ctx, *, description):
    result = db_act.add(description)
    await ctx.send(result)

@bot.command()
async def show_task(ctx):
    tasks = db_act.get_all()
    if not tasks:
        await ctx.send("Tidak ada tugas.")
    else:
        message = "\n".join([f"{id}. {desc} - {'Selesai' if status else 'Belum'}" for id, desc, status in tasks])
        await ctx.send(message)

@bot.command()
async def delete_task(ctx, task_id: int):
    result = db_act.delete(task_id)
    await ctx.send(result)

@bot.command()
async def complete_task(ctx, task_id: int):
    result = db_act.mark(task_id, 1)
    await ctx.send(result)

@bot.command()
async def undo_mark(ctx, task_id: int):
    result = db_act.mark(task_id, 0)
    await ctx.send(result)

if __name__ == "__main__":

    bot.run(TOKEN)

