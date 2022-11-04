import pygame

#模块初始化
pygame.init()
pygame.joystick.init()

#实例化一个类，只连接一个手柄的话默认为0
joystick = pygame.joystick.Joystick(0)
joystick.init()

done = False
while not done:
    for event_ in pygame.event.get():
        if event_.type == pygame.JOYAXISMOTION or event_.type ==pygame.JOYHATMOTION:
            try:
                joystick.rumble(high_frequency=10,low_frequency=1,duration=0)
                #官方文档给出，duration为0的时候为持续震动，需要用stop_rumble()函数打断施法，具体参数有待测试。
            except KeyboardInterrupt:
                print("无法通过脚本控制电机")
pygame.quit()
