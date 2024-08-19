from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
#Home view
def home(request):
    searchTerm=request.GET.get('searchMovie')
    if searchTerm:
        movies=Movie.objects.filter(title__icontains=searchTerm)     
    else:
        movies=Movie.objects.all()               
    return render(request, 'home.html', {'searchTerm':searchTerm, "movies":movies})

## About View
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    email=request.GET.get('email')                               
    return render(request, 'signup.html', {'email':email})


#Detail view 
def detail(request, movie_id):
    movie=get_object_or_404(Movie, pk=movie_id)
    reviews=Review.objects.filter(movie = movie)
    
    return render(request, 'detail.html', {"movie":movie, 'reviews': reviews})


#Create view
@login_required
def createreview(request, movie_id):
    movie=get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'createreview.html', {'form':ReviewForm(), 'movie':movie})
    
    else:
        try:
            form=ReviewForm(request.POST)
            newReview=form.save(commit=False)
            newReview.user=request.user
            newReview.movie=movie 
            newReview.save()
            
            return redirect('detail', newReview.movie_id)

        except ValueError:
            return render(request, 'createreview.html', {'form':ReviewForm(), 'error':'Bad data passed in '})
        
                    
@login_required
def updatereview(request, review_id):
    review=get_object_or_404(
        Review, pk=review_id, user=request.user 
                             )
    
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updateview.html')
    
    else:
        try:
            form =ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie_id) 
        except ValueError:
            return render(request, 'updateview.html',
                          {'review':review, 'form':form,
                          'error':'Bad data in form'})
            
           
           
def deletereview(request, review_id):
    review=get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)
    