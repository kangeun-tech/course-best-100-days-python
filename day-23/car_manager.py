from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# position = (260, random.randrange(-280, 280))


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    # def __init__(self):
    #     super().__init__()
    #     self.shape("square")
    #     self.color(random.choice(COLORS))
    #     self.shapesize(stretch_wid=1, stretch_len=2)
    #     self.penup()
    #     self.goto(position)
    
    # def move(self):
    #     new_x = self.xcor() - MOVE_INCREMENT
    #     new_y = self.ycor()
    #     self.goto(new_x, new_y)
        

  
