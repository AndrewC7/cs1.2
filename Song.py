class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  def get_title(self):
    return self.__title
  
  
  def set_title(self, title):
    self.__title = str(title).title()


  def get_next_song(self):
    return self.__next_song


  def set_next_song(self, next_title):
    self.__next_song = next_title


  # TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return (f"Song Title: {self.get_title()}")


  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return (f"{self.get_title()} -> {self.get_next_song()}")
