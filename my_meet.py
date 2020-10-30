import time
import webbrowser
import pyautogui as pag
import schedule

# Global variables
meet_url = str(input('Enter the meeting id/url :').strip())
meet_join_time = str(input('Enter meet joining time in 24hour format: ').strip())
command = input("Do you want to change browser path?(Yes/No): ").strip()
if command.lower() == ("yes" or "ye" or "y"):
    browser_path = input("Enter your browser path: ")  # Enter your browser path
else:
    print("Setting default browser path. ")
    browser_path = ''

meet_time = int(input('Enter total minutes you want to attend the meet: ').strip())
comment_ask = input('Do you want to print your attendance info in comments(Yes/No) :').strip()

if comment_ask.lower() == ('yes' or 'ye' or 'y'):
    print("Please Enter the following details to be shown in comments")
    name = input('Please enter your name :').strip()
    regNo = input('Enter your register number :').strip()
    year_sec = input('Enter your Year and Section :').strip()
    foo = True
else:
    foo = False


def meeting_join():
    if browser_path is None:
        webbrowser.get().open_new(meet_url)
    else:
        webbrowser.get(browser_path).open_new(meet_url)
    time.sleep(15)
    pag.hotkey('ctrl', 'd')
    pag.hotkey('ctrl', 'e')
    time.sleep(3)

    for i in range(6):
        pag.press('tab')

    time.sleep(2)
    pag.press('enter')
    print("Session has started and will continue for %s minutes" % meet_time)
    time.sleep(2)


def comment(name, reg_no, year_sec):
    time.sleep(10)
    pag.hotkey('ctrl', 'alt', 'c')
    time.sleep(2)
    pag.press('enter')

    time.sleep(4)
    name = "Name: " + name
    pag.write(name, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift', 'enter')
    reg_no = "Reg. No." + reg_no
    pag.write(reg_no, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift', 'enter')
    year_sec = "Year/Sec: " + year_sec
    pag.write(year_sec, interval=0.1)
    pag.press('enter')
    time.sleep(3)
    pag.press('esc')


def mainFunc():
    meeting_join()
    if foo:
        comment(name, regNo, year_sec)

    time.sleep(meet_time * 60)
    pag.hotkey('ctrl', 'w')
    print('Meeting ended')
    exit()


if __name__ == "__main__":
    schedule.every(1).day.at("%s" % meet_join_time).do(mainFunc)
    print("Scheduling meeting at ", meet_join_time)

    while True:
        schedule.run_pending()
        time.sleep(1)
