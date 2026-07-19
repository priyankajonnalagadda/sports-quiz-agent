from src.generator import generate_quiz

print("=" * 60)
print("AI SPORTS QUIZ")
print("=" * 60)

quiz = generate_quiz(
    sport="Cricket",
    difficulty="Medium"
)

print(quiz)