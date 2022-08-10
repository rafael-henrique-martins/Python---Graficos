import io
import base64
from matplotlib import pyplot as plt

# For more graphics
# https://seaborn.pydata.org/
# https://plotly.com/python/#basic-charts


cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]

bytes_io = io.BytesIO()

fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)
plt.savefig(bytes_io, format='png', bbox_inches="tight")
plt.close()

bytes_io = base64.b64encode(bytes_io.getvalue()).decode("utf-8").replace("\n", "")

imagem = base64.b64decode(bytes_io)

with open("image_pie.png", "wb") as img_file1:
    img_file1.write(imagem)
