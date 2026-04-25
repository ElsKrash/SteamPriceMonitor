import matplotlib.pyplot as plt
import uuid

from database.models import PricePoint

class Graph:
    def __init__(self, prices, dates):
        self.__prices = prices
        self.__dates = dates

    @classmethod
    async def create(cls, data: list[PricePoint]):
        price = [i.price for i in data]
        date = [i.date for i in data]
        return cls(price, date)

    def save_graph(self):

        fig, ax = plt.subplots()
        
        ax.bar(self.__dates, self.__prices, width=0.15, color="#ffffff")

        ax.set_facecolor("#131416")
        fig.set_facecolor("#131416")

        ax.tick_params(colors="#ffffff")
        ax.xaxis.label.set_color("#ffffff")
        ax.yaxis.label.set_color("#ffffff")

        fig.autofmt_xdate()

        name = f"graph{uuid.uuid4()}.jpg"
        plt.savefig(fname=name, format="jpg", dpi=1000)
        return name
