#!/usr/bin/env python3

from app.menus.subsMenu import subsMenu
from app.core.helpers.UI import UI

ui = UI()


def main():
    while True:
        ui.warn("Enter a single domain to discover its subdomains.")
        domain = ui.get_input("Type domain here")
        if not domain:
            ui.err("Domain is required")
            break

        subsMenu(domain)

if __name__ == "__main__":
    main()