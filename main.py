from telethon.sync import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import re

# بيانات تسجيل الدخول
api_id = 24472149
api_hash = 'df7d7fa5c8d628b9bf822ef793598747'
phone = '+9647810424454'

client = TelegramClient('user_session', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    code = input("📩 أدخل كود التحقق: ")
    try:
        client.sign_in(phone, code)
    except SessionPasswordNeededError:
        password = input("🔐 الحساب يحتوي على كلمة مرور (Two-Step)، أدخلها هنا: ")
        client.sign_in(password=password)

# حذف الروابط
def remove_links(text):
    return re.sub(r'http\S+|www\S+|t\.me\S+|bit\.ly\S+', '', text).strip()

# القنوات المراد مراقبتها
channels = ['‏SabrenNews22', 'MydoctorA96']

@client.on(events.NewMessage(chats=channels))
async def handler(event):
    msg = event.message
    text = msg.message or ""
    clean_caption = remove_links(text)

    if msg.media:
        await client.send_file(
            'imamhussains',
            file=msg.media,
            caption=clean_caption if clean_caption else None
        )
    elif clean_caption:
        await client.send_message('imamhussains', clean_caption)

print("✅ البوت يعمل الآن ويرسل الوسائط مع التعليق (في رسالة واحدة).")
client.run_until_disconnected()