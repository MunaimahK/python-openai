import os
import openai
from packaging import version
from dotenv import load_dotenv

load_dotenv()


required_version = version.parse("1.1.1") # replace the version by the version you want
current_version = version.parse(openai.__version__)

if current_version < required_version:
    raise ValueError(f"Error: OpenAI version {openai.__version__}"
                     " is less than the required version 1.1.1")
else:
    print("OpenAI version is compatible.")

# -- Now we can get to it
from openai import OpenAI

print('OPENAI WAS GREAT AGAIN')

#-------------------------------------------------------------
from openai import AzureOpenAI
 
client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION"),
)
 
message_text = [
    {
        "role": "system",
        "content": "I am providing a rubric to grade student responses to a the following physics conceptual problem.\n\nQuestion: Why do we draw the normal force vector on an object's FBD\n\nAs an instructor, you are to award the student response 1 point for each condition satsified in the rubric.\n\nRubric:\n1. Student knows that Newton's law implies every force has an equal and opposite force\n2. Student knows that the normal force must be present or else the object will sink\n3. Student knows that gravity is downward so normal force must be upward\n\nHere is the student response:\n\nWe draw a normal force vector because of newton's laws. Every force has an equal and opposite force. Since gravity acts on all objects, the normal force is in the opposite direction of gravity.\n\nNow, grade the student's response.\n\n\nAnswer:\n\nThis student receives 2 points. \nThe student mentions Newton's laws saying every force has an equal and opposite force.\nThe student mentions normal force is in the opposite direction of gravity\nThe student does not mentione that without normal force, the object would sink.\nSo the student satisfied 2 of 3 rubric conditions.  \n\nNow grade the next student's answer:\n\nI think normal force is drawn because gravity goes down and normal force needs to go up. I don't know which law that is.\n\nHow many points does the student get?\n",
    }
]
 
completion = client.chat.completions.create(
    model=os.getenv("MODEL_NAME"),
    messages=message_text,
    temperature=0.8,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
)

print(completion.choices[0].message.content)