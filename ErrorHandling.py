class InvalideFunctionArg(Exception):
    """Exception raised when the argument of a function is not a valade argument"""

    def __init__(self, invaladeArgument, value, expected):
        #super().__init__(invaladeArgument, value, expected)
        self.invaladeArgument = invaladeArgument
        self.value = value
        self.expected = expected

    def __str__(self):
            return f"Argument {self.invaladeArgument} recived incorrect value | expected: ({self.expected}) | recived: ({self.value})"
