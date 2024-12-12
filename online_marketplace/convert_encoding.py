# -*- coding: utf-8 -*-
import codecs

input_file = "app.py"  # Имя файла, который нужно преобразовать
output_file = "app_utf8.py"  # Имя нового файла

with codecs.open(input_file, "r", encoding="cp1251") as source:
    content = source.read()

with codecs.open(output_file, "w", encoding="utf-8") as target:
    target.write(content)

print(f"Файл сохранен как {output_file} в кодировке UTF-8")