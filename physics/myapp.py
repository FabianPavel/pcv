# myapp.py
import physics

height = 1000  # Výška volného pádu (metrů)
planet_gravity = 9.81  # Gravitace planety (m/s^2)
planet_radius = 6371000  # Poloměr Země (metrů)
relative_velocity = 0.8 * physics.SPEED_OF_LIGHT  # Relativní rychlost (80 % rychlosti světla)
local_speed = 250  # Lokální rychlost objektu (m/s)
sound_speed = physics.SPEED_OF_SOUND  # Rychlost zvuku v místě

# Použití funkcí z modulu physics
free_fall_time = physics.calculate_free_fall_time(height)
escape_velocity = physics.calculate_escape_velocity(planet_gravity, planet_radius)
time_dilation = physics.calculate_time_dilation(relative_velocity)
mach_number = physics.calculate_mach_number(local_speed, sound_speed)

print(f"Čas volného pádu na Zemi z výšky {height} m je {free_fall_time:.2f} sekund.")
print(f"Úniková rychlost z planety s gravitací {planet_gravity} m/s^2 a poloměrem {planet_radius} m je {escape_velocity:.2f} m/s.")
print(f"Dilatace času při relativní rychlosti {relative_velocity} m/s je {time_dilation:.4f}.")
print(f"Machovo číslo při lokální rychlosti {local_speed} m/s a rychlosti zvuku {sound_speed} m/s je {mach_number:.2f}.")