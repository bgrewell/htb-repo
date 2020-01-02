# HTB Repo
This project is one I created to help stay more organized when working on hackthebox.eu, the project has a basic skeleton that follows the way challenges are organized on the site itself as well as some scripts to help with interacting with the site using another project of mine `HTBClient` which inteacts with the hackthebox.eu site through the REST API that is used by the website itself.

## Requirements
1. www.hackthebox.eu account (this has only been tested with VIP accounts)
2. python3
3. git

## Getting Started
First things first you will need to clone the project to your local system. I recommend creating a spot where you want to store your work on hackthebox.eu then using the below command to clone the repository.

```
git clone https://github.com/BGrewell/htb-repo
```

You should see an output similar to below (number of items etc. will change over time)

```
root@kali:~/repos# git clone https://github.com/BGrewell/htb-repo
Cloning into 'htb-repo'...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 15 (delta 1), reused 15 (delta 1), pack-reused 0
Unpacking objects: 100% (15/15), done.
```

Once complete you should change into the root of the repository

```
cd htb-repo
```

You will then need to initialize a virtual environment (or if you prefer you can just install the dependencies using pip) and activate the virtual environment and install the required packages.

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Next you will need to set your hackthebox.eu username and password as environmental variables

```
export HTB_USER='<your username>'
export HTB_PASS='<your password>' 
# NOTE: be sure to use single quotes as shown above if your password contains characters that bash will attempt to expand
```

Once this is complete you should be able to update the basic skeleton repository with machine spacific information by using the following command from the root of the repository

```
./update.py
```

This will go through and create directories, metadata and scripts for all current machines on hackthebox.eu and you should see an output such as this listed below (again your boxes may be different)

```
(venv) root@kali:~/repos/htb-repo# ./update.py 
[+] Created directory for lame
[+] Created directory for legacy
[+] Created directory for devel
             ...
             ...
[+] Created directory for obscurity
[+] Created directory for resolute
[+] Created directory for playertwo
```

and if you enter a directory you should see the following directories and files

```
init.sh           # script to start working on a machine
.meta/            # metadata related to the machine
notes.md          # markdown file for notes on the system
scans/            # scans as well as some scripts to do a quick/full scan
scripts/          # scripts that control the machine via the HTBClient module
src/              # source code for any tools or scripts for the machine
tokens/           # tokens (ssh keys, logins etc. for the machine)
tools/            # specific tools that you wrote or aquired for the machine
```

### Change remote repo to your own *Private* repository
**This is very important and needs to be in bold. Make sure you do not publish this to a public repository, keep your work private!**

1. Create a **private** repository on a site like github.com


## Script Details

### Init.sh
This script is designed to get you started working on a machine. What is does is it creates a metadata file .meta/initialized which is empty but can be used to find boxes that you have started working on. It also creates a symlink to the current directory in `htb-repo/machines/current` so it is easier to get to the current machine you are working on (especially if you have been away for a while) then it adds the machine to your `todo` list on hackthebox.eu and finally `starts` the box (shutting down any you currently have running) so that you can start working on it. 

### scripts/start.sh
Helper script that uses `HTBClient` to start a machine from the command line. In this case it is setup to start the machine for the directory you are currently inside.

### scripts/stop.sh
Helper script that uses `HTBClient` to stop a machine from the command line. In this case it is setup to stop the machine for the directory you are currently inside.

### scripts/todo.sh
Helper script that uses `HTBClient` to toggle todo for a machine from the command line. In this case it is setup to toggle the machine for the directory you are currently inside.

### scripts/extend.sh
Helper script that uses `HTBClient` to extend a machine from the command line. In this case it is setup to extend the machine for the directory you are currently inside.

### scripts/own.sh
Helper script that uses `HTBClient` to own a machine from the command line. In this case it is setup to own the machine for the directory you are currently inside. You need to pass the flag and how difficult you felt it was from 0-10

### scans/nmap-quick.sh
Helper script that launches an nmap scan with common quick settings

### scans/nmap-full.sh
Helper script that launches an nmap scan with full port scan settings
