import pandas as pd

item_name = "data/movies_final.csv"

def random_items():
    movies_df = pd.read_csv(item_name)
    movies_df = movies_df.fillna("")
    # 데이터프레임은 파이썬에서 쓰는 데이터형식이기때문에 딕셔너리로 바꾸어서 전달해야 오류가 나지 않음
    # to_dict (list, series, split, tight, records, index)로도 가능
    result_items = movies_df.sample(n=10).to_dict("records")
    return result_items

def random_genre_items(genre):
    movies_df = pd.read_csv(item_name)
    # 장르라는 여러가지의 장르가 있는데 해당 필드에 그 글자가 있는지 있다 없다로 표현해줌
    # x.lower로 x를 모두 소문자로 바꾸어줌
    genre_df = movies_df[movies_df['genres'].apply(lambda x: genre in x.lower())]
    genre_df = genre_df.fillna('')
    result_items = genre_df.sample(n=10).to_dict('records')
    return result_items


def classic_items():
    movies_df = pd.read_csv(item_name)
    movies_df = movies_df.fillna("")
    # 평점 평균 계산
    movies_df['rmean'] = movies_df['rmean'].astype(float)
    mean_movies = movies_df.sort_values(by='rmean', ascending=False)
    # 상위 10개 영화 추출
    classic_movie = mean_movies.head(10).to_dict("records")
    return classic_movie


