

import requests
def getDataList(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Referer': 'https://www.quikr.com/jobs/icici-bank+zwqxj1519612219',
        'Origin': 'https://www.quikr.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Connection': 'keep-alive',
     
    }
    
    data = 'role%5B%5D&city%5B%5D&locality%5B%5D&salary%5B%5D&type%5B%5D&sort%5B0%5D=relevancy&company%5B%5D&keyword%5B0%5D=icici-bank&isMyNorthEastCityFilter=false&page={}'
    data=data.format(page)
    
    response = requests.post('https://www.quikr.com/jobs/jobsAjax/search', headers=headers, data=data)
    return response.json()

totalpage = 10
for page in range(1, totalpage):
    pagewise=getDataList(page)
    # print(pagewise) print these to understand structre or see json file
    # print("\n\n")
    print(pagewise['json']['searchResponse']['jobList'])
