# 📄 AI Text Analyzer

A Python-based web application built with **Streamlit** that analyzes text extracted from PDF documents. It provides document statistics, word-frequency analysis, visualizations, and downloadable analysis reports.

## ✨ Features

- **PDF Upload:** Upload PDF documents directly through the web interface.
- **Text Extraction:** Extract readable text from PDF pages using PyPDF.
- **Document Statistics:** Calculate character count, word count, and sentence count.
- **Word Frequency Analysis:** Count word occurrences after converting text to lowercase and removing punctuation.
- **Top 3 Words:** Identify the three most frequently occurring words.
- **Interactive Visualization:** Display word frequencies using a bar chart.
- **Frequency Table:** View word counts in a sortable-style data table.
- **Text Preview:** Preview the extracted text before reviewing the analysis.
- **Downloadable Report:** Download the analysis results as a `.txt` file.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Streamlit** — Web application interface
- **PyPDF** — PDF text extraction
- **Standard Python Libraries** — Text preprocessing and data analysis

## 📂 Project Structure

```text
ai-text-analyzer/
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact files in your repository may vary depending on which development files you choose to keep.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-text-analyzer.git
cd ai-text-analyzer
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` is not already created, generate it from your active project environment:

```bash
python -m pip freeze > requirements.txt
```

Alternatively, install the primary dependencies directly:

```bash
python -m pip install streamlit pypdf
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

`http://localhost:8501`

## 🚀 How to Use

1. Launch the application.
2. Upload a PDF document using the file uploader.
3. Wait for the application to extract the document's text.
4. Review the character, word, and sentence counts.
5. Explore the extracted text preview.
6. View the top three words and word-frequency chart.
7. Review the complete word-frequency table.
8. Download the analysis report for future reference.

## 📊 Analysis Method

The application processes extracted text using the following steps:

1. Extract text from each PDF page.
2. Calculate basic document statistics.
3. Remove punctuation and normalize words to lowercase.
4. Count the occurrences of each word using a Python dictionary.
5. Sort words by frequency to identify the most common terms.
6. Present the results through Streamlit components and a bar chart.
7. Generate a downloadable text report.

## ⚠️ Limitations

- Scanned PDFs containing only images may not produce readable text because OCR is not implemented.
- Sentence counting is based on punctuation marks (`.`, `!`, and `?`) and may not always match the actual number of sentences.
- Word-frequency counts include common words such as *the*, *is*, and *and* unless stop-word filtering is added.
- PDF extraction quality depends on the document's structure and text encoding.

## 🎯 Learning Objectives

This project helped me practice:

- Python functions and dictionaries
- String manipulation and text preprocessing
- File handling and PDF processing
- Sorting and frequency analysis
- Building interactive applications with Streamlit
- Displaying data using tables and charts
- Generating downloadable reports
- Organizing a Python project for GitHub

## 🔮 Future Improvements

Potential enhancements include:

- Stop-word removal
- OCR support for scanned PDFs
- Keyword extraction and document summarization
- Sentiment analysis
- Support for multiple document formats
- Exporting reports to PDF or CSV

## 👨‍💻 Author

**Siddharth Tyagi**

GitHub: [YOUR_GITHUB_USERNAME](https://github.com/YOUR_GITHUB_USERNAME)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub!
