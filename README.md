# Kanoon Saathi

A voice-first guide for people who need to understand a problem or a paper before they go to a lawyer or a police station. It is built for farmers, women, and anyone who is more comfortable speaking than reading.

Kanoon Saathi is not a lawyer. It does not file a case, and it does not tell you to sign. It explains the situation in plain words, says how urgent it is, and points to official help.

## What you can do

- Tap once and talk. Tap again to stop.
- Hear the answer in Hindi or English without any API key, using the phone's own voice.
- With a [Gnani](https://app.gnani.ai/voice/) key, listening and speaking use Gnani Prisma and Timbre across Hindi, English, Tamil, Telugu, Kannada, Malayalam, Marathi, Punjabi, Bengali, and Gujarati.
- With an OpenAI-compatible key, answers can be spoken in the language you picked, and a photo of a paper is explained in that language.
- Photos and conversations are not stored.

Built-in guides cover occupied land, online threats, court papers, bills, and a paper someone is pushing you to sign. If the words sound like immediate danger, the screen asks you to call **112**, and **181** if you are a woman in danger.

## Run

```powershell
cd C:\Users\aditi\kanoon-saathi
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000

Put keys in `.env` only if you have them. The app still answers the built-in situations without keys.

| Key | What it unlocks |
| --- | --- |
| `GNANI_API_KEY` | Indian-language listening and the Shivani voice |
| `OPENAI_API_KEY` | Answers in the other languages, and reading a photo of a paper |

`OPENAI_BASE_URL` can point at any OpenAI-compatible endpoint.

## Limits

Land records, court forms, and police practice change by state. The guide says which office to ask, and leaves the exact form to a District Legal Services Authority lawyer. Do not treat a spoken answer as a decision to sign, pay, or file.
