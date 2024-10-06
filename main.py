import telebot
from telebot import types

bot = telebot.TeleBot('7808598669:AAExCoJqPmufiy5W5elNrDT3ksR3E01LU1s')

@bot.message_handler(content_types = ['photo'])
def get_photo(message):
    bot.reply_to(message, 'Мне очень интересно посмотреть, что изображено в этом файле, но увы, я не могу! :(')

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, f'''👋 <b>Привет,</b> {message.from_user.first_name}, <b>меня зовут Ван Ямано и я являюсь телеграмм ботом семьи</b> <em><u>Virtual Province!</u></em>

<b>Я могу перенаправить Вас в</b> <em><u>официальный Discord сервер</u></em> <b>нашей семьи, где в дальнейшем помогу освоиться. Для этого Вам нужно :</b>

• Скачать приложение Discord из GooglePlay или AppStore 📱
                     
• Зарегистрировать аккаунт в приложении 🪪
                     
• Ввести команду /discord в моём поле ввода сообщений и перейти по ссылке 💬
                     
🎮 <b>Либо, Вы можете использовать браузерную версию. Однако я рекомендую к эксплуатации мобильное приложение.</b>

💿 <b>В Discord сервере Вы сможете узнать много полезной и важной информации, для дальнейшего прибывания в семье</b> <u>Virtual Province</u>.
                
❓ <b>Если у Вас возникнут вопросы, то я могу на них ответить! Для этого просто введите команду</b> /questions''', parse_mode = 'html')

@bot.message_handler(commands = ['discord'])
def ds(message):
    bot.send_message(message.chat.id, f'''💻 <b>Ссылка на официальный Discord сервер семьи Virtual Province :</b>

• Нету ссылки :3''', parse_mode = 'html')

@bot.message_handler(commands = ['questions'])
def questions(message):
    bot.send_message(message.chat.id, f'''🤔 <b>Выберите интересующие Вас вопросы из списка :</b>

• Безопасность ссылки – /safe 🔐

• Кто ты? – /me 👋

📝 <b>В дальнейшем данный список будет дополняться.</b>''', parse_mode = 'html')
    
@bot.message_handler(commands = ['safe'])
def safe(message):
    url = 'https://i.postimg.cc/4xFSWwZ7/507-20241005164255.png'
    bot.send_message(message.chat.id, '''⚠️ <b>Безопасная ли эта ссылка? – Конечно!

✅ Специально для Вас я проверил её на VirusTotal – самом известном сервисе по проверке файлов, ссылок и многого другого на вирусы!</b>''', parse_mode = 'html')
    bot.send_photo(message.chat.id, photo = url)

@bot.message_handler(commands = ['me'])
def me(message):
    bot.send_message(message.chat.id, '''💾 <b> Я являюсь ботом, для помощи участникам, а так же обработки информации, которую мне предоставляет мой создатель. Помимо телеграмма я есть и в приложении Discord, где выполняю те же функции, что и здесь, однако там ассортимент команд чуть больше.

🕹️ С радостью бы пообщался с Вами, но увы не могу в силу своих возможностей :3</b>''', parse_mode = 'html')

bot.infinity_polling(none_stop = True)