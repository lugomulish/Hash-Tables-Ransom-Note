def ransom_note(magazine, ransom):
    hash_words = {}

    # Create the hash tabled with the words on the
    # magazine and put the number of occurrence in the value.
    for m_word in magazine:
        if hash_words.get(m_word) != None:
            if (hash_words[m_word] > 0):
                hash_words[m_word] += 1
        else:
            hash_words[m_word] = 1

    # Check if exist the word in the hash table
    for r_word in ransom:
        if hash_words.get(r_word) is None or hash_words[r_word] == 0:
            return False
        else:
            hash_words[r_word] -= 1

    return True


m = "Put you text1 here"
n = "Put you text2 here"
magazine_list = m.split(' ')
ransom_list = n.split(' ')
answer = ransom_note(magazine_list, ransom_list)

if answer:
    print "Yes"
else:
    print "No"
