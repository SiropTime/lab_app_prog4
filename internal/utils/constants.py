import os

from dotenv import load_dotenv

load_dotenv(".env")
TOKEN = os.environ.get("TOKEN")
WELCOME_MESSAGE = """
                  Лабораторная работа №4. Выполнена Мальцевым Тимофеем Дмитриевичем
                  Группа ИДБ-21-10.
                  Телеграм-бот для поиска статей, книг и рецензий на кино на New York Times через их API.
                  """
