from datetime import date

import forex_python.converter


forex_python.converter.get_rates("PLN")
forex_python.converter.get_rate("PLN", "USD")

date_obj = date.fromisoformat("2026-02-26")  # Thu
date_obj = date.fromisoformat("2026-02-27")  # Fri
date_obj = date.fromisoformat("2026-02-28")  # Sat
date_obj = date.fromisoformat("2026-03-01")  # Sun
date_obj = date.fromisoformat("2026-03-02")  # Mon
date_obj = date.fromisoformat("2026-03-03")  # Tue
date_obj = date.fromisoformat("2026-03-04")  # Wed

forex_python.converter.get_rate("PLN", "USD", date_obj)
forex_python.converter.get_rate("USD", "PLN", date_obj)

{
    c: round(1 / r, 4)
    for (c, r) in forex_python.converter.get_rates("PLN", date_obj).items()
    if c in ["USD", "EUR", "CHF", "GBP"]
}
