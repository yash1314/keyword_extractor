class utilities:
    def __init__(self):
        pass

    def sentence_count(self, text):
        sentences = text.split(".")
        return len(sentences[:-1])

    def word_count(self, text):
        words = text.split(" ")
        return len(words)

    def paragraph_count(self, text):
        paragraph = text.split("\n")
        return len(paragraph)


