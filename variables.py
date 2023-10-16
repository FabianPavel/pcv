students_count = 42
rating = 4.5
is_published = True

print("Typ students_count:", type(students_count))
print("Identity students_count:", id(students_count))

print("Typ rating:", type(rating))
print("Identity rating:", id(rating))

print("Typ is_published:", type(is_published))
print("Identity is_published:", id(is_published))


"""
V Pythonu jsou k dispozici následující bitové operátory:

& (bitový součin)
| (bitový součet)
^ (bitový xor)
~ (bitový negace)
<< (bitový posun doleva)
>> (bitový posun doprava)
"""

# Úkol B
myself_binary = int('01010010', 2)  # Převod binárního čísla na desítkové
print("Binární číslo v desítkové soustavě:", myself_binary)

# Bitový posun o 2 bity doprava
myself_binary_shifted = myself_binary >> 2
print("Binární číslo po bitovém posunu:", myself_binary_shifted)

# Hexadecimální číslo
hex_number = 0x1A
# Bitový součin
result = hex_number & myself_binary
print(f"Binární součin čísla {hex(hex_number)} a {bin(myself_binary)} je {bin(result)}")

