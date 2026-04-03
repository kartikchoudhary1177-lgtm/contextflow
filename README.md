# contextflow
# ContextFlow AI – Contextual Chatbot API

ContextFlow AI is a Django-based contextual chatbot API that supports **Text Mode** and **Image Mode** responses. The chatbot stores conversation history and generates responses using AI models.

This project demonstrates backend API development, AI integration, and contextual conversation handling.

---

## Features

- Context-aware chatbot
- Text responses using Google Gemini API
- Image generation from user prompts
- Conversation history stored in database
- REST API built with Django REST Framework
- Easy API testing using Postman

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Google Gemini API
- Hugging Face (free image generation)
- MySQL

---

## Project Structure

```
contextflow/
│
├── chatbot/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── services.py
│   └── urls.py
│
├── user_auth/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── contextflow/
│   ├── settings.py
│   └── urls.py
│
└── manage.py
```


## API Endpoints

### Create Conversation

POST  
`/api/conversations/ `

### Get Conversation Messages

GET  
`/api/conversations/{conversation_id}/messages/`

### Chat API

POST  
`/api/chat/`

---

## Example Request (Text Mode)

```json
{
 "conversation_id": 1,
 "message": "What is artificial intelligence?",
 "mode": "text"
}
```

---

## Example Response (Text Mode)

```json
{
 "question": "What is artificial intelligence?",
 "answer": "Artificial intelligence is the simulation of human intelligence by machines."
}
```

---

## Example Request (Image Mode)

```json
{
 "conversation_id": 1,
 "message": "dog wearing sunglasses",
 "mode": "image"
}
```

---

## Example Response (Image Mode)

```json
{
 "question": "dog wearing sunglasses",
 "image_url": "https://image.pollinations.ai/prompt/dog%20wearing%20sunglasses"
}
```

---

# Running the Project Locally

### Clone the repository

```
git clone https://github.com/kartikchoudhary1177-lgtm
cd contextflow
```

---

### Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### Install dependencies

```
pip install -r requirements.txt
```

---

### Add Gemini API key

Open **settings.py** and add

```
GEMINI_API_KEY = "your_api_key"
```

Generate API key here:

https://aistudio.google.com/app/apikey

---

### Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### Run development server

```
python manage.py runserver
```

Server will run at

```
http://127.0.0.1:8000/
```

---

## Testing the API

Use **Postman** to test the chatbot API.

Example request

```
POST http://127.0.0.1:8000/api/chat/
```

## Author

**Kartik Choudhary**  
Backend Developer
