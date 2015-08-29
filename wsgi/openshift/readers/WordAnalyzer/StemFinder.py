import os, time

def word_ref(base, editted, ref):
#Returns the base word if the
#editted word is not contained in the reference
    if editted in ref:
        return editted
    else:
        return base

def getStem(word, all_words, irregular):
    if len(word) < 4 or word not in all_words:
    #Words of length three or less are stems
        return word
    else:
    #Check for special cases
        if word in irregular.keys():
            return irregular[word]

    #Handles apostrophes. cat's -> cat
    if word[-2:] == "'s":
        word = word[:-2] + word[-1]
    if word[-2:] == "s'":
        word = word[:-1]

    #Creates the checkStem function to evaluate whether a stemmed
    #word is a real word. If it isn't, returns the original word
    checkStem = lambda x: word_ref(word, x, all_words)

    if word[-1] == 's':
        if word[-4:] == 'ness' and len(word) > 4:
            #Requiring word greater than 4 because Ness is also a proper noun
            #Words ending in ness should have the ness removed
            #Example: happiness -> happy
                if word[-5] == 'i' and word[:-4] not in all_words:
                    return checkStem(word[:-5] + 'y')
                return checkStem(word[:-4])
        if word[-2] == 'e':
            if word[-3] == 'i' and len(word) > 4:
            #words ending in ies -> y example babies -> baby
                return checkStem(word[:-3] + 'y')
            #Words ending in 'es' are plural if preceeded by ch, s or x
            if word[-3] in ['s', 'x'] or word[-4:][:-2] == 'ch':
                if word[-3] == 'v':
                    word[-3] = 'f'
                if word[-3] in ['c', 'z']:
                    return checkStem(word[:-1])
                return checkStem(word[:-2])
        if word[-2] != 's':
        #Words with double 's' like pass are not plural
            return checkStem(word[:-1])
        return word

    if word[-2:] == 'ae':
        return checkStem(word[:-1])

    if word[-2:] == 'ly':
    #Example: quickly -> quick
        if word[:-2][-3:] == 'ing' and len(word) > 6:
        #Removes 'ing' from back of word, one extra in case of stem change
        #Example: bedding -> bed, frying -> fry
            return checkStem(word[:-5])
        return checkStem(word[:-2])

    if word[-2:] == 'ed':
    #Removes ed from back of word, expect in case of stem change
    #Example: talked -> talk, stopped -> stop, freed -> free
        if word[-3] in ['e', 'o', 'y'] and word[:-1] in all_words:
            return checkStem(word[:-1])
        if word[-3] == word[-4]:
            return checkStem(word[:-3])
        if word[-4:][:2] == "ck" and word[:-2] not in all_words:
        #Picnicked -> picnic but licked -> lick
            return checkStem(word[:-3])
        if word[:-1] in all_words:
            return checkStem(word[:-1])
        return checkStem(word[:-2])

    if word[-3:] == 'ing' and len(word) > 4:
    #Removes 'ing' from back of word, one extra in case of stem change
    #Example: bedding -> bed, frying -> fry
        if word[-5] == word[-4] and word[:-3] not in all_words:
            return checkStem(word[:-4])
        if word[-5:][:2] == "ck" and checkStem(word[:-4]) != word:
        #Picnicking-> picnic but licking -> lick
            return checkStem(word[:-4])
        if word[-5:][:2] == "it":
            return checkStem(word[:-3] + 'e')
        if word[:-3] + 'e' in all_words:
            return checkStem(word[:-3] + 'e')
        return checkStem(word[:-3])
    return word

def test_stem(word, all_words, irregular):
    stime = time.time()
    getStem(word, all_words, irregular)
    return time.time() - stime
