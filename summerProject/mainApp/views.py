from django.shortcuts import render
from mainApp.forms import userInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'mainApp/index.html')

@login_required
def movieRate(request):

    return render(request,'mainApp/movieRate.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
    registered = False

    if request.method == "POST":
        user_form = userInfoForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

    else:
        user_form = userInfoForm

    return  render(request, 'mainApp/index.html',
                        {'user_form':user_form,
                         'registered':registered})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password =password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("failed log in")
            return HttpResponse("Didnt work")
    else:
        return render(request,'mainApp/login.html',{})

@csrf_exempt
def recommendor(request):
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "summerProject.settings")

    import django
    django.setup()

    import numpy as np

        # your imports, e.g. Django models
    from mainApp.models import userRatings
    import pandas as pd

    array = request.POST.getlist("ratings[]")
    array = [array[x:x+1] for x in range(0, len(array), 1)]
    df = pd.DataFrame(columns=["movie_id", "title", "user_id", "rating"])
    for i in range(len(array)):
        df = df.append(pd.Series(np.array(array[i][0].split(",")),index=["movie_id", "title", "user_id", "rating"]),ignore_index=True)

    movie_id = userRatings.objects.values_list('movie_id', flat=True)
    movie_id = list(movie_id)

    user_id = userRatings.objects.values_list('user_id', flat=True)
    user_id = list(user_id)

    title = userRatings.objects.values_list('title', flat=True)
    title = list(title)

    rating = userRatings.objects.values_list('rating', flat=True)
    rating = list(rating)
    #
    ratings = np.column_stack((movie_id, title, user_id, rating))
    #
    ratings = pd.DataFrame(ratings, columns = ["movie_id", "title", "user_id", "rating"])
    ratings = ratings.append(df)
    #
    ratings[['movie_id','user_id','rating']] = ratings[['movie_id','user_id','rating']].apply(pd.to_numeric)
    userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating',aggfunc='first')
    #
    corrMatrix = userRatings.corr()
    #
    corrMatrix = userRatings.corr(method='pearson', min_periods=100)
    #
    # myRatings = userRatings.loc[944].dropna()
    print(userRatings.loc[944].dropna())

    # simCandidates = pd.Series()
    # for i in range(0, len(myRatings.index)):
    #     # print(i)
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
    # # simCandidates = simCandidates.drop(myRatings.index)
    # simCandidates = simCandidates[0:10]
    # #
    # print("RECOMMENDATIONS.................")
    # print(simCandidates)
    return render(request,'mainApp/index.html')
