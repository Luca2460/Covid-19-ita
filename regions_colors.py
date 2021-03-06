"""Simple script to compute how many people are subject to a given color restriction on a given day

It takes advantage of the data at https://it.wikipedia.org/wiki/Gestione_della_pandemia_di_COVID-19_in_Italia
(bottom of the page)
"""

# ("date", +1 or -1, region name, color)

# Trento and Bolzano have been ignored as few people live there compared to a whole italian region.

data = [("2020-12-20", 1, "valle", "y"), 
        ("2020-12-24", -1, "valle", "y"), 
        ("2021-01-11", 1, "valle", "y"),
        ("2021-01-17", -1, "valle", "y"),
        ("2021-02-01", 1, "valle", "y"),
        ("2021-03-15", -1, "valle", "y"),
        ("2021-05-24", 1, "valle", "y"),
        ("2021-06-28", -1, "valle", "y"),
        ("2022-01-10", 1, "valle", "y"),
        ("2022-01-17", -1, "valle", "y"),
        ("2022-02-21", 1, "valle", "y"),
        ("2022-03-14", -1, "valle", "y"),
        ("2020-12-13", 1, "piemonte", "y"),
        ("2020-12-24", -1, "piemonte", "y"),
        ("2021-01-11", 1, "piemonte", "y"),
        ("2021-01-17", -1, "piemonte", "y"),
        ("2021-02-01", 1, "piemonte", "y"),
        ("2021-03-01", -1, "piemonte", "y"),
        ("2021-04-26", 1, "piemonte", "y"),
        ("2021-06-14", -1, "piemonte", "y"),
        ("2022-01-03", 1, "piemonte", "y"),
        ("2022-01-24", -1, "piemonte", "y"),
        ("2022-02-21", 1, "piemonte", "y"),
        ("2022-03-07", -1, "piemonte", "y"),
        ("2020-11-06", 1, "liguria", "y"),
        ("2020-11-11", -1, "liguria", "y"),
        ("2020-11-29", 1, "liguria", "y"),
        ("2020-12-24", -1, "liguria", "y"),
        ("2021-01-11", 1, "liguria", "y"),
        ("2021-01-17", -1, "liguria", "y"),
        ("2021-02-01", 1, "liguria", "y"),
        ("2021-02-14", -1, "liguria", "y"),
        ("2021-03-01", 1, "liguria", "y"),
        ("2021-03-15", -1, "liguria", "y"),
        ("2021-04-26", 1, "liguria", "y"),
        ("2021-06-07", -1, "liguria", "y"),
        ("2021-12-20", 1, "liguria", "y"),
        ("2022-03-14", -1, "liguria", "y"),
        ("2020-12-13", 1, "lombardia", "y"),
        ("2020-12-24", -1, "lombardia", "y"),
        ("2021-02-01", 1, "lombardia", "y"),
        ("2021-03-01", -1, "lombardia", "y"),
        ("2021-04-26", 1, "lombardia", "y"),
        ("2021-06-14", -1, "lombardia", "y"),
        ("2022-01-03", 1, "lombardia", "y"),
        ("2021-02-28", -1, "lombardia", "y"),
        ("2020-11-06", 1, "veneto", "y"),
        ("2020-12-24", -1, "veneto", "y"),
        ("2021-02-01", 1, "veneto", "y"),
        ("2021-03-08", -1, "veneto", "y"),
        ("2021-04-26", 1, "veneto", "y"),
        ("2021-06-07", -1, "veneto", "y"),
        ("2021-12-21", 1, "veneto", "y"),
        ("2022-02-28", -1, "veneto", "y"),
        ("2020-11-06", 1, "friuli", "y"),
        ("2020-11-15", -1, "friuli", "y"),
        ("2020-12-06", 1, "friuli", "y"),
        ("2020-12-24", -1, "friuli", "y"),
        ("2021-01-11", 1, "friuli", "y"),
        ("2021-01-17", -1, "friuli", "y"),
        ("2021-02-01", 1, "friuli", "y"),
        ("2021-03-15", -1, "friuli", "y"),
        ("2021-04-26", 1, "friuli", "y"),
        ("2021-05-31", -1, "friuli", "y"),
        ("2021-11-29", 1, "friuli", "y"),
        ("2022-01-24", -1, "friuli", "y"),
        ("2022-02-28", 1, "friuli", "y"),
        ("2022-03-14", -1, "friuli", "y"),
        ("2020-11-06", 1, "emilia", "y"),
        ("2020-11-15", -1, "emilia", "y"),
        ("2020-12-06", 1, "emilia", "y"),
        ("2020-12-24", -1, "emilia", "y"),
        ("2021-02-01", 1, "emilia", "y"),
        ("2021-02-21", -1, "emilia", "y"),
        ("2021-04-26", 1, "emilia", "y"),
        ("2021-06-14", -1, "emilia", "y"),
        ("2022-01-10", 1, "emilia", "y"),
        ("2022-03-14", -1, "emilia", "y"),
        ("2020-11-06", 1, "toscana", "y"),
        ("2020-11-11", -1, "toscana", "y"),
        ("2020-12-20", 1, "toscana", "y"),
        ("2020-12-24", -1, "toscana", "y"),
        ("2021-01-11", 1, "toscana", "y"),
        ("2021-02-14", -1, "toscana", "y"),
        ("2021-04-26", 1, "toscana", "y"),
        ("2021-06-21", -1, "toscana", "y"),
        ("2022-01-10", 1, "toscana", "y"),
        ("2022-03-14", -1, "toscana", "y"),
        ("2020-11-06", 1, "umbria", "y"),
        ("2020-11-11", -1, "umbria", "y"),
        ("2020-12-06", 1, "umbria", "y"),
        ("2020-12-24", -1, "umbria", "y"),
        ("2021-01-11", 1, "umbria", "y"),
        ("2021-01-17", -1, "umbria", "y"),
        ("2021-04-26", 1, "umbria", "y"),
        ("2021-06-07", -1, "umbria", "y"),
        ("2020-11-06", 1, "marche", "y"),
        ("2020-11-15", -1, "marche", "y"),
        ("2020-12-06", 1, "marche", "y"),
        ("2020-12-24", -1, "marche", "y"),
        ("2021-01-11", 1, "marche", "y"),
        ("2021-01-17", -1, "marche", "y"),
        ("2021-02-01", 1, "marche", "y"),
        ("2021-03-01", -1, "marche", "y"),
        ("2021-04-26", 1, "marche", "y"),
        ("2021-06-21", -1, "marche", "y"),
        ("2021-12-21", 1, "marche", "y"),
        ("2022-02-07", -1, "marche", "y"),
        ("2022-02-21", 1, "marche", "y"),
        ("2022-03-21", -1, "marche", "y"),
        ("2020-11-06", 1, "lazio", "y"),
        ("2020-12-24", -1, "lazio", "y"),
        ("2021-01-11", 1, "lazio", "y"),
        ("2021-01-17", -1, "lazio", "y"),
        ("2021-02-01", 1, "lazio", "y"),
        ("2021-03-15", -1, "lazio", "y"),
        ("2021-04-26", 1, "lazio", "y"),
        ("2021-06-14", -1, "lazio", "y"),
        ("2022-01-03", 1, "lazio", "y"),
        ("2022-03-21", -1, "lazio", "y"),
        ("2020-11-06", 1, "abruzzo", "y"),
        ("2020-11-11", -1, "abruzzo", "y"),
        ("2021-01-11", 1, "abruzzo", "y"),
        ("2021-01-17", -1, "abruzzo", "y"),
        ("2021-02-01", 1, "abruzzo", "y"),
        ("2021-02-13", -1, "abruzzo", "y"),
        ("2021-04-26", 1, "abruzzo", "y"),
        ("2021-06-07", -1, "abruzzo", "y"),
        ("2022-01-10", 1, "abruzzo", "y"),
        ("2022-01-24", -1, "abruzzo", "y"),
        ("2022-02-21", 1, "abruzzo", "y"),
        ("2022-03-07", -1, "abruzzo", "y"),
        ("2020-11-06", 1, "molise", "y"),
        ("2020-12-24", -1, "molise", "y"),
        ("2021-01-11", 1, "molise", "y"),
        ("2021-02-21", -1, "molise", "y"),
        ("2021-04-26", 1, "molise", "y"),
        ("2021-05-30", -1, "molise", "y"),
        ("2022-02-14", 1, "molise", "y"),
        ("2022-03-14", -1, "molise", "y"),
        ("2020-11-06", 1, "campania", "y"),
        ("2020-11-15", -1, "campania", "y"),
        ("2021-01-11", 1, "campania", "y"),
        ("2021-02-21", -1, "campania", "y"),
        ("2021-04-26", 1, "campania", "y"),
        ("2021-06-21", -1, "campania", "y"),
        ("2022-01-17", 1, "campania", "y"),
        ("2022-02-28", -1, "campania", "y"),
        ("2020-12-06", 1, "puglia", "y"),
        ("2020-12-24", -1, "puglia", "y"),
        ("2021-01-11", 1, "puglia", "y"),
        ("2021-01-17", -1, "puglia", "y"),
        ("2021-02-11", 1, "puglia", "y"),
        ("2021-03-15", -1, "puglia", "y"),
        ("2021-05-10", 1, "puglia", "y"),
        ("2021-06-14", -1, "puglia", "y"),
        ("2021-01-24", 1, "puglia", "y"),
        ("2021-03-14", -1, "puglia", "y"),
        ("2020-11-06", 1, "basilicata", "y"),
        ("2020-11-11", -1, "basilicata", "y"),
        ("2020-12-13", 1, "basilicata", "y"),
        ("2020-12-24", -1, "basilicata", "y"),
        ("2021-01-11", 1, "basilicata", "y"),
        ("2021-03-01", -1, "basilicata", "y"),
        ("2021-05-10", 1, "basilicata", "y"),
        ("2021-06-21", -1, "basilicata", "y"),
        ("2020-12-13", 1, "calabria", "y"),
        ("2020-12-24", -1, "calabria", "y"),
        ("2021-02-01", 1, "calabria", "y"),
        ("2021-03-15", -1, "calabria", "y"),
        ("2021-05-10", 1, "calabria", "y"),
        ("2021-06-21", -1, "calabria", "y"),
        ("2021-12-13", 1, "calabria", "y"),
        ("2022-03-21", -1, "calabria", "y"),
        ("2020-11-29", 1, "sicilia", "y"),
        ("2020-12-24", -1, "sicilia", "y"),
        ("2021-02-15", 1, "sicilia", "y"),
        ("2021-03-15", -1, "sicilia", "y"),
        ("2021-05-17", 1, "sicilia", "y"),
        ("2021-06-21", -1, "sicilia", "y"),
        ("2021-08-30", 1, "sicilia", "y"),
        ("2021-10-09", -1, "sicilia", "y"),
        ("2022-01-03", 1, "sicilia", "y"),
        ("2022-01-24", -1, "sicilia", "y"),
        ("2022-02-14", 1, "sicilia", "y"),
        ("2022-03-14", -1, "sicilia", "y"),
        ("2020-11-06", 1, "sardegna", "y"),
        ("2020-12-24", -1, "sardegna", "y"),
        ("2021-01-11", 1, "sardegna", "y"),
        ("2021-01-24", -1, "sardegna", "y"),
        ("2021-02-08", 1, "sardegna", "y"),
        ("2021-03-01", -1, "sardegna", "y"),
        ("2021-05-17", 1, "sardegna", "y"),
        ("2021-05-31", -1, "sardegna", "y"),
        ("2022-01-24", 1, "sardegna", "y"),
        ("2022-03-28", -1, "sardegna", "y"),
        ("2020-12-16", 1, "valle", "o"),
        ("2020-12-20", -1, "valle", "o"),
        ("2021-01-17", 1, "valle", "o"),
        ("2021-02-01", -1, "valle", "o"),
        ("2021-03-15", 1, "valle", "o"),
        ("2021-03-29", -1, "valle", "o"),
        ("2021-04-26", 1, "valle", "o"),
        ("2021-05-03", -1, "valle", "o"),
        ("2021-05-10", 1, "valle", "o"),
        ("2021-05-24", -1, "valle", "o"),
        ("2022-01-17", 1, "valle", "o"),
        ("2022-02-21", -1, "valle", "o"),
        ("2020-11-29", 1, "piemonte", "o"),
        ("2020-12-13", -1, "piemonte", "o"),
        ("2021-01-17", 1, "piemonte", "o"),
        ("2021-02-01", -1, "piemonte", "o"),
        ("2021-03-01", 1, "piemonte", "o"),
        ("2021-03-15", -1, "piemonte", "o"),
        ("2021-04-12", 1, "piemonte", "o"),
        ("2021-04-26", -1, "piemonte", "o"),
        ("2022-01-24", 1, "piemonte", "o"),
        ("2022-02-21", -1, "piemonte", "o"),
        ("2020-11-11", 1, "liguria", "o"),
        ("2020-11-29", -1, "liguria", "o"),
        ("2021-01-17", 1, "liguria", "o"),
        ("2021-02-01", -1, "liguria", "o"),
        ("2021-02-14", 1, "liguria", "o"),
        ("2021-03-01", -1, "liguria", "o"),
        ("2021-03-15", 1, "liguria", "o"),
        ("2021-04-26", -1, "liguria", "o"),
        ("2020-11-29", 1, "lombardia", "o"),
        ("2020-12-13", -1, "lombardia", "o"),
        ("2021-01-11", 1, "lombardia", "o"),
        ("2021-01-17", -1, "lombardia", "o"),
        ("2021-01-24", 1, "lombardia", "o"),
        ("2021-02-01", -1, "lombardia", "o"),
        ("2021-03-01", 1, "lombardia", "o"),
        ("2021-03-15", -1, "lombardia", "o"),
        ("2021-04-12", 1, "lombardia", "o"),
        ("2021-04-25", -1, "lombardia", "o"),
        ("2021-01-11", 1, "veneto", "o"),
        ("2021-02-01", -1, "veneto", "o"),
        ("2021-03-08", 1, "veneto", "o"),
        ("2021-03-15", -1, "veneto", "o"),
        ("2021-04-06", 1, "veneto", "o"),
        ("2021-04-26", -1, "veneto", "o"),
        ("2020-11-15", 1, "friuli", "o"),
        ("2020-12-06", -1, "friuli", "o"),
        ("2021-01-17", 1, "friuli", "o"),
        ("2021-02-01", -1, "friuli", "o"),
        ("2021-03-08", 1, "friuli", "o"),
        ("2021-03-15", -1, "friuli", "o"),
        ("2021-04-12", 1, "friuli", "o"),
        ("2021-04-26", -1, "friuli", "o"),
        ("2022-01-24", 1, "friuli", "o"),
        ("2022-02-28", -1, "friuli", "o"),
        ("2020-11-15", 1, "emilia", "o"),
        ("2020-12-06", -1, "emilia", "o"),
        ("2021-01-11", 1, "emilia", "o"),
        ("2021-02-01", -1, "emilia", "o"),
        ("2021-02-21", 1, "emilia", "o"),
        ("2021-03-15", -1, "emilia", "o"),
        ("2021-04-12", 1, "emilia", "o"),
        ("2021-04-26", -1, "emilia", "o"),
        ("2020-11-11", 1, "umbria", "o"),
        ("2020-12-04", -1, "umbria", "o"),
        ("2021-01-17", 1, "umbria", "o"),
        ("2021-04-26", -1, "umbria", "o"),
        ("2020-11-15", 1, "marche", "o"),
        ("2020-12-06", -1, "marche", "o"),
        ("2021-01-17", 1, "marche", "o"),
        ("2021-02-01", -1, "marche", "o"),
        ("2021-03-01", 1, "marche", "o"),
        ("2021-03-15", -1, "marche", "o"),
        ("2021-04-06", 1, "marche", "o"),
        ("2021-04-26", -1, "marche", "o"),
        ("2022-02-07", 1, "marche", "o"),
        ("2022-02-21", -1, "marche", "o"),
        ("2021-01-17", 1, "lazio", "o"),
        ("2021-02-01", -1, "lazio", "o"),
        ("2021-03-30", 1, "lazio", "o"),
        ("2021-04-26", -1, "lazio", "o"),
        ("2020-11-11", 1, "abruzzo", "o"),
        ("2020-11-18", -1, "abruzzo", "o"),
        ("2020-12-07", 1, "abruzzo", "o"),
        ("2020-12-24", -1, "abruzzo", "o"),
        ("2021-01-17", 1, "abruzzo", "o"),
        ("2021-02-01", -1, "abruzzo", "o"),
        ("2021-02-14", 1, "abruzzo", "o"),
        ("2021-04-26", -1, "abruzzo", "o"),
        ("2022-01-24", 1, "abruzzo", "o"),
        ("2022-02-21", -1, "abruzzo", "o"),
        ("2021-02-21", 1, "molise", "o"),
        ("2021-03-01", -1, "molise", "o"),
        ("2021-03-22", 1, "molise", "o"),
        ("2021-04-26", -1, "molise", "o"),
        ("2020-12-06", 1, "campania", "o"),
        ("2020-12-24", -1, "campania", "o"),
        ("2021-02-21", 1, "campania", "o"),
        ("2021-03-08", -1, "campania", "o"),
        ("2021-04-19", 1, "campania", "o"),
        ("2021-04-26", -1, "campania", "o"),
        ("2020-11-06", 1, "puglia", "o"),
        ("2020-12-06", -1, "puglia", "o"),
        ("2021-01-17", 1, "puglia", "o"),
        ("2021-02-11", -1, "puglia", "o"),
        ("2021-04-26", 1, "puglia", "o"),
        ("2021-05-10", -1, "puglia", "o"),
        ("2020-11-11", 1, "basilicata", "o"),
        ("2020-12-13", -1, "basilicata", "o"),
        ("2021-03-16", 1, "basilicata", "o"),
        ("2021-05-10", -1, "basilicata", "o"),
        ("2020-11-29", 1, "calabria", "o"),
        ("2020-12-13", -1, "calabria", "o"),
        ("2021-01-11", 1, "calabria", "o"),
        ("2021-02-01", -1, "calabria", "o"),
        ("2021-03-15", 1, "calabria", "o"),
        ("2021-03-29", -1, "calabria", "o"),
        ("2021-04-12", 1, "calabria", "o"),
        ("2021-05-10", -1, "calabria", "o"),
        ("2020-11-06", 1, "sicilia", "o"),
        ("2020-11-29", -1, "sicilia", "o"),
        ("2021-01-11", 1, "sicilia", "o"),
        ("2021-01-17", -1, "sicilia", "o"),
        ("2021-02-01", 1, "sicilia", "o"),
        ("2021-02-15", -1, "sicilia", "o"),
        ("2021-03-15", 1, "sicilia", "o"),
        ("2021-05-17", -1, "sicilia", "o"),
        ("2022-01-24", 1, "sicilia", "o"),
        ("2022-02-14", -1, "sicilia", "o"),
        ("2021-01-24", 1, "sardegna", "o"),
        ("2021-02-08", -1, "sardegna", "o"),
        ("2021-03-22", 1, "sardegna", "o"),
        ("2021-04-11", -1, "sardegna", "o"),
        ("2021-05-03", 1, "sardegna", "o"),
        ("2021-05-17", -1, "sardegna", "o"),
        ("2021-06-28", 1, "valle", "w"),
        ("2022-01-10", -1, "valle", "w"),
        ("2022-03-14", 1, "valle", "w"),
        ("2022-04-01", -1, "valle", "w"),
        ("2021-06-17", 1, "piemonte", "w"),
        ("2022-01-02", -1, "piemonte", "w"),
        ("2022-03-07", 1, "piemonte", "w"),
        ("2022-04-01", -1, "piemonte", "w"),
        ("2021-06-07", 1, "liguria", "w"),
        ("2021-12-20", -1, "liguria", "w"),
        ("2022-03-14", 1, "liguria", "w"),
        ("2022-04-01", -1, "liguria", "w"),
        ("2021-06-14", 1, "lombardia", "w"),
        ("2022-01-03", -1, "lombardia", "w"),
        ("2022-02-28", 1, "lombardia", "w"),
        ("2022-04-01", -1, "lombardia", "w"),
        ("2021-06-07", 1, "veneto", "w"),
        ("2021-12-20", -1, "veneto", "w"),
        ("2022-02-28", 1, "veneto", "w"),
        ("2022-04-01", -1, "veneto", "w"),
        ("2021-05-31", 1, "friuli", "w"),
        ("2021-11-29", -1, "friuli", "w"),
        ("2022-03-14", 1, "friuli", "w"),
        ("2022-04-01", -1, "friuli", "w"),
        ("2021-06-14", 1, "emilia", "w"),
        ("2022-01-10", -1, "emilia", "w"),
        ("2022-03-14", 1, "emilia", "w"),
        ("2022-04-01", -1, "emilia", "w"),
        ("2021-06-21", 1, "toscana", "w"),
        ("2022-01-10", -1, "toscana", "w"),
        ("2022-03-14", 1, "toscana", "w"),
        ("2022-04-01", -1, "toscana", "w"),
        ("2021-06-07", 1, "umbria", "w"),
        ("2022-04-01", -1, "umbria", "w"),
        ("2021-06-21", 1, "marche", "w"),
        ("2021-12-10", -1, "marche", "w"),
        ("2022-03-21", 1, "marche", "w"),
        ("2022-04-01", -1, "marche", "w"),
        ("2021-06-14", 1, "lazio", "w"),
        ("2022-01-03", -1, "lazio", "w"),
        ("2022-03-21", 1, "lazio", "w"),
        ("2022-04-01", -1, "lazio", "w"),
        ("2021-06-07", 1, "abruzzo", "w"),
        ("2022-01-10", -1, "abruzzo", "w"),
        ("2022-03-07", 1, "abruzzo", "w"),
        ("2022-04-01", -1, "abruzzo", "w"),
        ("2021-05-31", 1, "molise", "w"),
        ("2022-02-13", -1, "molise", "w"),
        ("2022-03-14", 1, "molise", "w"),
        ("2022-04-01", -1, "molise", "w"),
        ("2021-06-21", 1, "campania", "w"),
        ("2022-01-17", -1, "campania", "w"),
        ("2022-02-28", 1, "campania", "w"),
        ("2022-04-01", -1, "campania", "w"),
        ("2021-06-14", 1, "puglia", "w"),
        ("2022-01-24", -1, "puglia", "w"),
        ("2022-03-14", 1, "puglia", "w"),
        ("2022-04-01", -1, "puglia", "w"),
        ("2021-06-21", 1, "basilicata", "w"),
        ("2022-04-01", -1, "basilicata", "w"),
        ("2021-06-21", 1, "calabria", "w"),
        ("2021-12-13", -1, "calabria", "w"),
        ("2022-03-21", 1, "calabria", "w"),
        ("2022-04-01", -1, "calabria", "w"),
        ("2021-06-21", 1, "sicilia", "w"),
        ("2021-08-30", -1, "sicilia", "w"),
        ("2021-10-09", 1, "sicilia", "w"),
        ("2022-01-03", -1, "sicilia", "w"),
        ("2022-03-14", 1, "sicilia", "w"),
        ("2022-04-01", -1, "sicilia", "w"),
        ("2021-03-01", 1, "sardegna", "w"),
        ("2021-03-22", -1, "sardegna", "w"),
        ("2021-05-31", 1, "sardegna", "w"),
        ("2022-01-24", -1, "sardegna", "w"),
        ("2022-03-28", 1, "sardegna", "w"),
        ("2022-04-01", -1, "sardegna", "w"),
        ("2020-11-06", 1, "valle", "r"),
        ("2020-12-06", -1, "valle", "r"),
        ("2021-03-29", 1, "valle", "r"),
        ("2021-04-26", -1, "valle", "r"),
        ("2021-05-03", 1, "valle", "r"),
        ("2021-05-10", -1, "valle", "r"),
        ("2020-11-06", 1, "piemonte", "r"),
        ("2020-11-29", -1, "piemonte", "r"),
        ("2021-03-15", 1, "piemonte", "r"),
        ("2021-04-12", -1, "piemonte", "r"),
        ("2020-11-06", 1, "lombardia", "r"),
        ("2020-11-29", -1, "lombardia", "r"),
        ("2021-01-17", 1, "lombardia", "r"),
        ("2021-01-24", -1, "lombardia", "r"),
        ("2021-03-15", 1, "lombardia", "r"),
        ("2021-04-12", -1, "lombardia", "r"),
        ("2021-03-15", 1, "veneto", "r"),
        ("2021-04-06", -1, "veneto", "r"),
        ("2021-03-15", 1, "friuli", "r"),
        ("2021-04-12", -1, "friuli", "r"),
        ("2021-03-15", 1, "emilia", "r"),
        ("2021-04-12", -1, "emilia", "r"),
        ("2020-11-15", 1, "toscana", "r"),
        ("2020-12-06", -1, "toscana", "r"),
        ("2021-03-29", 1, "toscana", "r"),
        ("2021-04-12", -1, "toscana", "r"),
        ("2021-03-15", 1, "marche", "r"),
        ("2021-04-06", -1, "marche", "r"),
        ("2021-03-15", 1, "lazio", "r"),
        ("2021-03-19", -1, "lazio", "r"),
        ("2020-11-18", 1, "abruzzo", "r"),
        ("2020-12-07", -1, "abruzzo", "r"),
        ("2021-03-01", 1, "molise", "r"),
        ("2021-03-22", -1, "molise", "r"),
        ("2020-11-15", 1, "campania", "r"),
        ("2020-12-06", -1, "campania", "r"),
        ("2021-03-08", 1, "campania", "r"),
        ("2021-04-19", -1, "campania", "r"),
        ("2021-03-15", 1, "puglia", "r"),
        ("2021-04-26", -1, "puglia", "r"),
        ("2021-03-01", 1, "puglia", "r"),
        ("2021-03-16", -1, "puglia", "r"),
        ("2020-11-06", 1, "calabria", "r"),
        ("2020-11-29", -1, "calabria", "r"),
        ("2021-03-29", 1, "calabria", "r"),
        ("2021-04-12", -1, "calabria", "r"),
        ("2021-01-17", 1, "sicilia", "r"),
        ("2021-02-01", -1, "sicilia", "r"),
        ("2021-04-12", 1, "sardegna", "r"),
        ("2021-05-03", -1, "sardegna", "r"),
        ("2021-06-28", 1, "all", "w"),
        ("2021-08-30", -1, "all", "w"),
        ("2021-10-09", 1, "all", "w"),
        ("2021-11-29", -1, "all", "w"),
        ("2022-03-28", 1, "all", "w"),
        ("2022-04-01", -1, "all", "w"),
        ("2021-01-07", 1, "all", "y"),
        ("2021-01-09", -1, "all", "y"),
        ("2021-05-24", 1, "all", "y"),
        ("2021-05-31", -1, "all", "y"),
        ("2020-12-28", 1, "all", "o"),
        ("2020-12-31", -1, "all", "o"),
        ("2021-01-04", 1, "all", "o"),
        ("2021-01-05", -1, "all", "o"),
        ("2021-01-09", 1, "all", "o"),
        ("2021-01-11", -1, "all", "o"),
        ("2020-12-24", 1, "all", "r"),
        ("2020-12-28", -1, "all", "r"),
        ("2020-12-31", 1, "all", "r"),
        ("2021-01-04", -1, "all", "r"),
        ("2021-01-05", 1, "all", "r"),
        ("2021-01-07", -1, "all", "r"),
        ("2021-04-03", 1, "all", "r"),
        ("2021-04-06", -1, "all", "r"),]
