EARTH_GRAVITY = 9.81
MOON_GRAVITY = 1.625
SPEED_OF_LIGHT = 299792458
SPEED_OF_SOUND = 343

def calculate_free_fall_time(height):
    """
    Tato funkce spočítá čas volného pádu objektu na Zemi ze zadané výšky.
    :param height: Výška v metrech.
    :return: Čas volného pádu v sekundách.
    """
    time = (2 * height / EARTH_GRAVITY) ** 0.5
    return time

def calculate_escape_velocity(planet_gravity, planet_radius):
    """
    Tato funkce spočítá únikovou rychlost z planety s danou gravitací a poloměrem.
    :param planet_gravity: Gravitace planety v m/s^2.
    :param planet_radius: Poloměr planety v metrech.
    :return: Úniková rychlost v m/s.
    """
    escape_velocity = (2 * planet_gravity * planet_radius) ** 0.5
    return escape_velocity

def calculate_time_dilation(relative_velocity):
    """
    Tato funkce spočítá dilataci času na základě relativní rychlosti objektu.
    :param relative_velocity: Relativní rychlost vzhledem k rychlosti světla.
    :return: Dilatace času (Lorentz faktor).
    """
    lorentz_factor = 1 / ((1 - (relative_velocity ** 2 / SPEED_OF_LIGHT ** 2)) ** 0.5)
    return lorentz_factor

def calculate_mach_number(local_speed, sound_speed):
    """
    Tato funkce spočítá Machovo číslo na základě lokální rychlosti a rychlosti zvuku.
    :param local_speed: Lokální rychlost objektu v m/s.
    :param sound_speed: Rychlost zvuku v místě v m/s.
    :return: Machovo číslo.
    """
    mach_number = local_speed / sound_speed
    return mach_number