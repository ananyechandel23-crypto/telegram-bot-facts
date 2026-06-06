import requests
import schedule
import time

BOT_TOKEN = "8891305577:AAFevJRwNaaUKpMm_Hp0TZAYbdg06NYZ_ZM"
CHAT_ID = "5985565344"

def send_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en", timeout=10)
        fact = response.json()["text"]
        message = f"🌟 Daily Random Fact\n\n📌 {fact}\n\n🕐 Your daily fact!"
    except Exception as e:
        message = f"Error fetching fact: {str(e)}"

    result = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"},
        timeout=10
    )
    print(result.text)

send_fact()
schedule.every().day.at("05:30").do(send_fact)
print("Bot running... daily at 11:00 AM IST")
while True:
    schedule.run_pending()
    time.sleep(30)
