import os

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

information = """
Paul Adrien Maurice Dirac OM FRS[6] (/dɪˈræk/; 8 August 1902 – 20 October 1984) was an English theoretical physicist who is considered to be one of the founders of 
quantum mechanics and quantum electrodynamics. He is credited with laying the foundations of quantum field theory.
He was the Lucasian Professor of Mathematics at the University of Cambridge, a professor of physics at Florida State University and the University of Miami, 
and a 1933 Nobel Prize in Physics recipient.
"""


def get_summary_chain() -> LLMChain:
    summary_template = """
         given the information {information} I want you to create:
         1. a short summary
         2. two interesting facts about them
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={},
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)


if __name__ == "__main__":
    print(f"""running with key: {OPENAI_API_KEY}""")
    chain = get_summary_chain()
    print(chain.run(information=information))
