import datetime
import random
import threading
import time

import config
import schedule




def start_scheduler(time: str, job,args, time_interval: int=2):
    """starts threaded scheduler which runs the function `job`
    everyday at time=`time` + `time_interval` in seconds
    
    Usage: 
    start_scheduler(time="19:44",job=print_this, args=['foo','bar'], time_interval=5)
    
    where `print_this` is a function that takes args as argument"""

    schedule.every().day.at(time).do(_schedule_next_run, job=job, time_interval=time_interval, args=args)
    x = threading.Thread(target=_run_scheduler_thread)
    x.start()


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


def _next_weekday(day: datetime.datetime, weekday: int) -> datetime.datetime:
    """returns next selected weekday after `day`"""

    days_ahead = weekday - day.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return day + datetime.timedelta(days_ahead)


def _work(job, args):
   func = job
   func(*args)
   return schedule.CancelJob

def _run_scheduler_thread():
    while True:
        schedule.run_pending()
        time.sleep(1)

def _schedule_next_run(job, time_interval, args):
    # get random sends within 3 hours
    time_span = random.randint(1, time_interval)
    # run job after time_pan once
    schedule.every(time_span).seconds.do(_work, job=job, args=args)


if __name__ == '__main__':
    print(random_morning())
