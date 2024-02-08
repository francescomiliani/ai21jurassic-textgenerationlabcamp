## Description: This is a simple example of how to use the AI21 API to generate text using the J2-Mid model.
## Author: Francesco Miliani
## Date: 2024-02-08
## Reference: https://docs.ai21.com/reference/python-sdk
## GitHub: https://github.com/AI21Labs/ai21-python

from dotenv import load_dotenv
import os, json
from ai21 import AI21Client, AI21APIError
from ai21.models import ChatMessage, RoleType, Penalty
from ai21 import errors as ai21_errors
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

# Example 0 - Token Counting
example_text = "This is an example text"
amount = client.count_tokens(text=example_text)  # returns int
print(f'Token Counting of \'{example_text}\': {amount}')

print(f'Prompt: {_prompt}')

## Example 1 - Completion
response_mid = client.completion.create(
  model="j2-mid",
  #prompt="These are a few of my favorite",
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

# Example 2 - Chat
## Reference: https://github.com/AI21Labs/ai21-python/blob/main/examples/studio/chat.py

system = "You're a support engineer in a SaaS company"

# Messages example
messages = []
# messages = [
#     ChatMessage(text="Hello, I need help with a signup process.", role=RoleType.USER),
#     ChatMessage(text="Hi Alice, I can help you with that. What seems to be the problem?", role=RoleType.ASSISTANT),
#     ChatMessage(text="I am having trouble signing up for your product with my Google account.", role=RoleType.USER),
# ]

while True:
    _prompt = input("Enter your prompt: ")
    print(f'User Prompt: {_prompt}')

    messages.append(ChatMessage(text=_prompt, role=RoleType.ASSISTANT))
    try:
        response = client.chat.create(
            messages=messages,
            model="j2-ultra",
            system=system,
            # max_tokens=150,
            # temperature=0.7,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0,
            # count_penalty=Penalty(
            #     scale=0,
            #     apply_to_emojis=False,
            #     apply_to_numbers=False,
            #     apply_to_stopwords=False,
            #     apply_to_punctuation=False,
            #     apply_to_whitespaces=False,
            # ),
            # stop_sequences=["\n", "System:", "User:"],
        )
        # print(response)
        _response_text = response.outputs[0].text
        print(f'AI: {_response_text}')
        messages.append(ChatMessage(text=_response_text, role=RoleType.ASSISTANT))
    except ai21_errors.AI21ServerError as e:
        print("Server error and could not be reached")
        print(e.details)
    except ai21_errors.TooManyRequestsError as e:
        print("A 429 status code was returned. Slow down on the requests")
    except AI21APIError as e:
        print("A non 200 status code error. For more error types see ai21.errors")
    except Exception as e:
        print(f'An error occurred: {e}')
