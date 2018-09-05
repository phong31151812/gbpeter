from event import Event
from peter_lib import voice_detech
from peter_lib import mining_hotword
from peter_lib import mining_text
from peter_lib import job_event
import os
import threading
class peterbot(object):
    def __init__(self):
        self.hotword_time=24
        self.ask_time=3
        self.event=None
        self._task = threading.Thread(target=self._run_task)
        self.count=int(Event().readl())
        print(self.count)
    def start(self):
        self._task.start()

    def _run_task(self):
        Event().write("0")
        job_event("reset").run()
        while True:
            self.event=Event().read()
            if self.event == "0":
                pass
            elif self.event == "1":
                if not self.hotword_time==0:
                    self.count=self.count%12
                    text, audio = voice_detech(self.count).get_data()
                    if text:
                        su=mining_hotword(text).run()
                        job_event(su,text).run()
                        if su == "name_find":
                            Event().write("2")
                            self.hotword_time=24
                        elif su == "name_not_find":
                            self.hotword_time -= 1
                    else:
                        self.hotword_time -= 1
                    self.count+=1
                else:
                    
                    self.hotword_time=24
                    job_event("back_to_hey").run()
                    Event().write("0")
                    Event().writel(str(self.count))
            elif self.event == "2":
                if not self.ask_time==0:
                    self.count=self.count%12
                    text1, audio1 = voice_detech(self.count).get_data()
                    if text1:
                        print("1")
                        su=mining_text(text1).run()
                        print(su)
                        if su =="shut down":
                             Event().writel(str(self.count))
                             os.system("sudo shutdown now -h")
                             break
                        job_event(su,text1,audio1).run()
                        self.ask_time=3
                    else:
                        self.ask_time -= 1
                    self.count+=1
                else:
                    self.ask_time=3
                    job_event("name_again").run()
                    Event().write("1")
                    Event().writel(str(self.count))
                    
def main():
    try:
        peterbot().start()
    except:
        print("the")

if __name__ == '__main__':
    main()


           
