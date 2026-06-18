# pandas_trainer.py - ПОЛНЫЙ ТРЕНАЖЕР ПО ВСЕМУ КОНСПЕКТУ
import random
import os

# ============================================================
# 1. ВОПРОСЫ ПО SERIES
# ============================================================
series_questions = [
    {"q": "Как создать Series из списка [100, 102, 104]?", "a": "pd.Series([100, 102, 104])"},
    {"q": "Как создать Series с собственными индексами 'a', 'b', 'c'?", "a": "pd.Series(data, index=['a', 'b', 'c'])"},
    {"q": "Как получить доступ к элементу Series по метке 'apartment #1'?", "a": "series.loc['apartment #1']"},
    {"q": "Как получить доступ к элементу Series по позиции (индексу 0)?", "a": "series.iloc[0]"},
    {"q": "Как изменить значение элемента в Series по метке 'Day 1'?", "a": "series.loc['Day 1'] = 200"},
    {"q": "Как отфильтровать Series, оставив только элементы >= 200?", "a": "series[series >= 200]"},
    {"q": "Как создать Series из словаря {'Day 1': 1750, 'Day 2': 2100}?", "a": "pd.Series({'Day 1': 1750, 'Day 2': 2100})"},
    {"q": "Какой метод используется для доступа по метке в Series?", "a": ".loc[]"},
    {"q": "Какой метод используется для доступа по позиции в Series?", "a": ".iloc[]"},
]

# ============================================================
# 2. ВОПРОСЫ ПО DATA FRAME
# ============================================================
dataframe_questions = [
    {"q": "Как создать DataFrame из словаря с колонками 'Name' и 'Age'?", "a": "pd.DataFrame({'Name': ['A','B'], 'Age': [25,30]})"},
    {"q": "Как задать собственные индексы строк при создании DataFrame?", "a": "pd.DataFrame(data, index=['Row1', 'Row2'])"},
    {"q": "Как получить строку по метке 'Employee 1' в DataFrame?", "a": "df.loc['Employee 1']"},
    {"q": "Как получить первую строку DataFrame по позиции?", "a": "df.iloc[0]"},
    {"q": "Как добавить новую колонку 'Job' в DataFrame?", "a": "df['Job'] = ['Cook', 'N/A']"},
    {"q": "Как добавить новую строку в DataFrame с помощью concat?", "a": "df = pd.concat([df, new_row])"},
    {"q": "Какой метод объединяет два DataFrame по вертикали?", "a": "pd.concat()"},
]

# ============================================================
# 3. ВОПРОСЫ ПО IMPORTING
# ============================================================
importing_questions = [
    {"q": "Как прочитать CSV файл 'pokemon.csv'?", "a": "pd.read_csv('pokemon.csv')"},
    {"q": "Как прочитать JSON файл 'pokemon.json'?", "a": "pd.read_json('pokemon.json')"},
    {"q": "Какой метод выводит все строки DataFrame без сокращений?", "a": "df.to_string()"},
    {"q": "Сколько строк по умолчанию показывает print(df) при чтении CSV?", "a": "первые 5 и последние 5 строк"},
]

# ============================================================
# 4. ВОПРОСЫ ПО SELECTION
# ============================================================
selection_questions = [
    {"q": "Как выбрать одну колонку 'Name' из DataFrame?", "a": "df['Name']"},
    {"q": "Как выбрать несколько колонок 'Name', 'Height', 'Weight'?", "a": "df[['Name', 'Height', 'Weight']]"},
    {"q": "Как сделать колонку 'Name' индексом при чтении CSV?", "a": "pd.read_csv('pokemon.csv', index_col='Name')"},
    {"q": "Как получить строку по метке 'Bulbasaur' после установки индекса?", "a": "df.loc['Bulbasaur']"},
    {"q": "Как сделать срез строк 'Charizard':'Blastoise' и выбрать колонки 'Height', 'Weight'?", "a": "df.loc['Charizard':'Blastoise', ['Height', 'Weight']]"},
    {"q": "Как выбрать строки с 0 по 10 с шагом 2 и колонки с 0 по 3?", "a": "df.iloc[0:11:2, 0:3]"},
    {"q": "Как обработать ошибку при поиске покемона, которого нет в индексе?", "a": "try: df.loc[name] except KeyError: print('Not found')"},
]

