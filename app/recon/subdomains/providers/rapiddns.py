from bs4 import BeautifulSoup
from app.core.network.session import engine


def parse_rapiddns(html: str, domain: str) -> set[str]:
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


async def rapiddns(domain: str) -> set[str]:
    url = f"https://rapiddns.io/subdomain/{domain}"

    try:
        response = await engine.request('GET', url)
        if response['success']:
            html = response['response'].text
            subdomains = parse_rapiddns(html, domain)
            return {
                "success": True,
                "subdomains": sorted(subdomains)
            }

    except Exception as e:
        return {
            "success": False,
            "subdomains": sorted(subdomains),
            "error": f"rapiddns error: {e}"
        }
