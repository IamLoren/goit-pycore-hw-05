# Завдання 4: Консольний бот-помічник

Консольний бот для управління контактами з обробкою помилок через декоратори.

## Функціональність

Бот підтримує наступні команди:

- `hello` - Привітання від бота
- `add [ім'я] [телефон]` - Додати новий контакт
- `change [ім'я] [телефон]` - Змінити телефон існуючого контакту
- `phone [ім'я]` - Показати телефон контакту
- `all` - Показати всі збережені контакти
- `close` або `exit` - Вийти з програми

## Обробка помилок

Всі помилки введення обробляються декоратором `input_error`, який:

- Перехоплює винятки `KeyError`, `ValueError`, `IndexError`
- Повертає зрозумілі повідомлення про помилки
- Не зупиняє виконання програми

## Приклад використання

```bash
python task_4.py
```

### Діалог з ботом:

```
Welcome to the assistant bot!
Enter a command: hello
How can I help you?

Enter a command: add
Enter the argument for the command

Enter a command: add Bob
Enter the argument for the command

Enter a command: add Jime 0501234356
Contact added.

Enter a command: add Alice 0671234567
Contact added.

Enter a command: phone
Enter the argument for the command

Enter a command: phone Jime
0501234356

Enter a command: phone Unknown
Contact not found.

Enter a command: all
Jime: 0501234356
Alice: 0671234567

Enter a command: change Jime 0509999999
Contact updated.

Enter a command: phone Jime
0509999999

Enter a command: close
Good bye!
```

## Технічні деталі

### Декоратор input_error

Декоратор обробляє три типи помилок:

1. **ValueError** - недостатня кількість аргументів

   - Повідомлення: "Enter the argument for the command"

2. **IndexError** - відсутні обов'язкові аргументи

   - Повідомлення: "Enter the argument for the command"

3. **KeyError** - контакт не знайдено
   - Повідомлення: "Contact not found."

### Функції

- `add_contact(args, contacts)` - Додає новий контакт
- `change_contact(args, contacts)` - Змінює телефон існуючого контакту
- `show_phone(args, contacts)` - Показує телефон контакту
- `show_all(args, contacts)` - Показує всі контакти
- `parse_input(user_input)` - Парсить введення користувача

Всі функції-обробники команд обгорнуті декоратором `@input_error`.
