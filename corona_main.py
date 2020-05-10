import requests
from bs4 import BeautifulSoup
import csv
from corona_info import extract_info

file = open("corona_info.csv", mode = "w", newline = "")
writer = csv.writer(file)
writer.writerow(["city", "district", "hospital", "contact"])

info_html = requests.get("https://www.mohw.go.kr/react/popup_200128_3.html")
# hospital_html.encoding = "utf-8"
hospital_soup = BeautifulSoup(info_html.text, "html.parser")
hospital_list_box = hospital_soup.find("tbody", {"class" : "tb_center"}) 
hospital_list = hospital_list_box.find_all("tr")

final_result = extract_info(hospital_list)

for result in final_result:
    row = []
    row.append(result["city"])
    row.append(result["district"])
    row.append(result["hospital"])
    row.append(result["contact"])

    writer.writerow(row)

print("end") 