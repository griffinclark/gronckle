from langchain_community.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
import openai
from text_splitter_prompt import text_splitter_prompt

# This is the smart chunker that we'll use for separating ideas
def split_chunks_responsibly(text_to_split, target_chunk_size, context, model):     
    # We'll let the user choose the model
    model = model
    llm = ChatOpenAI(model=model, openai_api_key=openai.api_key)

    # Create the prompt chain that we'll use to prompt the LLM
    prompt_template = PromptTemplate(
        input_variables=["text_splitter_prompt", "text_to_split", "target_chunk_size"],  # Define the input variables your prompt uses
        template=text_splitter_prompt + """
            %Here is the context for what this data is about:%
            {context}

            %Here is the data to chunk:%
            {text_to_split}
            
        Keep the chunks of text as close to the same length as possible. You should use {target_chunk_size} tokens as your ceiling for how large chunks can be, but it is more important to keep ideas together than it is to keep the chunks the same length. If you have to split a chunk into two, do so, but try to keep the chunks as close to the same length as possible. 
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)
    llm_response = chain.run(
        text_splitter_prompt=text_splitter_prompt, 
        text_to_split=text_to_split, 
        context=context,
        target_chunk_size=target_chunk_size
        )
    broken_out_chunks = llm_response.split("%%")
    return broken_out_chunks
