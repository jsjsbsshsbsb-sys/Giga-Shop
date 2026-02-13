import telebot
from telebot import types

TOKEN = "8402217438:AAG9pnOaSB3uUfnsLddZWmxQ3QmKR45DJl8"
bot = telebot.TeleBot(TOKEN)

user_data = {}
waiting_screenshot = set()
pending_orders = {}
ADMIN_IDS = [-1003810980568]

# Меню
menu_markup = types.InlineKeyboardMarkup()
diamonds_btn = types.InlineKeyboardButton("💎Алмазы💎", callback_data="diamonds")
vauncher_btn = types.InlineKeyboardButton("🎁Ваучнеры🎁", callback_data="vaunchers")
steam_btn = types.InlineKeyboardButton("💲Пополнение Steam💲", callback_data="steam")
tg_stars = types.InlineKeyboardButton("🌟Телеграмм звезды🌟", callback_data="tg_stars")
support_btn = types.InlineKeyboardButton("🆘Поддержка🆘", callback_data="support")
reviews_btn = types.InlineKeyboardButton("🎉Отзывы🎉", callback_data="reviews")
menu_markup.add(diamonds_btn, vauncher_btn)
menu_markup.add(steam_btn, tg_stars)
menu_markup.add(support_btn, reviews_btn)

go_back_markup = types.InlineKeyboardMarkup()
go_back_btn = types.InlineKeyboardButton("Назад", callback_data="back")
go_back_markup.add(go_back_btn)

pay_markup = types.InlineKeyboardMarkup()
pay_btn = types.InlineKeyboardButton("💳 Перейти к оплате", url="https://example.com")
pay_markup.add(pay_btn)

def check_sub(user_id):
    try:
        member = bot.get_chat_member("@Acash_05", user_id)
        return member.status in ("member", "administrator", "creator")
    except:
        return False

@bot.message_handler(commands=["start"])
def private_hendler(message):
    if not check_sub(message.from_user.id):
        markup = types.InlineKeyboardMarkup()
        subscribe_btn = types.InlineKeyboardButton("📢 Подписаться", url="https://t.me/Acash_05")
        check_sub_btn = types.InlineKeyboardButton("🟢 Проверить", callback_data="check_sub")
        markup.add(subscribe_btn, check_sub_btn)
        bot.send_message(
            message.chat.id,
            "Вы не подписаны на наш телеграмм канал!\nБот заработает после подписки!",
            reply_markup=markup
        )
    else:
        send_main_menu(message)

@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_sub_button(call):
    if check_sub(call.from_user.id):
        bot.answer_callback_query(call.id, "✅ Вы подписаны! Можно пользоваться ботом.", show_alert=True)
        edit_main_menu(call.message)  # Изменил здесь
    else:
        bot.answer_callback_query(call.id, "❌ Вы ещё не подписаны на канал!", show_alert=True)

def send_main_menu(message):
    """Отправляет новое сообщение с меню"""
    bot.send_message(
        message.chat.id,
        "<blockquote>✅ Добро пожаловать в GIgaShop\n\nВыберите что хотите приобрести! 👇</blockquote>",
        reply_markup=menu_markup, parse_mode="html"
    )

def edit_main_menu(message):
    """Редактирует текущее сообщение на меню"""
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<blockquote>✅ Добро пожаловать в GIgaShop\n\nВыберите что хотите приобрести! 👇</blockquote>",
        reply_markup=menu_markup, parse_mode="html"
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    uid = call.from_user.id

    if call.data == "diamonds":
        diamons_markup = types.InlineKeyboardMarkup()
        diamods105 = types.InlineKeyboardButton("💎105💎", callback_data="diam105")
        diamods200 = types.InlineKeyboardButton("💎200💎", callback_data="diam200")
        diamons_markup.add(diamods105, diamods200)
        diamons_markup.add(types.InlineKeyboardButton("Назад", callback_data="back"))
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="<blockquote>✨Выберите количество алмазов ниже!👇</blockquote>",
                            parse_mode="html", reply_markup=diamons_markup)

    elif call.data == "diam105":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="Введите свой игровой ID!")
        user_data[uid] = {"diamonds": 105}

    elif call.data == "diam200":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="Введите свой игровой ID!")
        user_data[uid] = {"diamonds": 200}

    elif call.data == "vaunchers":
        vauncher_markup = types.InlineKeyboardMarkup()
        lite_vauncher_btn = types.InlineKeyboardButton("Lite Ваунчер🎉", callback_data="lite_vauncher")
        weekly_vauncher_btn = types.InlineKeyboardButton("Недельный Ваунчер✨", callback_data="weekly_vauncher")
        month_vauncher_btn = types.InlineKeyboardButton("Месячный Ваунчер🌟", callback_data="month_vauncher")
        vauncher_markup.add(lite_vauncher_btn, weekly_vauncher_btn, month_vauncher_btn)
        vauncher_markup.add(types.InlineKeyboardButton("Назад", callback_data="back"))
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="<blockquote>Выберите Ваунчер✨</blockquote>",
                            parse_mode="html", reply_markup=vauncher_markup)

    elif call.data == "lite_vauncher":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="Введите свой игровой ID!")
        user_data[uid] = {"vauncher": "Lite Ваунчер🎉"}

    elif call.data == "weekly_vauncher":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="Введите свой игровой ID!")
        user_data[uid] = {"vauncher": "Недельный Ваунчер✨"}

    elif call.data == "month_vauncher":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="Введите свой игровой ID!")
        user_data[uid] = {"vauncher": "Месячный Ваунчер🌟"}

    elif call.data == "back":
        bot.answer_callback_query(call.id)
        edit_main_menu(call.message)  # ИЗМЕНЕНИЕ: теперь редактирует, а не отправляет новое

    elif call.data == "support":
        support_markup = types.InlineKeyboardMarkup()
        buy_problems_btn = types.InlineKeyboardButton("Проблеммы с покупкой🤷‍♀️", callback_data="buy_problems")
        support_chat_btn = types.InlineKeyboardButton("Чат Поддержки🛠", callback_data="support_chat")
        rules_btn = types.InlineKeyboardButton("Правила🧰", callback_data="rules")
        cooperation_btn = types.InlineKeyboardButton("Сотрудничество🎁", callback_data="cooperation")
        support_markup.add(buy_problems_btn, support_chat_btn, cooperation_btn, rules_btn)
        support_markup.add(types.InlineKeyboardButton("Назад", callback_data="back"))
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="<blockquote>Вы во вкладке поддержки! Выберите что у вас случилось ниже в списке!</blockquote>",
                            reply_markup=support_markup, parse_mode="html")

    elif call.data == "reviews":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="Отзывы в разработке", reply_markup=go_back_markup)
    
    elif call.data.startswith(("approve_", "reject_")):
        admin_order_handler(call)

