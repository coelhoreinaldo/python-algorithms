def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    count = 0

    for student_arrive, student_leave in permanence_period:
        if not isinstance(student_arrive, int) or not isinstance(
            student_leave, int
        ):
            return None
        if student_arrive <= target_time <= student_leave:
            count += 1

    return count
