import string
import sys
import os


def get_text():
    option = input('Enter 1 to enter text or Enter 2 for reading from the file\n')
    if option=='1':
        text = input('Enter the text\n')
    elif option=='2':

        try: 
            with open('sample.txt', 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print('File not found')
            sys.exit()

    else:
        print('Enter correct option')

    return text



def analyze_text(text):
    # Count characters before preprocessing
    characters = len(text)

    # Count words
    words = text.split()

    # Count sentences
    sentences = 0
    for char in text:
        if char in ".!?":
            sentences += 1

    # Remove punctuation and convert to lowercase
    cleaned_text = text.translate(
        str.maketrans("", "", string.punctuation)
    ).lower()

    word_list = cleaned_text.split()

    # Calculate word frequencies
    freq = {}

    for word in word_list:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    # Sort words by frequency (highest first)
    sorted_words = sorted(
        freq.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Get top 3 most frequent words
    top_words = sorted_words[:3]

    # Return all results together
    return {
        "characters": characters,
        "words": len(words),
        "sentences": sentences,
        "frequencies": freq,
        "top_words": top_words
    }




def display_results(results):
    print("\n========== AI TEXT ANALYZER ==========")

    print(f"\nTotal characters: {results['characters']}")
    print(f"Total words: {results['words']}")
    print(f"Total sentences: {results['sentences']}")

    print("\n--- Word Frequencies ---")
    for word, count in results["frequencies"].items():
        print(f"{word}: {count}")

    print("\n--- Top 3 Words ---")
    for word, count in results["top_words"]:
        print(f"{word}: {count}")






def save_report(results):
    with open("report.txt", "w") as file:
        file.write("========== AI TEXT ANALYZER REPORT ==========\n\n")

        file.write(f"Total characters: {results['characters']}\n")
        file.write(f"Total words: {results['words']}\n")
        file.write(f"Total sentences: {results['sentences']}\n")

        file.write("\n--- Word Frequencies ---\n")
        for word, count in results["frequencies"].items():
            file.write(f"{word}: {count}\n")

        file.write("\n--- Top 3 Words ---\n")
        for word, count in results["top_words"]:
            file.write(f"{word}: {count}\n")

    print("\nReport saved successfully to report.txt")

text = get_text()

if text is not None:
    results = analyze_text(text)
    display_results(results)
    save_report(results)