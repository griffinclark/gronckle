# Smart Chunking With OpenAI and Cassandra
In order to build RAG applications, users have to take the data that they want to use in their application and store it in a database. Assuming an unknown data structure and pattern, the state of the art for chunking information is to use a recursive text chunk splitter which breaks text down into sentences (when possible) and store it in a vector database (VDB). However, developers can see significant performance gains in their applications by chunking their information based on ideas instead of arbitrary chunk size. This ensures that ideas stay together and the LLM is passed complete ideas as the context that it's using to generate answers. 

## Prerequisites
- Python 3.6+
- Access to OpenAI API (GPT-4)
- Cassandra database setup (optional)
- openai, uuid, re, langchain_community packages installed

## Features

- **Idea-Based Chunking**: Utilizes OpenAI's language model to intelligently split text into chunks that preserve complete ideas.
- **Customizable Chunk Sizes**: Allows specifying target chunk sizes while prioritizing the preservation of logical ideas.
- **Text Sanitization**: Includes optional sanitization of chunks for safe storage in databases and compatibility with Python scripts.
- **Integration with Astra DB**: Supports storing the processed chunks directly into a specified keyspace in Astra DB, leveraging Cassandra for scalable and efficient data management.

## Best Practices
**Contextual Relevance:** Ensure the context provided is highly relevant to the data being chunked for optimal segmentation.
**Model Selection:** Choose the model that best suits your needs. While gpt-4-1106-preview is set as the default for its balance of performance and quality, other models may be more appropriate based on your specific requirements
