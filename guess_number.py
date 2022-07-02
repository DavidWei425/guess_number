#猜數字遊戲
import random
print('請在0~100間輸入數字直到猜中密碼')
mina=0
maxb=100
code = random.randint(mina,maxb)
guess=int(input('請在'+str(mina)+'~'+str(maxb)+'之間輸入數字 : '))
while True : 
    if guess in range(mina,maxb+1):
        if guess == code:
            break
        elif guess<code:
            mina = guess
        elif guess>code:
            maxb = guess
    else:
        print('輸入值不在範圍內,請重新輸入')
    guess=int(input('請在'+str(mina)+'~'+str(maxb)+'之間輸入數字 : '))        
print('猜中密碼為 : ', code)