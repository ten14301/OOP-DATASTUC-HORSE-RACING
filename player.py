import json
class Player:
    def __init__(self, name="", coin=0):
        self.name = name
        self.coin = coin

    @property
    def return_name(self) -> str:
        return str(self.name)
    
    @property
    def return_coin(self) -> int:
        return int(self.coin)
    
    def update_coin(self,coin):
        self.coin += coin

    
    def update_name(self,name):
        self.name = name



    def auto_save(self):
    
        file_path = "./data/data.json"
        # อ่านข้อมูล JSON จากไฟล์
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        # อัปเดตข้อมูล
        data["AUTO"]["name"] = self.name
        data["AUTO"]["coin"] = self.coin

        # บันทึกข้อมูล JSON ลงในไฟล์
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)