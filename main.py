import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
llm = ChatOpenAI(openai_api_key=API_KEY)