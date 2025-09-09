import streamlit as st
from pdf2docx import Converter
import tempfile
import os

def pdf_to_word(pdf_file, output_path):
    cv = Converter(pdf_file)
    cv.convert(output_path, start=0, end=None)  # full document
    cv.close()

def main():
    st.set_page_config(page_title="PDF to Word Converter", page_icon="📄")
    st.title("📄 PDF to Word ")
    st.write(" Alege fisierul sau 'drag and drop'.")

    uploaded_file = st.file_uploader("Alege fisierul", type=["pdf"])

    if uploaded_file is not None:
        if st.button("Convert to Word"):
            with st.spinner("Converting... Please wait."):
                # Save uploaded PDF to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                    tmp_pdf.write(uploaded_file.read())
                    tmp_pdf_path = tmp_pdf.name

                # Temporary Word output
                with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_docx:
                    tmp_docx_path = tmp_docx.name

                # Convert PDF → Word
                pdf_to_word(tmp_pdf_path, tmp_docx_path)

                # Download button
                with open(tmp_docx_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Word File",
                        data=f,
                        file_name="converted.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

                # Clean up
                os.remove(tmp_pdf_path)
                os.remove(tmp_docx_path)

if __name__ == "__main__":
    main()

