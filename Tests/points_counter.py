from os import listdir

FOLDER = r"C:\Users\Piotr\PycharmProjects\PJN2021\Tests"
STUDENT_INDEX = "s452694"
MAX_POINTS = 900


def is_csv_file(file_to_check):
    return file_to_check.endswith(".csv")


if __name__ == "__main__":
    current_points = 0
    current_max_points = 0
    for file in listdir(FOLDER):

        if is_csv_file(file):
            # print(file)

            with open(FOLDER + "\\" + file, "r", encoding='latin2') as current_file:
                data_reader = current_file.readlines()

                for row in data_reader:

                    if row.startswith(STUDENT_INDEX):

                        row = row.split(';')
                        points_received = int(row[4])
                        points_max = int(row[5])

                        # print("{}/{}".format(points_received, points_max))

                        current_max_points += points_max
                        current_points += points_received

    print("Punkty uzyskane / Max punktów z obecnych quizów: {}/{}".format(current_points*5, current_max_points*5))
    print("Punkty uzyskane / Max punktów: {}/{}".format(current_points * 5, MAX_POINTS))
