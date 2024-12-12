# -*- coding: utf-8 -*-
import codecs

input_file = "app.py"  # ��� �����, ������� ����� �������������
output_file = "app_utf8.py"  # ��� ������ �����

with codecs.open(input_file, "r", encoding="cp1251") as source:
    content = source.read()

with codecs.open(output_file, "w", encoding="utf-8") as target:
    target.write(content)

print(f"���� �������� ��� {output_file} � ��������� UTF-8")