from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm=OpenAI(model="gpt-5.6-terra")
result=llm.invoke("which is best company of india in India describe it?")

print(result)