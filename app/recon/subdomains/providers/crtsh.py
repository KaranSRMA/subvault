from app.core.network.session import engine


async def crtsh(domain: str) -> set[str]:
    subdomains = set()
    url = f"https://crt.sh/?q=%.{domain}&output=json"

    try:
        response = await engine.request('GET', url)
        if response['success']:
            data = response['response'].json()
            for entry in data:
                name_value = entry.get("name_value", "")
                for host in name_value.split("\n"):
                    host = host.strip().lower()
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
            "error": f"crt.sh error: {e}"
        }
