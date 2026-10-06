import openai
import streamlit as st

openai.api_key  = '' # Your API Key

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

context = {'role': 'system', 'content': """
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collect the order, \
and then ask if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally, you collect the payment. \
Make sure to clarify all options, extras, and sizes to uniquely \
identify the item from the menu. \
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""}

if "Chat" not in st.session_state:
    st.session_state["Chat"] = []

st.session_state["Chat"].append(context)           

def collect_messages(prompt):
    st.session_state["Chat"].append({'role': 'user', 'content': prompt})
    response = get_completion_from_messages(st.session_state["Chat"])
    st.session_state["Chat"].append({'role': 'assistant', 'content': response})

    for message in st.session_state["Chat"]:
        if message['role'] == 'user':
            st.text(f'User: {message["content"]}')
        elif message['role'] == 'assistant':
            st.text(f'Assistant: {message["content"]}')

st.title('OrderBot - Pizza Restaurant Ordering')

user_input = st.text_input('User:')

if st.button('Chat!'):
    collect_messages(user_input)

    st.write('OrderBot is ready to assist you!')




