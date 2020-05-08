import rumps, time 

rumps.debug_mode(True)

class StatusBarPomodoro(rumps.App):
    def __init__(self):
        self.seconds = 1500
        self.active = True
        super(StatusBarPomodoro, self).__init__("Pomodoro Timer", title = str(time.strftime("%M:%S", time.gmtime(self.seconds))))
        self.menu = ["Start Timer", "Stop Timer", None, "About"]

    @rumps.clicked("Start Timer")
    def start(self, sender):
        rumps.alert("Timer Started")
        for i in range(1501):
            # if not self.active:
            #     super(StatusBarPomodoro, self).__init__("Pomodoro Timer", title = str(time.strftime("%M:%S", time.gmtime(self.seconds))))
            #     break
            time.sleep(1)
            super(StatusBarPomodoro, self).__init__("Pomodoro Timer", title = str(time.strftime("%M:%S", time.gmtime(self.seconds - i))))
        rumps.alert("Time's up! Take a break!")
        self.active = True


    @rumps.clicked("Stop Timer")
    def stop(self, sender):
        self.active = False
        rumps.alert("Test msg: Timer Stopped")

    @rumps.clicked("About")
    def about(self, sender):
        rumps.alert("Developed by Bo Stevens, mostly for his own productivity.\n\n\
Follow me at http://www.github.com/PropeReferio")

if __name__ == "__main__":
    StatusBarPomodoro().run()