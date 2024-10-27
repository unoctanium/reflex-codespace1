import reflex as rx

class State(rx.State):
    text: str = "Test2"
    color: str = "red"

    def flip_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"


@rx.page(route='/test2')
def test2():
    return rx.box(
        rx.badge(
            State.text,
            color_scheme = State.color,
            on_click = State.flip_color,
        ),
    )

class Test3Component(rx.ComponentState):
    text: str = "test3.2"
    color: str = "red"

    def flip_color(self):
        if self.color == "red":
            self.color = "white"
        else:
            self.color = "red"
        
    @classmethod
    def get_component(cls, **props):
        return rx.button(
            cls.text, 
            color = cls.color,
            on_click = cls.flip_color,
            **props
        )

test3_component = Test3Component.create()

@rx.page(route="/test3")
def test3():
    return rx.box(
        test3_component,
    )

