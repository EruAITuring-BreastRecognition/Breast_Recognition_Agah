import shutil
import os

png_dir = r"C:\Users\Agah\Desktop\png_tum_veriler"
xml_dir = r"C:\Users\Agah\Desktop\etiket_tum_veriler"


for i in os.listdir(png_dir):
    if i.endswith('.xml'):
        png_dosya = os.path.join(png_dir, i)
        xml_dosya = os.path.join(xml_dir, i)
        shutil.move(png_dosya, xml_dosya)

#a