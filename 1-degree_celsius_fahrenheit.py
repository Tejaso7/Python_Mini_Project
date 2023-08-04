def convert_to_degree_celsius(value_Fahrenheit):
    f = float(value_Fahrenheit)
    celsius = (f - 32) * 5/9
    return celsius

print(convert_to_degree_celsius(78))