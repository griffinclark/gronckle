
# The main function that users will call
import tiktoken
from split_text_responsibly import split_chunks_responsibly
import openai
import re
import uuid
from langchain_community.embeddings import OpenAIEmbeddings


def chunk_smartly(
        strings_to_chunk, 
        context, 
        openai_api_key,
        target_chunk_size=1000,
        model="gpt-4-1106-preview",
        sanitize=True,
        astra_session=None,
        keyspace=None,
        max_context_length=2048
        ):
    """
    Chunk the given documents into smaller chunks using OpenAI's language model.

    Parameters:
    - strings_to_chunk (list): A list of strings to be chunked.
    - context (str): A strings for the LLM describing what your data is about. This should be fairly short (1-2 sentences) and let the model know what your data is.
    - openai_api_key (str): The API key for accessing OpenAI's services.
    - target_chunk_size (int, optional): The desired size of each chunk. Defaults to 1000. Note that the actual size of the chunks may vary.
    - model (str, optional): The name or ID of the OpenAI language model to use. Defaults to "gpt-4-1106-preview", which is recommended to preserve quality.
    - sanitize (bool, optional): Whether to sanitize the chunks before storing them in the database. Defaults to True.
    - astra_session (astra.Session, optional): A session object for the Astra database. If one is passed, data will be stored in Astra. Defaults to None.
    - keyspace (str, optional): The keyspace in the Astra database to store the data. Required if astra_session is not None.
    Returns:
    - list: A list of strings, each representing a chunk of the input documents.
    """
   
    openai.api_key = openai_api_key
    for document in strings_to_chunk:
        # If the document has more tokens than the maximum context length, truncate it and add the rest to the back of strings_to_chunk

        # Get token count assuming openai encodings
        encoding = tiktoken.get_encoding("cl100k_base")
        num_tokens = len(encoding.encode(document))
        if num_tokens > max_context_length:
            strings_to_chunk.append(document[max_context_length:])
            document = document[:max_context_length]
        split_docs = split_chunks_responsibly(
            document, 
            target_chunk_size, 
            context, 
            model)
        # This is done in two separate steps because eventually we may want to add a lightweight validator into here
        # for each document, store it in the vector database as a separate document
        for chunk_text in split_docs:
            if sanitize:
                # Escape braces to prevent format string issues in Python
                chunk_text = chunk_text.replace("{", "{{").replace("}", "}}")
                # Allow alphanumeric characters, whitespace, braces, and common punctuation
                # Adjust the character set in the regex below as needed for your specific requirements
                chunk_text = re.sub(r"[^\w\s{}.,;:!?'\"-]", "", chunk_text)
            if astra_session is not None and keyspace is not None:
                # Get the embeddings
                embedding = OpenAIEmbeddings().embed_document(chunk_text)
                                    
                # Generate a unique ID for the document
                doc_id = uuid.uuid4()
                
                # Store the document in the vector database
                insert_stmt = astra_session.prepare(f"""
                        INSERT INTO {keyspace}.text_embeddings0 (id, text, embedding)
                        VALUES (?, ?, ?)
                    """)
                astra_session.execute(insert_stmt, [doc_id, chunk_text, embedding])
    return split_docs