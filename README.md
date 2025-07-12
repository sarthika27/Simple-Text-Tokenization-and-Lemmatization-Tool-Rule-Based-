# Simple-Text-Tokenization-and-Lemmatization-Tool-Rule-Based-

# 🧹 Text Cleaner Tool (Tokenization & Stemming)

A simple Python-based command-line tool that takes a sentence, tokenizes it, applies basic rule-based stemming, displays the cleaned result, and saves it to a log file.

## 📦 Project Structure
text_cleaner_tool/
├── main.py # Main driver script
├── README.md # Project description and instructions
├── modules/ # Contains all processing modules
│ ├── init.py
│ ├── input_module.py # Takes user input
│ ├── tokenizer.py # Splits sentence into tokens
│ ├── stemmer.py # Applies rule-based stemming
│ ├── cleaner_viewer.py # Displays original vs cleaned tokens
│ └── log_exporter.py # Saves cleaned tokens to a log file

---

## 🚀 How It Works

1. The program asks you to enter a sentence.
2. It splits the sentence into individual words (tokens).
3. Applies simple rule-based stemming to clean the words.
4. Displays both original and cleaned words side by side.
5. Saves the cleaned words to logs/cleaned_output.txt.

---

## 🔧 Requirements

- Python 3.6 or higher
- No external libraries required (uses only built-in modules)

---

## Run the main script

run main.py


