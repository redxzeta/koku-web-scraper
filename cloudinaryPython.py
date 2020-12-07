from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import os

file_list = os.listdir('images/category_one')
urls = []
counter = 1
name = "name"
folder_name = "images/category_one"
for i in file_list:
    public_id = f"category_one_{counter}"
    upload_image = f"images/category_one/{i}"
    print(upload_image)
    response = upload(upload_image, public_id=public_id, folder=folder_name)
    img_url = response['secure_url']
    urls.append(img_url)
    counter += 1

with open('urls.txt', 'w', encoding='utf-8') as writer:
    for j in urls:
        writer.write(f"{j}\n")
