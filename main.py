from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)
        if  not (isinstance(value, str) and value.isdigit() and len(value) == 10):
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        return self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            return self.phones.remove(phone_obj)


    def edit_phone(self, phone, new_phone):
        if self.find_phone(phone):
            self.add_phone(new_phone)
            return self.remove_phone(phone)
        else:
            raise ValueError


    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


    def find(self, name) -> Record:
        if name in self.data:
            return self.data[name]


    def delete(self, name):
        self.data.pop(name)
        return


    def __str__(self):
        return '\n'.join(f'{self.data[item]}' for item in self.data)


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
# john.remove_phone("1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")
