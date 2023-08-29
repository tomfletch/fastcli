from __future__ import annotations
from typing import Dict, Callable, List

RouteFuncT = Callable[[], str]
FuncT = Callable[[], None]

class Router:
    routes: Dict[str, Callable[[], None]] = {}

    def register(self, route: str) -> Callable[[RouteFuncT], RouteFuncT]:
        def decorator(func: RouteFuncT) -> RouteFuncT:
            self.routes[route] = func
            return func
        return decorator
    
    def include_router(self, route: str, router: Router):
        self.routes[route] = router

    def route(self, request: List[str]) -> str:
        if len(request) == 0:
            this_route = ''
        else:
            this_route = request[0]
        
        if this_route not in self.routes:
            return None

        registered_route = self.routes[this_route]

        if isinstance(registered_route, Router):
            return registered_route.route(request[1:])

        return registered_route()
