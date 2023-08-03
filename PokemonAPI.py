# Using Python 3.x +
# use "lib" package from PyPI
from lib import lib
import replicate

lib = lib({'token': "your_token"})

"""
Pokemon Fusion API
"""
def fusion_pokemon(pokemon1: str, pokemon2: str):
    # make API request
    result = lib.keith.pokefusion['@0.2.0']({
    'headPokemon': pokemon1,
    'bodyPokemon': pokemon2
    })

    return result

"""
Text to Pokemon API
"""
def generate_ai_pokemon(description: str):
    output = replicate.run(
        "lambdal/text-to-pokemon:ff6cc781634191dd3c49097a615d2fc01b0a8aae31c448e55039a04dcbf36bba",
        input={"prompt": description}
    )  

    return output