from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "HRY"
    addresses_name = (
        "2021-03-19T13:31:23.873945/Democracy_Club__06May2021 LB Haringey.tsv"
    )
    stations_name = (
        "2021-03-19T13:31:23.873945/Democracy_Club__06May2021 LB Haringey.tsv"
    )
    elections = ["2021-05-06"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if record.addressline6 in [
            "N4 2DF",
            "N22 7UL",
            "N22 7AD",
            "N22 8JR",
            "N22 8ET",
            "N15 4HZ",
            "N17 6LE",
            "N10 3TA",
            "N22 8HT",
            "N17 6PF",
            "N17 0JE",
            "N15 5DJ",
            "N15 4DA",
            "N6 4NT",
            "N15 6JU",
            "N22 7DD",
            "N17 9EZ",
            "N4 1EL",
            "N15 3BH",
            "N15 5BT",
        ]:
            return None

        if uprn in [
            "10022940843",  # 72A HIGH ROAD, LONDON
            "100023656852",  # FLAT C 381 HIGH ROAD, WOOD GREEN, LONDON
            "100021236879",  # GROUND FLOOR FLAT 186 WEST GREEN ROAD, TOTTENHAM, LONDON
            "100021171953",  # 16 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171954",  # 18 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171955",  # 20 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171956",  # 21 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171957",  # 22 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171958",  # 23 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171959",  # 24 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171960",  # 25 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171961",  # 26 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171962",  # 27 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171963",  # 28 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171964",  # 29 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171965",  # 30 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021171966",  # 31 DALBYS CRESCENT, SELBY ROAD, LONDON N17 8HF
            "100021189348",  # 77 SEAFORD ROAD, LONDON
            "100021190559",  # 107 HIGH ROAD, LONDON
            "100021195610",  # FLAT B 41 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3QX
            "100021195611",  # FLAT C 41 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3QX
            "100021195622",  # FLAT 3 46 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "100021195632",  # FLAT A 52 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "100021195886",  # FIRST FLOOR LEFT FLAT 170-172 LANGHAM ROAD, TOTTENHAM, LONDON
            "100021195887",  # GROUND FLOOR FLAT 170-172 LANGHAM ROAD, TOTTENHAM, LONDON
            "100021197337",  # 9A LINDEN ROAD, LONDON    N15 3QB
            "100021197338",  # 9B LINDEN ROAD, LONDON    N15 3QB
            "100021204915",  # 12 MUSWELL HILL ROAD, LONDON
            "100021204930",  # 22 MUSWELL HILL ROAD, LONDON
            "100021236685",  # FIRST FLOOR FLAT 24 WEST GREEN ROAD, TOTTENHAM, LONDON
            "100021236940",  # FIRST FLOOR FLAT 294 WEST GREEN ROAD, TOTTENHAM, LONDON
            "100021236969",  # 333B WEST GREEN ROAD, TOTTENHAM, LONDON
            "100023151858",  # FLAT A 34 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "100023151859",  # FLAT B 34 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "100023151860",  # FLAT C 34 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "100023151861",  # FLAT D 34 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "100023151879",  # FLAT B 52 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "100023151880",  # FLAT C 52 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "100023152045",  # 41 LANGHAM ROAD, LONDON    N15 3QX
            "100023152046",  # FLAT A 29 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3QX
            "100023152047",  # FLAT B 29 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3QX
            "100023165966",  # 80 WHITE HART LANE, LONDON
            "10022936454",  # FLAT A 489 SEVEN SISTERS ROAD, TOTTENHAM, LONDON
            "10022936455",  # FLAT B 489 SEVEN SISTERS ROAD, TOTTENHAM, LONDON
            "10090476835",  # FLAT 1, 679 GREEN LANES, LONDON
            "10090478231",  # 1 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478232",  # 2 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478233",  # 3 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478234",  # 4 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478235",  # 5 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478236",  # 6 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478237",  # 7 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478238",  # 8 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478240",  # UNIT 1, 9 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478241",  # UNIT 2, 9 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478242",  # UNIT 3, 9 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "10090478243",  # 10 HARPERS YARD, RUSKIN ROAD, LONDON	N17 8NT
            "200002046191",  # FLAT 2 46 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "200002046198",  # FLAT 1 46 LANGHAM ROAD, TOTTENHAM, LONDON    N15 3RA
            "10093594318",  # FLAT 6, LYDIA COURT, 334 HIGH ROAD, LONDON
            "10003976515",  # SHOP 24 WEST GREEN ROAD, TOTTENHAM, LONDON
            "200002049331",  # 74B CHESTER ROAD, LONDON
            "100021206006",  # 28A MUSWELL HILL ROAD, LONDON
            "10093590583",  # 5A VINCENT ROAD, LONDON
        ]:
            return None

        return super().address_record_to_dict(record)
