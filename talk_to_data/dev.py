#from pathlib import Path

#import pandas as pd
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
# from langchain.chat_models import ChatOpenAI
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain.pydantic_v1 import BaseModel, Field
# from langchain.tools.retriever import create_retriever_tool
# from langchain.vectorstores import FAISS
# from langchain_experimental.tools import PythonAstREPLTool
import bigframes.pandas as bpd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI



# Load data
df = bpd.read_gbq("SELECT name, job, created, transactions, revenue, permission, crm_id, items FROM `annular-form-389809.merged_data.crm_ga4` where event_name = 'add_to_cart' LIMIT 10").to_pandas()

# Defining llm
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

# Defining agent
agent = create_pandas_dataframe_agent(llm, df, verbose=True)

# Default prompt
agent.run("How many unique customers have permission")
