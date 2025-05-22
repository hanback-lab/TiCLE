from btaudioamp import BtAudioAmp

bt = BtAudioAmp(mode=6, scan=7, down=27, up=11)
is_play = True

msg = """Bluetooth Audio Amplifier Control
Press 'mode' to switch be and smartphone pairing
smartphone audio play
"""

def setup():
    print(msg)

def loop():
    global is_play
    cmd = input("command: ").lower()

    if cmd == "down":
        bt.down()
    elif cmd == "up":
        bt.up()
    elif cmd == "next":
        if is_play:
            bt.next()
    elif cmd == "prev":
        if is_play:
            bt.prev()
    elif cmd == "pause":
        if is_play:
            bt.pause_resume()
            is_play = False
    elif cmd == "resume":
        if not is_play:
            bt.pause_resume()
            is_play = True
    else:
        print("Unknown command: {cmd}")

def cleanup():
    pass

if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except KeyboardInterrupt:
        cleanup()