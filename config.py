# URL pattern of the website
# f"https://wise.com/gb/send-money/?sourceCurrency={from_currency}&targetCurrency={to_currency}&sourceAmount={amount}"
URL_WISE = "https://wise.com/gb/send-money/?"
FROM_WISE = "sourceCurrency="
TO_WISE = "&targetCurrency="
AMOUNT_WISE = "&sourceAmount="
# f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}"
URL_XE = "https://www.xe.com/currencyconverter/convert/?"
AMOUNT_XE = "Amount="
FROM_XE = "&From="
TO_XE = "&To="

# HTML tag and class for scraping of wise.come 
TAG_WISE = "span"
CLASS_WISE = "tw-calculator-breakdown-rate__value"

# HTML tag and class for scraping of www.xe.com
TAG_XE = "div"
CLASS_XE = "unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx"

# define a list of proxy IPs
PROXY_IPS = ["192.168.0.1:8080", "192.168.0.2:8080", "192.168.0.3:8080"]