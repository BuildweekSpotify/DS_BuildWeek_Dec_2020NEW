import pandas as pd
import ast
import itertools

df_track = pd.read_csv('csv/data.csv')
# df_artist = pd.read_csv('https://raw.githubusercontent.com/vjmiyagi/DS_BuildWeek_Dec_2020/main/csv/data_by_artist.csv')
# df_genres = pd.read_csv('https://raw.githubusercontent.com/vjmiyagi/DS_BuildWeek_Dec_2020/main/csv/data_by_genres.csv')
# df_year = pd.read_csv('https://raw.githubusercontent.com/vjmiyagi/DS_BuildWeek_Dec_2020/main/csv/data_by_year.csv')
df_track_genres = pd.read_csv('csv/data_w_genres.csv')

# df_track.merge(df_track_genres,)
master_genres = pd.read_csv("csv/master_genres.csv")
print(master_genres.head())
# def transform(long_name: str) -> str:
# for genres in master_genres.genres
def find_add_to(name: str) -> str:
    for short_name, long_name in itertools.zip_longest(master_genres.genres, df_track_genres.genres):
        column_w_lists = ast.literal_eval(long_name)
        if short_name in column_w_lists:
            return short_name
    else:
        return "other"

df_track_genres["master_genres"] = df_track_genres["genres"].apply(find_add_to)
print(df_track_genres.head(5))
print(df_track_genres.genres.dtypes)


