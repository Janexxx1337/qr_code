import qrcode
# пример данных
data = "http://janexxx1337.ru"
# имя конечного файла
filename = "site.png"
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)