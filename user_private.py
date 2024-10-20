import random
from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests
from pprint import pprint
from config import token, EDAMAM_APP_ID,EDAMAM_APP_KEY
user_private_router = Router()

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start"), KeyboardButton(text="/about")],
    ],
    resize_keyboard=True
)


async def send_welcome_message(message: types.Message):
    await message.answer("Welcome to the Recipe Bot! 🍽️\n\n"
                         "You can search for any recipe by typing your query. For example, type 'chicken pasta' or 'egg, bread, salt' to get recipes for chicken pasta.\n\n"
                         "Start your search now and discover delicious recipes!",
                         reply_markup=menu_keyboard)

@user_private_router.message(CommandStart())
async def start(message: types.Message):
    await send_welcome_message(message)

@user_private_router.message(Command('about'))
async def about(message: types.Message):
    await send_welcome_message(message)


@user_private_router.message()
async def random_recipe(message: types.Message):
        try:
            url = 'https://api.edamam.com/api/recipes/v2'
            params = {
            'q': message.text,
            'app_id': EDAMAM_APP_ID,
            'app_key': EDAMAM_APP_KEY,
            'type': 'public'
            }
            r = requests.get(url, params=params)
            data = r.json()

            data = data
            if 'hits' in data and len(data['hits']) > 0:
                recipe = data['hits'][0]['recipe']
                recipe_name = recipe['label']
                recipe_url = recipe['url']
                ingredients = recipe['ingredientLines']

                m = f"✨ *{recipe_name}* ✨\n\n"
                m += "🔗 [View Recipe](" + recipe_url + ")\n\n"
                m += "📝 *Ingredients:*\n"
                m += '\n'.join(ingredients)

                await message.answer(m)
            else:
                await message.answer("Sorry, I couldn't find any recipes.")

        except Exception as ex:
            await message.answer('there was problem') 
