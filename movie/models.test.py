from .models import Movie

def test_movie_str_method():
    movie = Movie(title='Test Movie')
    assert str(movie) == 'Test Movie'
    
    
    
    
    
    
    
