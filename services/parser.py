import aiohttp
import datetime
import asyncio

class Tracker():
    @staticmethod
    async def create(game_id):
        obj = Tracker(game_id)
        await obj.update()
        if hasattr(obj, "_Tracker__price"):
            return obj
        return None

    def __init__(self, game_id):
        self._game_id = str(game_id)

    async def update(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://store.steampowered.com/api/appdetails?appids={self._game_id}") as data:
                data_json = await data.json()
                data_json = data_json[self._game_id]
                if data.status == 200:
                    if data_json["success"] and data_json["data"].get("price_overview", False):
                        self.__game_name = data_json["data"]["name"]
                        self.__price = data_json["data"]["price_overview"]["final_formatted"]
                        self.__date = datetime.datetime.now().replace(microsecond=0)

    @property
    def game_id(self) -> int:
            return int(self._game_id)
    
    @property
    def game_name(self) -> str:
         return self.__game_name

    @property
    def price(self) -> float:
            allowed = "0123456789.,"
            clean_price = "".join(c for c in self.__price if c in allowed)
            
            return clean_price.replace(",", ".").strip()
    
    @property
    def date(self) -> datetime.datetime:
            return self.__date

if __name__ == "__main__":
    async def main():
        dont_starve = await Tracker.create(322330)
        print(dont_starve.price)

    asyncio.run(main())