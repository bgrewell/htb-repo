# HTB Repo
This project is one I created to help stay more organized when working on hackthebox.eu, the project has a basic skeleton that follows the way challenges are organized on the site itself as well as some scripts to help with interacting with the site using another project of mine `HTBClient` which inteacts with the hackthebox.eu site through the REST API that is used by the website itself.

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
