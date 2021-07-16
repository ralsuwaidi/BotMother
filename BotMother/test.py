import schedule
import threading
import random
import time

def print_this(arg, barg):
    print(arg)
    print(barg,"yarg")

def _work(job, args):
   func = job
   func(*args)
   return schedule.CancelJob




def _run_scheduler_thread():
    while True:
        schedule.run_pending()
        time.sleep(1)
        all_jobs = schedule.get_jobs()
        print(all_jobs)

def _schedule_next_run(job, time_interval, args):
    # get random sends within 3 hours
    time_span = random.randint(1, time_interval)
    # run job after time_pan once
    schedule.every(time_span).seconds.do(_work, job=job, args=args)

def start_scheduler(time: str, job,args, time_interval: int=2):
    """starts threaded scheduler which runs the function `job`
    everyday at time=`time` + `time_interval` in seconds
    
    Usage: 
    start_scheduler(time="19:44",job=print_this, args=['foo','bar'], time_interval=5)
    
    where `print_this` is a function that takes args as argument"""

    schedule.every().day.at(time).do(_schedule_next_run, job=job, time_interval=time_interval, args=args)
    x = threading.Thread(target=_run_scheduler_thread)
    x.start()


if __name__ == "__main__":
    start_scheduler(time="19:44",job=print_this, args=['foo','bar'], time_interval=5)

# def my_job():
#     print('Foo')

# # Run every 5 to 10 seconds.

# while True:
#     schedule.run_pending()
#     time.sleep(1)