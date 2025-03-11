from geopy.geocoders import Nominatim


class Transformer:
    def __init__(self, data):
        self.data = data

    def get_coordinates(self):
        geolocator = Nominatim(user_agent="etl_rental_123")
        try:
            location = geolocator.geocode(self.data["location"])

            if location:
                return (location.latitude, location.longitude)
            else:
                print(f'No se pudieron obtener las coordenadas de {self.data["url"]}')
                return None
        except:
            print(f'No se pudieron obtener las coordenadas de {self.data["url"]}')
            return None

    def get_data(self):
        data = self.data
        data["full_price"] = data["price"] + data["bills"]
        data["coordinates"] = self.get_coordinates()
        return data
