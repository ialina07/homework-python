def build_tree(text):
    """Строим дерево Хаффмана"""
    if not text:
        return None

    # Считаем частоты символов
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Делаем список узлов: (символ, частота, левый, правый)
    nodes = [(char, f, None, None) for char, f in freq.items()]

    # Строим дерево
    while len(nodes) > 1:
        # Сортируем по возрастанию частот
        nodes.sort(key=lambda x: x[1])

        # Берем два самых частых
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Создаем родителя
        parent = (None, left[1] + right[1], left, right)
        nodes.append(parent)

    return nodes[0] if nodes else None


def build_codes(node, code="", codes=None):
    """Строим таблицу кодов"""
    if codes is None:
        codes = {}

    if node is None:
        return codes

    # Если это лист (есть символ)
    if node[0] is not None:
        codes[node[0]] = code if code else "0"
        return codes

    # Идем в левого и правого потомка
    build_codes(node[2], code + "0", codes)  # left
    build_codes(node[3], code + "1", codes)  # right

    return codes


def encode(text):
    """Кодируем текст"""
    if not text:
        return "", {}

    tree = build_tree(text)
    codes = build_codes(tree)

    encoded = ''.join(codes[char] for char in text)
    return encoded, codes


def decode(encoded, codes):
    """Декодируем текст"""
    if not encoded or not codes:
        return ""

    # Делаем обратную таблицу
    reverse = {code: char for char, code in codes.items()}

    result = []
    current = ""

    for bit in encoded:
        current += bit
        if current in reverse:
            result.append(reverse[current])
            current = ""

    return ''.join(result)


def serialize_table(codes):
    """Упаковываем таблицу в байты"""
    # Формат: каждый символ записываем как [длина:1 байт][символ в utf-8][код]
    table_data = bytearray()

    for char, code in codes.items():
        # Кодируем символ в UTF-8
        char_bytes = char.encode('utf-8')

        # Записываем длину символа (1 байт)
        table_data.append(len(char_bytes))

        # Записываем сам символ
        table_data.extend(char_bytes)

        # Записываем длину кода (1 байт)
        table_data.append(len(code))

        # Записываем код (биты как байты)
        # Дополняем код нулями до кратного 8
        code_padded = code + '0' * (8 - len(code) % 8) if len(code) % 8 != 0 else code
        for i in range(0, len(code_padded), 8):
            byte_str = code_padded[i:i + 8]
            table_data.append(int(byte_str, 2))

    return table_data


def deserialize_table(table_data):
    """Распаковываем таблицу из байтов"""
    codes = {}
    i = 0

    while i < len(table_data):
        # Читаем длину символа
        char_len = table_data[i]
        i += 1

        # Читаем символ
        char_bytes = table_data[i:i + char_len]
        char = char_bytes.decode('utf-8')
        i += char_len

        # Читаем длину кода
        code_len = table_data[i]
        i += 1

        # Читаем код
        code_bits = []
        bytes_needed = (code_len + 7) // 8  # Округляем вверх до целых байтов

        for j in range(bytes_needed):
            byte = table_data[i]
            i += 1
            # Конвертируем байт в 8 битов
            bits = format(byte, '08b')
            code_bits.append(bits)

        # Объединяем биты и обрезаем до нужной длины
        full_code = ''.join(code_bits)
        code = full_code[:code_len]

        codes[char] = code

    return codes


def bits_to_bytes(bits):
    """Преобразуем битовую строку в байты"""
    padding = 8 - len(bits) % 8
    if padding == 8:
        padding = 0

    # Добавляем нули в конец
    bits += '0' * padding

    # Конвертируем в байты
    bytes_data = bytearray()
    for i in range(0, len(bits), 8):
        byte_str = bits[i:i + 8]
        bytes_data.append(int(byte_str, 2))

    return bytes_data, padding


def bytes_to_bits(bytes_data, padding):
    """Преобразуем байты в битовую строку"""
    bits = ""
    for byte in bytes_data:
        bits += format(byte, '08b')

    # Убираем добавленные нули
    if padding > 0:
        bits = bits[:-padding]

    return bits


def encode_file(input_file, output_file):
    """Кодируем файл с сохранением таблицы"""
    try:
        # Пытаемся прочитать как текстовый файл
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except:
        # Если не получается, читаем как бинарный
        with open(input_file, 'rb') as f:
            binary_data = f.read()
            # Преобразуем бинарные данные в строку для обработки
            text = ''.join(chr(byte) for byte in binary_data)

    # Кодируем текст
    encoded_bits, codes = encode(text)

    # Упаковываем таблицу в байты
    table_data = serialize_table(codes)

    # Преобразуем закодированные биты в байты
    encoded_bytes, padding = bits_to_bytes(encoded_bits)

    # Записываем в выходной файл
    with open(output_file, 'wb') as f:
        # 1. Заголовок: размер таблицы (4 байта)
        f.write(len(table_data).to_bytes(4, byteorder='big'))

        # 2. Сама таблица
        f.write(table_data)

        # 3. Количество padding битов (1 байт)
        f.write(padding.to_bytes(1, byteorder='big'))

        # 4. Закодированные данные
        f.write(encoded_bytes)

    print(f"Файл '{input_file}' успешно закодирован в '{output_file}'")


def decode_file(input_file, output_file):
    """Декодируем файл, читая таблицу из заголовка"""
    with open(input_file, 'rb') as f:
        # 1. Читаем размер таблицы
        table_size = int.from_bytes(f.read(4), byteorder='big')

        # 2. Читаем таблицу
        table_data = f.read(table_size)
        codes = deserialize_table(table_data)

        # 3. Читаем количество padding битов
        padding = int.from_bytes(f.read(1), byteorder='big')

        # 4. Читаем закодированные данные
        encoded_bytes = f.read()

    # Преобразуем байты в биты
    encoded_bits = bytes_to_bits(encoded_bytes, padding)

    # Декодируем
    decoded_text = decode(encoded_bits, codes)

    # Пытаемся определить, был ли исходный файл текстовым или бинарным
    try:
        # Пробуем записать как текстовый файл
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decoded_text)
    except:
        # Если не получается, записываем как бинарный
        with open(output_file, 'wb') as f:
            # Преобразуем строку обратно в байты
            binary_data = bytes(ord(char) for char in decoded_text)
            f.write(binary_data)

    print(f"Файл '{input_file}' успешно декодирован в '{output_file}'")
