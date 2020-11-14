# coding=utf-8
import os
import re

import requests
import time
import zipfile
import io

if __name__ == '__main__':

    config_file_path = "config.txt"
    web_content = requests.get("http://idea.medeming.com/jets/").content.decode("utf8")
    search_regex = re.compile(r"更新日期：(?P<month>\d+)月(?P<day>\d+)号")
    result = search_regex.search(web_content)
    update_year = time.gmtime().tm_year
    update_month = 0
    update_day = 0
    if result:
        result = result.groupdict()
        update_month = result.get('month', 0)
        update_day = result.get('day', 0)
        if os.path.exists(config_file_path):
            with open(config_file_path, "r") as f:
                temp_year, temp_month, temp_day = f.read().split("-")
                pre_update_time = time.mktime(time.strptime(f"{temp_year}-{temp_month}-{temp_day}", "%Y-%m-%d"))
                current_update_time = time.mktime(time.strptime(f"{update_year}-{update_month}-{update_day}", "%Y-%m-%d"))
                if int(current_update_time - pre_update_time) > 0:
                    print("Can be updated")
            with open(config_file_path, "w") as f:
                f.write(f"{update_year}-{update_month}-{update_day}")

        print(f"last update time: {update_year}-{update_month}-{update_day}\n")

    active_zip = requests.get("http://idea.medeming.com/jets/images/jihuoma.zip")

    file_stream = io.BytesIO()
    file_stream.write(active_zip.content)

    z = zipfile.ZipFile(file_stream, mode="r")
    file_names = z.namelist()

    target_file = [x for x in file_names if "2018" in x or "later" in x]

    if len(target_file) == 0:
        print("the target file is null")
    for index, name in enumerate(target_file):
        print(f"parse file: {name}")
        if not os.path.exists(config_file_path):
            with open(config_file_path, "w") as f:
                f.write(f"{update_year}-{update_month}-{update_day}")
        with open("active_code.txt", "w") as f:
            f.write(z.read(name).decode("utf-8"))
            break
