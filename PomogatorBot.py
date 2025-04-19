
from telegram import Update, Bot
from json_reader import JsonReader
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import telegram.ext.filters as filters

class PomogatorBot:
    token = ""
    json_handler = JsonReader('chats.json')

    def __init__(self):
        pass

    async def add_chat(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        msg = update.message.text.split(" ")[0]
        self.json_handler.write(data={msg: update.message.chat_id})
        await self.bot.send_message(update.message.chat_id, "группа успешно сохранена")


    async def save(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        caption = update.message.caption
        message = update.message.text
        command = caption if caption else message
        chat_id = self.json_handler.read_id(command.split(" ")[0])
        if chat_id:
            if caption:
                document = update.message.document
                video = update.message.video
                if document:
                    await context.bot.send_document(chat_id, document)
                elif video:
                    await context.bot.send_video(chat_id, video)
                else:
                    photo = update.message.photo[-1]
                    file = await context.bot.get_file(photo.file_id)
                    await context.bot.send_photo(chat_id, photo= file.file_id)
                await context.bot.send_message(chat_id, self.get_text(caption))
            elif message:
                await context.bot.send_message(chat_id, self.get_text(command))
        else:
            await update.message.reply_text(f'чата {command.split(" ")[0]} не существует')

    def get_text(self, command: str): return " ".join(command.split(" ")[1:])

    def get_command_heandlers(self) -> list[:CommandHandler]:
       return [
            CommandHandler("add", self.add_chat),
            MessageHandler(filters.TEXT | filters.CAPTION, self.save),
            ]