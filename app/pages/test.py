import reflex as rx

@rx.page(route='/test')
def test():
    return rx.box(
        rx.text("hi")
    )

