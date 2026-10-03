class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width  * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
     
    def get_diagonal(self):
        return (self.width** 2 + self.height ** 2 ) ** 0.5 
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else: 
            picture = ""
            for i in range(self.height):
                for j in range(self.width):
                    picture += "*"
                picture += "\n"
            return picture

    def get_amount_inside(self, shape):
        max_width = self.width // shape.width
        max_height = self.height // shape.height
        return max_width * max_height
        
class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side) 
        self.side = side

    def __str__(self):
            return f"Square(side={self.width})"

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
    
    def set_side(self, side):
        self.height = side
        self.width = side
        self.side = side


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    rect2 = Rectangle(3, 6)
    print(rect.get_picture())

    print(Rectangle(3, 52).get_picture())
    Rectangle(15,10).get_amount_inside(Square(5))
    Rectangle(4,8).get_amount_inside(Rectangle(3, 6))
    Rectangle(2,3).get_amount_inside(Rectangle(3, 6))

    print(Rectangle(15,10).get_amount_inside(Square(5)))
    print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
    print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))