from openai import OpenAI

from src.config import OPENAI_API_KEY, DEFAULT_MODEL
from src.database import search_historical_facts
from src.search import get_live_news_context

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def generate_quiz(sport, difficulty):
    """
    Generate a sports quiz using historical facts
    from ChromaDB and latest sports news.
    """

    # Historical facts
    historical = search_historical_facts(
        sport=sport,
        query=f"{sport} history records championships",
        n_results=3,
    )

    history_text = "\n".join(historical)

    # Live news
    latest_news = get_live_news_context(sport)

    context = f"""
HISTORICAL FACTS
----------------
{history_text}

LATEST SPORTS NEWS
------------------
{latest_news}
"""

    system_prompt = f"""
You are an expert Sports Quiz Generator.

Use ONLY the supplied context.

Never invent facts.

Context:

{context}
"""

    user_prompt = f"""
Generate exactly 4 multiple-choice questions.

Sport: {sport}

Difficulty: {difficulty}

For each question use:

Question:
A)
B)
C)
D)

Correct Answer:

Explanation:

The explanation must be based only on the supplied context.
"""

    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0.5,
        max_tokens=1200,
    )

    return response.choices[0].message.content