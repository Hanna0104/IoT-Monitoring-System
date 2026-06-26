import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from influxdb import InfluxDBClient

# Configurare logare pentru a vedea erorile in terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Conectarea la InfluxDB - am setat localhost pentru ca rulezi din Windows
# Asigura-te ca baza de date se numeste 'prepractica'
client = InfluxDBClient(host='localhost', port=8086, database='prepractica')

async def start(update, context):
    mesaj = (
        "Salut! Sunt asistentul tău IoT. 🤖\n\n"
        "Comenzi disponibile:\n"
        "/temperatura - Afișează ultima temperatură\n"
        "/umiditate - Afișează ultima umiditate\n"
        "/both - Afișează ambele valori simultan"
    )
    await update.message.reply_text(mesaj)

async def temperatura(update, context):
    try:
        # Se interogheaza tabela 'senzori' - modifica numele daca in baza ta se numeste altfel
        result = client.query('SELECT last(temperatura) FROM senzori')
        points = list(result.get_points())
        if points:
            val = points[0]['last']
            await update.message.reply_text(f"🌡️ Temperatura curentă: {val:.2f} °C")
        else:
            await update.message.reply_text("Nu am găsit date despre temperatură.")
    except Exception as e:
        await update.message.reply_text("Eroare la baza de date.")
        logging.error(e)

async def umiditate(update, context):
    try:
        result = client.query('SELECT last(umiditate) FROM senzori')
        points = list(result.get_points())
        if points:
            val = points[0]['last']
            await update.message.reply_text(f"💧 Umiditatea curentă: {val:.2f} %")
        else:
            await update.message.reply_text("Nu am găsit date despre umiditate.")
    except Exception as e:
        await update.message.reply_text("Eroare la baza de date.")
        logging.error(e)

async def both(update, context):
    try:
        res_t = client.query('SELECT last(temperatura) FROM senzori')
        res_u = client.query('SELECT last(umiditate) FROM senzori')
        pts_t = list(res_t.get_points())
        pts_u = list(res_u.get_points())
        
        txt = "📊 **Date Curente:**\n\n"
        txt += f"🌡️ Temperatura: {pts_t[0]['last']:.2f} °C\n" if pts_t else "🌡️ Temp: Lipsă\n"
        txt += f"💧 Umiditate: {pts_u[0]['last']:.2f} %\n" if pts_u else "💧 Umid: Lipsă\n"
        
        await update.message.reply_text(txt, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text("Eroare la baza de date.")
        logging.error(e)

if __name__ == '__main__':
    # TOKENUL TAU AICI
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("temperatura", temperatura))
    app.add_handler(CommandHandler("umiditate", umiditate))
    app.add_handler(CommandHandler("both", both))
    
    print("🚀 Botul a pornit și ascultă comenzi...")
    app.run_polling()