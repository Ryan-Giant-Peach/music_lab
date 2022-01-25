import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository 
import repositories.artist_repository as artist_repository



artist_1 = Artist("Tenacious D")
artist_repository.save(artist_1)


album_1 = Album("Pick Of Destiny", artist_1, "Rock")
album_repository.save(album_1) 

# artist1 = User("Deirdre", "Barlow")
# user_repository.save(user1)

# user_repository.delete_all()
# task_repository.delete_all()

# user1 = User("Deirdre", "Barlow")
# user_repository.save(user1)
# user2 = User("Ken", "Barlow")
# user_repository.save(user2)


# task1 = Task("Crush my enemies", user1, 10)
# task_repository.save(task1)

# task2 = Task("See them driven before me", user2, 50)
# task_repository.save(task2)

# found_users = user_repository.select_all()

# tasks_assigned = user_repository.tasks(user1)

# pdb.set_trace()