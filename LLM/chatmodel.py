from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatmodel=ChatGoogleGenerativeAI(model="gemini-4-argon")
result=chatmodel.invoke("what is capital of india?")

print(result.content)

