n = 3 #剩餘機會
while True:
    password = input('請輸入密碼: ')
    if password == 'a123456': #是否輸入正確密碼
        print('登入成功!')
        break #逃出迴圈
    n = n - 1
    if n > 0: 
        print('密碼錯誤! 還有', n , '次機會') #次數0以前的印出
    if n == 0: 
        print('沒機會嘗試了! 要鎖帳號了!')  #次數0的印出
        break
    