

import requests

headers = {
    'authority': 'www.quikr.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache, no-transform',
    'content-type': 'application/json',
    # 'cookie': 'new_prefer_city=delhi; abRand=63; brsampl=81908.920; __at=037fd969-9c40-4426-9817-a370cd9d90d0; __an=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2OTI2OTcyMTEsInYiOiI0IiwiY3JlYXRlZEF0IjoxNjkyNjk3MjExLCJ1dWlkIjoiMWM3MmNiYTEtODNjYi00NzBiLTkxOTEtNzAyNjM2MGFmMzFlIiwicGxhdGZvcm0iOiJRVUlLUiIsImV4cCI6MTY5NTI4OTIxMX0.tMAB0MspES1hSsxaPxY-LDkTo-6pmtjyWYJvY--vAyE; _jk_id=21f39336-87f0-4976-a21b-1d8a8be87700; _gid=GA1.2.978582806.1692697199; __utma=119021961.1874654685.1692697199.1692697199.1692697199.1; __utmc=119021961; __utmz=119021961.1692697199.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; usession=967821692697211; _gcl_au=1.1.634319487.1692697200; _fbp=fb.1.1692697200411.2042718569; _cc_id=64fbd3db1238a1e765cd6d5827644fe8; panoramaId_expiry=1692783599881; panoramaId=fa43d6c9e719c3b4229b62619c21a9fb927a1347bc5e812bd914fc32552e462d; panoramaIdType=panoDevice; __gpi=UID=00000c309cf07b6a:T=1692697199:RT=1692697199:S=ALNI_MYJd86AAG74a81MY196IxhTPl45WQ; utmztrack=119021961.1692697199.1.1.utmcsr%3Dgoogle%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic%7Cutmctr%3D%28not+provided%29; cto_bundle=nFKr-l9oUGJWSTdGaU1scFJQMnJEZURxWmUxZmgwVkIwSSUyRmZaU00xOE8zaG4wclROZGlTVTltWUlpdnk5ZnoybWRjcUp3OWVCR0tEd1NPZFZWU1pQTjZUJTJCQzBnV1l1c2tVUVhjb1BEckVHOGE2ZSUyRjA2c2RLMjF3Wkw2Yms5Slk4NmdzdldxNyUyRmYzOWJJRlA3czRzQzlhciUyRkp3JTNEJTNE; _ga_WMY8XWRKEV=GS1.1.1692697199.1.1.1692697214.45.0.0; recentSearches=ICICI%20Bank; submitButtonClicked=yes; __utmb=119021961.12.9.1692697214194; _ga_GDJ981R2S6=GS1.1.1692697215.1.0.1692697215.0.0.0; _ga=GA1.2.1874654685.1692697199; __gads=ID=7a5804655720902f-22a408fafce20013:T=1692697199:RT=1692697216:S=ALNI_MZ_r_RcuvbUiiy8Uiqv1aAHc9NXEQ; abRandMobile=68; lang=en; qkrv=122.161.67.50.1692697276; qkru=122.161.67.50.1692697276; new_prefer_city=delhi',
    'origin': 'https://www.quikr.com',
    'referer': 'https://www.quikr.com/services/bank-accounts-in-delhi-evaluate?from=auto',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
}

json_data = {
    # 'userId': 123,
    'meRequest': {
        'userRequestChanged': False,
        # 'searchId': 597228824,
        'from': 10,
        'size': 1000,
        'filter': {
            'cityId': 1756,
        },
        # 'catId': 10001,
        'serviceId': 10213,
        'subCatId': 10212,
        'source': 'quikrConnect',
    },
}

response = requests.post(
    'https://www.quikr.com/services/api/qc/services/v1/createLeadAndGetSmes',
    # cookies=cookies,
    headers=headers,
    json=json_data,
)



