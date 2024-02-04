import flet as ft


def home(page: ft.Page):
    def on_click(e):
        page.update()

    return ft.View(
        '/',
        [
            ft.ElevatedButton(
                text='Hello World',
                on_click=on_click,
            )
        ]
    )
