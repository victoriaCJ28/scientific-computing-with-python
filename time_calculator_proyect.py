def add_time(start, duration, day=''):
    # Separar hora y AM/PM
    start = start.split(' ')
    start_index = start[0].split(':')
    duration = duration.split(':')
    indicator = False
    days_later = 0

    # Sumar los minutos
    result_min = int(start_index[1]) + int(duration[1])

    # Si los minutos pasan de 60, sumar 1 a la hora
    if result_min >= 60:
        start_index[0] = int(start_index[0]) + 1
        result_min = result_min - 60

    # Sumar las horas (ya con el posible +1 de los minutos)
    result_h = int(start_index[0]) + int(duration[0])

    # Calcular días completos pasados si se superan las 24 horas
    if result_h >= 24:
        days_later = int(duration[0]) // 24  # Cantidad de días enteros
        result_h = result_h % 24  # Ajustar la hora dentro del rango de 24

    # Cambiar de AM a PM o viceversa según el ciclo de 12 horas
    if result_h >= 12:
        if start[1] == 'AM':
            start[1] = 'PM'
        else:
            start[1] = 'AM'
            indicator = True
            days_later += 1  # Cambiar de PM a AM al pasar de medianoche suma 1 día

        if result_h > 12:
            result_h = result_h - 12
    elif result_h == 0:
        result_h = 12  # Ajustar para mostrar 12 en lugar de 0

    # Construcción del nuevo tiempo (hora:minuto AM/PM)
    new_time = str(result_h) + ':' + f"{result_min:02}" + ' ' + start[1]

    # Si se proporciona un día, calcular el nuevo día de la semana
    if day != '':
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        current_day_index = days_of_week.index(day.strip().capitalize())
        new_day_index = (current_day_index + int(days_later)) % 7
        day = days_of_week[new_day_index]
        new_time += ', ' + day

    # Agregar indicación de los días pasados
    if days_later > 0:
        if int(days_later) == 1:
            new_time += ' (next day)'
        else:
            new_time += f' ({int(days_later)} days later)'

    return new_time
print(add_time('3:00 PM', '3:10'))
# Expected: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Expected: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Expected: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Expected: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Expected: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Expected: 7:42 AM (9 days later)
