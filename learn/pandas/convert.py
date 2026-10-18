import pandas as pd

# Имя твоего текстового файла (путь без внутренних кавычек, с буквой 'r' впереди)
txt_filename = r'C:\Users\Денис\Documents\Программирование\Python\learn\pandas\enable1.txt'
csv_filename = 'words_output.csv'

# Шаг 1: Читаем текстовый файл построчно
with open(txt_filename, 'r', encoding='utf-8', errors='ignore') as f:
    # Удаляем лишние пробелы и переносы строк
    words = [line.strip() for line in f if line.strip()]

# Шаг 2: Создаем датафрейм (создадим столбцы со словом и его длиной)
df = pd.DataFrame(words, columns=['word'])
df['char_count'] = df['word'].str.len()

# Шаг 3: Сохраняем результат в CSV
df.to_csv(csv_filename, index=False, encoding='utf-8')

print(f"Готово! Файл сохранен как: {csv_filename}")