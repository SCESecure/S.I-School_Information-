import json

apikey = input("API 키를 입력하세요 : ")
atptcode = input("시도교육청코드를 입력하세요(중복되는 경우만 해당, 아니거나 혹은 모를 시 무시) : ")
school_nm = input("학교명을 입력하세요 : ")
ay = input("년도를 입력하세요 : ")
sem = input("학기를 입력하세요 : ")
grade = input("학년을 입력하세요 : ")
class_nm = input("반을 입력하세요 : ")

data = {"Basic" : {"apikey" : str(apikey), \
                   "atptcode" : str(atptcode), \
                   "school_nm" : str(school_nm), \
                    "SC" : {"ay" : str(ay), \
                            "sem" : str(sem), \
                            "grade" : str(grade), \
                            "class_nm" : str(class_nm)}}}

with open('basicfile.json', 'a+', encoding="UTF-8") as f :
    json.dump(data, f, ensure_ascii=False)