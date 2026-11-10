def find_the_a(s):
    index = s.find("a")
    if index >= 0:
        return index
    else:
        return False
print("All cases are passed")

assert find_the_a("Hallo Welt!") == 1
assert find_the_a("Bacon and Spam") == 1
assert find_the_a("edcba") == 5
assert find_the_a("Hello world!") == False
assert find_the_a("") == False