def remove(text: str) -> str:
    # Удаляет все гласные из строки (рус и англ)
    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
    return "".join(char for char in text if char not in vowels)
