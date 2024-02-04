import flet as ft
from flet_core import TemplateRoute

from flet_demo import routes
from flet_demo.details import details
from flet_demo.home import home
from flet_demo.post import post


def main(page: ft.Page):
    def on_route_change(e):
        page.views.clear()
        page.views.append(home(page))
        tr = TemplateRoute(page.route)
        if tr.match(routes.POST):
            page.views.append(post(page))
        if tr.match(routes.DETAILS):
            page.views.append(details(page, tr.id))
        page.update()

    def on_view_pop(e):
        page.views.pop()
        page.go(page.views[-1].route)

    page.on_route_change = on_route_change
    page.on_view_pop = on_view_pop
    page.go(page.route)


ft.app(target=main)
