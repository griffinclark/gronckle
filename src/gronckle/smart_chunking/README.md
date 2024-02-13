# Overview
In order to build RAG applications, users have to take the data that they want to use in their application and store it in a database. Assuming an unknown data structure and pattern, the state of the art for chunking information is to use a recursive text chunk splitter which breaks text down into sentences (when possible) and store it in a vector database (VDB). However, developers can see significant performance gains in their applications by chunking their information based on ideas instead of arbitrary chunk size. This ensures that ideas stay together and the LLM is passed complete ideas as the context that it's using to generate answers. 

# The Process
## Prerequisites 
1. Python 3.6+
2. Cassandra database access 
3. Access to OpenAI's API
4. The .zip file for Cassandra connection 
5. An astra-token.json file with authentication details for Cassandra

## Operations
1. Establish the connection to the VDB 
2. 