import httpx
from typing import Any

from app.config.config import CONFIG


class RequestEngine:
    def __init__(self):
        self.client = httpx.AsyncClient(follow_redirects=CONFIG["network"]["follow_redirects"],
                                         http2=CONFIG["network"]["http2"],
                                         headers=CONFIG["headers"],
                                         timeout=CONFIG["network"]["timeout"],)

    # Request
    async def request(self,
                       method: str,
                       url: str,
                       *,
                       data: Any | None = None,
                       json: Any | None = None,
                       params: dict[str, Any] | None = None,
                       headers: dict[str, str] | None = None,
                       cookies: dict[str, str] | None = None,
                       follow_redirects: bool | None = None,
                       timeout: float | httpx.Timeout | None = None,
                       **kwargs: Any):

        try:

            response = await self.client.request(method=method,
                                                 url=url,
                                                 data=data,
                                                 json=json,
                                                 params=params,
                                                 headers=headers,
                                                 cookies=cookies,
                                                 follow_redirects=follow_redirects,
                                                 timeout=timeout,
                                                 **kwargs,)

            return {
                "success": True,
                "response": response,
                "error": None,
            }

        except httpx.TimeoutException as e:
            return {
                "success": False,
                "response": None,
                "error": {
                    "type": "timeout",
                    "message": str(e),
                },
            }

        except httpx.ConnectError as e:
            return {
                "success": False,
                "response": None,
                "error": {
                    "type": "connect_error",
                    "message": str(e),
                },
            }

        except httpx.HTTPError as e:
            return {
                "success": False,
                "response": None,
                "error": {
                    "type": "http_error",
                    "message": str(e),
                },
            }

        except Exception as e:
            return {
                "success": False,
                "response": None,
                "error": {
                    "type": "unknown",
                    "message": str(e),
                },
            }

