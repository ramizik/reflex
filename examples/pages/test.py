import reflex as rx

class FormState(rx.State):
    form_data: dict = {}
    slider_values: list[float] = [20, 80]

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

@rx.page(route='/test')
def test_page() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.slider(
                    default_value=FormState.slider_values,
                    min=0,
                    max=100,
                    step=1,
                    name="slider-1"
                ),
                rx.slider(
                    default_value=FormState.slider_values,
                    min=0,
                    max=100,
                    step=1,
                    id = "slider-2"
                ),
                rx.button("Submit", type="submit"),

            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )