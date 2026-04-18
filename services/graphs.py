import matplotlib.pyplot as plt

class Graph:
    def __init__(self, prices, dates):
        self.__prices = prices
        self.__dates = dates

    @classmethod
    async def create(cls, data):
        return cls(data["price"], data["date"])

    @property
    async def show_graph(self):
        plt.plot(self.__dates, self.__prices)
        await plt.show()
