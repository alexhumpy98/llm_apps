import streamlit as st
import bigframes.pandas as bpd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Initialize the Streamlit app
st.title('Streamlit App for Language Model Interaction')

# Input fields for API key and prompt
api_key = st.text_input('Enter API key')
prompt = st.text_input('Enter prompt')

# Load data
df = bpd.read_gbq("SELECT name, job, created, transactions, revenue, permission, crm_id, items FROM `annular-form-389809.merged_data.crm_ga4` where event_name = 'add_to_cart'").to_pandas()

# Defining llm
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", api_key=api_key)

# Defining agent
agent = create_pandas_dataframe_agent(llm, df, verbose=True, top_k = 1000)

# When a prompt is entered, run the agent and display the output
if st.button('Run'):
    if not api_key or not prompt:
        st.error('Please enter both an API key and a prompt.')
    else:
        try:
            output = agent.run(prompt)
            st.success('Output:')
            st.write(output)
        except Exception as e:
            st.error(f'An error occurred: {e}')

