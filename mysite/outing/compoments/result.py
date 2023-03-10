
class Result:
    message = ""
    code = 200
    data = {}

    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data
