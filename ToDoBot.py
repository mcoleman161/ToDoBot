import discord
from discord.ext import commands

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Create an empty list to store the tasks
tasks = []

# Event to confirm the bot is running
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    user = await bot.fetch_user(126111364476305409)
    await user.send('Hello! I have started.')

# Command to add a task to the ToDo list
@bot.command()
async def add(ctx, *, task):
    tasks.append(task)
    await ctx.send(f'Task "{task}" added to the ToDo list.')

# Command to remove all tasks from the ToDo list
@bot.command()
async def clear(ctx):
    tasks.clear()
    await ctx.send('ToDo list cleared.')
    
# Command to list all tasks in the ToDo list
@bot.command()
async def list(ctx):
    if not tasks:
        await ctx.send('The ToDo list is empty.')
    else:
        task_list = '\n'.join(tasks)
        await ctx.send(f'Current tasks:\n{task_list}')

# Command to remove one or many tasks from the ToDo list
@bot.command()
async def remove(ctx, *indices):
    indices = list(map(int, indices))
    removed_tasks = []
    for index in sorted(indices, reverse=True):
        if index >= 0 and index < len(tasks):
            removed_tasks.append(tasks.pop(index))
    if removed_tasks:
        removed_list = '\n'.join(removed_tasks)
        await ctx.send(f'Removed tasks:\n{removed_list}')
    else:
        await ctx.send('No tasks were removed.')

# Run the bot
bot.run('YOUR_BOT_TOKEN')
