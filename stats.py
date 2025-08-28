def get_num_words(text:str):
    return len(text.split())


def get_num_chars(text: str) -> dict[str, int]:
    char_map = dict()

    for word in text.split():
        letters = list(word)

        for l in letters:
            if l.lower() in char_map:
                char_map[l.lower()] += 1
            else:
                char_map[l.lower()] = 1

    return char_map


def sort_char_counts(char_count: dict[str, int]) -> list[dict[str, int]]:
    sorted_list = []

    for c in char_count:
        sorted_list.append({ "char": c, "count": char_count[c]})

    sorted_list.sort(reverse=True, key=lambda item: item['count'])
    return sorted_list