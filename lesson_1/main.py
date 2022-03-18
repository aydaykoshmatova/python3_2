class Car:

    def __init__(self, title, model, color):
        self.title = title
        self.model = model
        self.color = color

    # """поведение - Method (def)"""

    def start_engine(self):
        print(f"On {self.title} {self.model} engine started!")


""""Instance """

bmw = Car('BMW', 'e38', 'blue')
print(
    f"Title: {bmw.title}\n Model: {bmw.model}\n Color: {bmw.color}"
)

