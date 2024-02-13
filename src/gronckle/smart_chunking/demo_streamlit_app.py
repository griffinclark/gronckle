import streamlit as st
from main import chunk_smartly  
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken


# Mockup for split_chunks_responsibly (replace with actual function)
def split_chunks_responsibly(document, target_chunk_size, context, model):
    # Mockup function that returns a list of chunks
    return [document[i:i+target_chunk_size] for i in range(0, len(document), target_chunk_size)]

# Streamlit App
def main():
    st.sidebar.title("Smart Chunking Demo")

    # User inputs in the sidebar
    user_input = st.sidebar.text_area("Text to Chunk", placeholder="Enter some text here...")
    target_chunk_size = st.sidebar.number_input("Target Chunk Size", value=200, step=100)
    openai_api_key = st.sidebar.text_input("OpenAI API Key", placeholder="Enter your API key")
    context = st.sidebar.text_area("Context", placeholder="Enter context here...")
    model_choice = st.sidebar.selectbox("Model", ["gpt-4-1106-preview", "gpt-3.5-turbo"], index=0)

    # Button to perform chunking
    if st.sidebar.button("Chunk Text"):
        with st.spinner("Chunking text..."):
            # Smart Chunking
            smart_chunks = chunk_smartly(
                strings_to_chunk=[user_input],
                context=context,
                openai_api_key=openai_api_key,
                target_chunk_size=target_chunk_size,
                model=model_choice,
                sanitize=True
            )

            # Recursive Character Text Splitting (LangChain)
            splitter = RecursiveCharacterTextSplitter(chunk_size=target_chunk_size)
            recursive_chunks = splitter.split_text(user_input)

        col1, col2 = st.columns(2)  # Create two columns for side-by-side comparison

        with col1:
            st.subheader("Smart Chunking Output")
            for i, chunk in enumerate(smart_chunks, start=1):
                st.write(f"Chunk {i}:")
                st.text(chunk)

        with col2:
            st.subheader("LangChain Recursive Text Chunk Splitter Output")
            for i, chunk in enumerate(recursive_chunks, start=1):
                st.write(f"Chunk {i}:")
                st.text(chunk)

if __name__ == "__main__":
    main()
