import csv
import json
import logging

import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../utills.log', "w")
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def read_json(filename):
    """Функция принимающая путь к файлу, считывает информацию c JSON файла"""
    try:
        """Это логер для функции read_file"""
        logger.info("Начал выгрузку с файла JSON формата")
        with open(filename, encoding="utf-8") as file:  # Открытие и считывание файла формата JSON
            reading = json.load(file)  # Преобразование JSON файла в пайтон обьект
            logger.info("Оконили выгрузку с файла JSON формата")
        return reading
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []  # В случае ошибки возвращает пустой список


def read_csv(filename):
    """Функция принимающая путь к файлу, считывает информацию c CSV файла"""
    try:
        """Это логер для функции read_file_csv"""
        logger.info("Начал выгрузку с файла csv формата")
        with open(filename, encoding="utf-8") as file:  # Открытие и считывание файла формата CSV
            reading_csv = csv.DictReader(file, delimiter=";")
            reading = [read for read in reading_csv]  # Считывание файла методом цикла
        logger.info("Окончили выгрузку с файла csv формата")
        return reading
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []  # В случае ошибки возвращает пустой список


def read_excel(filename):
    """Функция принимающая путь к файлу, считывает информацию c EXCEL файла"""
    try:
        """Это логер для функции read_file_excel"""
        logger.info("Начал выгрузку с файла excel формата")
        reading_excel = pd.read_excel(filename)  # считывание EXCEL файла
        new_list = []
        while True:
            for index, row in reading_excel.iterrows():  # Цикл по файлу и отбор необходимых данных
                list_file = {"id": row["id"], 'state': row["state"], 'date': row["date"], 'amount': row["amount"],
                             'currency_name': row["currency_name"],
                             'currency_code': row["currency_code"], 'from': row["from"], 'to': row["to"],
                             'description': row["description"]}
                new_list.append(list_file)  # добавление каждого цикла в новый список
            logger.info("Окончили выгрузку с файла excel формата")
            return new_list  # возвращает новый список
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []  # В случае ошибки возвращает пустой список
