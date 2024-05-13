from math import sin, pi

def get_c_from_angle(theta: float, wavelength: float, n: int=1):
    # using formula
    # 2d * sin(theta) = n * lambda
    # reagranged to 
    # d = (n/2) * lambda / sin(theta)
    return (n/2) * (wavelength / sin(theta * pi / 180))




if __name__ == '__main__':
    # parse file
    
    # pretend
    data = [23.87, 31.8, 32, 35.04, 44, 44.65, 45.9, 46.15, 53.9, 56, 56.75, 58, 65.9, 67, 74, 76, 79]
    
    for peak in data:
        print(f"c = {get_c_from_angle(peak, 1.5406)} Angstroms")
    