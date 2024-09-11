# Discord Storage
Discord Storage is a project that utilizes Discord channels and Flask to store files on Discord by splitting them into smaller chunks. This approach leverages Discord’s text and file upload capabilities to create a decentralized storage system using Discord’s infrastructure.

# Features
- File Chunking: Files are divided into smaller, manageable chunks to fit within Discord's file size limits.
- Flask Integration: A Flask server handles file uploads, chunk management, and retrieval.
- Discord Channels: Uses Discord channels to store file chunks, leveraging Discord's API to manage and retrieve data.
- Decentralized Storage: Utilizes Discord’s infrastructure for distributed file storage.
  
# Requirements
- Python 3.7+
- Flask (pip install Flask)
- Discord.py (pip install discord.py)
- A Discord Bot Token: You need a bot token from the Discord Developer Portal to interact with the Discord API.

# Usage
## Upload Files:
Access the Flask web interface at http://127.0.0.1:5000/.
Use the upload form to select and upload files. The Flask server will handle splitting the files into chunks and uploading them to the designated Discord channels.

## Retrieve Files:
To retrieve files, use the Flask web interface to request the file. The server will reassemble the chunks and provide the complete file for download.
