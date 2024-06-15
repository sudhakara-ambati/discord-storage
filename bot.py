from filesplit.split import Split
from filesplit.merge import Merge
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
token = 'MTI1MDkwMzkzNjg2NTQwNzAyNw.GZN1JH.3BwmuHbdD4a4q5twL7VvnXa-dq6PNf5YnkWVYk'

uploads_directory = "uploads"
Chunks_directory = "Chunks"

channel_dropdown = {}

@bot.event
async def on_ready():
    print("Bot is ready.")

def split_file(file_dir, output_chunks_dir):
    chunk_files = []
    for filename in os.listdir(file_dir):
        input_file = os.path.join(file_dir, filename)
        split = Split(input_file, output_chunks_dir)
        split.bysize(25 * 1024 * 1024)
    chunk_files = [file for file in os.listdir(output_chunks_dir)]
    return chunk_files

def merge_chunks(chunks_dir, output_file):
    merge = Merge(chunks_dir, os.path.dirname(output_file), os.path.basename(output_file))
    merge.merge()

async def sendchunks(file_base_name):
    chunk_files_only = split_file(uploads_directory, Chunks_directory)
    all_chunk_files = [file for file in os.listdir(Chunks_directory)]
    uploads_files = [file for file in os.listdir(uploads_directory)]
    guild = bot.get_guild(1250905958264078417)
    new_channel = await guild.create_text_channel(file_base_name)

    channel_dropdown[file_base_name] = new_channel.id

    for chunk_file in chunk_files_only:
        chunk_file_send = os.path.join(Chunks_directory, chunk_file)
        await new_channel.send(file=discord.File(chunk_file_send))
        os.remove(chunk_file_send)

    for uploads in uploads_files:
        uploads_delete = os.path.join(uploads_directory, uploads)
        os.remove(uploads_delete)
