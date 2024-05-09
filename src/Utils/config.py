import os
import sys
import json
import Utils.utils as uu
opj = os.path.join
from langchain.schema import HumanMessage, SystemMessage, AIMessage
# from agent_tools import agent_tools
from langchain.agents import tool

class Parameters:
    def __init__(self, options_path = opj('Config/settings.json')):
        self.options_path = options_path
        self.options = uu.get_config(options_path)
        self.messages_dict = {}

        credentials_p = opj(self.options['credentials_p'])

        self.save_history = self.options['save_history']
        self.infinite_chat = self.options['infinite_chat']
        self.sys_msg = [SystemMessage(
                content="Ты бот-ассистент Макс, который помогает пользователю в любых вопросах. Ты умеешь искать в интернете используя инструменты"
            )]
        self.messages = self.sys_msg

        with open(credentials_p, 'r') as f:
            self.credentials = f.read()

        if os.path.isfile(opj('src/chat/messages.json')):
            self.messages_dict = uu.get_config(opj('src/chat/messages.json'))
            self.messages = self.as_messages()
            print(self.messages)


        self.tools = [Tools.get_word_length]
        
                                

        




    def dump_messages(self):
        self.messages_todict()
        with open(opj('src/chat/messages.json'), 'w') as f:
            json.dump(self.messages_dict, f)

    def messages_todict(self):
        for i in range(len(self.messages)):
            # print(type(self.messages[i]))
            self.messages_dict[i] = {"type" : self.messages[i].type,
                                    "content": self.messages[i].content}
        return self.messages_dict
        
    def as_messages(self):
        msg_list = []
        types = {
            'human': HumanMessage,
            'system': SystemMessage,
            'ai': AIMessage
        }
        for elem in self.messages_dict:
            msg_list.append(types[self.messages_dict[elem]["type"]](content = self.messages_dict[elem]["content"]))
        return msg_list
    
class Tools:
    def __init__(self) -> None:
        pass
    
    @tool
    def get_word_length(word: str) -> int:
        """Returns the length of a word."""
        return len(word)
                                

                
                
    
        


