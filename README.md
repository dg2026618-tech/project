Web VPython 3.2

e = box(size = vec(12,15,12), color = color.cyan, pos = vec(0,0,0))#elevator

#box(size = vec(10,15,0.5), color = color.cyan, pos = vec(0,-7,6.5),opacity = 0.1)

box(size = vec(0.5,150,50), pos = vec(25,0,31),opacity = 1)#wall(out)
box(size = vec(0.5,150,50), pos = vec(-25,0,31),opacity = 1)

box(size = vec(19,150,0.5), pos = vec(16,0,6),opacity = 1)
box(size = vec(19,150,0.5), pos = vec(-16,0,6),opacity = 1)

box(size = vec(50,0.5,50), pos = vec(0,15,31),opacity = 1)#f6
box(size = vec(50,0.5,50), pos = vec(0,-15,31),opacity = 1)#f5
box(size = vec(50,0.5,50), pos = vec(0,45,31),opacity = 1)#f4
box(size = vec(50,0.5,50), pos = vec(0,-45,31),opacity = 1)#f3
box(size = vec(50,0.5,50), pos = vec(0,75,31),opacity = 1)#f2
box(size = vec(50,0.5,50), pos = vec(0,-75,31),opacity = 1)#f1

box(size = vec(0.5,150,12), opacity = 1, pos = vec(6.5,0,0))#wall(in)
box(size = vec(0.5,150,12), opacity = 1, pos = vec(-6.5,0,0))
box(size = vec(13,150,0.5), opacity = 1, pos = vec(0,0,-6.5))
box(size = vec(19,15,0.5), pos = vec(0,7.5,6),opacity = 1)
#box(size = vec(13,150,0.5), opacity = 0.5, pos = vec(0,0,0))
#v1 = vector(0.1, 4, 0)
#k = keysdown()

#control
while 1:
    k = keysdown()
    rate(100)
    if 'w' in k:
        e.pos.y = e.pos.y + 1
    if 's' in k:
        e.pos.y = e.pos.y - 1
    if '1' in k:#-67
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
        
#    if '1' in k:
#        e.pos.y = -67
#    if '2' in k:
#        e.pos.y = -37
#    if '3' in k:
#        e.pos.y = -7
#    if '4' in k:
#        e.pos.y = 23
#    if '5' in k:
#        e.pos.y = 53
#           
    
