
class Author:
    def __init__ (self, name, birthday, birth_country, biography):
        self.name = name
        self.birthday = birthday
        self.birth_country = birth_country
        self.biography = biography
    

    def get_author(self):
        return self.name

    def author_info(self):
        return self.name, self.birthday, self.birth_country, self.biography
        
    