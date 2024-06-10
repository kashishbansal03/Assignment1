import csv

def read_csv_file(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


file_path = 'txt1.txt'  
read_csv_file(file_path)
