def add_time(start, duration, starting_day=None):
    weekdays = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ]

    days = 0
    hours, minutes = map(int, start.split()[0].split(":"))
    period = start.split()[1]
    duration_hours, duration_minutes = map(int, duration.split(":"))

    minutes += duration_minutes
    if minutes >= 60:
        hours += minutes // 60
        minutes -= 60

    if period == "PM":
        hours += 12

    hours += duration_hours
    if hours >= 24:
        days = hours // 24
        hours %= 24

    if hours >= 12:
        hours -= 12
        period = "PM"
    else:
        period = "AM"

    if hours == 0:
        hours = 12

    result = "{}:{:02d} {}".format(hours, minutes, period)

    if starting_day is not None:
        day_index = weekdays.index(starting_day.capitalize())
        result += ", " + weekdays[(day_index + days - (day_index + days) // 7 * 7)]

    if days > 0:
        if days == 1:
            result += " (next day)"
        else:
            result += " ({} days later)".format(days)

    return result
