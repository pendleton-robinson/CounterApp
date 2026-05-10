class CounterModel:
    def __init__(self):
        self.value = 0

    def increment(self, amount):
        self.value += amount

    def decrement(self, amount):
        self.value -= amount

    def getValue(self):
        return self.value