import re
def clean_text(text):
    # Заменяем имена и фамилии на '[censored]'
    text = re.sub(r'\b[A-ZА-Я][a-zа-я]+\s[A-ZА-Я][a-zа-я]+\b', '[censored]', text)

    # Заменяем номера телефонов на '[censored]'
    text = re.sub(r'\+\d{11}\b', '[censored]', text)

    # Заменяем данные геолокации на '[censored]'
    text = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', '[censored]', text)

    return text
# Чтение текста из файла
"""file_path = 'secret_letter.txt'  # Укажите путь к вашему файлу
with open(file_path, 'r',encoding="utf-8") as file:
    text = file.read()
# Очистка текста от конфиденциальных данных
cleaned_text = clean_text(text)
# Запись очищенного текста обратно в файл
cleaned_file_path = 'cleaned_file.txt'  # Укажите путь для сохранения очищенного текста
with open(cleaned_file_path, 'w',encoding="utf-8") as file:
    file.write(cleaned_text)
print("Конфиденциальные данные успешно заменены на [censored] и сохранены в файл 'cleaned_file.txt'.")"""
text = "Привет, как дела? Привет! Да, все отлично, спасибо. Как твои дела? Ну, немного устал последние дни, но в целом тоже неплохо. Планируем встретиться на выходных? Нет, cегодня получил звонок от Ивана Петрова. Его номер: +78881231213. Он сообщил о сделке по адресу 123.45.67.89. Странно, Мария Ивановна назначила встречу по тому же адресу."