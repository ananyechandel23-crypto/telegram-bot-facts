import requests
import schedule
import time
from datetime import datetime

BOT_TOKEN = "8891305577:AAFevJRwNaaUKpMm_Hp0TZAYbdg06NYZ_ZM"
CHAT_ID = 5985565344

def get_random_fact():
    try:
        # Uses Numbers API for date facts with long descriptions
        response = requests.get("http://numbersapi.com/random/trivia?json")
        data = response.json()
        number = data["number"]
        fact = data["text"]
        
        # Get a second fun fact from another free API
        response2 = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
        data2 = response2.json()
        bonus_fact = data2["text"]
        
        message = (
            f"🌟 Daily Random Fact\n\n"
            f"📌 Fact of the Day:\n{fact}\n\n"
            f"💡 Bonus Fact:\n{bonus_fact}\n\n"
            f"🕐 Delivered fresh every day at 11:00 AM IST"
        )
        return message
    except Exception as e:
        return f"⚠️ Could not fetch fact today. Error: {str(e)}"

def send_fact():
    message = get_random_fact()
    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
    )
    if response.status_code == 200:
        print(f"✅ Fact sent successfully at {datetime.now()}")
    else:
        print(f"❌ Failed to send: {response.text}")

def run_scheduler():
    schedule.every().day.at("05:30").do(send_fact)  # 11:00 AM IST = 05:30 UTC
    print("🤖 Bot is running... Sending fact daily at 11:00 AM IST")
    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    print("🚀 Sending test fact now...")
    send_fact()
    run_scheduler()
