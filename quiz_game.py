import requests
import html
import random


def get_questions(amount=5):
    category_id = "9"  # General Knowledge
    url = f"https://opentdb.com/api.php?amount={amount}&category={category_id}&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data["results"]


def run_quiz():
    print("🎯 Welcome to the General Knowledge Quiz!\n")
    questions = get_questions()

    score = 0

    for i, q in enumerate(questions, 1):
        question = html.unescape(q["question"])
        correct_answer = html.unescape(q["correct_answer"])
        incorrect_answers = [html.unescape(ans)
                             for ans in q["incorrect_answers"]]

        options = incorrect_answers + [correct_answer]
        random.shuffle(options)

        print(f"Q{i}: {question}")
        for idx, option in enumerate(options):
            print(f"{chr(65 + idx)}. {option}")

        user_input = input("Your answer (A/B/C/D): ").upper()

        try:
            selected_option = options[ord(user_input) - 65]
        except:
            print("❌ Invalid input. Skipping question.\n")
            continue

        if selected_option == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was: {correct_answer}\n")

    print(f"🏁 Quiz Over! Your final score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()
