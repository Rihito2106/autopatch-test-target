def get_initials(name):
    parts = name.split(" ")
    if len(parts) < 2:
        return parts[0][0]
    else:
        return parts[0][0] + parts[1][0]
