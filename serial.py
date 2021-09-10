"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "Increment starting from start"
        self.start = start
        self.increment = 0
        
    def generate(self):
        "Increments 1"
        num = self.start
        num += self.increment
        self.increment += 1
        return num
    def reset(self):
        "Resets the return value to start"
        self.increment = 0