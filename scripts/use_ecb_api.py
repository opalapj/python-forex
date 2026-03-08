import io
import urllib.parse

import pandas as pd
import requests


protocol = "https"
wsEntryPoint = "data-api.ecb.europa.eu/service"
resource = "data"
flowRef = "EXR"
key_components = {
    "the_frequency_at_which_they_are_measured": "D",  # (e.g. daily – code D)
    "the_currency_being_measured": "PLN",  # (e.g. US dollar – code USD)
    "the_currency_against_which_the_above_currency_is_being_measured": "EUR",  # (e.g. euro – code EUR)
    "the_type_of_exchange_rates": "SP00",  # (e.g. foreign exchange reference rates – code SP00)
    "the_time_series_variation": "A",  # (e.g. average or standardised measure for a given frequency – code A)
}
parameters_components = {
    "format": "csvdata",
    "startPeriod": "2025-01-01",
    "endPeriod": "2026-01-01",
}


def compose_key(components):
    return ".".join(components.values())


def compose_parameters(components):
    return urllib.parse.urlencode(components)


def compose_path(*components):
    return "/".join(components)


def compose_url(*components):
    return urllib.parse.urlunsplit((
        *components, # Scheme, netloc, path, query.
        None,  # Fragment counterpart.
    ))


def main():
    url = compose_url(
        protocol,  # Scheme counterpart.
        wsEntryPoint,  # Netloc counterpart.
        compose_path(resource, flowRef, compose_key(key_components)),  # Path counterpart.
        compose_parameters(parameters_components),  # Query counterpart.
    )
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text))
    print(df)


if __name__ == "__main__":
    main()
