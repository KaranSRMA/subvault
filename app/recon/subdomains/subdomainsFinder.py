from app.recon.subdomains.providers.anubisdb import anubisdb
from app.recon.subdomains.providers.crtsh import crtsh
from app.recon.subdomains.providers.dnsdumpster import dnsdumpster
from app.recon.subdomains.providers.hackertarget import hackertarget
from app.recon.subdomains.providers.rapiddns import rapiddns
from app.recon.subdomains.providers.shodan import shodan
from app.recon.subdomains.providers.crtname import crtname
from app.recon.subdomains.providers.certspotter import certspotter

from app.core.helpers.UI import UI


ui = UI()


class SubFinder:
    def __init__(self):
        self.subdomains = set()

    async def _runSubsFunctions(self, domain, funcs):
        try:
            success = False
            error = "Results not found"
            for func in funcs:
                ui.info(f"Running {func.__name__} for subdomains enumeration.")
                result = await func(domain)

                if not result['success']:
                    ui.err(result['error'])

                    if len(result['subdomains']) > 0:
                        self.subdomains.update(result['subdomains'])
                        continue
                    continue

                self.subdomains.update(result['subdomains'])
                success = True
                error = None
                ui.success(
                    f"{func.__name__} enumeration successful. Found {len(result['subdomains'])} subdomains.")
            return {
                "success": success,
                "error": error
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"[ERROR] runReconFunctions error: {e}"
            }

    async def enumerateSubdomains(self, domain):
        try:
            funcs = []
            funcs.extend([anubisdb, dnsdumpster, hackertarget,
                         rapiddns, shodan, crtsh, crtname, certspotter])

            subs = await self._runSubsFunctions(domain, funcs)

            if not subs['success']:
                return {
                    "success": False,
                    "subdomains": sorted(self.subdomains),
                    "error": subs['error']
                }

            return {
                "success": True,
                "subdomains": sorted(self.subdomains)
            }
        except Exception as e:
            return {
                "success": False,
                "subdomains": sorted(self.subdomains),
                "error": f"[ERROR] At enumerateSubdomains(): {e}"
            }
