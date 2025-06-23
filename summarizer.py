from langchain_community.chat_models import ChatOllama
from langchain.chains.summarize import load_summarize_chain
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "" # Removed for security

# ChatGPT summarizer
class Summarizer():
    def __init__(self):
        self.client = OpenAI(organization='') # Removed for security

    def summarize(self, article):
        completion = self.client.chat.completions.create( model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Respond with a summary of the following article in 100 words or less: {article}"}])
        return completion.choices[0].message.content

    def summarize_articles(self, articles):
        for article in articles:
            article.summary = self.summarize(article.text)

# Local Llama summarizer
class Summarizer_Llama():

    MODEL = "llama3:8b-instruct-q8_0"

    def __init__(self):
        self.llm = ChatOllama(model=self.MODEL, temperature=0)

    def summarize(self, article):
        cmds = [("system", "You are a helpful assistant."),
                "human", f"Respond with 100 words"]
        response = self.llm.invoke(cmds)
        return response.content

    def summarize_articles(self, articles):
        for article in articles:
            article.summary = self.summarize(article.text)
