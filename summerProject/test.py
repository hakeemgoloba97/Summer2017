# def calculateRecommendations(self):
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "summerProject.settings")

import django
django.setup()

import numpy as np

    # your imports, e.g. Django models
from mainApp.models import userRatings
import pandas as pd
lol = [u'1', u'Toy Story (1995)', u'308', u'4']
df = pd.DataFrame(columns=["movie_id", "title", "user_id", "rating"])
df = df.append(pd.Series(lol[0].split(","), index=["movie_id", "title", "user_id", "rating"]), ignore_index=True)

movie_id = userRatings.objects.values_list('movie_id', flat=True)
movie_id = list(movie_id)

user_id = userRatings.objects.values_list('user_id', flat=True)
user_id = list(user_id)

title = userRatings.objects.values_list('title', flat=True)
title = list(title)

rating = userRatings.objects.values_list('rating', flat=True)
rating = list(rating)

ratings = np.column_stack((movie_id, title, user_id, rating))

print(np.array_equal(ratings[0],np.array(lol)))


ratings = pd.DataFrame(ratings, columns = ["movie_id", "title", "user_id", "rating"])
ratings[['movie_id','user_id','rating']] = ratings[['movie_id','user_id','rating']].apply(pd.to_numeric)
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating',aggfunc='first')
# if(not userRatings.loc[944].empty):
#     print(userRatings.loc[944].dropna())

corrMatrix = userRatings.corr()

corrMatrix = userRatings.corr(method='pearson', min_periods=100)

myRatings = userRatings.loc[943].dropna()
print(len(userRatings))
# print(type(userRatings.loc[908]))
print(myRatings)
simCandidates = pd.Series()
# print(simCandidates)
# for i in range(0, len(myRatings.index)):
#     print ("Adding sims for " + myRatings.index[i] + "...")
#     # Retrieve similar movies to this one that I rated
#     sims = corrMatrix[myRatings.index[i]].dropna()
#         # Now scale its similarity by how well I rated this movie
#     sims = sims.map(lambda x: x * myRatings[i])
#         # Add the score to the list of similarity candidates
#     simCandidates = simCandidates.append(sims)
#
#     #Glance at our results so far:
# simCandidates = simCandidates.groupby(simCandidates.index).sum()
# simCandidates.sort_values(inplace = True, ascending = False)
# simCandidates = simCandidates.drop(myRatings.index)
# simCandidates = simCandidates[0:10]
#
# print(simCandidates)
# return(simCandidates)

    # return HttpResponse(json.dumps(data))
    # r_cols = ['user_id', 'movie_id', 'rating']
    # ratings = pd.read_csv('C:/Users/Hakeem/Desktop/DataScience-Python3/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

    # m_cols = ['movie_id', 'title']
    # movies = pd.read_csv('C:/Users/Hakeem/Desktop/DataScience-Python3/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

    # ratings = pd.merge(movies, ratings)
    # df = ratings
    # df.to_csv('C:/Users/Hakeem/Desktop/out.csv')

    # # ratings.head
    # df
