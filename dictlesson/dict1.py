TRAN_DICT = {"Привет": "Hi", "Пока": "Bye", "Как": "How", "Что": "what", "кто": "who", "кошка": "Cat", "собака": "dog",
             "животное": "pet", "Я": "I", "ты": "you"}
ERROR_MSG = 'Не найдено'
def find_word_by_key(word: str) -> str:
    try:
        return TRAN_DICT[word]
    except Exception:
        return ERROR_MSG
    
def find_word_by_val(word: str) -> str:
    for k, v in TRAN_DICT.items():
        if v == word: return k
    return ERROR_MSG

def reverse_dict() -> dict:
    new = dict()
    for k, v in TRAN_DICT.items():
        new[v] = k
    return new
print(reverse_dict())