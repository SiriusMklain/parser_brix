import json
import requests
from lxml.html import fromstring
from fpdf import FPDF
import qrcode
import os


if __name__ == "__main__":
    #img = qrcode.make('Some data here')
    #type(img)  # qrcode.image.pil.PilImage
    #img.save("some_file.png")
#
    #pdf = FPDF()
    #pdf.add_page()
    #pdf.image("some_file.png", x=10, y=8, w=100)
    #pdf.set_font("Arial", size=12)
    #pdf.ln(85)  # ниже на 85
    #pdf.cell(200, 10, txt="{}".format("some_file.png"), ln=1)
    #pdf.ln(1)  # ниже на 85
    #pdf.cell(200, 10, txt="{}".format("some_file.png"), ln=1)
    #pdf.output("add_image.pdf")

    #brands = requests.get("https://brixogroup.com/catalog/api/vehicle/brand").json()
#
    #for brand in brands["result"]:
    #    brand_id = brand['id']
    #    models = requests.get(f"https://brixogroup.com/catalog/api/vehicle/brand/{brand_id}/model?carBrand={brand_id}"
    #                          ).json()
    #    for model in models["result"]:
    #        model_id = model["id"]
    #        for vehicle in model["vehicles"]:
    #            vehicle_id = vehicle["id"]
#
    #            goods = requests.get(
    #                f"https://brixogroup.com/catalog/api/article/by-vehicle/{vehicle_id}?supplier=NiBK").json()
    #            print(goods)


    #d = requests.get("https://brixogroup.com/catalog/part/6416").text
    #r = fromstring(d)
##
    #print(r.xpath("//span[@class='page-part__part-code']/text()"))
#
    #names = r.xpath("//div[@class='part-properties__name']/text()")
    #values = r.xpath("//div[@class='part-properties__value part-properties__value--large']/text() |"
    #                 "//div[@class='part-properties__value']/text()")
##
    #if len(names) != len(values):
    #    raise ValueError("ERROR names != values!!!!!!!")
##
    #for name, value in zip(names, values):
    #    print(name, value)
##
    #print(" ".join(r.xpath("//tr[@class='grid__body-row grid__body-row--pointer']//text()")))

    for p in os.walk(r"F:\Projects\brix_parser\к"):
        for file in p[2]:
            name, ext = os.path.splitext(file)
            os.rename(fr"F:\Projects\brix_parser\к\{file}", fr"F:\Projects\brix_parser\к\{name[:-3] + ext}")
            #print(name, name[:-3])

    pass





