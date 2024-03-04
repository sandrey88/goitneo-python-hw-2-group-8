contacts = {}

# Обробка вводу.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Додавання нового контакту в пам'ять.
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Додавання в пам'ять нового номеру телефону для контакту, що вже існує.
def change_contact(args):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

# Вивід у консоль номеру телефону для зазначеного контакту.
def show_phone(args):
    name = args[0]
    phone = contacts.get(name)
    return phone if phone else "Contact not found."

# Вивід у консоль всіх збережених контактів з номерами телефонів.
def show_all():
    if not contacts:
        return "No contacts found."
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

# Основна функція зі всією логікою взаємодії з користувачем.
def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")

# Запуск основної функції.
if __name__ == "__main__":
    main()