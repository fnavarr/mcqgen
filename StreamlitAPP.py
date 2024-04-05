# Import basic packages 
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

# Next step is to creatr te SteamlitAPP, so first we will load the json file

with open('C:\Users\Fernando Navarro\MCQProject\response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

# Create the title
st.title("MCQ Creator application with LangCgain")


# Create a form usin st.form 
with st.form("user_inputs"):
    # File Upload
    upload_file=st.file_uploader("Upload a PDF or TXT File")
    # Input fields
    mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=50)
    # Subject
    subject=st.text_input("Insert Subject", max_chars=20)
    # Quiz Tone
    tone=st.text_input("Complexity Level of Questions", max_chars=20, placeholder="Simple")

    # Add button
    button=st.form_submit_button("Create MCQs")

    # Validate if everyting is set 
    if button and upload_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(upload_file)
                # Count tokens and cost of API Call
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
                #st.write(response)

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total Cost: {cb.total_cost}")
                if isinstance(response, dict):
                    # Extract qye quiz data from the response
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index(df.index +1)
                            st.table(df)
                            # Display the review in text box as well
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")
                    else:
                        st.write(response)        
