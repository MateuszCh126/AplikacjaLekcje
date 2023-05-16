from flet import *
from views import views_handler
def main(page: Page):
    pass

    def rout_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            View(
                views_handler(page)[page.route]
            )
        )


        page.on_route_change=rout_change
        page.go('/login')
app(target=main)