import matplotlib.pyplot as plt

class Graph:
    def __init__(self, prices, dates):
        self.__prices = prices
        self.__dates = dates

    @classmethod
    async def create(cls, data):
        return cls(data["price"], data["date"])

    @property
    def save_graph(self):

        fig, ax = plt.subplots()
        
        ax.bar(self.__dates, self.__prices, width=0.15, color="#ffffff")

        ax.set_facecolor("#1c1d22")
        fig.set_facecolor("#1c1d22")

        ax.tick_params(colors="#ffffff")
        ax.xaxis.label.set_color("#ffffff")
        ax.yaxis.label.set_color("#ffffff")

        fig.autofmt_xdate()

        plt.savefig(fname="graph.jpg", format="jpg", dpi=1000)
