from multiprocessing import Process
from os import (
    environ,
    system,
)
from sys import argv
from requests import post
from time import sleep
import platform

POMODORO_LENGTH = 25 * 60
BREAK_LENGTH = 5 * 60

BEEMINDER_KEY = ''
USER = ''
GOAL = ''

BEEMINDER_API_ENDPOINT = "https://www.beeminder.com/api/v1/{}"
BEEMINDER_POST_ENDPOINT = BEEMINDER_API_ENDPOINT.format(
    "/users/{USER}/goals/{GOAL}/datapoints.json?"
    "auth_token={BEEMINDER_KEY}".format(**locals()))

messages = {
    'pomodoro_start': 'Pomodoro has started.',
    'pomodoro_over': 'Pomodoro over.',
    'break_start': 'Take a break, {}.'.format(USER),
    'break_over': 'Break over.',
    'transferring': 'Transferring data to Beeminder.',
    'time_remaining': 'Time Remaining'}


def say_print(message_id):
    message = messages[message_id]
    print(message)
    p = Process(target=lambda: system("say {}".format(message)))
    p.start()


def send_data(activity=""):
    response = post(
        BEEMINDER_POST_ENDPOINT,
        data={'comment': activity, 'value': '1'})
    assert response.status_code < 400, response.text
    return response


def timer(length):
    for i in reversed(range(length)):
        minutes = i // 60
        seconds = i % 60
        print("\r", end='')
        print(
            "{}: {:02}:{:02}".format(
                messages['time_remaining'],
                minutes, seconds),
            end='',
            flush=True)
        sleep(1)
    print("")


def pomodoro(activity, length=POMODORO_LENGTH):
    say_print('pomodoro_start')
    timer(length)
    say_print('pomodoro_over')
    send_notification(activity, 'face-cool')

    say_print('transferring')
    send_data(activity)

    say_print('break_start')
    timer(BREAK_LENGTH)
    say_print('break_over')


def send_notification(activity, expression):
    os = check_operating_system()
    if os == 'Linux':
        cmd = "notify-send '%s Pomodoro' '%s Done!' -i %s"\
              % (GOAL, activity, expression)
    elif os == 'Darwin':
        cmd = 'osascript -e \'display notification "%s 🍺" with title "%s" sound name "default"\''\
              % (activity, GOAL)
    system(cmd)


def check_operating_system():
    return platform.system()


def main():
    assert len(argv) >= 2
    msg = argv[1]
    if len(argv) == 3:
        length = int(argv[2]) * 60
    else:
        length = POMODORO_LENGTH

    pomodoro(msg, length=length)


if __name__ == "__main__":
    main()
