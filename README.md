# discord_bot

A little Discord Bot that is able to receive a slash commands to generate a Pokemon Fusion via `/pokemon_fusion`

![Pokemon Fusion](https://github.com/lucaskohstall/discord_bot/blob/main/media/fusion.gif?raw=true)

It also connect to a Text-To-Pokemon AI to generate your own Pokemon via `/generate_pokemon`

![Pokemon Generation](https://github.com/lucaskohstall/discord_bot/blob/main/media/generation.gif?raw=true)

## Usage

```  
pip3 install -r requirements.txt 
```

## Create Discord Application
Grant the application the following permissions

- bot
- application-commands
- Send Messages

## Create .env file

Add your application Token (Discord Developer Portal -> Your Application -> Bot -> Reset token)

Create Accounts & API Tokens of the used APIs (Check PokemonAPI.py)

## Setup the application

Discord Developer Portal -> Your Application -> OAuth2 -> URL Generator
- Select bot & application commands permissions
- Use URL and invite bot to your server
- Accept all permissions

Start the script

```
python3 src/PokemonFusionCommandy.py
```

