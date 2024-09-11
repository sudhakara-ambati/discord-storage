# Discord Storage

**Discord Storage** is a unique project that leverages Discord channels and Flask to create a decentralized file storage system. By splitting files into smaller chunks and using Discord's text and file upload capabilities, this system allows you to store and manage files on Discord in a novel way.

## Features

- **File Chunking:** Efficiently divides large files into smaller, manageable chunks that fit within Discord’s file size limits.
- **Flask Integration:** Utilizes a Flask server to handle file uploads, manage chunks, and retrieve data.
- **Discord Channels:** Stores file chunks in Discord channels, leveraging Discord’s API for data management and retrieval.
- **Decentralized Storage:** Capitalizes on Discord’s infrastructure to provide a distributed file storage solution.

## Requirements

- **Python 3.7+**
- **Flask:** Install with `pip install Flask`
- **discord.py:** Install with `pip install discord.py`
- **A Discord Bot Token:** Obtain a bot token from the [Discord Developer Portal](https://discord.com/developers/applications) to interact with the Discord API.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/sudhakara-ambati/discord-storage.git
    cd discord-storage
    ```

2. **Configure Your Bot Token:**

    Edit the ```bot.py``` file in the project root and add your Discord bot token:

    ```
    TOKEN=your_bot_token_here
    ```

3. **Run the Flask Server:**

    ```bash
    flask run
    ```

## Usage

### Upload Files

1. Access the Flask web interface at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
2. Use the upload form to select and upload files. The Flask server will split the files into chunks and upload them to the designated Discord channels.

### Retrieve Files

1. To retrieve files, navigate to the Flask web interface.
2. Request the file you wish to download. The server will reassemble the chunks and provide the complete file for download.

## Project Structure

- **app.py:** Main Flask application handling routes for file uploads and retrieval.
- **bot.py:** Contains the logic for interacting with Discord channels to manage and store file chunks.
- **README.md:** This documentation file.
