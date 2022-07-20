class flashcard:
  def __init__(self, word, meaning):
    self.word = word
    self.meaning = meaning
    def __str__(self):
      return self.word+' ( '+self.meaning+' )'
    
    flash = []
   
