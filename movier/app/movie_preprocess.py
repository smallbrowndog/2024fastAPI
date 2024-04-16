import pandas as pd

movies_df = pd.read_csv("data/movies.csv")

movies_df['movieId'] = movies_df['movieId'].astype(str)

links_df = pd.read_csv("data/links.csv", dtype=str)

# linksd.csv에 있는 movieId와 movies.csv에 있는 movieId가 같은것끼리 찾아서 데이터 합치기
merged_df = movies_df.merge(links_df, on='movieId', how='left')
print(merged_df)
print(merged_df.columns)
print('=' * 50, 'end', '=' * 50)

# http://www.imdb.com/title/tt{row}로 아이디를 집어넣게 되면 해당 영화 imdb사이트로 진입하게 됨
def add_url(row):
    return f'http://www.imdb.com/title/tt{row}'

# 위에서 imdb사이트 링크를 합치기
# merged_df['url'] = 'http://www.imdb.com/title/tt' + merged_df['imdbId'].astype(str)
merged_df['url'] = merged_df['imdbId'].apply(lambda x:add_url(x))

print(merged_df)
print(merged_df.columns)
print('=' * 50, 'end', '=' * 50)

# ratings.csv에서 데이터 받아오기
ratings_df = pd.read_csv('data/ratings.csv')
ratings_df['movieId'] = ratings_df['movieId'].astype(str)

# movieId별로 그룹화하고 개수 세기
agg_df_c = ratings_df.groupby('movieId').count()
print(agg_df_c)
print('=' * 50, 'end', '=' * 50)

# movieId별로 그룹화하고 평균내기
agg_df_a = ratings_df.groupby('movieId').mean()
print(agg_df_a)
print('=' * 50, 'end', '=' * 50)

# movieId별로 그룹화하고 개수, 평균 열 만들기
agg_df = ratings_df.groupby('movieId'). \
    agg(rcount = ('rating', 'count'), rmean = ('rating', 'mean'))
print(agg_df)
print('=' * 50, 'end', '=' * 50)

merged_df = merged_df.merge(agg_df, on='movieId', how='left')
print(merged_df)
print(merged_df.columns)
print('=' * 50, 'end', '=' * 50)

import requests
from tqdm import tqdm

def add_poster(df):
    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        tmdb_id = row["tmdbId"]
        tmdb_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=f2a1fddeef038db026fb3e05415e80f2&language=en-US"
        result = requests.get(tmdb_url)
        # final url : https://image.tmdb.org/t/p/original/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg
        try:
            df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original" + result.json()['poster_path']
        except (TypeError, KeyError) as e:
            # toy story poster as default
            df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg"
    return df

merged_df['poster_path'] = None
merged_df = add_poster(merged_df)
print(merged_df)

merged_df.to_csv('data/movies_final.csv', index=None)