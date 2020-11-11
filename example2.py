import time
import schedule

start_job = schedule.every().day.at('14:45').do(lambda: start_jobB('14:46'))


def start_jobB(end):
    while time.strftime("%H:%M", time.localtime()) != end:
        print('LOOOP...2....')
        time.sleep(10)
    schedule.cancel_job(start_job)
    print("EXIT")


while 1:
    schedule.run_pending()
    time.sleep(1)
