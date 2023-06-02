def study_schedule(permanence_period, time):
    try:
        time_count = 0
        for schdle in permanence_period:
            time_count += 1 if time >= schdle[0] and time <= schdle[1] else 0
        return time_count
    except TypeError:
        return None
