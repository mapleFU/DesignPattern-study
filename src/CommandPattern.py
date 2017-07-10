"""
命令模式
"""


class Receiver:
    """
    命令的接受 处理者
    """
    pass


class Invoker:
    """
    命令，由Client创建
    各函数重载excute
    """
    def __init__(self, rec: Receiver):
        self.rec = rec

    def excute(self):
        """
        虚对象，对其进行处理
        """
        pass


class Client:
    """
    命令的发出者
    """
    def use_command(self, command: Invoker):
        """
        :param command: a 
        :return: excute the invoker
        """
        command.excute()


class Light(Receiver):
    def __init__(self):
        self.on = False
        self.light = 10

    def turn(self):
        """
        灯光取反
        """
        self.on = not self.on

    def set_light(self, newlight: int):
        """
        :param newlight: 新亮度 
        """
        self.light = newlight

    def show_data(self):
        if self.on:
            print('灯是开的， 亮度{}'.format(
                self.light
            ))
        else:
            print('灯没开')


class RemoteController(Client):
    def __init__(self):
        print('You have create an remote')


class TurnCmd(Invoker):
    def excute(self):
        self.rec.turn()


# 感觉还是不应该创建的时候这么写...
class SetCmd(Invoker):
    def __init__(self, rec: Light, light: int):
        """
        :param rec: 
        :param light: 
        """
        # init without help
        super().__init__(rec)
        self.set = light

    def excute(self):
        self.rec.set_light(self.set)


if __name__ == '__main__':
    rmc = RemoteController()
    light1 = Light()
    light1.show_data()

    cmd1 = TurnCmd(light1)
    cmd1.excute()
    light1.show_data()

    cmd2 = SetCmd(light1, 20)
    cmd2.excute()
    light1.show_data()

