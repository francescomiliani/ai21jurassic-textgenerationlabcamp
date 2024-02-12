## Description: This is a simple example of how to use the AI21 API to generate text using the J2-Mid model.
## Author: Francesco Miliani
## Date: 2024-02-08
## Reference: https://docs.ai21.com/reference/python-sdk
## GitHub: https://github.com/AI21Labs/ai21-python

from dotenv import load_dotenv
import os
from ai21 import AI21Client
# Load variables from the .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
print(f"\t API_KEY: {API_KEY}")
 
client = AI21Client(api_key=API_KEY)

_prompt = """
Complete the following sentence.
Sentence: These are a few of my favorite
Completion: things. Cream-colored ponies and crisp apple strudels.

##

Complete the following sentence.
Sentence: These are a few of my favorite
Completion: rock bands: The Beatles, The Doors, Fleetwood Mac.

##

Complete the following sentence.
Sentence: These are a few of my favorite
Completion:
"""

# J2 Mid

print(f'Prompt: {_prompt}')

response_mid = client.completion.create(
  model="j2-mid",
  prompt=_prompt,
  num_results=1,
  max_tokens=2,
  temperature=0.4,
  top_k_return=0,
  top_p=1,
  stop_sequences=["##"]
)

# print(response_mid)
for i in range(len(response_mid.completions)):
    print(response_mid.completions[i].data.text)
    print("\n")
