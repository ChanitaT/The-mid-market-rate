import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from get_exchange_rate import get_exchange_rate

app = FastAPI()

class Conversion(BaseModel):
    converted_amount: float
    rate: float
    metadata: dict

conversion_history = []

@app.get("/convert")
async def convert_currency(amount: float, from_currency: str, to_currency: str):
    try:
        # get the exchange rate from a reliable source
        rate = await get_exchange_rate(from_currency, to_currency)
        if rate is None:
            raise HTTPException(status_code=400, detail="Could not get exchange rate.")
        # calculate the converted amount
        converted_amount = amount * float(rate)
        # create a dictionary to hold the conversion data
        conversion_data = {
            "converted_amount": converted_amount,
            "rate": rate,
            "metadata": {
                "time_of_conversion": datetime.datetime.now().isoformat(),
                "from_currency": from_currency,
                "to_currency": to_currency
            }
        }
        # add the conversion data to the history list
        conversion_history.append(conversion_data)
        return Conversion(**conversion_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/currencies")
async def currencies(from_currency: str, to_currency: str):
    try:
        # get supported currencies from a reliable source
        rate = await get_exchange_rate(from_currency, to_currency)
        if rate is None:
            raise HTTPException(status_code=400, detail="Could not get exchange rate.")
        return {'currency': rate}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/history")
def history():
    if not conversion_history:
        raise HTTPException(status_code=204, detail="No previous conversions.")
    return conversion_history
