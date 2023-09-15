import json
import datetime

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
