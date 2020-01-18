class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: str):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        """
        Move the entity by a given amount

        :param int dx: amount to move the entity on the x-axis
        :param int dy: amount to move the entity on the y-axis
        """
        self.x += dx
        self.y += dy