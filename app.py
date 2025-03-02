from winotify import Notification, audio
import sqlite3
import time
import random

def get_random_zekr():
    try:
        conn = sqlite3.connect('azkar.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM azkar')
        azkar = cursor.fetchall()
        if not azkar:
            return None, None
        zekr = random.choice(azkar)
        return zekr[1], zekr[0]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None, None
    finally:
        conn.close()

def show_notification(zekr, description):
    msg = Notification(app_id="Azkar App",
                       title=zekr,
                       msg=description,
                       duration="long")
    
    msg.set_audio(audio.Default, loop=False)
    msg.show()

def main():
    while True:
        zekr, description = get_random_zekr()
        show_notification(zekr, description)
        time.sleep(30*60)

if __name__ == '__main__': 
    main()