from telegram.ext import Updater, CommandHandler
# Import bagian-bagian yang diperlukan dari library

def mulai(update, context):
    update.message.reply_text(
        'Halo, {}'.format(update.message.from_user.first_name))
        
def info(update, context):
    msg = "Facemist saffron SapaxStore terbaeeekk"
    update.message.reply_text(
        '{}'.format(msg))
        
def love(update, context):
    name = update.message.from_user.first_name
    if name == "RandsX":
      update.message.reply_text("Andre love Ifsafa")
    else:
      update.message.reply_text("Ifsafa love Andre")
      
# Fungsi di atas akan menjawab pengirim pesan dengan
# kata Halo + Nama Depan pengirim pesan

updater = Updater('1441609812:AAGtZTvlKGyH2ZPhpoW_JFXaA87otaVPYps', use_context=True)
# variabel updater diisi dengan kelas Updater, yang diberi
# token bot yang kita gunakan

updater.dispatcher.add_handler(CommandHandler('start', mulai))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('love', love))


updater.start_polling()
updater.idle()
# updater selalu menunggu jika ada pesan baru yang diterima bot
