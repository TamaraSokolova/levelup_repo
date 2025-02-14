def Rez_(V, angle_g):
    if V<=0 & angle_g<=0:
        raise ValueError('Значение должно быть больше нуля')


if __name__ == "__main__":
    V = int(input())
    angle_g = int(input())
    
    result = Rez_(a, b, c)

    print(result)