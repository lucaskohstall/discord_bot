import os

from PokemonAPI import *
from interactions import *
from dotenv import load_dotenv

load_dotenv()

intents = Intents.DEFAULT | Intents.MESSAGE_CONTENT
bot = Client(intents=intents)

@listen()
async def on_ready():
    print("Ready")

"""
Pokemon Fusion Command
"""
@slash_command(
    name="pokemon_fusion",
    description="Pokemon Fusion"
)
@slash_option(
    name="pokemon1",
    description="Pokemon 1",
    required=True,
    opt_type=OptionType.STRING
)
@slash_option(
    name="pokemon2",
    description="Pokemon 2",
    required=True,
    opt_type=OptionType.STRING
)
async def my_first_command(ctx: SlashContext, pokemon1: str, pokemon2: str):
    result = fusion_pokemon(pokemon1, pokemon2)

    # TODO: Error handling
    url = result['image_url']

    await ctx.send(url)

"""
Modal for Text-To Pokemon command
"""
@slash_command(
    name="generate_pokemon", 
    description="Create a AI generated Pokemon."
)
async def my_command_function(ctx: SlashContext):
    my_modal = Modal(
        ParagraphText(label="Describe the Pokemon you want to create", custom_id="long_text"),
        title="AI Pokemon",
    )
    await ctx.send_modal(modal=my_modal)

    # Read response
    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)
    message = await modal_ctx.send("Generating Pokemon...")

    # Wait for Pokemon generation
    response = generate_ai_pokemon(modal_ctx.responses["long_text"])
    url = response[0]

    await message.delete()
    await modal_ctx.send(url)

@message_context_menu(name="repeat")
async def repeat(ctx: ContextMenuContext):
    message: Message = ctx.target
    await ctx.send(message.content)

bot.start(os.environ['TOKEN'])