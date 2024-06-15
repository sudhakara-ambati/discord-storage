from flask import Flask, render_template, request, redirect, send_file, flash
import os
import threading
import sys
from bot import sendchunks, token, bot, uploads_directory, Chunks_directory, channel_dropdown, merge_chunks
import discord
from discord.ext import commands
import asyncio
import time

app = Flask(__name__)
app.secret_key = "abc"
UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    clear_uploads()
    update_channel_dropdown()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file:
            filename = file.filename
            file_channel_name = file.filename.split('.')[0]
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            sending_chunks = asyncio.run_coroutine_threadsafe(sendchunks(str(file_channel_name)), bot.loop)
            sending_chunks.result()

            flash("Finished uploading")

            return redirect('/')

    uploaded_files = os.listdir(UPLOAD_FOLDER)
    options = [{'value': file, 'label': file} for file in uploaded_files]

    return render_template('index.html', filebasenames=list(channel_dropdown.keys()))

@app.route('/download', methods=['POST'])
def download():
    guild = bot.get_guild(1250905958264078417)
    selected_channel_name = request.form['file']
    selected_channel_id = channel_dropdown[selected_channel_name]
    selected_channel = discord.utils.get(guild.channels, id=selected_channel_id)

    async def download_attachments(channel):
        async for message in channel.history(limit=None):
            for attachment in message.attachments:
                await attachment.save(os.path.join(Chunks_directory, attachment.filename))

        chunks_files_dir = os.listdir(Chunks_directory)
        return chunks_files_dir

    download_future = asyncio.run_coroutine_threadsafe(download_attachments(selected_channel), bot.loop)
    chunk_files = download_future.result()

    if chunk_files:
        file_extension = os.path.splitext(chunk_files[1])[1]

    if file_extension:
        merged_file_path = os.path.join(UPLOAD_FOLDER, f"{selected_channel_name}{file_extension}")
        merge_chunks(Chunks_directory, merged_file_path)

    return send_file(merged_file_path, as_attachment=True)

@app.route('/delete_channel', methods=['POST'])
def delete_channel():
    selected_channel_name_delete = request.form['file']
    selected_channel_id_delete = channel_dropdown[selected_channel_name_delete]
    guild = bot.get_guild(1250905958264078417)
    channel = discord.utils.get(guild.channels, id=int(selected_channel_id_delete))

    if channel:
        asyncio.run_coroutine_threadsafe(channel.delete(), bot.loop)
        flash(f'{channel.name} deleted successfully!')
    else:
        flash('Channel not found!')

    update_channel_dropdown()

    return redirect('/')


def update_channel_dropdown():
    global channel_dropdown
    guild = bot.get_guild(1250905958264078417)
    channels = {channel.name: channel.id for channel in guild.channels if isinstance(channel, discord.TextChannel)}
    channel_dropdown = channels

def clear_uploads():
    uploads_dir = os.listdir(uploads_directory)
    for upload_file in uploads_dir:
        os.remove(os.path.join(uploads_directory, upload_file))

def start_bot():
    bot.run(token)

bot_thread = threading.Thread(target=start_bot)
bot_thread.start()

if __name__ == '__main__':
    app.run(debug=True)


#Add BytesIO to make everything faster instead of downloading the files
#Add renaming and deleting channels
#Use threads to make everything faster