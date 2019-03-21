import lxml.html
import requests

from .person import Person

PHONEBOOK_URL = 'http://localhost:5000'
PERSON_XPATH = '//tr[@class="person"]'


class Phonebook:
    def __init__(self):
        s = requests.Session()
        r = s.get(PHONEBOOK_URL)
        html = lxml.html.fromstring(r.text)

        self.directory = []

        for el in html.xpath(PERSON_XPATH):
            self.directory.append(Person(el))

        # FIXME
        # self.directory.sort()

    def get_all(self):
        return self.directory

    def query_name(self, q):
        results = []
        for p in self.directory:
            if q.lower() in p.last.lower() or q in p.first.lower():
                results.append(p)
        return results

    def query_phone(self, q):
        results = []
        for p in self.directory:
            if q in p.phone:
                results.append(p)
        return results

if __name__ == '__main__':
    
