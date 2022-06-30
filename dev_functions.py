def get_formatted_name(first,last,middle=''):
    """concatenate first and last name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"

    return full_name


if __name__ == "__main__":
    print(get_formatted_name('dev','raj'))