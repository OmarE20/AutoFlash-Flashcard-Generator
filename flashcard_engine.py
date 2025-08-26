from transformers import pipeline

question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

def generate_flashcards(text, num_cards=10):
    flashcards = []
    sentences = text.split(". ")

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence.split()) < 6:
            continue

        try:
            # Format for highlighting the answer inside the context
            formatted = f"generate question: <hl>{sentence}<hl> {text}"
            result = question_generator(formatted, max_length=64, do_sample=False)

            if result and isinstance(result, list):
                question = result[0]["generated_text"]
                answer = sentence
                flashcards.append((f"Q: {question}", f"A: {answer}"))
        except Exception:
            continue

        if len(flashcards) >= num_cards:
            break

    return flashcards