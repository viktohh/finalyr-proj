def check_lecturer_username(username):
    if not username.lower().endswith("@futa.edu.ng"):
        return False
    return True