# ============================================================
# 5. ВОПРОСЫ ПО FILTERING
# ============================================================
filtering_questions = [
    {"q": "Как отфильтровать покемонов с ростом >= 2?", "a": "df[df['Height'] >= 2]"},
    {"q": "Как отфильтровать покемонов, у которых Type1 == 'Water' ИЛИ Type2 == 'Water'?", "a": "df[(df['Type1'] == 'Water') | (df['Type2'] == 'Water')]"},
    {"q": "Как отфильтровать покемонов, у которых Type1 == 'Fire' И Type2 == 'Flying'?", "a": "df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]"},
    {"q": "Какой оператор используется для логического И в pandas?", "a": "& (амперсанд)"},
    {"q": "Какой оператор используется для логического ИЛИ в pandas?", "a": "| (вертикальная черта)"},
]

# ============================================================
# 6. ВОПРОСЫ ПО AGGREGATION
# ============================================================
aggregation_questions = [
    {"q": "Как найти среднее значение всех числовых колонок?", "a": "df.mean(numeric_only=True)"},
    {"q": "Как найти сумму всех числовых колонок?", "a": "df.sum(numeric_only=True)"},
    {"q": "Как найти минимальное значение в числовых колонках?", "a": "df.min(numeric_only=True)"},
    {"q": "Как найти максимальное значение в числовых колонках?", "a": "df.max(numeric_only=True)"},
    {"q": "Как посчитать количество НЕпустых значений в каждой колонке?", "a": "df.count()"},
    {"q": "Как найти среднее значение колонки 'Height'?", "a": "df['Height'].mean()"},
    {"q": "Как найти сумму значений колонки 'Height'?", "a": "df['Height'].sum()"},
    {"q": "Как найти минимальное значение в колонке 'Height'?", "a": "df['Height'].min()"},
    {"q": "Как найти максимальное значение в колонке 'Height'?", "a": "df['Height'].max()"},
    {"q": "Как посчитать количество значений в колонке 'Height'?", "a": "df['Height'].count()"},
    {"q": "Как сгруппировать данные по колонке 'Type1'?", "a": "df.groupby('Type1')"},
    {"q": "Как найти средний рост для каждого типа покемонов?", "a": "df.groupby('Type1')['Height'].mean()"},
    {"q": "Как найти сумму ростов для каждого типа покемонов?", "a": "df.groupby('Type1')['Height'].sum()"},
]

# ============================================================
# 7. ВОПРОСЫ ПО DATA CLEANING
# ============================================================
cleaning_questions = [
    {"q": "Как удалить колонку 'Legendary' из DataFrame?", "a": "df.drop(columns=['Legendary'])"},
    {"q": "Как удалить несколько колонок 'Legendary' и 'No'?", "a": "df.drop(columns=['Legendary', 'No'])"},
    {"q": "Как удалить строки, где в колонке 'Type2' есть NaN?", "a": "df.dropna(subset=['Type2'])"},
    {"q": "Как заменить NaN на 'None' в колонке 'Type2'?", "a": "df.fillna({'Type2': 'None'})"},
    {"q": "Как заменить значения 'Grass' на 'GRASS' в колонке 'Type1'?", "a": "df['Type1'].replace({'Grass': 'GRASS'})"},
    {"q": "Как привести все имена покемонов к нижнему регистру?", "a": "df['Name'].str.lower()"},
    {"q": "Как привести все имена покемонов к верхнему регистру?", "a": "df['Name'].str.upper()"},
    {"q": "Как изменить тип данных колонки 'Legendary' на bool?", "a": "df['Legendary'].astype(bool)"},
    {"q": "Как удалить дубликаты из DataFrame?", "a": "df.drop_duplicates()"},
    {"q": "Как сохранить очищенный DataFrame в CSV?", "a": "df.to_csv('pokemon_cleaned.csv', index=False)"},
]

# ============================================================
# 8. ВОПРОСЫ ПО DATA OVERVIEW (новый блок)
# ============================================================
overview_questions = [
    {"q": "Как показать первые 5 строк DataFrame?", "a": "df.head()"},
    {"q": "Как показать информацию о колонках (типы данных, пропуски)?", "a": "df.info()"},
    {"q": "Как показать статистику по числовым колонкам?", "a": "df.describe()"},
]

