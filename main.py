from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse #DAR UNA RESPUESTA


app = FastAPI ()

app.title = "MI PRIMERA APP "
app.version = "0.1.1"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]
    

@app.get("/", tags=["Home"]) # ("/") donde me voy a conectar 
def message():
    return HTMLResponse (content="<h1> Mi aplicacion Sencilla")

@app.get("/movies", tags=["movies"])
def get_movies():
    return movies

@app.get("/movies/ {id}", tags=["movies"]) 
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
        
@app.get("/movies/", tags=["movies"]) 
def get_movie_by_category(category: str):
    for movie in movies:
        if movie["category"] == category:
            return movie

@app.post("/Movies", tags=["movies"])
def create_movie(id: int = Body(),
                 title: str = Body(),
                 overview: str = Body(),
                 year: str = Body(),
                 rating: float = Body(),
                 category: str = Body()):
    movies.append({
        "id" : id,
        "title" : title,
        "overview" : overview, 
        "year" : year,
        "rating" : rating, 
        "category" : category, 
    })
    return movies

@app.put("/movies/{id}", tags=['movies'])
def update_movie(id: int,
                 title: str = Body(),
                 overview: str = Body(),
                 year: str = Body(),
                 rating: float = Body(),
                 category: str = Body()):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
            break
    return movies

@app.delete("/movies/{id}", tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies