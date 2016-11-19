from nltk.tokenize import RegexpTokenizer

initial_word = 'math'
match_term = 'skills'
word_offset = 6

tokenizer = RegexpTokenizer(r'\w+')


def positive_or_zero(number, offset):
    """Subtract offset from number.
    Return zero if result is less than zero, else return result."""
    if number - offset <= 0:
        out = 0
    else:
        out = number - offset
    return out


def determine_all_locations_with_offset(locations, offset):
    """Get set of locations within range of given offset."""
    out_list = []
    for number in locations:
        out_list.extend(list(range(
            positive_or_zero(number, offset),
            number + offset)))
    return set(out_list)


def colocate_words(word_list, initial_word,
                   search_word, offset, output_words=False):
    initial_locations = []
    for i, word in enumerate(word_list):
        if word.lower() == initial_word.lower():
            initial_locations.append(i)
    all_locations = determine_all_locations_with_offset(initial_locations, offset)

    words_to_search = []
    for location in all_locations:
        if not location >= len(word_list):
            words_to_search.append(word_list[location])
        else:
            words_to_search.append(word_list[-1])

    counter = 0
    for word in words_to_search:
        if word.lower() == search_word.lower():
            counter += 1
    if output_words is False:
        return counter
    else:
        if counter > 0:
            return  words_to_search
        else:
            return False

        
with open('sheet.csv', 'r') as file:
    responses = file.readlines()

occurances = 0
    
for response in responses:
    words = tokenizer.tokenize(response)

    occurances += colocate_words(words, initial_word, match_term, word_offset)

print(occurances)


