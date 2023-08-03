# discord_bot

A little Discord Bot that is able to receive a slash commands to generate a Pokemon Fusion
`/pokemon_fusion`
![Pokemon Fusion](URL or file path)

It also connect to a Text-To-Pokemon AI to generate your own Pokemon via
`/generate_pokemon`
![Pokemon Generation](URL or file path)



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

Start the script

```
python3 PokemonFusionCommandy.py
```

