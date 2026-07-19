# 🏆 AI-Powered Sports Quiz Generator

An AI-powered Sports Quiz Generator built using **Retrieval-Augmented Generation (RAG)**. The application combines historical sports facts stored in **ChromaDB** with the latest sports news retrieved from the web to generate dynamic multiple-choice quizzes using a Large Language Model (LLM).

---

## 🚀 Features

- Generate AI-powered sports quizzes
- Supports multiple sports:
  - Cricket
  - Football
  - Basketball
  - Tennis
  - Badminton
- Difficulty levels:
  - Easy
  - Medium
  - Hard
- Uses Retrieval-Augmented Generation (RAG)
- Retrieves historical facts from ChromaDB
- Fetches latest sports news using DDGS
- Generates contextual quizzes using an OpenRouter LLM
- Simple Streamlit-based user interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- ChromaDB
- OpenRouter API
- OpenAI Python SDK
- DDGS (DuckDuckGo Search)
- Sentence Transformers
- Python Dotenv

---

## 📂 Project Structure

```
sports-quiz-agent/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── data/
│   └── sports_facts.json
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── search.py
│   └── generator.py
│
├── test_generator.py
├── test_search.py
└── tests/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/priyankajonnalagadda/sports-quiz-agent.git

cd sports-quiz-agent
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 Test Individual Modules

Test Web Search

```bash
python test_search.py
```

Test Quiz Generation

```bash
python test_generator.py
```

---

## 🔄 How It Works

1. User selects a sport and difficulty level.
2. Historical sports facts are retrieved from ChromaDB.
3. Latest sports news is fetched using DDGS.
4. Both sources are combined using the RAG approach.
5. The LLM generates contextual multiple-choice quiz questions.
6. The generated quiz is displayed in the Streamlit interface.

---

## 📸 Sample Output

```
Question:
Who won the first ICC Cricket World Cup?

A) India
B) Australia
C) West Indies
D) England

Correct Answer:
C) West Indies

Explanation:
The first ICC Cricket World Cup was won by West Indies in 1975.
```

---

## 📌 Future Improvements

- Timer-based quiz mode
- User authentication
- Score tracking
- Leaderboard
- Additional sports
- Voice-based quiz generation
- PDF export of quizzes

---

## 👩‍💻 Author

**Priyanka Jonnalagadda**

GitHub: https://github.com/priyankajonnalagadda

---
