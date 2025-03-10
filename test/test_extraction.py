from extraction import Extractor, ZonaPropScraper, ArgenPropScraper

def test_get_price_zona_prop():
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(url)
    price = extractor.get_price()
    print(price)

    assert isinstance(price, float)
    assert price == 400000

def test_get_bills_zona_prop():
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(url)
    bills = extractor.get_bills()
    print(bills)

    assert isinstance(bills, float)
    assert bills == 50000

def test_get_rooms_zona_prop():
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(url)
    rooms = extractor.get_rooms()
    print(rooms)

    assert isinstance(rooms, int)
    assert rooms == 1

def test_get_location_zona_prop():
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(url)
    location = extractor.get_location()
    print(location)

    assert isinstance(location, str)
    assert location == "Mosconi 2717,  Villa Pueyrredón, Capital Federal"

def test_get_size_zona_prop():
    url = "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-excelente-monoambiente-al-frente-con-balcon-55231811.html"
    extractor = Extractor(url)
    size = extractor.get_size()
    print(size)

    assert isinstance(size, float)
    assert size == 27

def test_get_price_argen_prop():
    url = "https://www.argenprop.com/departamento-en-alquiler-en-villa-pueyrredon-1-ambiente--17033034"
    extractor = Extractor(url)
    price = extractor.get_price()
    print(price)

    assert isinstance(price, float)
    assert price == 450000

def test_get_bills_argen_prop():
    url = "https://www.argenprop.com/departamento-en-alquiler-en-villa-pueyrredon-1-ambiente--17033034"
    extractor = Extractor(url)
    bills = extractor.get_bills()
    print(bills)

    assert isinstance(bills, float)
    assert bills == 48000

def test_get_rooms_argen_prop():
    url = "https://www.argenprop.com/departamento-en-alquiler-en-villa-pueyrredon-1-ambiente--17033034"
    extractor = Extractor(url)
    rooms = extractor.get_rooms()
    print(rooms)

    assert isinstance(rooms, int)
    assert rooms == 1

def test_get_rooms_argen_prop_2():
    url = "https://www.argenprop.com/departamento-en-alquiler-en-villa-pueyrredon-2-ambientes--17065744"
    extractor = Extractor(url)
    rooms = extractor.get_rooms()
    print(rooms)

    assert isinstance(rooms, int)
    assert rooms == 2

def test_get_location_argen_prop():
    url = "https://www.argenprop.com/departamento-en-alquiler-en-villa-pueyrredon-2-ambientes--17065744"
    extractor = Extractor(url)
    location = extractor.get_location()
    print(location)

    assert isinstance(location, str)
    assert location == "Artigas  4600, Piso 4"

def test_get_size_argen_prop():
    url = "https://www.argenprop.com/departamento-en-alquiler-en-villa-pueyrredon-2-ambientes--17065744"
    extractor = Extractor(url)
    size = extractor.get_size()
    print(size)

    assert isinstance(size, float)
    assert size == 40