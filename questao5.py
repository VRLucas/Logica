def inverte_string(string):
    inverted_string = ""
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

# Testando com a string "hello"
string_invertida = inverte_string("hello")
print(string_invertida)