# ============================================================
# 9. ВОПРОСЫ ПО APPLY (новый блок)
# ============================================================
apply_questions = [
    {"q": "Как применить лямбда-функцию к колонке 'Height' (перевести метры в сантиметры)?", "a": "df['Height'].apply(lambda x: x * 100)"},
    {"q": "Как создать новую колонку 'Height_cm' с применением лямбда-функции?", "a": "df['Height_cm'] = df['Height'].apply(lambda x: x * 100)"},
    {"q": "Как применить пользовательскую функцию к колонке 'Weight' для создания категорий?", "a": "df['Weight'].apply(categorize_weight)"},
    {"q": "Как применить функцию к нескольким колонкам с использованием axis=1?", "a": "df.apply(calculate_bmi, axis=1)"},
]

# ============================================================
# 10. ВОПРОСЫ ПО PIVOT TABLE (новый блок)
# ============================================================
pivot_questions = [
    {"q": "Как создать сводную таблицу со средним ростом по типам?", "a": "pd.pivot_table(df, values='Height', index='Type1', aggfunc='mean')"},
    {"q": "Как создать сводную таблицу с несколькими колонками и функциями?", "a": "pd.pivot_table(df, values=['Height','Weight'], index='Type1', aggfunc={'Height':['mean','max'], 'Weight':['mean','max']})"},
    {"q": "Как создать двумерную сводную таблицу с индексом 'Type1' и колонками 'Legendary'?", "a": "pd.pivot_table(df, values='Height', index='Type1', columns='Legendary', aggfunc='mean', fill_value=0)"},
]

# ============================================================
# 11. ВОПРОСЫ ПО MERGING (новый блок)
# ============================================================
merging_questions = [
    {"q": "Как объединить две таблицы по колонке 'ID'?", "a": "pd.merge(df1, df2, on='ID')"},
    {"q": "Как сделать inner join при объединении таблиц?", "a": "pd.merge(df1, df2, on='ID', how='inner')"},
    {"q": "Как сделать left join при объединении таблиц?", "a": "pd.merge(df1, df2, on='ID', how='left')"},
    {"q": "Как сделать right join при объединении таблиц?", "a": "pd.merge(df1, df2, on='ID', how='right')"},
    {"q": "Как сделать outer join при объединении таблиц?", "a": "pd.merge(df1, df2, on='ID', how='outer')"},
]

# ============================================================
# ОБЪЕДИНЯЕМ ВСЕ ВОПРОСЫ
# ============================================================
all_questions = (
    series_questions +
    dataframe_questions +
    importing_questions +
    selection_questions +
    filtering_questions +
    aggregation_questions +
    cleaning_questions +
    overview_questions +
    apply_questions +
    pivot_questions +
    merging_questions
)

# ============================================================
# ФУНКЦИИ ТРЕНАЖЕРА
# ============================================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("="*70)
    print("  🐼 ПОЛНЫЙ ТРЕНАЖЕР ПО PANDAS")
    print("  📚 Все разделы конспекта")
    print("="*70)

def print_stats(correct, wrong, total, answered):
    print(f"\n📊 Статистика:")
    print(f"   ✅ Правильно: {correct}")
    print(f"   ❌ Неправильно: {wrong}")
    print(f"   📈 Прогресс: {answered}/{total} ({round(answered/total*100 if total > 0 else 0, 1)}%)")

def get_section(card):
    """Определяет раздел вопроса"""
    if card in series_questions:
        return "⭐ SERIES"
    elif card in dataframe_questions:
        return "⭐⭐ DATA FRAME"
    elif card in importing_questions:
        return "⭐ IMPORTING"
    elif card in selection_questions:
        return "⭐⭐ SELECTION"
    elif card in filtering_questions:
        return "⭐⭐⭐ FILTERING"
    elif card in aggregation_questions:
        return "⭐⭐⭐ AGGREGATION"
    elif card in cleaning_questions:
        return "⭐⭐⭐ DATA CLEANING"
    elif card in overview_questions:
        return "⭐ DATA OVERVIEW"
    elif card in apply_questions:
        return "⭐⭐⭐⭐ APPLY"
    elif card in pivot_questions:
        return "⭐⭐⭐⭐ PIVOT TABLE"
    elif card in merging_questions:
        return "⭐⭐⭐⭐⭐ MERGING"
    else:
        return "❓ НЕИЗВЕСТНО"

