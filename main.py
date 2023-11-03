import requests
import click
from queue import Queue
import threading

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
PURPLE = "\033[0;35m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
@click.group()
def cli():
    pass

def check(q):
    while not q.empty():
        sub=q.get()
        errors=[]
        try:
            response=requests.get(f'http://{sub}')
            if response.status_code == 404 :
                pass
            else:
                if response.status_code == 200:
                    print(f"{sub} : {GREEN}[{response.status_code}]{END} {BLUE}[{response.headers.get('server','N/A')}]{END}")
                else:
                    print(f"{sub} {YELLOW}[{response.status_code}]{END} [{response.headers.get('server','N/A')}]")
        except requests.exceptions.ConnectionError as e:
            pass
            errors.append(f'{sub} [???] [ERROR]')

@cli.command()
@click.option('-f','--filename',help="The filename containing the list of subdomains")
@click.option('-t','--threads',help='Threads to use (increases the speed of the scan) [default=10]',default=10)
def start(filename,threads):
    with open(filename, 'r') as s:
        subdomains= s.read().splitlines()
    
    q=Queue()
    
    for sub in subdomains:
        q.put(sub)
    print(RED + BLINK+ BOLD+"                       press 'ctrl+c' when the probing has stopped"+ END)
    threads_check=[]
    for _ in range(threads):
        check_thread=threading.Thread(target=check, args=(q,))
        threads_check.append(check_thread)

    for thread in threads_check:
        thread.start()

if __name__ == '__main__':
    cli()