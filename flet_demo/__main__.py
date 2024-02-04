import flet as ft

from flet_demo.home import home


def main(page: ft.Page):
    def on_route_change(e):
        page.views.clear()
        page.views.append(home(page))
        page.update()

    def on_view_pop():
        page.views.pop()
        page.go(page.views[-1].route)

    page.appbar = ft.AppBar(title=ft.Text('Flet Demo'))
    page.padding = ft.padding.all(16)
    page.on_route_change = on_route_change
    page.on_view_pop = on_view_pop
    page.go(page.route)


ft.app(target=main)
