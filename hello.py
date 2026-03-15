from datetime import datetime


def greet(name):
    """Greet the user by name."""
    print(f"Hello, {name}!")


def greet_by_time(name):
    """Greet the user based on the time of day."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 17:
        greeting = "Good afternoon"
    elif 17 <= hour < 21:
        greeting = "Good evening"
    else:
        greeting = "Good night"
    print(f"{greeting}, {name}!")


if __name__ == "__main__":
    greet("World")
    greet_by_time("World")