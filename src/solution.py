from __future__ import annotations

from itertools import chain
from typing import cast

from model import Route
from queries import Queries
from common.repository import Repository


class Solution(Repository, Queries):

    @staticmethod
    def type_mapper(values: dict[str, any]) -> Route | Route.Flight:
        match values:
            case {"country": _}:
                route = Route(**values)
                route.operator = next(
                    Route.Airline[entry.name]
                    for entry in Route.Airline
                    if entry.value == route.operator
                )
                return route
            case {"registration": _}:
                return Route.Flight(**values)

    @property
    def entities(self) -> list[Route]:
        return cast(list[Route], super().entities)

    def group_by_airline(self) -> dict[Route.Airline, list[Route]]:
        return {
            airline: [
                route
                for route in self.entities
                if route.operator == airline
            ]
            for airline in {
                route.operator
                for route in self.entities
            }
        }

    def count_of_countries(self, airline: Route.Airline) -> int:
        return len(
            {
                route.country
                for route in self.entities
                if route.operator == airline
            }
        )

    def order(self) -> list[Route]:
        return sorted(
            self.entities,
            key=lambda route: (route.country, route.operator)
        )

    def get_registrations(self) -> set[str]:
        return {
            flight.registration
            for flight in chain.from_iterable(
                [
                    route.flights
                    for route in self.entities
                ]
            )
        }

    def get_routes_having_delay(self) -> Route:
        return next(
            route
            for route in self.entities
            if sum([
                flight.delay
                for flight in route.flights
            ]) >= 15
        )


def main() -> None:
    repository = Solution(r"../data/routes.json")

    for lego_set in repository.entities:
        print(lego_set)

    print("===")
    # TODO invocations go here


if __name__ == "__main__":
    main()
