#Lets make a musicion class
#attributes- instrument, years of playing, name, genre

class Musician(object):
    """a class to create musicians"""
    def __init__(self, name, instrument, genre, years_playing):
        self.name = name
        self.instrument = instrument
        self.genre = genre
        self.years_playing = years_playing
    def descripton(self):
        print('Hi i am {0}, I have been playing {2} for {3} years.'.format(
            self.name,
            self.genre,
            self.isntrument,
            self.years_playing
        ))


beyonce = Musician('Beyonce Knowles', 'voice', 'R&b', 20)

jimmy_hendrix = Musician('Jimmy Hendrix ', ' guitar ', 'Rock', 10)

print('Hi i am ' + beyonce.name + 'I play ' + beyonce.instrument)
print(jimmy_hendrix.instrument)
print(beyonce.genre)
