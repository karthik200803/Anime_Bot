from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
import random

TOKEN = "8731476743:AAGN2k8WxN7MTphKjv3hy36tN-oRnxRAO6M"

players = {}

opponents = [
    {"name": "Zombozo", "img": "https://static.wikia.nocookie.net/villains/images/7/72/Zombozo.png/revision/latest?cb=20120926010037"},
    {"name": "Dr.Animo", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8HS_bhIqk5cdtXY7wSV_i6-aYqshxwjwFbg&s"},
    {"name": "Hex", "img": "https://static.wikia.nocookie.net/ben10/images/7/76/Hex_Original_Series.png/revision/latest/scale-to-width/360?cb=20190731070906"},
    {"name": "Charmcaster", "img": "https://static.wikia.nocookie.net/ben10/images/4/40/Charmcaster.png/revision/latest/scale-to-width/360?cb=20190821085614"},
    {"name": "Seven Seven", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiP9q95XA0jAHpO6TrQi1rAf7ZB3OhT8M_Tg&s"}
]


def start(update, context):

    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://m.media-amazon.com/images/M/MV5BYWVjODZjNDgtYjk4ZS00OTg5LTg5NDQtZDMxZDQ4ZmM5MGJmXkEyXkFqcGc@._V1_QL75_UX190_CR0,2,190,281_.jpg",
        caption=f"Welcome To The Ben 10 Verse"

    )

    Keyboard = [
        ["/explore", "/close"]
    ]

    reply_markup = ReplyKeyboardMarkup(Keyboard, resize_keyboard=True)

    update.message.reply_text(
        "🔥 Bot Is Working\nChoose Action:",
        reply_markup=reply_markup
    )


def button(update, context):
    query = update.callback_query
    query.answer()
    user = query.from_user.id

    # ⚔️ START BATTLE
    if query.data == "battle":
        keyboard = [
            [InlineKeyboardButton("⚔️ Attack", callback_data="attack")],
            [InlineKeyboardButton(
                "Special_Attack", callback_data="special_atk")]
        ]

        query.edit_message_caption(
            caption="⚔️ Battle Started!\nUse Attack",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # ⚔️ ATTACK
    if query.data == "attack":

        if user not in players:
            query.edit_message_text("Use /start first")
            return

        damage = random.randint(10, 15)
        enemy_damage = random.randint(10, 15)

        players[user]["enemy_hp"] -= damage
        players[user]["hp"] -= enemy_damage

        msg = f"""
⚔️ Your Attack Deals : {damage}
💥 Enemy Attack Deals : {enemy_damage}

❤️ Your Remaininig HP: {players[user]["hp"]}
👹 Enemy Remaining HP: {players[user]["enemy_hp"]}
"""
        if players[user]["enemy_hp"] <= 0 & players[user]["enemy_hp"] < players[user]["hp"]:
            msg += "\n🏆 You Have Crushed The Enemy !"
            del players[user]
            query.edit_message_caption(caption=msg)
            return

        elif players[user]["hp"] <= 0 & players[user]["enemy_hp"] > players[user]["hp"]:
            msg += "\n💀 The Enemy Has Overhelmed You !"
            del players[user]
            query.edit_message_caption(caption=msg)
            return

        keyboard = [
            [InlineKeyboardButton("⚔️ Attack", callback_data="attack")],
            [InlineKeyboardButton(
                "Special_Attack", callback_data="special_atk")]
        ]

        query.edit_message_caption(
            caption=msg,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return
    # Special Attack
    elif query.data == "special_atk":

        if user not in players:
            query.edit_message_text("Use /start first")
            return

        Special_damage = random.randint(25, 30)
        spenemy_damage = random.randint(25, 30)

        players[user]["enemy_hp"] -= Special_damage
        players[user]["hp"] -= spenemy_damage

        msg = f"""
⚔️ Your Attack Deals : {Special_damage}
💥 Enemy Attack Deals : {spenemy_damage}

❤️ Your Remaininig HP: {players[user]["hp"]}
👹 Enemy Remaining HP: {players[user]["enemy_hp"]}
"""

        if players[user]["enemy_hp"] <= 0:
            msg += "\n🏆 You Have Crushed The Enemy !"
            del players[user]
            query.edit_message_caption(caption=msg)
            return

        elif players[user]["hp"] <= 0:
            msg += "\n💀 The Enemy Has Overhelmed You !"
            del players[user]
            query.edit_message_caption(caption=msg)
            return

        keyboard = [
            [InlineKeyboardButton("⚔️ Attack", callback_data="attack")],
            [InlineKeyboardButton(
                "Special_Attack", callback_data="special_atk")]
        ]

        query.edit_message_caption(
            caption=msg,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return


def explore(update, context):
    user = update.effective_user.id

    enemy = random.choice(opponents)

    players[user] = {
        "hp": 100,
        "enemy_hp": 100,
        "enemy_name": enemy["name"]
    }

    keyboard = [
        [InlineKeyboardButton("⚔️ Battle", callback_data="battle")]
    ]

    update.message.reply_photo(
        photo=enemy["img"],
        caption=f"👹 You encountered {enemy['name']}!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def Close(update, context):
    update.message.reply_text(
        "Menu Closed",
        reply_markup=ReplyKeyboardRemove()
    )


updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("close", Close))
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(button))
dp.add_handler(CommandHandler("explore", explore))

updater.start_polling()
updater.idle()
