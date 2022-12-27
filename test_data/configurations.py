from datetime import datetime, timedelta


def get_local_datetime():
    local_datetime = {
        "date_now": datetime.now().strftime("%d-%b-%Y %I:%M %p")[0:11],
        "time_now": datetime.now().strftime("%d-%b-%Y %I:%M %p")[12:20]
    }
    return local_datetime


def print_window_size(browser):
    print(browser.get_window_size())
