# Helper functions here

import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        
        except Exception as e:
            raise Exception("Error al intentar leer el archivo PDF")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "Formato de archivo no soportado, únicamente .txt y .pdf"
            )
    
def get_table_data(quiz_str):
    try:
        # Convert the quiz from a str to dict
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]

        # Iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq=value["mcq"]
            options=" || ".join(
                [
                    f"{option}-> {option-value}" for option, option_value in value["options"].items()
                ]
            )     
            correct=value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        
