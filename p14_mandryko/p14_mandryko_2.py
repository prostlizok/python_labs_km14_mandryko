import json

with open("annotations\image_info_test-dev2017.json") as file:
    data = json.load(file)

print("Amount of images in json file:", len(data['images']))
print("Amount of categories in json file:", len(data['categories']))

images_list = sorted(data['images'], key = lambda i: i['id'])
first = images_list[0]
last = images_list[-1]
print("\n----Image 000000000001.jpg info----")
print("Image url:", first.get("coco_url"),"\nImage height:", first.get("height"), "\nImage width:", first.get("width"), "\nImage id:",first.get("id"))
print("-"*12)
print("Name of the image with biggest id:", last.get("file_name"))
print("-"*12)


