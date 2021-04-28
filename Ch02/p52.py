oneLine = "this is one line string"
print("t 글자수 :", oneLine.count("t"))

print(oneLine.startswith("this"))
print(oneLine.startswith("that"))

print(oneLine.replace("this", "that"))

multiLine = """this is
multi line
string"""
sent = multiLine.split("\n")
print("문장 :",sent)

words = oneLine.split(" ")
print("단어 :", words)

sent2 = ", ".join(words)
print(sent2)