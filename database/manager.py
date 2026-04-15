import asyncpg

class DataBaseManager:
    def __init__(self, pool):
        self.__pool: asyncpg.Pool = pool 

    @classmethod
    async def create(cls, user, password):
        pool = await asyncpg.create_pool(user=user, password=password)
        return cls(pool)

    async def close(self):
        self.__pool.close()

    async def add_game(self, game_id, name, last_check):
        await self.__pool.execute("INSERT INTO games (game_id, name, last_check) VALUES ($1, $2, $3)", game_id, name, last_check)
    
    async def remove_game(self, game_id):
        return await self.__pool.execute("DELETE FROM games WHHERE game_id=$1", game_id)