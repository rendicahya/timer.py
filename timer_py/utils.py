def format_time(time, ms_digits, format) -> str:
    hour = time // 3600
    min = time % 3600 // 60
    sec = time % 60
    ms = str(time % 1)[2 : ms_digits + 2]

    return format % (hour, min, sec, ms)
