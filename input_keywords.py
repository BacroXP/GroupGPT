import random

class Keyword:
    def __init__(self, file_path):
        self.file_path = file_path
        self.keywords = {}

    def get_keywords_from_file(self):
        keyword_file = open(self.file_path).read()
        keywords_raw = keyword_file[:-1].split("$")

        for id in keywords_raw:
            keyword, value = id.split(">")
            self.keywords[keyword] = float(value)
    
    def write_keywords_to_file(self):
        with open(self.file_path, "w") as file:
            keyword_string = ""
            for keyword, value in self.keywords.items():
                keyword_string += f"{keyword}>{value}$"

            file.write(keyword_string)

    def revalue(self, words):
        self.get_keywords_from_file()

        for word in words:
            self.keywords[word] += random.uniform(-1, 1) / 10
            self.keywords[word] = abs(self.keywords[word])
    
    def get_value(self, word):
        return self.keywords[word]

    def reset(self):
        open(self.file_path, "w").write("")
