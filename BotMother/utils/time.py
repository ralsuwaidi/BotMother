import config
import random
import datetime


def random_morning():
    """return next random morning time"""

    today = datetime.datetime.now()

    next_morning_day = random.randint(config.MORNING_DAYS[0],  
                                      config.MORNING_DAYS[len(config.MORNING_DAYS)-1])

    next_morning_time = random.randint(config.MORNING_TIMES[0],  
                                      config.MORNING_TIMES[len(config.MORNING_TIMES)-1])
    next_day = _next_weekday(today, next_morning_day)
    next_day = next_day.replace(hour=next_morning_time)
    return next_day


def random_event():
    """returns next time for random event"""

    pass


def _next_weekday(day: datetime.datetime, weekday: int)->datetime.datetime:
    """returns next selected weekday after `day`"""

    days_ahead = weekday - day.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return day + datetime.timedelta(days_ahead)


if __name__ == '__main__':
    print(random_morning())
