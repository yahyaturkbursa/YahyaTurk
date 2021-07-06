import json
dosya=open("yahyaturk.json","r")
json_dosya=json.load(dosya)
print("AD VE SOYAD : ", json_dosya["kimlik"][0]["Ad"]+ " " + json_dosya["kimlik"][0]["Soyad"])
dosya.close()


