import json
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Brix(scrapy.Spider):
    name = "brix"
    custom_settings = {
        "DOWNLOAD_DELAY": 0
    }

    def __init__(self):
        super().__init__()
        self.supplier = "NiBK"

    def start_requests(self):
        yield scrapy.Request("https://brixogroup.com/catalog/api/vehicle/brand", callback=self.parse_urls,
                             meta={
                                 "level": "brands"
                             })

    def parse_urls(self, response):
        level = response.meta.get("level")

        if level == "brands":
            brands = json.loads(response.text)
            for brand in brands["result"]:
                brand_id = brand['id']

                yield scrapy.Request(
                    f"https://brixogroup.com/catalog/api/vehicle/brand/{brand_id}/model?carBrand={brand_id}",
                    callback=self.parse_urls, meta={
                        "level": "models",
                    })
        elif level == "models":
            models = json.loads(response.text)
            for model in models["result"]:
                for vehicle in model["vehicles"]:
                    vehicle_id = vehicle["id"]

                    yield scrapy.Request(
                        f"https://brixogroup.com/catalog/api/article/by-vehicle/{vehicle_id}?supplier={self.supplier}",
                        callback=self.parse_urls, meta={
                            "level": "vehicles",
                        })
        elif level == "vehicles":
            vehicles = json.loads(response.text)

            for vehicle in vehicles["result"]["articles"]:
                yield scrapy.Request(f"https://brixogroup.com/catalog/part/{vehicle['id']}",
                                     callback=self.parse_item)

    def parse_item(self, response):
        item_name = " ".join(response.xpath("//h1[@class='page-part__title']//text()").getall())

        names = response.xpath("//div[@class='part-properties__name']/text()").getall()
        values = response.xpath("//div[@class='part-properties__value part-properties__value--large']/text() |"
                                "//div[@class='part-properties__value']/text()").getall()

        if len(names) != len(values):
            raise ValueError("ERROR names != values!!!!!!!")

        characteristics = {}
        for name, value in zip(names, values):
            characteristics.update({name: value})

        compatibles = []
        compatible = response.xpath("//tr[@class='grid__body-row grid__body-row--pointer']//text()").getall()
        for i in range(0, len(compatible), 4):
            compatibles.append(" ".join(compatible[i:i+4]))

        article = response.xpath("//span[@class='page-part__part-code']/text()").getall()[1]

        result = {
            "url": response.request.url,
            "article": article,
            "name": item_name,
            "compatibles": compatibles,
            "characteristics": characteristics
        }

        yield result


if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())

    process.crawl('brix')
    process.start()









