import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

#setup intents for bot
intents = discord.Intents.default()
intents.message_content = True


# Create a bot instance with ! being the prefix
bot = commands.Bot(command_prefix='!', intents=intents)


# Replace 'your_token_here' with your actual bot token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


# Create an empty list to store the tasks
tasks = []

# Event to confirm the bot is running
@bot.event
async def on_ready():
    # this is for if it is joined to a channel print(f'{bot.user.name} has connected to Discord!')
    user = await bot.fetch_user(126111364476305409)

    try:
        await user.send('Hello! I have started.')
    except discord.Forbidden:
        print('Could not send message to user')

# Note: ctx is the context object that contains information about the message and the channel it was sent from it is required for all commands
    # ctx.send is used to send a message to the channel the command was used in
    # ctx.author is the user who sent the message

# Command to add a task to the ToDo list 
    
 #Note: The * in the parameter means that the rest of the message will be stored in the task variable
    # This allows us to store tasks with spaces in them
    # Example: !add Buy groceries
@bot.command()
async def add(ctx, *, task):
    tasks.append(task)
    await ctx.send(f'Task "{task}" added to the ToDo list.')

# Command to remove all tasks from the ToDo list
@bot.command()
async def clear(ctx):
    tasks.clear()
    await ctx.author.send('ToDo list cleared.')
    
# Command to list all tasks in the ToDo list
@bot.command()
async def listTasks(ctx):
    if not tasks:
        await ctx.send('The ToDo list is empty.')
    else:
        #how can we change the following to include the index of each task?
        #task_list = '\n'.join(tasks)
        task_list = '\n'.join(f'Task {i}: {task}' for i, task in enumerate(tasks))
        await ctx.author.send(f'Current tasks:\n{task_list}')

# Command to remove one or many tasks from the ToDo list
@bot.command()
async def remove(ctx, *indices): # example: !remove 1 2 3
    print (indices)
    indices = list(map(int, indices)) # Convert list of indices to integers then back into a list
    removed_tasks = [] # Create a new list to store the removed tasks
    for index in sorted(indices, reverse=True): # Loop through the indices in reverse order
        if index >= 0 and index < len(tasks): # Check if the index is valid
            removed_tasks.append(tasks.pop(index)) # Remove the task from the list and add it to the removed_tasks list
    if removed_tasks:
        removed_list = '\n'.join(removed_tasks) 
        print("tasks were removed")
        await ctx.author.send(f'Removed tasks:\n{removed_list}') 
    else:
        print("No tasks were removed")
        await ctx.author.send('No tasks were removed.')

# Run the bot
bot.run(TOKEN)
