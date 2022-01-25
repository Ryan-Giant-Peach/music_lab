import pdb
from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['album_name'], artist, row['genre'], row['id'])
        albums.append(album)
    return albums

def save(album):
    sql = "INSERT INTO albums (album_name, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

# def select(id):
#     task = None
#     sql = "SELECT * FROM tasks WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     if result is not None:
#         user = user_repository.select(result['user_id'])
#         task = Task(result['description'], user, result['duration'], result['completed'], result['id'])
#     return task

# def delete_all():
#     sql = "DELETE FROM tasks"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM tasks WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def update(task):
#     sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [task.description, task.user.id, task.duration, task.completed, task.id]
#     run_sql(sql, values)