from turtle import*              # turtle 모듈에서 모든것을 불러온다
class Ball:                      # class를 선언한다
    def __init__(self, color, size, speed): # __init__을 사용해
                                            # self, speed, color, model라고 하는 속성을 초기화하여 클래스에 부여한다

        self.x = 0                          # 공의 x좌표를 0으로 둔다
        self.y = 0                          # 공의 y좌표를 0으로 둔다
        self.xspeed = speed                 # 공의 x좌표의 이동 속도를 xspeed라는 동작을 사용해 변수 speed에 저장한다 
        self.yspeed = speed                 # 공의 y좌표의 이동 속도를 yspeed라는 동작을 사용해 변수 speed에 저장한다 
        self.size = size                    # size라는 동작에 대한 변수 값은 size이다 

        self.color = color                  
        self.turtle= Turtle()               # 클래스 안에 거북이 객체를 생성하여 저장한다
        self.turtle.shape("circle")         # 거북이의 모양을 원 모양으로 한다
        self.turtle.color(color)            # 거북이의 색을 color라는 동작,속성을 활용해 표현한다
        self.turtle.resizemode("user")      
        self.turtle.shapesize(size, size, 10)     
        
    def move(self):                         # drive라는함수에 self라는 속성을 부여한다      
        self.x  += self.xspeed              # 기존의 x좌표인 0에 추가되는 값을 더해간다    
        self.y  += self.yspeed              # 기존의 y좌표인 0에 추가되는 값을 더해간다
        self.turtle.goto(self.x , self.y)

ball = Ball("red",2,1)                      # 색상은 red, size는 2, 이동속도를 2로 설정한다.
for i in range(100):                        # 아래의 내용을 100번 반복한다 
    ball.move()                             # 공을 움직이는 메소드인 move()를 활용한다  
