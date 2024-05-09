import os
import sys
sys.path.append('src')
from Utils.config import Parameters
import Utils.utils as uu
# import agent_tools.agent_tools as at 
from langchain.agents import AgentExecutor, create_gigachat_functions_agent


"""Пример работы с чатом через gigachain"""

from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat


parameters = Parameters()

def get_output():
    global parameters
    user_input = uu.get_input()
    parameters.messages.append(HumanMessage(content=user_input))
    res = chat(parameters.messages)
    parameters.messages.append(res)
    print("Bot: ", res.content)
    parameters.dump_messages()
    if not parameters.save_history:
        parameters.messages = parameters.sys_msg
    return res

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials = parameters.credentials, 
                verify_ssl_certs=False)
agent_wordlen = create_gigachat_functions_agent(chat, parameters.tools)
agent_wordlen_executor = AgentExecutor(
    agent=agent_wordlen,
    tools=parameters.tools,
    verbose=True,
)


if parameters.infinite_chat:
    while True:
        get_output()
else:
    get_output()
