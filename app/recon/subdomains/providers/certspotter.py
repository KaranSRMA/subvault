from app.core.network.session import engine

async def certspotter(domain: str) -> dict:
    subdomains = set()
    url = f"https://api.certspotter.com/v1/issuances"

    try:
        response = await engine.request('GET', url, params={"domain": domain, "include_subdomains":True, "expand":"dns_names"})

        if response['success']:
            data = response['response'].json()
            for item in data:
                for subs in item["dns_names"]:
                    host = subs.strip().lower()
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
            "error": f"Certspotter error: {e}"
        }
