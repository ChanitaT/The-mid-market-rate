# The-mid-market-rate
This is a simple API built using **`FastAPI`** that allows users to convert currencies using real-time exchange rates. The API also provides a history of all previous conversions and a list of supported currencies.

## Installation
You will need to have Docker installed on your machine to run this application. Once you have Docker, you can build the container by running the following command in the root directory of the code:

```
docker build -t my-fastapi-app . 
```

This will build the container and give it the tag "my-fastapi-app".
## Running the application
Once the container is built, you can run it by using the following command:

```
docker run -p 8000:8000 my-fastapi-app 
```

This will start the container and map port 8000 on your host machine to port 8000 in the container.
## API documentation
The API documentation is available at _`http://localhost:8000/docs`_ once the container is running. The API has the following endpoints:

* `/convert`: This endpoint allows you to convert between different currencies. You will need to provide the following parameters: amount (float), from_currency (string), and to_currency (string). The endpoint returns a JSON object with the following fields: converted_amount (float), rate (float), and metadata (dictionary).

Example Request URL: 
```
http://localhost:8000/convert?amount=100&from_currency=USD&to_currency=EUR
```

Response body:
```
{
  "converted_amount": 92.05499999999999,
  "rate": 0.92055,
  "metadata": {
    "time_of_conversion": "2023-01-24T09:49:45.188072",
    "from_currency": "USD",
    "to_currency": "EUR"
  }
}
```

* `/currencies`: This endpoint allows you to get the supported currencies from get_exchange_rate package. You will need to provide the following parameters: from_currency (string) and to_currency (string). The endpoint returns a JSON object with the currency rate.

Example Request URL: 
```
http://127.0.0.1:8000/currencies?from_currency=USD&to_currency=EUR
```
Response body:
```
{"currency": "0.920950"}
```

* `/history`: This endpoint allows you to get the conversion history. The endpoint returns a list of JSON objects, each representing a single conversion.
