import requests
import pandas as pd
import time
from xml.etree import ElementTree as ET

API_KEY = "f03ae0eab722ef6baacbd0995737b381c73160d593d5572e271eb71a49a4eff0"
BASE_URL = "https://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList"

page_no = 1
per_page = 100
all_records = []

while True:
    params = {
        "serviceKey": API_KEY,
        "pageNo": page_no,
        "numOfRows": per_page,
        "type": "xml"
    }

    res = requests.get(BASE_URL, params=params)
    root = ET.fromstring(res.text)

    items = root.findall(".//item")
    total_count = root.findtext(".//totalCount")

    if not items:
        print("모든 데이터 수집 완료")
        break

    for item in items:
        record = {
            "제품명": item.findtext("itemName"),
            "업체명": item.findtext("entpName"),
            "효능효과": item.findtext("efcyQesitm"),
            "사용법": item.findtext("useMethodQesitm"),
            "주의사항": item.findtext("warnQesitm"),
            "주의사항(상세)": item.findtext("atpnQesitm"),
            "상호작용": item.findtext("intrcQesitm"),
            "부작용": item.findtext("seQesitm"),
            "보관법": item.findtext("depositMethodQesitm"),
        }
        all_records.append(record)

    print(f"{page_no} 페이지 완료 (누적 {len(all_records)}건)")
    page_no += 1
    time.sleep(0.3) 

df = pd.DataFrame(all_records)
df.to_csv("drug_data_full.csv", index=False, encoding="utf-8-sig")

print("💾 CSV 저장 완료: drug_data_full.csv")