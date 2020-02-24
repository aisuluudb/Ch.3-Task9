def reverse_sentence (text):
    for t in text.split():
        return(' '.join(text.split()[::-1]))
print (reverse_sentence("Today   is   a   big day"))

#separate each wotd of a string to be able to read any word separately (bringing it to the list)
#read each word separately as by indexes from the end
#and then join back words to a string
