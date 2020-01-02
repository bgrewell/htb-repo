# HTB Repo
This project is one I created to help stay more organized when working on hackthebox.eu, the project has a basic skeleton that follows the way challenges are organized on the site itself as well as some scripts to help with interacting with the site using another project of mine `HTBClient` which inteacts with the hackthebox.eu site through the REST API that is used by the website itself.

## Requirements
1. www.hackthebox.eu account (this has only been tested with VIP accounts, feel free to let me know how it works with free)
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

and if you enter a directory you should see the following


