import getpass
import os


if not os.environ.get("OPEN_API_KEY"):
    os.environ["OPEN_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

print(model.invoke("Hello, World"))