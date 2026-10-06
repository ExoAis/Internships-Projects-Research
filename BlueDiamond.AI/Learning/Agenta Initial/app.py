import agenta as ag
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('OPENAI_API_KEY')

default_prompt = "What is a good name for a company that makes {product}?"


@ag.post
def generate(
    product: str,
    temperature: ag.FloatParam = 0.9,
    prompt_template: ag.TextParam = default_prompt,
) -> str:
    llm = OpenAI(temperature=temperature, openai_api_key=key)
    prompt = PromptTemplate(input_variables=["product"], template=prompt_template,)
    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run(product=product)

    return output
