# Import basic packages 
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging


# Importing necesary packages from langchain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# Load environment variables
load_dotenv()

# Access the env variable
key=os.getenv("OPEN_API_KEY")

llm = ChatOpenAI(open_api_key=key, model_name="gpt-3.5-turbo", temperature=0.7)

# The input prompt template 

TEMPLATE = """
Text:{text}
Eres un creador experto de MCQ. Dado el texto anterior, es tu trabajo \
crear un cuestionario de {number} preguntas de opción múltiple para {subject} estudiantes en {tone} tone.
Make sure to format your response like RESPONSE_JSON bellow an use it as a guide. \
Asegurate de hacer {number} MCQs
{response_json}
"""

# The input prompt with the variables that the user is going to pass

quiz_generation_prompt = PromptTemplate(
    input_variables = ["text", "number", "subject", "tone", "respose_json"],
    template = TEMPLATE
)

# Create the chain to connect altogether

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

TEMPLATE2 = """ 
Eres un experto gramático y escritor. Se realizó una prueba de opción múltiple para estudiantes de {subject}. \
Debe evaluar la complejidad de la pregunta y realizar un análisis completo del cuestionario. Utilice únicamente un máximo de 50 palabras para mayor complejidad.
si el cuestionario no se ajusta a las capacidades cognitivas y analíticas de los estudiantes, \
actualice las preguntas del cuestionario que deben cambiarse y cambie el tono para que se ajuste perfectamente a las habilidades del estudiante
Preguntas frecuentes del cuestionario:
{quiz}

Verifique con un escritor experto en español el cuestionario anterior:
"""

# The chain evaluation

quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE)

# The quiz evaluation chain

review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


# Next we are going to connect both chains with SequentiaChain

generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                          output_variables = ["quiz", "review"], verbose=True)


