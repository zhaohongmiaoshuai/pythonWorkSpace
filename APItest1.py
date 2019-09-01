#_*_ coding:UTF-8 _*_
import json
jsonstring = '{"user_man":[{"name":"peer"},{"name":"xiaoming"}],'\
    '"user_woman":[{"name":"Anni"},{"name":"zhangsan"}]}'
json_data = json.loads(jsonstring)
print(json_data.get("user_man"))
print(json_data.get("user_woman"))
print(json_data.get("user_man")[0].get("name"))
print(json_data.get("user_woman")[0].get("name"))
print(json_data)
print(json_data["user_man"][0]["name"])
print(json_data["user_man"][0].get("name"))