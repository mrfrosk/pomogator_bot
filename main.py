from telegram.ext import ApplicationBuilder
from PomogatorBot import PomogatorBot


bot = PomogatorBot()
app = ApplicationBuilder().token(bot.token).build()

for command in bot.get_command_heandlers():
    app.add_handler(command)


app.run_polling()