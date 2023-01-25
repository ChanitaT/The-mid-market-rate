import asyncio
from scraper import get_exchange_rate_wise, get_exchange_rate_xe

async def get_exchange_rate_from_wise(from_currency, to_currency):
    result = get_exchange_rate_wise(amount=1, from_currency=from_currency, to_currency=to_currency)
    return result['rate']

async def get_exchange_rate_from_xe(from_currency, to_currency):
    result = get_exchange_rate_xe(amount=1, from_currency=from_currency, to_currency=to_currency)
    return result['rate']

async def get_exchange_rate(from_currency, to_currency):
    rate, _ = await asyncio.gather(
        get_exchange_rate_from_wise(from_currency, to_currency),
        get_exchange_rate_from_xe(from_currency, to_currency), 
        return_exceptions=True
        )
    return rate
