#define the class
class Flashcard:
#define the class variables
    flashcards = []

#define the init function
    def __init__(self, word, mean, mean2, mean3):
        self.word = word
        self.mean = mean
        self.mean2 = mean2
        self.mean3 = mean3
        Flashcard.flashcards.append({'word': self.word, 'means': self.mean, 'means2': self.mean2, 'means3': self.mean3})

#define the methods
    def __str__(self):
        pass
        msg = "Word: " + self.word + "    Synonyms: " + self.mean + "  " + self.mean2 + "  " + self.mean3
        return msg

    def flash():
        s = {'correct': 0, 'total': 0}
        for x in Flashcard.flashcards:
            q = x['word']
            a = x['means']
            b = x['means2']
            c = x['means3']
            t = input("What does " + q + " mean? ")
            if t == a or t == b or t == c:
                print("Correct!")
                s['correct'] = int(s['correct']) + 1
                s['total'] = int(s['total']) + 1
                print(str(s['correct']) + "/" + str(s['total']))
            else:
                print("Incorrect! Correct answers are " + a + ", " + b + ", or " + c + ".")
                s['total'] = int(s['total']) + 1
                print(str(s['correct']) + "/" + str(s['total']))

    def get_all():
        for x in Flashcard.flashcards:
            print("\nWord: " + x['word'] + "    Synonyms: " + x['means'] + "  " + x['means2'] + "  " + x['means3'])


#create 4 instance of this class and test all the methods
f1 = Flashcard("serene", "quiet", "silent", "calm")
f2 = Flashcard("dreadful", "bad", "awful", "terrible")
f3 = Flashcard("commence", "start", "begin", "initiate")
f4 = Flashcard("livid", "mad", "angry", "furious")


#INTERFACE
run = True
while run:
    menu = input("\n >--< FLASHCARDS >--< \n Enter 1 to STUDY\n Enter 2 to PRACTICE\n Enter 0 to EXIT\n")
    if int(menu) == 1:
        Flashcard.get_all()
    elif int(menu) == 2:
        Flashcard.flash()
    elif int(menu) == 0:
        run = False
        break
    else: print("Invalid option. Try again.")
