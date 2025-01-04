from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> str:
    return (f'Главная страница')


@app.get("/user/admin")
async def read_root() -> str:
    return (f'Вы вошли как администратор')


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return (f'Вы вошли как пользователь № {user_id}')


@app.get('/user')
async def get_user_info(username: str, age: int):
    return (f'Информация о пользователе. Имя: {username}, Возраст: {age}')
