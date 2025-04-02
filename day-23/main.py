import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

# car_count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    CarManager.create_car()
    CarManager.move_cars()

    # car_count += 1
    # if car_count == 6:
    #     car = CarManager()
    #     car.move()
    #     car_count = 0
    


# 3. 거북이와 자동차의 충돌이 감지되면 게임을 멈추세요. 
# 풀다가 막히면, 5단계 설명 영상을 확인해 보세요.

# 4. 거북이가 화면의 위쪽 가장자리(즉, FINISH_LINE_Y)에 도달했는지 감지하고, 
# 도달했다면 거북이를 시작 위치로 다시 보내고 자동차의 속도를 올리세요. 
# 힌트) MOVE_INCREMENT 속성을 만들어서 자동차 속도를 증가시켜 보세요. 
# 풀다가 막히면, 6단계 풀이 영상을 확인해 보세요.

# 5. 현재 게임 레벨을 보여주는 점수판을 만드세요. 
# 거북이가 성공적으로 길을 건널 때마다 레벨이 올라갑니다. 
# 거북이와 자동차가 부딪히면 화면 중앙에 ‘게임 종료’가 표시되어야 합니다. 
# 풀다가 막히면, 7단계 설명 영상을 확인해 보세요.