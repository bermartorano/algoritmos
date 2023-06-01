permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5)]

def study_schedule(permanence_period, target_time):
    try:
        target_time_count = 0
        for schedule in permanence_period:
            target_time_count += 1 if target_time >= schedule[0] and target_time <= schedule[1] else 0
        return target_time_count
    except:
        return None

print(study_schedule(permanence_period, 'joao'))