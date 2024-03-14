import httpx


class HttpxRequest:
    @classmethod
    async def get(
        cls, url: str, params: dict | None = None, headers: dict | None = None
    ) -> dict:
        """
        发送GET请求
        @param url: 请求URL
        @param params: 请求参数
        @param headers: 请求头
        @return: 响应内容
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()
        return response.json()

    @classmethod
    async def post(
        cls,
        url: str,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        headers: dict | None = None,
    ) -> dict:
        """
        发送POST请求
        @param url: 请求URL
        @param params: 请求参数
        @param headers: 请求头
        @return: 响应内容
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, params=params, data=data, json=json, headers=headers
            )
            response.raise_for_status()
            return response.json()
