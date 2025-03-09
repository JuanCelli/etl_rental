from extraction import Extractor, ZonaPropScraper

def test_get_price_zona_prop():
    scraper = ZonaPropScraper()
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(scraper, url)
    price = extractor.get_price()
    print(price)

    assert isinstance(price, float)
    assert price == 400000

def test_get_bills_zona_prop():
    scraper = ZonaPropScraper()
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(scraper, url)
    bills = extractor.get_bills()
    print(bills)

    assert isinstance(bills, float)
    assert bills == 50000

def test_get_rooms_zona_prop():
    scraper = ZonaPropScraper()
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(scraper, url)
    rooms = extractor.get_rooms()
    print(rooms)

    assert isinstance(rooms, int)
    assert rooms == 1

def test_get_location_zona_prop():
    scraper = ZonaPropScraper()
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(scraper, url)
    location = extractor.get_location()
    print(location)

    assert isinstance(location, str)
    assert location == "Mosconi 2717,  Villa Pueyrredón, Capital Federal"

def test_get_size_zona_prop():
    scraper = ZonaPropScraper()
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(scraper, url)
    size = extractor.get_size()
    print(size)

    assert isinstance(size, float)
    assert size == 27