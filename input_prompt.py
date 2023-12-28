
class Prompt:
    def __init__(self):
        self.arguments = []

    def get_new_prompt(self, words):
        input_txt = ""
        
        for arg_id, arg in enumerate(words):
            if arg_id != 0:
                input_txt += arg
                input_txt += " "

        return input_txt
