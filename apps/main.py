'''Основная программа.

Выгружает данные из doc файла.
'''
from pprint import pprint
import pandas as pd
from docx import Document


def main():
    '''Основаная функция.'''

    document = Document('data/lab_result-220622-для студентов.docx')
    result = []
    for table in document.tables:
        for row in table.rows:
            result.append([i.text.strip() for i in row.cells])

            pprint(result)
    data = pd.DataFrame(result)

    data = data.to_csv('demo.csv')


if __name__ == '__main__':
    main()
