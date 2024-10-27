import reflex as rx

@rx.page(route='/test2')
def test2():
    return rx.box(
        rx.text("test2")
    )