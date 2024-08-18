import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate  # Is used to design my own chart prompt.
from langchain_core.output_parsers import StrOutputParser # 

os.environ['OPENAI_API_KEY']= os.getenv("OPENAI_API_KEY")

# for langsmith tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please resplond to the question asked"),
        ("user","Question:{question}")
    ]
)

# Streamlit Framework
st.title("LangChain Demo With Google LLama2 Model")
input_text=st.text_input("What question you have in mind?")


## Ollama LLama2 Model
llm=Ollama(model="llama3")

output_parser=StrOutputParser()

chain= prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
