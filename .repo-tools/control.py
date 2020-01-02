#!/usr/bin/env python3
import os
import argparse
from HTBClient import client


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Controls hackthebox.eu boxes')
    parser.add_argument('--user', dest="user", type=str, help='hackthebox username')
    parser.add_argument('--pass', dest='password', type=str, help='hackthebox password')
    parser.add_argument('--machine', dest='machine', type=str, help='hackthebox machine name')
    parser.add_argument('action', type=str, help='action to perform')
    args = parser.parse_args()

    valid_actions = ['start', 'stop', 'extend', 'own', 'todo']
    if args.action not in valid_actions:
        print(f'the requested action {args.action} is not valid')
        exit(-1)

    if args.user is not None:
        htb_user = args.user
    else:
        htb_user = os.getenv('HTB_USER')

    if args.password is not None:
        htb_pass = args.password
    else:
        htb_pass = os.getenv('HTB_PASS')

    if htb_user is None or htb_pass is None:
        print('[!] Error: Username and Password must be set.')
        print('[!] You can either pass them at the command line with --user and --pass or set environmental variables')
        print('--Example--')
        print('\nexport HTB_USER=someone@address.com')
        print('export HTB_PASS=hopefullyagoodpassword')
        exit(-1)

    client = client.Client()
    client.login(htb_user, htb_pass)
    machines = client.machines()
    assigned = client.assigned()

    machine_name = args.machine.lower()
    if machine_name in machines:
        machine = machines[machine_name]
    else:
        print('[!] Error: machine not found!')
        exit(-1)

    current = None
    if len(assigned) > 0:
        id = assigned[0]['id']
        for key, machine in machines.items():
            if machine.identifier == id:
                current = machine

    if args.action.lower() == 'start':
        if current is not None:
            current.stop()
        machine.start()
    elif args.action.lower() == 'stop':
        machine.stop()
    elif args.action.lower() == 'extend':
        machine.extend()
    elif args.action.lower() == 'own':
        print('[!] not yet implemented')
    elif args.action.lower() == 'todo':
        machine.todo()
