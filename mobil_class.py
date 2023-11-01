class Mobile:
    def __init__(self,):
        self.brand = " "
        self.tech = " "
        self.camera = " "
        self.batteries = " "
        self.country = " "

    def set_brand(self, brand):
        self.brand = brand

    def set_tech(self,tech):
        self.tech = tech

    def set_camera(self,front_camara,back_camara):
        self.front_camara = front_camara
        self.back_camara = back_camara

    def get_camera(self):
        return f"{self.front_camara} {self.back_camara}"

    def set_batteries(self, batteries):
        self.batteries = batteries

    def set_country(self, country):
        self.country = country


class Vivo_xyz(Mobile):

    def __init__(self,model_no,color):
        super().__init__()
        self.color = color
        self.model_no = model_no

class One_Pluse(Mobile):

    def __init__(self,model_no,color):
        super().__init__()
        self.color = color
        self.model_no = model_no



vivo_phone = Vivo_xyz(model_no="V1", color="Black")

one_plus = One_Pluse(model_no="abc", color="pink")


vivo_phone.set_brand("Vivo")
vivo_phone.set_tech("5G")
vivo_phone.set_camera("12MP", "48MP")
vivo_phone.set_batteries("4000 mAh")
vivo_phone.set_country("China")

print("=" * 80)
print(f"Vivo Phone Model No: {vivo_phone.model_no}")
print(f"Vivo Phone Color: {vivo_phone.color}")
print(f"Vivo Phone Camera: {vivo_phone.get_camera()}")
print(f"Vivo Phone Batteries: {vivo_phone.batteries}")
print(f"Vivo Phone Country: {vivo_phone.country}")

print("=" * 80)

print(f"OnePlus Phone Model No: {one_plus.model_no}")
print(f"OnePlus Phone Color: {one_plus.color}")
print(f"OnePlus Phone Camera: {one_plus.get_camera}")
print(f"OnePlus Phone Batteries: {one_plus.batteries}")
print(f"OnePlus Phone Country: {one_plus.country}")






