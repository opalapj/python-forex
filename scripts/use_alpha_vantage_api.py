import io
import urllib.parse

import pandas as pd
import requests


scheme = "https"
netloc = "www.alphavantage.co"
path = "query"
query_components = {
    "function": "FX_DAILY",
    "from_symbol": "EUR",
    "to_symbol": "PLN",
    "outputsize": "full",
    "datatype": "csv",
    "apikey": "Z1WTY5DA98IEAVXG",
}


def compose_query(components):
    return urllib.parse.urlencode(components)


def compose_url(*components):
    return urllib.parse.urlunsplit((
        *components, # Scheme, netloc, path, query.
        None,  # Fragment counterpart.
    ))


def main():
    url = compose_url(
        scheme,
        netloc,
        path,
        compose_query(query_components),
    )
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text))
    print(df)


if __name__ == "__main__":
    main()
