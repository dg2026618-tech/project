Web VPython 3.2

e = box(size = vec(12,15,12), color = color.cyan, pos = vec(0,0,0))#elevator

#box(size = vec(10,15,0.5), color = color.cyan, pos = vec(0,-7,6.5),opacity = 0.1)

box(size = vec(0.5,150,50), pos = vec(25,0,31),opacity = 1)#오른쪽 외부 벽
box(size = vec(0.5,150,50), pos = vec(-25,0,31),opacity = 1)#왼쪽 외부 벽

box(size = vec(19,150,0.5), pos = vec(16,0,6),opacity = 0.5)#오른쪽 후면 벽
box(size = vec(19,150,0.5), pos = vec(-16,0,6),opacity = 0.5)#왼쪽 후면 벽

box(size = vec(50,0.5,50), pos = vec(0,15,31),opacity = 1)#4층 바닥
box(size = vec(50,0.5,50), pos = vec(0,-15,31),opacity = 1)#3층 바닥
box(size = vec(50,0.5,50), pos = vec(0,45,31),opacity = 1)#5층 바닥
box(size = vec(50,0.5,50), pos = vec(0,-45,31),opacity = 1)#2층 바닥
box(size = vec(50,0.5,50), pos = vec(0,75,31),opacity = 1)#6층 바닥
box(size = vec(50,0.5,50), pos = vec(0,-75,31),opacity = 1)#1층 바닥

box(size = vec(0.5,150,12), opacity = 1, pos = vec(6.5,0,0))#wall(in)
box(size = vec(0.5,150,12), opacity = 1, pos = vec(-6.5,0,0))
box(size = vec(13,150,0.5), opacity = 1, pos = vec(0,0,-6.5))

box(size = vec(13,15,0.5), pos = vec(0,7.5,6),opacity = 0.5)#5층 후면 벽
box(size = vec(13,15,0.5), pos = vec(0,37.5,6),opacity = 0.5)#4층 후면 벽
box(size = vec(13,15,0.5), pos = vec(0,67.5,6),opacity = 0.5)#3층 후면 벽
box(size = vec(13,15,0.5), pos = vec(0,-22.5,6),opacity = 0.5)#2 층 후면 벽
box(size = vec(13,15,0.5), pos = vec(0,-52.5,6),opacity = 0.5)#1 층 후면 벽

#엘리베이터 문
a = 86
b = 93
c = 94
f3r = box(size = vec(6.5,15,0.5), pos = vec(3.25,-7.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#3층 오른쪽
f3l = box(size = vec(6.5,15,0.5), pos = vec(-3.25,-7.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#3층 왼쪽
f4r = box(size = vec(6.5,15,0.5), pos = vec(3.25,22.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#4층 오른쪽
f4l = box(size = vec(6.5,15,0.5), pos = vec(-3.25,22.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#4층 왼쪽
f3r = box(size = vec(6.5,15,0.5), pos = vec(3.25,55.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#5층 오른쪽
f3l = box(size = vec(6.5,15,0.5), pos = vec(-3.25,55.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#5층 왼쪽
f2r = box(size = vec(6.5,15,0.5), pos = vec(3.25,-37.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#2층 오른쪽
f2l = box(size = vec(6.5,15,0.5), pos = vec(-3.25,-37.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#2층 왼쪽
f1r = box(size = vec(6.5,15,0.5), pos = vec(3.25,-67.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#1층 오른쪽
f1l =box(size = vec(6.5,15,0.5), pos = vec(-3.25,-67.5,6),opacity = 0.5, color = vec(a/255, b/255, c/255))#1층 왼쪽
#와이어
box(size = vec(0.5,150,0.5),color = vec(21/255,0/255,255/255))

#mesage
#while 1:
#    rate(100)
#    if e.pos == vec(0,-75,31):
#        print("f6")
#실행하면 랙걸려서 멈춤

#control
while 1:
    k = keysdown()
    rate(100)
    #각 층에 도착했을때 층 수 프린트
    if e.pos == vec(0,-67,0):
        print("1층입니다")
        f1l.pos.x = f1l.pos.x -1
        f1r.pos.x = f1r.pos.x + 1
        if f1l.pos.x == 8.25
            f1l.pos.x = 8.25
        if f1r.pos.x == -1.75
            f1r.pos.x = -1.75
        
    if e.pos == vec(0,-37,0):
        print("2층입니다")
    if e.pos == vec(0,-7,0):
        print("3층입니다")
    if e.pos == vec(0,23,0):
        print("4층입니다")
    if e.pos == vec(0,53,0):
        print("5층입니다")

        
    if 'w' in k:
        e.pos.y = e.pos.y + 1
    if 's' in k:
        e.pos.y = e.pos.y - 1
    if '1' in k:#-67
#        print("floor 1")
        for i in range(0,1000):
            if e.pos.y < -67:
                rate(50)
                e.pos.y += 1
                if e.pos.y == -67:
                    break
            if e.pos.y > -67:
                rate(50)
                e.pos.y += -1
                if e.pos.y == -67:
                    break
    if '2' in k:#-37
#        print("floor 2")
        for i in range(0,1000):
            if e.pos.y < -37:
                rate(50)
                e.pos.y += 1
                if e.pos.y == -37:
                    break
            if e.pos.y > -37:
                rate(50)
                e.pos.y += -1
                if e.pos.y == -37:
                    break
    if '3' in k:#-7
#        print("floor 3")
        for i in range(0,1000):
            if e.pos.y < -7:
                rate(50)
                e.pos.y += 1
                if e.pos.y == -7:
                    break
            if e.pos.y > -7:
                rate(50)
                e.pos.y += -1
                if e.pos.y == -7:
                    break
    if '4' in k:#23
#        print("floor 4")
        for i in range(0,1000):
            if e.pos.y < 23:
                rate(50)
                e.pos.y += 1
                if e.pos.y == 23:
                    break
            if e.pos.y > 23:
                rate(50)
                e.pos.y += -1
                if e.pos.y == 23:
                    break
    if '5' in k:#53
#        print("floor 5")
        for i in range(0,1000):
            if e.pos.y < 53:
                rate(50)
                e.pos.y += 1
                if e.pos.y == 53:
                    break
            if e.pos.y > 53:
                rate(50)
                e.pos.y += -1
                if e.pos.y == 53:
                    break
        
