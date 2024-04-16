from typing import Optional, List

import uvicorn as uvicorn
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware

from app.recommender import item_based_recommendation, user_based_recommendation
from resolver import random_items, random_genre_items

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello 김기주의 영화추천 서비스"}

@app.get("/all/")
async def random_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre:str):
    result = random_genre_items(genre)
    return {"result": result}

@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommendation(item_id)
    return {"result": result}

@app.get("/user-based/")
# Query(None)은 기본값을 주지 않겠다는 말
async def user_based(params:Optional [List[str]]=Query(None)):
    input_ratings_dict = dict(
        (int(x.split(":")[0]), float(x.split(":")[1])) for x in params)
    print(input_ratings_dict)
    result = user_based_recommendation(input_ratings_dict)
    return {"result" : result}


# 2024. 4. 3
# query parameter 실습
# http://localhost:8080/weather?q=Seoul&units=metric
@app.get("/weather/")
async def weather(q:Optional [List[str]]=Query(None), units:str='metric'):
    print(q)
    print(units)
    # http://localhost:8000/weather/?q=1:5&q=100:3&q=20:1 처럼 작성된 구문을 : 기준으로 1과 5로 나누는 코드
    q_dict = dict((int(x.split(":")[0]), float(x.split(":")[1])) for x in q)
    print(q_dict)
    return {"result": f'q={q} : units={units}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)