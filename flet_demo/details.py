import flet as ft

from flet_demo import routes
from flet_demo.repository import repository


def details(page: ft.Page, uid: int):
    user = repository.find(uid)
    return ft.View(
        route=routes.DETAILS.replace(':id', str(uid)),
        appbar=ft.AppBar(title=ft.Text("%s %s" % (user.first_name, user.last_name))),
        padding=ft.padding.symmetric(vertical=32, horizontal=16),
        controls=[
            ft.ListView(
                expand=1,
                spacing=16,
                controls=[
                ]
            )
        ]
    )
