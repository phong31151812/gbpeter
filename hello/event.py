class Event(object):
    def __init__(self):
        self.text=None      
    def write(self,st,tt=0):
        obj=open("abcd","w")
        obj.write(st)
        obj.close()
    def read(self):
        obj=open("abcd","r")
        self.text=obj.read()
        obj.close()
        return self.text
    def readl(self):
        obj=open("a","r")
        self.text=obj.read()
        obj.close()
        return self.text
    def writel(self,st,tt=0):
        obj=open("a","w")
        obj.write(st)
        obj.close()
