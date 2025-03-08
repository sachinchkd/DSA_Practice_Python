def word_count(String):
    count = 0
    for i in range(len(String)):
        if(String[i] == " "):
            count += 1
    return count+1

2
def word_frequencies(word, String):
    word_match_count = 0
    for i in range(word_count(String)-1):
        if(word == String.split(" ")[i]):
            word_match_count += 1

    return word_match_count

String = "Ram is bad boy. Ram is Ram and ram is shyam."
word = "Ram"
print(word_frequencies(word,String))

