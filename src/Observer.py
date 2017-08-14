class Subject:
    """
    注册的主题
    """
    def __init__(self):
        self.reged = list() # 注册的对象

    # def register_viewer(self, viewer: Viewer):
    def register_viewer(self, viewer):
        self.reged.append(viewer)

    def unregister_viewer(self, viewer):
        self.reged.remove(viewer)

    def notify_viewers(self, *args):
        for viewer in self.reged:
            viewer.update(args)


class Viewer:
    """
    观察者
    """
    def register(self, sub: Subject):
        sub.register_viewer(self)

    def unregister(self, sub: Subject):
        sub.unregister_viewer(self)

    def update(self, *args):
        pass


class MacauCasino(Subject):
    """
    同济大学澳门赌场
    """
    def __init__(self):
        super().__init__()
        print('全同济首家澳门赌场开业了！'
              '美丽学长在线发牌～')

    def add_player(self, player):
        self.notify_viewers('玩家{}加入了！'.format(
            player.name
        ))
        self.register_viewer(player)

    def remove_player(self, player):
        self.unregister_viewer(player)
        self.notify_viewers('玩家{}输光了～'.format(
            player.name
        ))


class Player(Viewer):
    def __init__(self, name):
        self.name = name

    def update(self, *args):
        """
        :param args: show the message
        """
        if len(args) == 1:
            print('[{}]: {}'.format(
                self.name,
                # TODO: find out why args like this
                args[0][0]
            ))

    def join_game(self, casino: MacauCasino):
        casino.add_player(self)

    def exit_game(self, casino: MacauCasino):
        casino.remove_player(self)


def main():
    casino = MacauCasino()
    mmx = Player('MMX')
    casino.add_player(mmx)
    fxw = Player('FXW')
    casino.add_player(fxw)
    casino.remove_player(mmx)
    lty = Player('LTY')
    casino.add_player(lty)

if __name__ == '__main__':
    main()


# OUTPUT:
# 全同济首家澳门赌场开业了！美丽学长在线发牌～
# [MMX]: 玩家FXW加入了！
# [FXW]: 玩家MMX输光了～
# [FXW]: 玩家LTY加入了！
