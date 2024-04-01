import os
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

if __name__=='__main__':
    load_dotenv()
    print('Hello LangChain!')


    summary_template="""
    given the {information} about a person,I want you to create:
    1. A short summary
    2. Two interesting facts about the person"""

    summary_prompt_template=PromptTemplate(input_variables=['information'],template=summary_template)

    llm=ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo')


