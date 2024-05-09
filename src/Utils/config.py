import os
import sys
import json
import Utils.utils as uu
opj = os.path.join
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.tools.tavily_search import TavilySearchResults
import pyfiglet
# from agent_tools import agent_tools
from langchain.agents import tool
import sympy
import requests
from PIL import Image
from io import BytesIO 
import matplotlib.pyplot as plt
import cv2
import numpy as np
import climage 
import urllib
import random
from bs4 import BeautifulSoup

class Parameters:
    def __init__(self, options_path = opj('Config/settings.json')):
        self.options_path = options_path
        self.options = uu.get_config(options_path)
        self.messages_dict = {}

        credentials_p = opj(self.options['credentials_p'])

        self.save_history = self.options['save_history']
        self.infinite_chat = self.options['infinite_chat']
        self.sys_msg = [SystemMessage(
                content="Ты бот-ассистент Макс, \
                который помогает пользователю в любых вопросах. \
                Ты умеешь искать в интернете используя инструменты, \
                выполнять несложные математические операции и создавать \
                баннеры с английским текстом и числами только с помощью инструмента. При запросе выполнить \
                математическую операцию от пользователя ВСЕГДА запускай \
                инструмент calculator. Когда пользователь хочет узнать информацию, актуальность которой важна ВСЕГДА \
                используй инструмент browse_internet. Этот инструмент нужен для поиска актуальной информации. \
                КАЖДЫЙ РАЗ когда просят нарисовать или показать картинку используй инструмент draw_banner."
            )]
        self.messages = self.sys_msg

        with open(credentials_p, 'r') as f:
            self.credentials = f.read()

        if os.path.isfile(opj('src/chat/messages.json')):
            self.messages_dict = uu.get_config(opj('src/chat/messages.json'))
            self.messages = self.as_messages()
            print(self.messages)


        # self.tools = [Tools.get_word_length]




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
        
        # self.search = TavilySearchResults()
        self.parameters = Parameters()
        self.tools = self.get_all_tools()
        # print(self.browse_internet('Картинки котика'))

    def get_all_tools(self):
        return [
            self.browse_internet,
            self.draw_banner, 
            self.calculator, 
            # self.clear_chat_history
            # self.download_and_show_image,
            # self.get_image_from_cite
                ]
    # def get_random_content(self,content: list):
    #     i = random.randint(0,len(content))
    #     return content[i]
    @tool
    def browse_internet(input: str):
        """ Выполняет поиск в интернете по заданному запросу, используется когда нужно получить актуальную информацию

        args: input (str): Запрос по которому необходимо выполнить поиск
        """
        search = TavilySearchResults()
        return search(input)
    @tool
    def draw_banner(number: str) -> None:
        """Создает баннер с текстом результатов кода в виде Ascii-графики

        Args:
            number (str): Число или текст латиницей, которое нужно нарисовать на баннере
        """
        pyfiglet.print_figlet(number, font="epic")

    @tool
    def calculator(input:str) -> str:
        """ Вычисляет математические операции такие как сложение, вычитание, деление и умножение

        Args:
            input (str): входные данные в строчном формате включающие в себя одну из операций: +, -, *, /. Например "1+2", "3-2", "10*5", "11/4" 
        """
        return(str(sympy.sympify(input)))

    
    @tool
    def get_image_from_cite(cite_url:str):
        """ Находит сайт по заданному адресу и извлекает случайную картинку из этого сайта
        Args:
            cite_url (str): Ссылка на сайт из которого необходимо извлечь изображение
        """
        response = requests.get(cite_url)
        soup = BeautifulSoup(response.text, features="html.parser")
        images = []
        for img in soup.findAll('img'):
            images.append(img.get('src'))
        print(images)
        i = random.randint(0,len(images))
        return images[i]


    @tool
    def download_and_show_image(image_url_adress:str):
        """ Выполняется ТОЛЬКО после выполнения инструмента по поиску информации в интернете.
        Скачивает картинку по заданному адресу и показывает ее
        args: image_url_adress (str): url адрес нахождения изображения
        """ 
        img_data = requests.get(image_url_adress).content
        try:
            img = Image.open(BytesIO(img_data)).convert('RGB')
            output = climage.convert_pil(img, is_unicode=True)
            print(output)
        except:
            return "Не удалось найти изображение :("
        
        
        

    

                
                
    
        


