import csv

#writing
with open("Twenty One Pilots.csv", "w", newline="") as csvfile:
    fieldnames = ['Song', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Song": "Heavydirtysoul",
                     "Year": "2015"})
    writer.writerow({"Song": "Ruby",
                     "Year": "2011"})
    writer.writerow({"Song": "Heathens",
                     "Year": "2016"})
    writer.writerow({"Song": "Nico And The Niners",
                     "Year": "2018"})
    writer.writerow({"Song": "Fairy Local",
                     "Year": "2015"})

#reading
with open("Twenty One Pilots.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for head in reader.fieldnames:
        print(head, end=" ")
    print("\n---------")
    for row in reader:
        print(row["Song"], row["Year"])
