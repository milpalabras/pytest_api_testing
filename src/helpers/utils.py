from datetime import datetime


def format_date(date):
    """
    :param date: datetime object"""
    return date.strftime("%d-%b-%y").upper()

#make function to format today date to return like 2024-03-13 14:32:52-03:00
def format_today_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S%z")
