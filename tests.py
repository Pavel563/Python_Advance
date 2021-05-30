import csv


def mean_def():
    with open("hw (2) (1).csv", "r") as file:
        reader = csv.DictReader(file)
        data = []
        weight_sum = 0
        height_sum = 0
        count = 0
        for line in reader:
            count += 1
            weight = line['Height(Inches)'].lstrip()
            height = line['Weight(Pounds)'].lstrip()
            weight_sum += float(weight)
            height_sum += float(height)
        weight = weight_sum / count
        height = height_sum / count
        data = {'weight': weight, 'height': height}
    return data


mean_def()
