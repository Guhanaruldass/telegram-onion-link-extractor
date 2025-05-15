# Telegram .onion Link Extractor

A Python script that connects to a Telegram channel using the Telethon library and extracts `.onion` URLs from recent messages.

---

## Features

- Connects to public Telegram channels (default: `@toronionlinks`).
- Fetches recent messages using the Telegram API.
- Extracts `.onion` URLs using regex.
- Saves extracted URLs to `onion_links.jsonl` in JSONL format.
- Handles Telegram login and authentication via API credentials.

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Guhanaruldass/telegram-onion-link-extractor.git
   cd telegram-onion-extractor
