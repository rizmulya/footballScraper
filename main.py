from Spiders.football import FootballSpider


spider = FootballSpider()
spider.exec(
    country_name="Spain",  # available country https://adamchoi.co.uk/overs/detailed
    output_csv="Reports/football_data.csv",
    # output_json="Reports/football_data.json"
)
