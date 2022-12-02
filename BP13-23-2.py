from turtle import*                             # turtle 모듈에서 모든것을 불러온다
class Car:                                      # 클래스를 선언한다
    def __init__(self, speed, color, model):    # __init__를 사용하여 self, speed, color, model라고 하는 속성을 초기화하여 클래스에 부여한다
        self.speed = speed                      # speed라는 속성에 대한 변수 값 speed라 정의한다 
        self.color = color                      # color라는 속성에 대한 변수 값을 color라 정의한다 
        self.model = model                      # model라는 속성에 대한 변수 값을 model라 정의한다 
        self.turtle = Turtle()                  # 클래스 안에 거북이 객체를 생성하여 저장한다
        self.turtle.shape("c:/car.gif")         # 거북이의 모양을 c드라이브의 car.gif로 저장한다

    def drive(self):                            # drive라는함수에 self라는 속성을 부여한다   
        self.turtle.forward(self.speed)         # turtle 객체는 동작인 self.speed만큼 속성forward에 의해 앞으로 직진한다

    def left_turn(self):                        # left_turn이라는함수에 self라는 속성을 부여한다  
        self.turtle.left(90)                    # turtle 객체는 속성 left에 의해 동작인 90만큼 회전한다 

register_shape("c:/car.gif")                    # 등록한 모양은  "c:/car.gif"이다  
myCar = Car(200, "red", "E-class")              # myCar는 200만큼의 스피드로  앞으로, 빨간색이고  e-class이다.     

for i in range(100):              # 아래의 문장을 100번 반복한다
    myCar.drive()                 # myCar에 위에서 정의한 drive()의 속성을 부여한다
    myCar.left_turn()             # myCar에 위에서 정의한 left_turn의 속성을 부여한다
