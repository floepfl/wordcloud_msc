from abc import ABC, abstractmethod

class Window(ABC):

    def __init__(self):
        self.subwindows = {}

    @abstractmethod
    def run(self, *args):
        raise NotImplementedError

    @abstractmethod
    def layout(self, *args):
        raise NotImplementedError

    # def close(self):
    #     self.window.close()
    #     for subwindow in self.subwindows.values():
    #         subwindow.close()