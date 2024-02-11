import flet as ft

from flet_demo import routes
from flet_demo.repository import repository


def details(page: ft.Page, uid: str):
    user = repository.find(uid)
    return ft.View(
        route=routes.DETAILS.replace(':id', uid),
        appbar=ft.AppBar(title=ft.Text("%s %s" % (user.first_name, user.last_name))),
        padding=ft.padding.symmetric(vertical=32, horizontal=16),
        controls=[
            ft.ListView(
                expand=1,
                spacing=16,
                controls=[
                    ft.Text('Email'),
                    ft.Container(
                        padding=ft.padding.only(bottom=8, left=16, right=16),
                        content=ft.Text(user.email, size=24),
                    ),
                    ft.Text('Phone'),
                    ft.Container(
                        padding=ft.padding.only(bottom=8, left=16, right=16),
                        content=ft.Text(user.phone, size=24),
                    ),
                    ft.Text('Tag'),
                    ft.Row(
                        wrap=True,
                        spacing=8,
                        run_spacing=8,
                        controls=[ft.Chip(label=ft.Text(r)) for r in user.tags],
                    )
                ]
            )
        ]
    )
