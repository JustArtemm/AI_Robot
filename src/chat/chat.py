import os
import sys
sys.path.append('src')
from Utils.config import Parameters, Tools
import Utils.utils as uu
# import agent_tools.agent_tools as at 
from langchain.agents import AgentExecutor, create_gigachat_functions_agent
from langchain.tools import tool
import pyfiglet
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import AgentExecutor, create_gigachat_functions_agent

"""Пример работы с чатом через gigachain"""

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models.gigachat import GigaChat
# from src.agent_tools.agent_tools import Tools
# from src.Utils.config import 


parameters = Parameters()

def get_output():
    global parameters
    user_input = uu.get_input()
    
    # res = chat(parameters.messages)
    # print(parameters.messages)

    res = agent_executor.invoke(
        {"chat_history": parameters.messages,
        "input": user_input }
        )["output"]
    parameters.messages.append(HumanMessage(content=user_input))
    parameters.messages.append(AIMessage(content = res))
    print("Bot: ", res)
    parameters.dump_messages()
    if not parameters.save_history:
        parameters.messages = parameters.sys_msg
    return res

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials = parameters.credentials, 
                verify_ssl_certs=False)



# search_tool = DuckDuckGoSearchRun()
# tools = [search_tool]
# tools = [search_tool, draw_banner]

Tls = Tools()



agent = create_gigachat_functions_agent(chat, Tls.get_all_tools())

#AgentExecutor создает среду, в которой будет работать агент
agent_executor = AgentExecutor(
    agent=agent,
    tools=Tls.get_all_tools(),
    verbose=True,
)


if parameters.infinite_chat:
    while True:
        get_output()
else:
    get_output()
