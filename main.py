from crontab import CronTab


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('SALAM QAQA')
    cron = CronTab(user='root')
    job_ex1 = cron.new(command='python example1.py')
    job_ex2 = cron.new(command='python example2.py')
    job_ex1.minute.every(5)
    job_ex2.minute.every(5)
    cron.write()
