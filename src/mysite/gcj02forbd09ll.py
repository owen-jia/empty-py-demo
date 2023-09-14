"""
高德坐标转百度坐标
（火星坐标转BD0911坐标）
20230511
"""

import sys
import json
import http
import requests

o_json_file_path = "./amap_fav.json"
t_json_file_path = "./amap.json"


def http_baidu(x=0, y=0):
    url = 'https://api.map.baidu.com/geoconv/v1/?from=3&to=5&ak=V2GGQ4PjvWhzHq7DNCE6xwMzHIp6u2FF&coords='
    url = url + str(x)+","+str(y)
    print(url)
    resp = requests.get(url)
    text = json.loads(resp.text)
    result = text['result'][0]
    print(result)
    x = result['x']
    y = result['y']
    return {"lng": x, "lat": y}


def read_json():
    file = open(file=o_json_file_path, mode="r", encoding='utf-8')
    a_fav = json.load(file)

    new_items = []
    for i in a_fav:
        lng = i['lng']
        lat = i['lat']
        name = i['label']
        time = i['create_time']
        t_r = http_baidu(lng, lat)
        new_items.append({'lng': t_r['lng'], 'lat': t_r['lat'], 'name': name, 'create_time': time})

    ta = {"total": len(a_fav), "items": new_items}
    file.close()
    return ta


def write_json(o={"total": 0, "items": []}):
    with open(file=t_json_file_path, mode="w", encoding='utf-8') as j_file:
        json.dump(o, j_file)
    j_file.close()


def main():
    jj = read_json()
    print(jj)
    write_json(jj)


if __name__ == '__main__':
    # http_baidu(121.760986,29.790781)
    main()
