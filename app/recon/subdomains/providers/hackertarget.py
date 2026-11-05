from app.core.network.session import engine


async def hackertarget(domain: str) -> set[str]:
    subdomains = set()
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"

    try:
        response = await engine.request('GET', url)
        if response['success']:
            data = response['response'].text.splitlines()
            for item in data:
                if not item.strip():
                    continue

                subdomain = item.split(",")[0]
                host = subdomain.strip().lower()
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
            "error": f"hackertarget error: {e}"
        }
