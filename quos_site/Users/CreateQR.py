import segno, os
 
def createqr(name, code):
    # создаем код
    qrcode = segno.make_qr(f"{code}")
    # сохраняем его в файл "metanit_qr.png"
    qrcode.save(f"QR_folder/{name}.png") 

if __name__ == "__main__":
    name = input("Название файл без расширения: ")
    code = input("Код: ")
    createqr(name=name, code=code)
