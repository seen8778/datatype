target = 85
count = 0

while True:
    try:
        guess = int(input("กรุณาทายตัวเลขระหว่าง 0 ถึง 100: "))
        count += 1

        if guess < 0 or guess > 100:
            print("ขอโทษด้วยตัวเลขไม่อยู่ในช่วงระหว่าง 0-100 กรุณาทายใหม่")
        elif guess < target:
            print("ขอโทษด้วยตัวเลขมีค่าน้อยเกินไปที่ตั้งไว้ กรุณาทายใหม่")
        elif guess > target:
            print("ขอโทษด้วยตัวเลขมีค่ามากเกินไปกว่าที่ตั้งไว้ กรุณาทายใหม่")
        else:
            print(f"ยินดีด้วยคุณทายถูก คุณทายทั้งหมด {count} ครั้ง")
            break
    except ValueError:
        print("กรุณาใส่เฉพาะจำนวนเต็มเท่านั้น")
