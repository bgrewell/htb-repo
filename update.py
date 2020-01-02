#!/usr/bin/env python3
import os
import json

from HTBClient import client

# common variables
machines_root = 'machines/'


def dir_exists(machine):
    machine_path = os.path.join(machines_root, machine.name)
    if not os.path.exists(machine_path):
        os.mkdir(machine_path)
        return False
    else:
        return True


def create_meta(machine):
    meta_path = os.path.join(machines_root, machine.name, '.meta')
    if not os.path.exists(meta_path):
        os.mkdir(meta_path)
        f = open(os.path.join(meta_path, 'box_info.md'), 'w+')
        f.write(f'# {machine.name}\n')
        f.write('```\n')
        f.write(f'id: {machine.identifier}\n')
        f.write(f'os: {machine.operating_system}\n')
        f.write(f'ip: {machine.ip}\n')
        f.write(f'points: {machine.points}\n')
        f.write(f'release: {machine.release}\n')
        f.write(f'retired_date: {machine.retired_date}\n')
        f.write(f'retired: {machine.retired}\n')
        f.write(f'maker: {machine.maker}\n')
        f.write(f'rating: {machine.rating}\n')
        f.write(f'user_owns: {machine.user_owns}\n')
        f.write(f'root_owns: {machine.root_owns}\n')
        f.write(f'free: {machine.free}\n')
        f.close()

        f = open(os.path.join(meta_path, 'box_info.json'), 'w+')
        json_info = json.dumps(machine.__dict__, default=lambda o: '<not serializable>')
        f.write(json_info)
        f.close()

        active_file = os.path.join(meta_path, 'active')
        retired_file = os.path.join(meta_path, 'retired')
        if machine.retired:
            open(retired_file, 'w+').close()
            if os.path.exists(active_file):
                os.remove(active_file)
        else:
            open(active_file, 'w+').close()
            if os.path.exists(retired_file):
                os.remove(retired_file)

        release_file = os.path.join(meta_path, 'release')
        f = open(release_file, 'w+')
        f.write(machine.release)
        f.close()


def create_scan(machine):
    scan_path = os.path.join(machines_root, machine.name, 'scans')
    if not os.path.exists(scan_path):
        os.mkdir(scan_path)
        os.mkdir(os.path.join(scan_path, 'nmap'))
        quick_scan = os.path.join(scan_path, 'nmap-quick.sh')
        quick = open(quick_scan, 'w+')
        quick.write('#!/usr/bin/env bash\n')
        quick.write('script_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )\n')
        quick.write('cd $script_path\n')
        quick.write('echo "" >> ../notes.md\n')
        quick.write('echo "## nmap Quick Scan Results" >> ../notes.md\n')
        quick.write("echo '```' >> ../notes.md\n")
        quick.write(f'nmap -T5 -sC -sV -oA nmap/quick {machine.ip} >> ../notes.md\n')
        quick.write("echo '```' >> ../notes.md\n")
        quick.close()
        os.chmod(quick_scan, 0o755)
        full_scan = os.path.join(scan_path, 'nmap-full.sh')
        full = open(full_scan, 'w+')
        full.write('#!/usr/bin/env bash\n')
        full.write('script_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )\n')
        full.write('cd $script_path\n')
        full.write('echo "" >> ../notes.md\n')
        full.write('echo "## nmap Full Scan Results" >> ../notes.md\n')
        full.write("echo '```' >> ../notes.md\n")
        full.write(f'nmap -T5 -sC -sV -p- -oA nmap/full {machine.ip}\n')
        full.write("echo '```' >> ../notes.md\n")
        full.close()
        os.chmod(full_scan, 0o755)


def create_tokens(machine):
    tokens_path = os.path.join(machines_root, machine.name, 'tokens')
    if not os.path.exists(tokens_path):
        os.mkdir(tokens_path)


def create_tools(machine):
    tools_path = os.path.join(machines_root, machine.name, 'tools')
    if not os.path.exists(tools_path):
        os.mkdir(tools_path)


def create_notes(machine):
    notes_path = os.path.join(machines_root, machine.name, 'notes.md')
    if not os.path.exists(notes_path):
        f = open(notes_path, 'w+')
        f.write(f'# {machine.name} Notes\n')
        f.write(f'```\n')
        f.write(f'id: {machine.identifier}\n')
        f.write(f'ip: {machine.ip}\n')
        f.write(f'```\n')
        f.close()


def create_src(machine):
    src_path = os.path.join(machines_root, machine.name, 'src')
    if not os.path.exists(src_path):
        os.mkdir(src_path)


def create_scripts(machine):
    scripts_path = os.path.join(machines_root, machine.name, 'scripts')
    if not os.path.exists(scripts_path):
        os.mkdir(scripts_path)
        actions = ['start', 'stop', 'extend', 'todo', 'own']
        for action in actions:
            script = os.path.join(scripts_path, f'{action}.sh')
            f = open(script, 'w+')
            f.write('#!/usr/bin/env bash\n')
            f.write('script_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )\n')
            f.write('cd "$script_path"\n')
            f.write(f'../../../.repo-tools/control.py --machine {machine.name} {action}\n')
            f.close()
            os.chmod(script, 0o755)

        init_script = os.path.join(machines_root, machine.name, 'init.sh')
        f = open(init_script, 'w+')
        f.write('#!/usr/bin/env bash\n')
        f.write('script_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )\n')
        f.write('cd "$script_path"\n')
        f.write('touch .meta/initialized\n')
        f.write('ln -s "$(pwd)" ../current\n')
        f.write('scripts/todo.sh\n')
        f.write('scripts/start.sh\n')
        f.close()
        os.chmod(init_script, 0o755)


if __name__ == '__main__':

    # get username and password
    htb_user = os.getenv('HTB_USER')
    htb_pass = os.getenv('HTB_PASS')

    if htb_user is None or htb_pass is None:
        print('[!] Error: Username and Password must be set in environmental variables.')
        print('[!] Below is an example')
        print('\nexport HTB_USER=someone@address.com')
        print('export HTB_PASS=hopefullyagoodpassword')
        exit(-1)

    # setup htb api connection
    api = client.Client()
    api.login(htb_user, htb_pass)

    # create directory structure
    #TODO: if user passes -s <machine_name> flag then it will only perform the update for that single machine

    # get list of all machines on hackthebox.eu
    machines = api.machines()

    # iterate through each machine and make sure there is a directory for it
    for key, machine in machines.items():
        if not dir_exists(machine):
            create_meta(machine)
            create_scan(machine)
            create_tokens(machine)
            create_tools(machine)
            create_notes(machine)
            create_scripts(machine)
            create_src(machine)
            print(f'[+] Created directory for {machine.name}')



