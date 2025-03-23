def number_of_words(booktext):
    words = booktext.split()
    return len(words)

def character_count(booktext):
    characters = {}

    for character in booktext:
        character = character.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    return characters
            
def sorted_characters(character_dictionary):
    sorted_list = []
    for character in character_dictionary:
        sorted_list.append({"character": character, "count": character_dictionary[character]})
    sorted_list.sort(reverse=True, key=lambda item: item["count"])
    return sorted_list