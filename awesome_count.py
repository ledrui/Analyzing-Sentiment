def awesome_count(dicts):
    """" Count the number of occurence of the word on the dict"""
    #print dicts
    
    result = 0
    word = 'for'
    for dict in dicts:
        print dict
        for words in dict:
            #print words
            if word in dict:
                result = dict[word]
                #yield dict[word]
                print dict[word]
            else:
                result = 0
                #yield 0
                print 0
            
            #print result
        continue

dicts = [{'and': 3, 'love': 1, 'it': 2, 'highly': 1, 'osocozy': 1, 
'bags': 1, 'holder.': 1, 'moist': 1, 'does': 1, 'recommend': 1, 'was': 1, 'wipes': 1, 'it.': 1, 
'early': 1, 'disappointed.': 1, 'not': 2, 'now': 1, 'wipe': 1, 'keps': 1, 'wise': 1, 'i': 1, 
'leak.': 1, 'planet': 1, 'my': 2, 'came': 1}

{'and': 2, 'quilt': 1, 'it': 1, 'comfortable': 1, 'warmer': 1, 'size': 1, 'anyone': 1, 
'for': 1, 'looking': 1, 'to': 1, 'recommend': 1, 'type': 1, 'full': 1, 'very': 1, 'looks...fit': 1, 
'than': 1, 'perfectly...would': 1, 'this': 1, 'of': 1, 'bed': 1, 'the': 1, 'soft': 1}

{'ingenious': 1, 'and': 3, 'love': 2, 'positive,': 1, 'is': 4, 'it': 1, 'losing': 1, 'fairy.': 1,
 'have': 1, 'in': 2, 'rid': 1, 'what': 1, 'her': 1, 'how': 1, 'to': 1, 'much': 1, 'has': 1, 
 'approach': 2, 'worth': 1, 'she': 1, 'tool.': 1, 'product': 2, 'clever': 1, 'chart': 1, 
 'else': 1, 'most': 1, 'artwork,': 1, 'ownership': 1, 'not': 1, 'little': 1, 'purchase.': 1,
'herself,': 1, 'a': 2, 'about': 1, 'daughter': 1, 'like': 1, 'anything': 1, 'getting': 1, 
'this': 3, 'of': 3, 'proud': 1, 'well': 1, 'this,': 1, 'i': 3, 'back,': 1, 'so': 1, 'binky.': 2, 
'loves': 1, 'found': 1, 'the': 7, 'my': 1}

{'and': 2, 'parents!!': 1, 'all': 2, 'puppet.': 1, 'help': 1, 'cried': 1, 'is': 3, 
'it': 1, 'soo': 1, 'rock!!': 1, 'way': 1, 'have': 1, 'pacifier': 1, 'my': 1, 'your': 1, 
'tried': 1, 'from': 1, 'for': 2, 'their': 2, 'when': 1, 'to': 5, 'going': 1, 'easy': 1, 
'pacifier,': 1, 'you': 2, 'save': 1, 'until': 1, "love's": 1, 'book!': 1, 'them': 4, 'buy': 1, 'ween': 1, 
'book,': 1, 'part': 1, 'understand': 1, 'it.this': 1, 'binky': 1, 'an': 1, 'with': 1, 'must': 1, 'a': 2, 
'great': 1, 'kids': 2, 'off': 1, 'gift': 1, 'this': 1, 'many': 1, 'work': 1, 'non-stop': 1, 'thumbuddy': 1, 
'will': 1, 'i': 2, 'expecting': 1, 'allow': 1, 'of': 1, 'found': 1, 'fairy': 1, 'where': 1, 'headaches.thanks': 1}

{'and': 2, 'cute': 1, 'help': 2, 'doll': 1, 'is': 2, "didn't": 1, 'it': 1, 'house,': 1, 'highly': 1, 
'product': 1, 'have': 1, 'pacifier': 1, 'comes.': 1, 'your': 1, 'special': 1, 'happens': 1, 'what': 1, 
'thumb': 1, 'would': 1, 'to': 6, 'lots': 1, 'explain': 1, 'when': 2, 'habit.': 1, 'any': 2, 'how': 1, 'book': 2, 
'item.': 1, 'recommend': 1, 'pacifier.': 1, 'adorable': 1, 'we': 2, 'sucking': 1, 'parent': 1, 'our': 2, 'stop': 1, 
'great': 1, 'movies': 1, 'break': 1, 'job': 1, 'important': 1, 'child': 1, 'telling': 1, 'using': 1, 
'binky': 3, 'trying': 1, 'with': 1, 'the': 6, 'a': 2, 'loss': 1, 'about': 2, 'made': 1, 'daughter': 1, 
'her': 1, 'gift': 1, 'i': 1, 'of': 2, 'favorite': 1, 'their': 1, 'this': 2, 'prepare': 1, 'does': 1, 
'fairy': 3, 'or': 1, 'came': 1, 'for': 2}
]