def run_training(questions, show_summary=True):
    """Запускает тренировку с переданным списком вопросов"""
    total = len(questions)
    correct = 0
    wrong = []
    
    # Перемешиваем карточки
    shuffled = questions.copy()
    random.shuffle(shuffled)
    
    for i, card in enumerate(shuffled, 1):
        clear_screen()
        print_header()
        print_stats(correct, len(wrong), total, i-1)
        print(f"\n📌 Карточка {i} из {total}")
        print(f"📚 Раздел: {get_section(card)}")
        print("\n" + "-"*70)
        print(f"\n❓ ВОПРОС: {card['q']}")
        print("\n" + "-"*70)
        
        input("Нажмите Enter, чтобы увидеть ответ...")
        
        print(f"\n✅ ОТВЕТ: {card['a']}")
        print("\n" + "-"*70)
        
        # Показываем подсказку для сложных вопросов
        if "pivot_table" in card['a']:
            print("\n💡 Подсказка: pivot_table() - альтернатива groupby")
        elif "apply" in card['a'] and "axis=1" in card['a']:
            print("\n💡 Подсказка: axis=1 применяет функцию к строкам")
        elif "merge" in card['a']:
            print("\n💡 Подсказка: merge() объединяет таблицы по ключу")
        elif "groupby" in card['a']:
            print("\n💡 Подсказка: groupby() группирует по уникальным значениям")
        elif "drop" in card['a'] and "columns" in card['a']:
            print("\n💡 Подсказка: drop(columns=[...]) удаляет колонки")
        elif "fillna" in card['a']:
            print("\n💡 Подсказка: fillna() заменяет пропуски")
        elif "str.lower" in card['a'] or "str.upper" in card['a']:
            print("\n💡 Подсказка: .str - доступ к строковым методам")
        
        while True:
            result = input("\nВы знали этот ответ? (y/n): ").lower()
            if result in ['y', 'n']:
                break
            print("Пожалуйста, введите 'y' или 'n'")
        
        if result == 'y':
            correct += 1
        else:
            wrong.append(card)
        
        if i < total:
            input("\nНажмите Enter для следующей карточки...")
    
    # Показываем результаты
    clear_screen()
    print_header()
    print(f"\n🏆 ТРЕНИРОВКА ЗАВЕРШЕНА!")
    print(f"\n📊 ИТОГИ:")
    print(f"   ✅ Правильно: {correct} из {total}")
    print(f"   ❌ Неправильно: {len(wrong)} из {total}")
    print(f"   📈 Точность: {round(correct/total*100, 1)}%")
    
    # Оценка
    score = round(correct/total*100, 1)
    print("\n" + "="*70)
    if score == 100:
        print("🏆 ИДЕАЛЬНО! Вы мастер Pandas!")
    elif score >= 90:
        print("🌟 ОТЛИЧНО! Вы отлично знаете pandas!")
    elif score >= 75:
        print("💪 ХОРОШО! Есть что повторить, но вы на верном пути!")
    elif score >= 60:
        print("📚 НЕПЛОХО! Повторите сложные разделы и попробуйте снова.")
    else:
        print("📖 НУЖНО ПОВТОРИТЬ! Пройдитесь по конспекту ещё раз.")
    print("="*70)
    
    # Показываем карточки для повторения
    if wrong:
        print("\n📝 КАРТОЧКИ ДЛЯ ПОВТОРЕНИЯ:")
        print("="*70)
        
        # Группируем по разделам для удобства
        wrong_by_section = {}
        for card in wrong:
            section = get_section(card)
            if section not in wrong_by_section:
                wrong_by_section[section] = []
            wrong_by_section[section].append(card)
        
        for section, cards in wrong_by_section.items():
            print(f"\n📚 {section}:")
            for card in cards:
                print(f"\n   ❓ {card['q']}")
                print(f"   ✅ {card['a']}")
    else:
        print("\n🎉 Отличная работа! Все карточки пройдены успешно!")
    
    print("\n" + "="*70)
    
    # Предложение повторить только сложные вопросы
    if wrong and show_summary:
        print("\n🔄 Хотите повторить только те вопросы, которые вызвали трудности?")
        repeat = input("Введите 'y' для повторения или 'n' для выхода: ").lower()
        if repeat == 'y':
            run_training(wrong, show_summary=False)  # Повторяем только сложные
        else:
            print("\nДо свидания! 🚀")
    else:
        print("\nДо свидания! 🚀")
    
    input("\nНажмите Enter для выхода...")

# ============================================================
# ЗАПУСК
# ============================================================
if __name__ == "__main__":
    run_training(all_questions)