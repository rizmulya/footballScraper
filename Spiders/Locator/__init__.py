from Driver import By


class Locator:
    ALL_MATCHES_BUTTON = (By.XPATH, "//label[@analytics-event='All matches']")
    COUNTRY_DROPDOWN = (By.ID, "country")
    MATCH_ROWS = (By.TAG_NAME, "tr")
    