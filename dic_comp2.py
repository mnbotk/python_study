
# coding: utf-8
e_seasons = ["Spring", "Summer", "Autumn", "Winter"]
j_seasons = ["春", "夏", "秋", "冬"]

seasons = {e:j for (e,j) in zip(e_seasons, j_seasons)}
print(seasons)
