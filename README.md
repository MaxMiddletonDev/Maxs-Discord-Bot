# Discord Bot

A feature-rich Discord bot built with discord.py, featuring fun commands, utilities, and more.

## Features

### General Commands
- `$cmds` - Display all available commands
- `$hello` - Receive a friendly greeting from the bot

### Fun Commands
- `$kanyequote` - Get a random Kanye West quote
- `$flipacoin @user [heads/tails]` - Flip a coin with another user
- `$eightball [question]` - Ask the magic 8-ball a question
- `$teamgen [number] @user1 @user2...` - Randomly generate teams from mentioned users

### Utility Commands
- `$ping` - Check the bot's latency
- `$whois [@user]` - Display information about a user

## Setup

### Prerequisites
- Python 3.11 or higher
- A Discord bot token

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. Install dependencies:
```bash
pip install discord.py
```

3. Set up your Discord bot token:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Navigate to the "Bot" section and create a bot
   - Copy the token
   - Set the `TOKEN` environment variable with your bot token

4. Run the bot:
```bash
python main.py
```

## Running on Replit

This bot is designed to run on Replit with a keep-alive mechanism:

1. Fork this Repl
2. Add your Discord bot token as a secret:
   - Click the lock icon (Secrets) in the left sidebar
   - Add a new secret with key `TOKEN` and your bot token as the value
3. Click "Run" to start the bot

The bot includes a Flask web server that keeps it running continuously on Replit.

## Project Structure

```
├── main.py           # Main bot file
├── keep_alive.py     # Flask server to keep bot alive
├── cogs/
│   ├── general.py    # General commands
│   ├── fun.py        # Fun commands
│   └── utility.py    # Utility commands
└── pyproject.toml    # Project dependencies
```

## Adding New Commands

To add new commands, create a new cog or edit existing ones in the `cogs/` directory. The bot automatically loads all cogs on startup.

Example:
```python
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def mycommand(self, ctx):
        await ctx.send("Hello!")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
