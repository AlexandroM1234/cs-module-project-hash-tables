def word_count(s):
    # Your code here
    word_count = {}

    list_word =  s.split()

    bad_word = r'" : ; , . - + = / \ | [ ] { } ( ) * ^ &'

    for word in list_word:
        lowercase = word.lower()
        if lowercase in bad_word:
            pass
        if lowercase not in word_count:
            word_count[lowercase] = 1
        else:
            word_count[lowercase] += 1
    return word_count

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))