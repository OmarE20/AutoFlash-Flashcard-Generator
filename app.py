from pdf_reader import extract_text_from_pdf
from flashcard_engine import generate_flashcards
import csv

def save_to_csv(flashcards, output_file="flashcards.csv"):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Answer"])
        writer.writerows(flashcards)

def main():
    path = input("Enter the path to your textbook PDF: ").strip()
    text = extract_text_from_pdf(path)
    flashcards = generate_flashcards(text, num_cards=10)
    
    print("\nGenerated Flashcards:\n")
    for i, (q, a) in enumerate(flashcards, 1):
        print(f"{i}. Q: {q}\n   A: {a}\n")

    save_to_csv(flashcards)
    print("Flashcards saved to flashcards.csv")

if __name__ == "__main__":
    main()