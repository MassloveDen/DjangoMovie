from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie


class MoviesView(ListView):

    # def get(self, request):
    #     movies = Movie.objects.all()
    #     return render(request, "movies/movie_list.html"), {"movie_list": movies})
    # Список фильмов
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"
    #queryset = Movie.objects.all()





class MovieDetailView(DetailView):
    # model = Movie
    # slug_field = "url"


    def get(self, request, slug):
        movies = Movie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {"movies": movies})

    # def get(self, request, pk):
    #     movie = Movie.objects.get(id=pk)
    #     return render(request, "movies/movie_detail.html", {"movies": movie})



# class MovieDetailView(View):
#
#     def get(self, request, slug):
#         movies = Movie.objects.get(url=slug)
#         return render(request, "movies/movie_detail.html"), {"movies": movies}


# class MovieDetailView(View):
#     model = Movie
#     slug_field = "url"

