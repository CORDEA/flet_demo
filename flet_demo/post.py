import flet as ft

from flet_demo import routes


def post(page: ft.Page):
    return ft.View(
        route=routes.POST,
        appbar=ft.AppBar(title=ft.Text('Post')),
        controls=[
            ft.TextField(),
            ft.TextField(),
            ft.TextField()
        ]
    )
