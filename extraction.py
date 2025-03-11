import re
import urllib.request
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class BaseScraper(ABC):
    """Objeto que contiene el schema caracteristico de cada sitio"""

    @abstractmethod
    def find_price(self, soup):
        pass

    @abstractmethod
    def find_bills(self, soup):
        pass

    @abstractmethod
    def find_rooms(self, soup):
        pass

    @abstractmethod
    def find_location(self, soup):
        pass

    @abstractmethod
    def find_size(self, soup):
        pass


class ZonaPropScraper(BaseScraper):
    def find_price(self, soup):
        price_div = soup.find("div", class_="price-value")

        if price_div:
            price_span = price_div.find_all("span")[1]
            if not price_span:
                return None
            rent_price_string = price_span.text.strip()
            rent_price = price_parser(rent_price_string)
            return rent_price
        return None

    def find_bills(self, soup):
        bills_span = soup.find("span", class_="price-expenses")
        if not bills_span:
            return None
        bills_string = bills_span.text.strip()
        bills_string = " ".join(bills_string.split(" ")[1:])
        bills = price_parser(bills_string)
        return bills

    def find_rooms(self, soup) -> int:
        rooms_h2 = soup.find("h2", class_="title-type-sup-property")
        if not rooms_h2:
            return None
        rooms_string = rooms_h2.text.strip()
        rooms_string = rooms_string.split("·")[2].strip()
        rooms_string = rooms_string[0]
        rooms = int(rooms_string)
        return rooms

    def find_location(self, soup):
        location_div = soup.find("div", class_="section-location-property")

        if location_div:
            location_h4 = location_div.find_all("h4")[0]
            if not location_h4:
                return None
            location = location_h4.text.strip()
            return location
        return None

    def find_size(self, soup) -> float:
        size_h2 = soup.find("h2", class_="title-type-sup-property")
        if not size_h2:
            return None
        size_string = size_h2.text.strip()
        size_string = size_string.split("·")[1].strip()
        size_string = size_string.replace("m²", "")
        size = float(size_string)
        return size


class ArgenPropScraper(BaseScraper):
    def find_price(self, soup):
        price_p = soup.find("p", class_="titlebar__price")
        if not price_p:
            return None
        rent_price_string = price_p.text.strip()
        rent_price = price_parser(rent_price_string)
        return rent_price

    def find_bills(self, soup):
        bills_p = soup.find("p", class_="titlebar__expenses")
        if not bills_p:
            return None
        bills_string = bills_p.text.strip()
        bills_string = bills_string.split(" ")[1]
        bills = price_parser(bills_string)
        return bills

    def find_rooms(self, soup):
        rooms_li = soup.find("li", attrs={"title": "Ambientes"})

        if rooms_li:
            rooms_p = rooms_li.find_all("p")[0]
            if not rooms_p:
                return None
            rooms_string = rooms_p.text.strip()
            if rooms_string == "Monoambiente":
                return 1

            rooms = int(rooms_string.split(" ")[0])
            return rooms
        return None

    def find_location(self, soup):
        location_h2 = soup.find("h2", class_="titlebar__address")
        if not location_h2:
            return None
        location_string = location_h2.text.strip()
        return location_string

    def find_size(self, soup):
        size_li = soup.find("li", attrs={"title": "Sup. cubierta"})
        if size_li:
            size_p = size_li.find_all("p")[0]
            if not size_p:
                return None
            size_string = size_p.text.strip()
            size = float(size_string.split(" ")[0])
            return size
        return None


def price_parser(price_string: str) -> float:
    string_pre_processed = price_string.replace(" ", "")
    string_pre_processed = string_pre_processed.replace("$", "")
    string_pre_processed = string_pre_processed.replace(".", "")
    price = float(string_pre_processed)
    return price


class Extractor:
    """Controlará la lógica de extraer info del sitio web"""

    def __init__(self, url: str):
        self.url = url
        self.page = self._get_page()
        self.scraper = StrategyScraper(self.url).get_scraper()
        self.soup = BeautifulSoup(self.page, "html.parser")

    def _get_page(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "*/*",
        }

        req = urllib.request.Request(self.url, headers=headers)

        try:
            with urllib.request.urlopen(req) as response:
                html = response.read().decode("utf-8")
                return html
        except urllib.error.HTTPError as e:
            print(f"Error HTTP: {e.code}")
            return None
        except urllib.error.URLError as e:
            print(f"Error de conexión: {e.reason}")
            return None

    def get_price(self):
        price = self.scraper.find_price(self.soup)
        if not price:
            raise Exception(
                f"No se pudo encontrar el precio de la propiedad, es posible que la estructura del sitio haya cambiado o que ya no esté disponible."
            )
        return price

    def get_bills(self):
        bills = self.scraper.find_bills(self.soup)
        return bills

    def get_rooms(self):
        rooms = self.scraper.find_rooms(self.soup)
        return rooms

    def get_location(self):
        location = self.scraper.find_location(self.soup)
        return location

    def get_size(self):
        size = self.scraper.find_size(self.soup)
        return size

    def get_data(self):
        data = {
            "price": self.get_price(),
            "bills": self.get_bills(),
            "rooms": self.get_rooms(),
            "location": self.get_location(),
            "size": self.get_size(),
            "url": self.url,
        }
        return data


class StrategyScraper:
    PATTERNS = {
        r"https?://(www\.)?zonaprop\.com": ZonaPropScraper,
        r"https?://(www\.)?argenprop\.com": ArgenPropScraper,
    }

    def __init__(self, url):
        self.url = url

    def get_scraper(self):
        for pattern, scraper in StrategyScraper.PATTERNS.items():
            if re.match(pattern, self.url):
                return scraper()

        raise ValueError("No hay un scraper registrado para esta URL.")
