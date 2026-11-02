def rectangle_area(length, width):
    area = length * width
    return area

length = float(input("Enter length: "))
width = float(input("Enter width: "))

result = rectangle_area(length, width)

print("Area of Rectangle:", result)