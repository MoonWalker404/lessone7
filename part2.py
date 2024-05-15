# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f"Сформирован отчет - {self.title} - {self.content}")
# Код без использования 2-го метода SOLLID открытости/закрытости 👆


from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)


report = Report("Заголовок отчета, его тут много", "Это текст отчета", TextFormatted())

report.docPrinter()
