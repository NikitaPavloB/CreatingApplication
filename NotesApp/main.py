import json
import datetime

# Функция для создания новой заметки


def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp,
    }
    notes.append(note)
    save_notes()
    print("Заметка успешно создана!")

# Функция для сохранения заметок в файл JSON


def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

# Главная функция


def main():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    while True:
        print("Доступные команды:")
        print("1. Создать заметку")
        print("2. Прочитать заметки с фильтрацией по дате")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из программы")
        choice = input("Введите номер команды: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
