"""
Test 
"""
temp_c , temp_f = 0.0 , 0.0# float

temp_c = float(input("Entrez une température exprimée en Celsius : "))
temp_f = temp_c * 1.8 + 32

print(f"{temp_c}°C = {temp_f:.1f}°F")
