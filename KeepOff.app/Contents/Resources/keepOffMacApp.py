import rumps

class KeepOff(rumps.App):
    def __init__(self):
        super(KeepOff, self).__init__("KO")
        self.menu = ["Start Blocker","Stop Blocker"]
        self.b_sites = [line.strip() for line in open("sites.txt", 'r+')]
        self.hosts_path = '/etc/hosts'
        self.lh = '127.0.0.1'
        rumps.debug_mode(True)

    @rumps.clicked("Start Blocker")
    def block(self,_):
        with open(self.hosts_path,'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in self.b_sites:
                if site not in hosts_content:
                    hostfile.write(self.lh + ' ' + site + '\n')

    @rumps.clicked("Stop Blocker")
    def unblock(self,_):
        with open(self.hosts_path,'r+') as hostfile:
            lines = hostfile.readlines() 
            hostfile.seek(0)
            for line in lines:
                if not any (site in line for site in self.b_sites):
                    hostfile.write(line)
            hostfile.truncate()

if __name__ == '__main__':
    KeepOff().run()