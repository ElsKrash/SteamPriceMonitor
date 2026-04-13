import matplotlib.pyplot as plt

class Graph:
    def __init__(self, prices, dates):
        self.__prices = prices
        self.__dates = dates
    
    @property
    def show_graph(self):
        plt.plot(self.__prices, self.__dates)
        plt.show()
