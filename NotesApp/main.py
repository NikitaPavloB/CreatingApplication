import json
import datetime


class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp
        }


class NoteManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_name, "r") as file:
                notes_data = json.load(file)
                notes = [Note(**note_data) for note_data in notes_data]
                return notes
        except FileNotFoundError:
            return []

    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        with open(self.file_name, "w") as file:
            json.dump(notes_data, file)

    def create_note(self, title, body):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(len(self.notes) + 1, title, body, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        return new_note

    def read_notes(self, date_filter=None):
        if date_filter:
            filtered_notes = [
                note for note in self.notes if date_filter in note.timestamp]
        else:
            filtered_notes = self.notes

        for note in filtered_notes:
            print(f"ID: {note.id}")
            print(f"Заголовок: {note.title}")
            print(f"Тело: {note.body}")
            print(f"Дата/время создания: {note.timestamp}\n")

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return
        print("Заметка с указанным ID не найдена.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return
        print("Заметка с указанным ID не найдена.")


def main():
    note_manager = NoteManager("notes.json")

    while True:
        print("Доступные команды:")
        print("1. Создать заметку")
        print("2. Прочитать заметки с фильтрацией по дате")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из программы")
        choice = input("Введите номер команды: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            note_manager.create_note(title, body)
            print("Заметка успешно создана!")
        elif choice == "2":
            date_filter = input("Введите дату фильтрации (гггг-мм-дд): ")
            note_manager.read_notes(date_filter)
        elif choice == "3":
            note_id = int(
                input("Введите ID заметки, которую хотите отредактировать: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            note_manager.edit_note(note_id, new_title, new_body)
            print("Заметка успешно отредактирована!")
        elif choice == "4":
            note_id = int(
                input("Введите ID заметки, которую хотите удалить: "))
            note_manager.delete_note(note_id)
            print("Заметка успешно удалена!")
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
