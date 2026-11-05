from bs4 import BeautifulSoup
import json

from app.core.network.session import engine


def parse_dnsdumpster(html: str, domain: str) -> set[str]:
    subdomains = set()

    soup = BeautifulSoup(html, "html.parser")

    for row in soup.find_all("tr"):
        cols = row.find_all("td")

        if not cols:
            continue

        host = cols[0].get_text(strip=True).lower()

        if host == domain or host.endswith(f".{domain}"):
            subdomains.add(host.removeprefix("*."))

    return subdomains


# for api.dnsdumpster.com/htmld/ which needs jwt 
# async def get_jwt() -> str:
#     url = "https://dnsdumpster.com/"
#     response = await engine.request('GET', url)
#     if response['success']:
#         html = response['response'].text
#         soup = BeautifulSoup(html, "html.parser")

#         form = soup.find("form", {"data-form-id": "mainform"})
#         headers = json.loads(form["hx-headers"])
#         jwt = headers["Authorization"]

#         return jwt
#     return False


async def dnsdumpster(domain: str) -> set[str]:
    url = "https://dnsdumpster.com/htmld/"

    # jwt = await get_jwt()
    # if not jwt:
    #     return {
    #         "success": False,
    #         "error": f"[ERROR] dnsdumpster error: JWT token not found"
    #     }

    try:
        response = await engine.request(
            'POST',
            url,
            data={"target": domain})

        
        if response['success']:
            html = response['response'].text
            subdomains = parse_dnsdumpster(html, domain)
            return {
                "success": True,
                "subdomains": sorted(subdomains)
            }

    except Exception as e:
        return {
            "success": False,
            "subdomains": sorted(subdomains),
            "error": f"dnsdumpster error: {e}"
        }
