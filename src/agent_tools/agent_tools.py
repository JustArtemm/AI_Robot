import os
from langchain.agents import tool
from langchain_community.tools.tavily_search import TavilySearchResults
import pyfiglet
import sympy




#Поиск в интернете
search = TavilySearchResults()


@tool
def draw_banner(number: str) -> None:
    """Рисует баннер с текстом результатов кода в виде Ascii-графики

    Args:
        number (str): Число или текст, которое нужно нарисовать на баннере
    """
    pyfiglet.print_figlet(number, font="epic")

@tool
def calculator(input:str) -> None:
    """ Вычисляет математические операции такие как сложение, вычитание, деление и умножение

    Args:
        input (str): входные данные в строчном формате включающие в себя одну из операций: +, -, *, /. Например "1+2", "3-2", "10*5", "11/4" 
    """
    sympy.sympify(input)

Tools = [search, draw_banner, calculator]
