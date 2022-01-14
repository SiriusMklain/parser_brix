# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import fpdf
import qrcode
import os
from datetime import datetime

from paths import *


fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'fonts'))


class BrixParserPipeline:
    def __init__(self):
        self.result_path = os.path.join(
            RESULTS_PATH,
            str(datetime.now()).replace(" ", "_").split(".")[0].replace(":", "-")
        )
        os.mkdir(self.result_path)

    def process_item(self, item, spider):
        print(f"ITEM NAME - {item['name']}")

        qrcode_name = os.path.join(TMP_PATH, f"{item['name']}.png")
        img = qrcode.make(item["url"])
        img.save(qrcode_name)
#
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.image(qrcode_name, x=10, y=8, w=50)
#
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 14)
#
        pdf.ln(51)
        pdf.cell(200, 10, txt=item["name"], ln=1)
#
        pdf.ln(1)
        for name, value in item["characteristics"].items():
            pdf.cell(200, 10, txt=f"{name}:"
                                  f" {value}", ln=1)
            pdf.ln(1)
#
        for c in item["compatibles"]:
            pdf.cell(200, 10, txt=c, ln=1)
            pdf.ln(1)
#
        pdf.output(os.path.join(self.result_path, f"{item['article']}.pdf"))
        os.remove(qrcode_name)

        return item
