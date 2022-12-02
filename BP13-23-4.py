from turtle import*              # turtle 모듈에서 모든것을 불러온다

class MyTurtle(Turtle):         # class를 선언하고 Turtle이라는 속성을 부여한다
    def glow(self,x,y):          # 해당위치를 설정하는 문장이다 
        self.fillcolor("red")   # 색상을 빨간색으로 채운다

turtle = MyTurtle()           
turtle.shape("turtle")        # 거북이의 모양으로 커서를 변경한다
turtle.onclick(turtle.glow)   # 거북이를 클릭하면 색상이 빨간색으로 변경된다

   
