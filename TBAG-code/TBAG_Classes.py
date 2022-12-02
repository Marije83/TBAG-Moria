class Scene():
    def __init__(self, scene_name, opener = "", win_closer = "", loose_closer = "", alternative_closer = ""):
        self.name = scene_name
        self.opener = opener
        self.win_closer = win_closer
        self.loose_closer = loose_closer
        self.alternative_closer = alternative_closer
        

    def print_opener(self):
        print(self.opener)

    def set_opener(self, opener):
        self.opener = opener

    def print_win_closer(self):
        print(self.win_closer)
    
    def set_win_closer(self, win_closer):
        self.win_closer = win_closer

    def print_loose_closer(self):
        print(self.loose_closer)
    
    def set_loose_closer(self, loose_closer):
        self.loose_closer = loose_closer

    def print_alternative_closer(self):
        print(self.alternative_closer)
    
    def set_alternative_closer(self, alternative_closer):
        self.alternative_closer = alternative_closer

    # requires user to press enter before continuing in the programme.
    def continue_enter (self):
        input("\nPress enter to continue\n")


class Question():
    def __init__(self, question_name):
        self.name = question_name
        self.text = None
        self.possible_answers = []
        self.answer = None
        self.validity = False

    def get_text(self):
        return self.text

    def print_text(self):
        print(self.text)

    def set_text(self, question_text):
        self.text = question_text
    
    def set_answer(self):
       self.answer = input("> ").lower()   

    def get_answer(self):
        return self.answer

    def check_answer_validity(self, possible_answers):
        self.possible_answers = possible_answers
        if self.answer in possible_answers:
            return True
        else:
            return False
