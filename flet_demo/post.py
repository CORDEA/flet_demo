import uuid

import flet as ft

from flet_demo import routes
from flet_demo.repository import repository
from flet_demo.user import User


def post(page: ft.Page):
    user = User(id=uuid.uuid4().hex, first_name='', last_name='', email='', phone='', tags=[])
    tags = []

    def on_first_name_change(e: ft.ControlEvent):
        user.first_name = e.control.value

    first_name = ft.TextField(hint_text='First name', on_change=on_first_name_change)

    def on_last_name_change(e: ft.ControlEvent):
        user.last_name = e.control.value

    last_name = ft.TextField(hint_text='Last name', on_change=on_last_name_change)

    def on_email_change(e: ft.ControlEvent):
        user.email = e.control.value

    email = ft.TextField(hint_text='Email', on_change=on_email_change)

    def on_phone_change(e: ft.ControlEvent):
        user.phone = e.control.value

    phone = ft.TextField(
        hint_text='Phone',
        on_change=on_phone_change,
        input_filter=ft.InputFilter(
            regex_string=r'[\d\+]'
        )
    )

    def on_tag_click(e: ft.ControlEvent):
        user.tags.remove(e.control.value)
        tags.remove(e.control)
        page.update()

    def on_tag_submit(e: ft.ControlEvent):
        user.tags.append(e.control.value)
        tags.append(ft.Chip(label=ft.Text(e.control.value), on_click=on_tag_click))
        e.control.value = ''
        page.update()

    def on_click(e):
        has_err = False
        if len(user.first_name) <= 0:
            first_name.error_text = 'The value is required'
            has_err = True
        else:
            first_name.error_text = ''
        if len(user.last_name) <= 0:
            last_name.error_text = 'The value is required'
            has_err = True
        else:
            last_name.error_text = ''
        if len(user.email) <= 0:
            email.error_text = 'The value is required'
            has_err = True
        else:
            email.error_text = ''
        if len(user.phone) <= 0:
            phone.error_text = 'The value is required'
            has_err = True
        else:
            phone.error_text = ''
        if has_err:
            page.update()
            return
        repository.insert(user)
        page.views.pop()
        page.go(page.views[-1].route)

    return ft.View(
        route=routes.POST,
        appbar=ft.AppBar(title=ft.Text('Post')),
        padding=ft.padding.symmetric(vertical=32, horizontal=16),
        floating_action_button=ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=on_click
        ),
        controls=[
            ft.ListView(
                expand=1,
                spacing=16,
                controls=[
                    first_name,
                    last_name,
                    ft.VerticalDivider(),
                    email,
                    phone,
                    ft.VerticalDivider(),
                    ft.TextField(hint_text='Tag', on_submit=on_tag_submit),
                    ft.Row(
                        wrap=True,
                        spacing=8,
                        run_spacing=8,
                        controls=tags,
                    )
                ]
            )
        ]
    )
