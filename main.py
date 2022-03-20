from rectangle import *
import re


def read_file(filename: str):
    nums = list()
    with open(filename) as file_object:
        lines = file_object.readlines()
    lines = filter(lambda x: x.strip(), lines)
    for line in lines:
        nums.append(list(map(float, re.split('; |, | |,', line))))

    return nums


def write_file(filename: str, data: str):
    with open(filename, 'w') as file_object:
        file_object.write(data)


def nums_list_to_rectangle_list(nums: list) -> list[Rectangle]:
    rectangles = list()
    vertices = list()
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if j % 2 == 0:
                point = Point(nums[i][j], nums[i][j + 1])
                vertices.append(point)
            else:
                continue
        try:
            rectangles.append(Rectangle(vertices[0], vertices[1]))
            vertices.clear()
        except Exception as e:
            vertices.clear()
            print(" error was " + str(type(e)) + str(e.args))
            pass
    return rectangles


def find_entered_rectangle(rectangles: list[Rectangle]) -> Rectangle:
    max_count = 0
    answer_rec = rectangles[0]
    for i in range(len(rectangles)):
        count = 0
        entered_rec = rectangles[i]
        for j in range(len(rectangles)):
            if i != j:
                if rectangles[i].is_entered_in(rectangles[j]):
                    count += 1
        if max_count < count:
            answer_rec = entered_rec
            max_count = count
        elif max_count == count:
            if answer_rec.find_perimetr() > entered_rec.find_perimetr():
                answer_rec = entered_rec
    return answer_rec


def main():
    rectangles = nums_list_to_rectangle_list(read_file("input01.txt"))
    answer_rec = find_entered_rectangle(rectangles)
    write_file("output.txt", answer_rec.__str__())


if __name__ == '__main__':
    main()
