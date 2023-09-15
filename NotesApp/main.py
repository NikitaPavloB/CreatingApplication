from note_manager import NoteManager


def main():
    note_manager = NoteManager("notes.json")

    while True:
        print("Доступные команды:")
        print("1. Создать заметку")
        print("2. Прочитать заметки с фильтрацией по дате")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Просмотреть заметку по ID")
        print("6. Просмотреть все заметки")
        print("7. Выйти из программы.\n")

        choice = input("Введите номер команды: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            note_manager.create_note(title, body)
            print("Заметка успешно создана!\n")

        elif choice == "2":
            date_filter = input("Введите дату фильтрации (гггг-мм-дд): ")
            note_manager.read_notes(date_filter)

        elif choice == "3":
            note_id = int(
                input("Введите ID заметки, которую хотите отредактировать: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            note_manager.edit_note(note_id, new_title, new_body)
            print("Заметка успешно отредактирована!\n")

        elif choice == "4":
            note_id = int(
                input("Введите ID заметки, которую хотите удалить: "))
            note_manager.delete_note(note_id)
            print("Заметка успешно удалена!\n")

        elif choice == "5":
            note_id = int(input("Введите ID заметки для просмотра:"))
            note_manager.view_note(note_id)
            print("\n")

        elif choice == "6":
            print("Список всех заметок:\n")
            note_manager.view_all_notes()
            print("\n")

        elif choice == "7":
            print("Программа завершена.")
            print("\n")
            break

        else:
            print("Неверная команда. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
