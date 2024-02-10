import flet as ft

from flet_demo import routes
from flet_demo.repository import repository


def _tags(tags):
    if len(tags) > 0:
        return [ft.Row(
            wrap=True,
            spacing=8,
            run_spacing=8,
            controls=[ft.Chip(label=ft.Text(e)) for e in tags]
        )]
    return []


def home(page: ft.Page):
    def on_card_click(e):
        page.go(routes.DETAILS.replace(':id', '1'))

    def on_click(e):
        page.go(routes.POST)

    users = [
        ft.Card(
            content=ft.Container(
                on_click=on_card_click,
                padding=16,
                content=ft.Column(
                    spacing=12,
                    controls=[ft.Text("%s %s" % (e.first_name, e.last_name), size=24)] + _tags(e.tags)
                )
            )
        )
        for e in repository.find_all()
    ]
    return ft.View(
        route=routes.HOME,
        appbar=ft.AppBar(title=ft.Text('Home')),
        padding=ft.padding.all(16),
        floating_action_button=ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=on_click
        ),
        controls=[
            ft.ListView(controls=users)
        ]
    )
