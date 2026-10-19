
import streamlit as st
import string
from pypdf import PdfReader
from io import BytesIO

st.set_page_config(
    page_title="AI Text Analyzer",
    page_icon="📄",
    layout="wide"
)


def extract_text_from_pdf(uploaded_file):
    pdf_bytes = BytesIO(uploaded_file.getvalue())
    reader = PdfReader(pdf_bytes)

    extracted_text = []

    for page in reader.pages:
        extracted_text.append(page.extract_text() or "")

    return "\n".join(extracted_text)


def analyze_text(text):
    characters = len(text)
    words = text.split()

    sentences = sum(
        1 for char in text if char in ".!?"
    )

    cleaned_text = text.translate(
        str.maketrans("", "", string.punctuation)
    ).lower()

    word_list = cleaned_text.split()

    frequencies = {}

    for word in word_list:
        frequencies[word] = frequencies.get(word, 0) + 1

    sorted_words = sorted(
        frequencies.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return {
        "characters": characters,
        "words": len(words),
        "sentences": sentences,
        "frequencies": frequencies,
        "top_words": sorted_words[:3]
    }


st.title("📄 AI Text Analyzer")
st.write(
    "Upload a PDF document to analyze its text, "
    "word frequencies, and most common words."
)

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    try:
        text = extract_text_from_pdf(uploaded_file)

        if not text.strip():
            st.warning(
                "No readable text was found. "
                "This PDF may contain scanned pages."
            )
        else:
            results = analyze_text(text)

            st.success("PDF processed successfully!")

            st.subheader("Document Statistics")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Characters",
                results["characters"]
            )
            col2.metric(
                "Words",
                results["words"]
            )
            col3.metric(
                "Sentences",
                results["sentences"]
            )

            with st.expander("Preview extracted text"):
                st.text_area(
                    "PDF text",
                    value=text,
                    height=250
                )

            st.subheader("Top 3 Most Frequent Words")

            if results["top_words"]:
                for word, count in results["top_words"]:
                    st.write(f"**{word}** — {count} occurrences")
            else:
                st.info("No words were found.")
            st.subheader("Word Frequency Analysis")

            sorted_frequencies = sorted(
                results["frequencies"].items(),
                key=lambda item: item[1],
                reverse=True
            )

            frequency_data = {
                "Word": [word for word, count in sorted_frequencies[:15]],
                "Count": [count for word, count in sorted_frequencies[:15]]
            }

            st.bar_chart(
                frequency_data,
                x="Word",
                y="Count"
            )

            st.dataframe(
                [
                    {"Word": word, "Count": count}
                    for word, count in sorted_frequencies
                ],
                use_container_width=True,
                hide_index=True
            )
            report_lines = [
                "========== AI TEXT ANALYZER REPORT ==========",
                "",
                f"File: {uploaded_file.name}",
                f"Characters: {results['characters']}",
                f"Words: {results['words']}",
                f"Sentences: {results['sentences']}",
                "",
                "--- Top 3 Words ---",
            ]

            for word, count in results["top_words"]:
                report_lines.append(f"{word}: {count}")

            report_lines.extend(["", "--- Word Frequencies ---"])

            for word, count in sorted(
                results["frequencies"].items(),
                key=lambda item: item[1],
                reverse=True
            ):
                report_lines.append(f"{word}: {count}")

            report = "\n".join(report_lines)

            st.download_button(
                "📥 Download Analysis Report",
                data=report,
                file_name="analysis_report.txt",
                mime="text/plain"
            )

    except Exception as error:
        st.error(f"Unable to process this PDF: {error}")
