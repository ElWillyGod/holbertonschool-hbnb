
'''
    Defines the city class.
    A city contains places and is inside a country.
    The name must also be unique in the same country.
'''

from trackedobject import TrackedObject
from validationlib import doesCountryExist, isCityNameDuplicated
from logicexceptions import CountryNotFoundError, CityNameDuplicated


class City(TrackedObject):
    """
        City Class.
    """

    def __init__(self,
                 name: str,
                 country_code: str,
                 *,
                 id: str = None,
                 created_at: str = None,
                 updated_at: str = None):
        super().__init__(id, created_at, updated_at)

        if not doesCountryExist(country_code):
            raise CountryNotFoundError(f"country '{country_code}' not found")
        self.country_code = country_code

        if isCityNameDuplicated(name, country_code):
            raise CityNameDuplicated(
                f"{name} already exists in {country_code}")
        self.name = name
