from app.core.network.session import engine


async def anubisdb(domain: str) -> set[str]:
    subdomains = set()
    url = f"https://anubisdb.com/subdomains/{domain}"

    try:
        response = await engine.request('GET', url)
        if response['success']:
            data = response['response'].json()
            for item in data:
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
            "error": f"Anubisdb error: {e}"
        }
