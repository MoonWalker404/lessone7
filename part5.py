# class Boook():
#     def read(self):
#         print("Чтение интересной истррии")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Boook()
#
#     def tell_story(self):
#         self.book.read()
# Это 5 принцип SOLID 👆
# Принцип инверсии зависимости (DIP, Dependency Inversion Principle)

from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Чтение интересной истррии")

class AudioBook(StorySource):
    def get_story(self):
        print("Чтение интересной истррии вслух")

class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

book = Book()
audioBook = AudioBook()

readerBook = StoryReader(book)
readerAudioBook = StoryReader(audioBook)

readerBook.tell_story()
readerAudioBook.tell_story()
