import math
# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    rect_area = length * width
    return rect_area

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    circle_area = 2 * math.pi * radius
    return circle_area

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    triangle_area = (base * height)/2
    return triangle_area

# TODO: Implement these volume functions
def calculate_cube_volume(side):
    cube_volume = side**3
    return cube_volume

def calculate_cylinder_volume(radius, height):
    cylinder_volume = radius*radius*height*math.pi
    return cylinder_volume

def calculate_sphere_volume(radius):
    sphere_volume = (4/3)*math.pi*radius**3
    return sphere_volume

# Menu function to allow user selection
def menu():
    print("Choose a calculation:")
    print("1. Area of Rectangle")
    print("2. Area of Circle")
    print("3. Area of Triangle")
    print("4. Volume of Cube")
    print("5. Volume of Cylinder")
    print("6. Volume of Sphere")

# Main logic to get user input and call the appropriate function
menu()
choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area:", calculate_rectangle_area(length, width))
elif choice == 2:
    radius = float(input("Enter radius: "))
    print("Area:", calculate_circle_area(radius))
elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area:", calculate_triangle_area(base, height))
elif choice == 4:
    side = float(input("Enter side length: "))
    print("Volume:", calculate_cube_volume(side))
elif choice == 5:
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    print("Volume:", calculate_cylinder_volume(radius, height))
elif choice == 6:
    radius = float(input("Enter radius: "))
    print("Volume:", calculate_sphere_volume(radius))
else:
    print("Invalid choice!")