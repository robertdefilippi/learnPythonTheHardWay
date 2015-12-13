class Song(object):
   
    def __init__(self, lyrics):
        self.lyrics = lyrics
   
    def sing_me_a_song(self):
        for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Notice the () at the end of the called class.

# Study Drills

beatles = Song(["She love you",
				"Yeah, yeah yeah!",
				"She loves you yeah!"])
				
print beatles.lyrics
# ['She love you', 'Yeah, yeah yeah!', 'She loves you yeah!']

beatles.sing_me_a_song()

lyrics_2 = ['Test', 'Test_2', 'Test_3']

Test_song = Song(lyrics_2)

Test_song.sing_me_a_song()
# Test
# Test_2
# Test_3