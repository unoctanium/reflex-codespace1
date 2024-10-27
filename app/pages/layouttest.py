import reflex as rx


@rx.page(route="/layouttest")
def layouttest():
    return rx.fragment(
        rx.flex(
            rx.card("Card1"),
            rx.card("Card2"),
            spacing="2",
            width="100%",
            min_height="100px",
            flex_direction="column",

        )
    )