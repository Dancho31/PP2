def show_info(*args, **kwargs):
    print("Args:", args)
    print("Keyword args:", kwargs)

show_info(1, 2, 3, name="Ann", age=20)