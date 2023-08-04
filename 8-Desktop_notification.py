import time
# pip install plyer
from plyer import notification

if __name__ == "__main__":
    while True:
        print('inside')
        notification.notify(
            title="ALERT!!!",
            message="Take a break! It has been an hour!",
            timeout=10
        )
        time.sleep(3)