@bot.message_handler(content_types=["text"])
def get_game_id(message):
    uid = message.from_user.id
    if uid not in user_data:
        return

    data = user_data[uid]
    data["game_id"] = message.text

    bot.send_message(
        message.chat.id,
        "💳 Оплатите заказ и пришлите скрин из истории перевода.\n\n"
        "❗ Алмазы/Ваучеры выдаются только после проверки оплаты.",
        reply_markup=pay_markup
    )
    waiting_screenshot.add(uid)

@bot.message_handler(content_types=["photo"])
def get_screenshot(message):
    uid = message.from_user.id
    if uid not in waiting_screenshot:
        return
    data = user_data.get(uid)
    if not data:
        return

    if "diamonds" in data:
        caption = f"🆕 ЗАКАЗ (Алмазы)\n\n👤 @{message.from_user.username}\n🆔 {uid}\n🎮 ID: {data['game_id']}\n💎 {data['diamonds']}"
    else:
        caption = f"🆕 ЗАКАЗ (Ваучер)\n\n👤 @{message.from_user.username}\n🆔 {uid}\n🎮 ID: {data['game_id']}\n🎁 {data['vauncher']}"

    admin_markup = types.InlineKeyboardMarkup()
    approve_btn = types.InlineKeyboardButton("✅ Принять", callback_data=f"approve_{uid}")
    reject_btn = types.InlineKeyboardButton("❌ Отклонить", callback_data=f"reject_{uid}")
    admin_markup.add(approve_btn, reject_btn)

    for admin in ADMIN_IDS:
        bot.send_photo(admin, message.photo[-1].file_id, caption=caption, reply_markup=admin_markup)

    bot.send_message(message.chat.id, "📌 Скрин получен. Админы проверят ваш заказ.")
    waiting_screenshot.remove(uid)
    pending_orders[uid] = data.copy()
    del user_data[uid]

def admin_order_handler(call):
    uid = int(call.data.split("_")[1])
    
    # УБРАЛИ ПРОВЕРКУ ПРАВ - теперь кнопки работают у всех в группе

    # Получаем данные заказа
    order_data = pending_orders.get(uid, {})
    admin_username = call.from_user.username
    if not admin_username:
        admin_username = f"id{call.from_user.id}"
    
    if call.data.startswith("approve_"):
        # Формируем информацию о заказе для сообщения админу
        if "diamonds" in order_data:
            order_info = f"Алмазы: {order_data['diamonds']}, ID: {order_data['game_id']}"
        else:
            order_info = f"Ваучер: {order_data['vauncher']}, ID: {order_data['game_id']}"
        
        # Обновляем сообщение у админа
        new_caption = f"✅ Заказ принял @{admin_username}\nЗаказ: {order_info}"
        try:
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption=new_caption,
                reply_markup=None  # Убираем кнопки
            )
            bot.answer_callback_query(call.id, "✅ Заказ подтверждён")
            bot.send_message(uid, "✅ Ваш заказ был принят! Товар будет выдан в течение ~1 часа.🕑", reply_markup=go_back_markup)
        except Exception as e:
            print(f"Ошибка при принятии заказа: {e}")
            bot.answer_callback_query(call.id, "❌ Ошибка при обработке", show_alert=True)
    else:
        # Обновляем сообщение у админа
        new_caption = f"❌ Заказ отклонил @{admin_username}"
        try:
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption=new_caption,
                reply_markup=None  # Убираем кнопки
            )
            bot.answer_callback_query(call.id, "❌ Заказ отклонён")
            bot.send_message(uid, "❌ Ваш заказ был отклонён. Свяжитесь с поддержкой для деталей.", reply_markup=go_back_markup)
        except Exception as e:
            print(f"Ошибка при отклонении заказа: {e}")
            bot.answer_callback_query(call.id, "❌ Ошибка при обработке", show_alert=True)

    # Убираем заказ из pending
    if uid in pending_orders:
        del pending_orders[uid]

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(non_stop=True)