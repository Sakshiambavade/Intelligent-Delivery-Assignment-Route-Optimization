from datetime import datetime, timedelta

def str_to_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def time_to_str(time_obj):
    return time_obj.strftime("%I:%M %p")

def add_minutes(time_obj, minutes):
    return time_obj + timedelta(minutes=minutes)
