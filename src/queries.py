from abc import abstractmethod, ABC

from model import Route


class Queries(ABC):
    """
    Defines queries that deal with flight routes.
    """

    @abstractmethod
    def count_of_countries(self, airline: Route.Airline) -> int:
        """
        Returns the count of distinct countries of flights operated by the given airline.

        :param airline: the airline
        :return: the count
        """

    @abstractmethod
    def order(self) -> list[Route]:
        """
        Returns a copy of the routes ordered by:

        * the country in ascending order
        * the operator in ascending order

        :return: the sorted list
        """

    @abstractmethod
    def group_by_airline(self) -> dict[Route.Airline, list[Route]]:
        """
        Groups the routes by the operators.

        :return: the grouping
        """

    @abstractmethod
    def get_registrations(self) -> set[str]:
        """
        Returns the registrations of aircrafts.

        :return: the registrations
        """

    @abstractmethod
    def get_routes_having_delay(self) -> Route:
        """
        Returns the first route which total delay is greater than 15 minutes.

        :return: the route
        """
