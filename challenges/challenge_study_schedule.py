def study_schedule(permanence_period, target_time):
    try:
        student_count = 0
        # percorrer a lista de periodos de permanencia
        for period in permanence_period:
            entry_time, exit_time = period
            # verificar se o periodo de permanencia inclui o target_time
            if entry_time <= target_time <= exit_time:
                student_count += 1

        return student_count

    # caso o target_time nao esteja no formato esperado
    except TypeError:
        return None
