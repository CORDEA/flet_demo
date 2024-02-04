import flet as ft

from flet_demo import routes


def home(page: ft.Page):
    def on_click(e):
        page.go(routes.POST)

    return ft.View(
        route=routes.HOME,
        appbar=ft.AppBar(title=ft.Text('Home')),
        floating_action_button=ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=on_click
        ),
        controls=[
        ]
    )
