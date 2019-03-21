LAST_XPATH='td[@class="last"]/text()'
FIRST_XPATH='td[@class="first"]/text()'
PHONE_XPATH='td[@class="phone"]/text()'


class Person:
    def __init__(self, el):
        """
        :param el: the lxml HTMLElement to unpack
        """
        self.last = el.xpath(LAST_XPATH)[0]
        self.first = el.xpath(FIRST_XPATH)[0]
        self.phone = el.xpath(PHONE_XPATH)[0]

    def __repr__(self):
        return "<Person last='{}', first='{}', phone='{}'"\
            .format(self.last, self.first, self.phone)

    def __str__(self):
        return "{}\t{}\t{}".format(self.last, self.first, self.phone)
