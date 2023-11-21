from Driver import By, WebDriverWait, EC, Select, pd
from Driver.WebDriver import WebDriver
from Spiders.Locator import Locator


class FootballSpider:
    def __init__(self):
        self.driver = WebDriver().driver

    def navigate_to_website(self):
        print("Navigating to the website...")
        self.driver.get("https://adamchoi.co.uk/overs/detailed")

    def load_all_matches(self):
        print("Website loaded...")
        all_matches_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locator.ALL_MATCHES_BUTTON)
        )
        all_matches_button.click()

    def select_country(self, country_name):
        dropdown = Select(WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locator.COUNTRY_DROPDOWN)
        ))
        dropdown.select_by_visible_text(country_name)

    def scrape_data(self):
        print("Scraping data...")
        match_elements = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(Locator.MATCH_ROWS)
        )
        date = []
        home_team = []
        score = []
        away_team = []
        for match in match_elements:
            date.append(match.find_element(By.XPATH, "./td[1]").text)
            home_team.append(match.find_element(By.XPATH, "./td[2]").text)
            score.append(match.find_element(By.XPATH, "./td[3]").text)
            away_team.append(match.find_element(By.XPATH, "./td[4]").text)
        return {"date": date, "home_team": home_team, "score": score, "away_team": away_team}

    def close_driver(self):
        self.driver.close()

    def exec(self, country_name, output_csv=False, output_json=False):
        self.navigate_to_website()
        self.load_all_matches()
        self.select_country(country_name)
        data = self.scrape_data()
        self.close_driver()

        df = pd.DataFrame(data)
        if output_csv:
            df.to_csv(output_csv, index=False)
        if output_json:
            df.to_json(output_json, orient="records", indent=4)
        print(df)
        print("Scraping successful!")
        