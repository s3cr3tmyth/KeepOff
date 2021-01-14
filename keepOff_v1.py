from datetime import datetime

end_time = datetime(2021,1,12,1)

b_sites = ['reddit.com','www.reddit.com']

hosts_path = '/etc/hosts'

lh = '127.0.0.1'


def block():
    if datetime.now() < end_time:
        print('Blocking In progress')
        with open(hosts_path,'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in b_sites:
                if site not in hosts_content:
                    hostfile.write(lh + ' ' + site + '\n')

    else:
        print('Unblocking in Progress')
        with open(hosts_path,'r+') as hostfile:
            lines = hostfile.readlines() 
            hostfile.seek(0)
            for line in lines:
                if not any (site in line for site in b_sites):
                    hostfile.write(line)
            hostfile.truncate()


if __name__ == '__main__':
    block()             