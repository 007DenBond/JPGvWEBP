import base64

# Название твоего файла с логотипом
filename = "DenBOND_logo.png" 

try:
    with open(filename, "rb") as image_file:
        # Читаем файл и кодируем в base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
    # Сохраняем огромный кусок текста в файл, чтобы удобно скопировать
    with open("logo_code.txt", "w") as text_file:
        text_file.write(encoded_string)
        
    print("✅ Успех! Код логотипа сохранен в файл 'logo_code.txt'.")
    print("Открой его, скопируй всё содержимое и жди Шаг 2.")
except FileNotFoundError:
    print(f"❌ Ошибка: Файл '{filename}' не найден в этой папке.")