data = sorted(data)

total_population = 59.37
regions = {"valle": 0.1257,
           "piemonte": 4.356,
           "liguria": 1.551,
           "lombardia": 10.06,
           "veneto": 4.906,
           "friuli": 1.215,
           "emilia": 4.459,
           "toscana": 3.73,
           "umbria": 0.882,
           "marche": 1.525,
           "lazio": 5.898,
           "abruzzo": 1.32,
           "molise": 0.305,
           "campania": 5.802,
           "puglia": 4.092,
           "basilicata": 0.562,
           "calabria": 1.947,
           "sicilia": 5,
           "sardegna": 1.64,
           "all": total_population}

percentages = {"w": 0, "y": 0, "o": 0, "r": 0}

times_and_percentages = []

curr_date = data[0][0]
for date in data:
    if date[0] != curr_date:
        times_and_percentages.append([curr_date, 
                                      float(percentages["w"]),
                                      float(percentages["y"]),
                                      float(percentages["o"]),
                                      float(percentages["r"])])
    curr_date = date[0]

    if date[1] == 1:
        percentages[date[3]] += regions[date[2]] / total_population

    elif date[1] == -1:
        percentages[date[3]] -= regions[date[2]] / total_population

times_and_percentages.append([curr_date, 
                                      float(percentages["w"]),
                                      float(percentages["y"]),
                                      float(percentages["o"]),
                                      float(percentages["r"])])


print(times_and_percentages)
