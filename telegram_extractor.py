from telethon import TelegramClient
import re
import json
from datetime import datetime
import asyncio

api_id = 28919656
api_hash = '88cab6de28dc21e870e95a321d040869'
channel_username = 'toronionlinks'

client = TelegramClient('session_name', api_id, api_hash)

# Regex for .onion URLs
onion_pattern = re.compile(r'http[s]?://[^\s]+\.onion')

async def main():
    await client.start()
    messages = await client.get_messages(channel_username, limit=100)

    with open("onion_links.jsonl", "a") as f:
        for message in messages:
            if message.message:
                links = onion_pattern.findall(message.message)
                if links:
                    for link in links:
                        result = {
                            "source": "telegram",
                            "url": link,
                            "discovered_at": datetime.utcnow().isoformat() + "Z",
                            "context": f"Found in Telegram channel @{channel_username}",
                            "status": "pending"
                        }
                        f.write(json.dumps(result) + "\n")
                        print(f"[+] Found: {link}")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
