import os


def get_integer(key, default_value):
    value = get_string(key, default_value)
    return int(value)


def get_string(key, default_value=None):
    return os.environ.get(key, default_value)


def get_existing_path(key, default_value):
    value = get_string(key, default_value)
    if not os.path.exists(value):
        raise ValueError("Path does not exist")
    return value
