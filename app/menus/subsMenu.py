import asyncio
from datetime import datetime
from app.core.helpers.UI import UI
from app.recon.subdomains.subdomainsFinder import SubFinder

ui = UI()
subfinder = SubFinder()


def subsMenu(domain):
    while True:

        result = asyncio.run(subfinder.enumerateSubdomains(domain))

        if not result['success']:
            ui.err(result['error'])
            return

        if len(result['subdomains']) <= 0:
            ui.warn("No result found!")
            return


        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{domain}_subdomains_{timestamp}.txt"


        with open(filename, "w") as file:
            for subs in result['subdomains']:
                file.write(subs + "\n")

        ui.success(
            f"Saved {len(result['subdomains'])} subdomains to {filename}")
        break
