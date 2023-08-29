from typing import Dict, Callable
from .router import Router

RouteFuncT = Callable[[], str]
FuncT = Callable[[], None]

class FastCLI:
    def __init__(self):
        self.router = Router()

    def register(self, route: str) -> Callable[[RouteFuncT], RouteFuncT]:
        return self.router.register(route)

    def include_router(self, route: str, router: Router):
        return self.router.include_router(route, router)

    def run(self):
        while True:
            raw_input = input('> ')
            request = raw_input.split()
            response = self.router.route(request)

            if response:
                print(response)
            else:
                print('Route not found')
