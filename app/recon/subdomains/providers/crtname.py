from app.core.network.session import engine


async def crtname(domain: str) -> dict:
    subdomains = set()
    url = f"https://crt.name/v1/search"

    try:
        response = await engine.request('GET', url, params={"apex": domain})

        if response['success']:
            data = response['response'].text
            for item in data.splitlines():
                host = item.strip().lower()
                if host.endswith(f".{domain}") or host == domain:
                    subdomains.add(host.lstrip("*."))


            return {
                "success": True,
                "subdomains": sorted(subdomains)
            }
    except Exception as e:
        return {
            "success": False,
            "subdomains": sorted(subdomains),
            "error": f"Crtname error: {e}"
        }

