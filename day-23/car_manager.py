from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# position = (260, random.randrange(-280, 280))

# 💡 Turtle을 상속하지 않은 이유: 하나가 아닌 '여러' 자동차를 관리하는 매니저 클래스이기 때문. 자동차 하나는 Turtle 인스턴스로 만들고, CarManager는 그런 자동차를 리스트로 모아 관리함
class CarManager():
    def __init__(self):
        # 💡 리스트에 저장하는 이유: 차를 매 루프마다 움직이게 하기 위하여.
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # 💡 self.car가 아니라 new_car인 이유: create_car() 함수 안에서 만든 자동차는 잠깐 생성되는 임시 변수임. 이걸 리스트에 넣고 관리하니까 이름은 new_car처럼 써도 됨. 
            # 💡 self.car라고 하면, 마지막으로 생성된 자동차만 저장되고 이전에 만든 애들은 다 사라짐. self.all_cars.에 넣을거니까 new_car로.
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
        

  
