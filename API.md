## Tool

The new tool would ...
1. create the directory structure.
2. create a tools directory.
3. place htbclient.py into the tools directory as htbclient
4. create scripts in each <machine>/ctrl/ folder called start, stop, reset, todo, extend, own
5. the scripts would be setup to call htbclient with the proper arguments for that machine
6. maybe make a script called note that creates note entries as I go instead of having to manually edit notes?
7. look at way to automatically save history file for all commands that were executed in that directory into a .history file?
8. have an option to perform scans on all systems, it will activate them, scan them with a fast and a full scan then it will shut them down and write a file to ./meta/scan_compelete to let it know not to scan it again in the future.

## List all machines

```
GET /api/machines/get/all
Host: www.hackthebox.eu
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.hackthebox.eu/home/machines
X-CSRF-TOKEN: KaHPLgD1TiSxTS6gNJmVwiw4owgphiY4vUOszPMc
X-Requested-With: XMLHttpRequest
Authorization: Bearer nj0ieDAMVgr53S41X0sIPuuuuep46jOqWK12QPedCp5spbDKJL59HNxMaeOU
X-XSRF-TOKEN: eyJpdiI6ImlxZ3MrKzF3RkVMaWoxdE9NXC93RTZ3PT0iLCJ2YWx1ZSI6InIyR3dlMDhGYjRUSHpGeWRuR2QyaStYZ1dxaE9CeG5JU2RFeXZKZFJMTjA1Y3d2Z01PelYxNTdoYTh0VFY1OSsiLCJtYWMiOiI3OGJjNDdjYWIzMWYzNWUxZGNhMDU5ZGQ0N2QwZGRmODQ1ZGQ0NTZjMzM4Zjc0ZjVlMGU1OTQ4NjJmMjVmZWUyIn0=
Cookie: __cfduid=dfba5a4aca49685722716cf491f3e5dcc1565641013; __stripe_mid=5b491dca-d52f-441f-8b09-a2584dcfa91d; XSRF-TOKEN=eyJpdiI6ImlxZ3MrKzF3RkVMaWoxdE9NXC93RTZ3PT0iLCJ2YWx1ZSI6InIyR3dlMDhGYjRUSHpGeWRuR2QyaStYZ1dxaE9CeG5JU2RFeXZKZFJMTjA1Y3d2Z01PelYxNTdoYTh0VFY1OSsiLCJtYWMiOiI3OGJjNDdjYWIzMWYzNWUxZGNhMDU5ZGQ0N2QwZGRmODQ1ZGQ0NTZjMzM4Zjc0ZjVlMGU1OTQ4NjJmMjVmZWUyIn0%3D; hackthebox_session=eyJpdiI6IlwvbWJ5QVF3dEpUbmFBZHpCUHlaRUh3PT0iLCJ2YWx1ZSI6IjQwSEU4Y2FXOXBvUExjUVJFXC9YeW12VUU1b0F1TlV2TDBuOUdzajhEQlhIQ2RHdjVGRGpONzE3QWpwR0IwZHJTIiwibWFjIjoiYzc3Yzg5NmFlOGYyZDdhMWNiZDA2ZDYzZTc2MzE5N2RhN2VjYTg2YzRlNDEzZmE4ZDg0MGYxMjNlY2RkNmNlMSJ9; __stripe_sid=904521a4-64d8-4262-aa32-da8a75d8184b
Connection: close
```

## Spawn machine
```
POST /api/vm/vip/assign/221 HTTP/1.1
Host: www.hackthebox.eu
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.hackthebox.eu/home/machines
X-CSRF-TOKEN: lc7Dsy9uG4U7hhIYmjay9qPV8ezcCiAOB0Q0GgOc
X-Requested-With: XMLHttpRequest
Authorization: Bearer nj0ieDAMVgr53S41X0sIPuuuuep46jOqWK12QPedCp5spbDKJL59HNxMaeOU
X-XSRF-TOKEN: eyJpdiI6IjBNTVwvdFpXYU5tOXJcLzQ0ODlmU1Bmdz09IiwidmFsdWUiOiJiSENhZFFRVVJ2a1Vyb2pBYUFkakpVOW9NNTF5ZG0wSURJT2orbGR2OWc1TTg1eTE1YVZaNm1IS1JEZTl4RFRSIiwibWFjIjoiOWM0ZjE2NmZjMGI3MDhhY2I5M2ZkOTFmOWY0ZmVmZTE5ZWFjMGIyNmJmNjVjYWNmMTEwMjhmZWE2ZTRjOGJjZCJ9
Cookie: __cfduid=dfba5a4aca49685722716cf491f3e5dcc1565641013; __stripe_mid=5b491dca-d52f-441f-8b09-a2584dcfa91d; XSRF-TOKEN=eyJpdiI6IjBNTVwvdFpXYU5tOXJcLzQ0ODlmU1Bmdz09IiwidmFsdWUiOiJiSENhZFFRVVJ2a1Vyb2pBYUFkakpVOW9NNTF5ZG0wSURJT2orbGR2OWc1TTg1eTE1YVZaNm1IS1JEZTl4RFRSIiwibWFjIjoiOWM0ZjE2NmZjMGI3MDhhY2I5M2ZkOTFmOWY0ZmVmZTE5ZWFjMGIyNmJmNjVjYWNmMTEwMjhmZWE2ZTRjOGJjZCJ9; hackthebox_session=eyJpdiI6ImtvTUpSeWl2aWlrbmJwcjlwMnNXYUE9PSIsInZhbHVlIjoiMDFCTHlrTWMydHZ0Tm9IenFoazN3UEFndHA4VXZEK0ZEbTBRcmQ3VUtOb2xKait0Q0NqcldXSVZUeHlnbkJkZyIsIm1hYyI6ImFiYjA2YWYyNDJkZjIyZDdiYzg0NGQyYmE5NDY3NGQ4NzVmNDliZWQ4MTZjNDhkZmQ5NDUzODU2MjZjMTA4NTcifQ%3D%3D; __stripe_sid=904521a4-64d8-4262-aa32-da8a75d8184b
Connection: close
Content-Length: 0
```

```
HTTP/1.1 200 OK
Date: Mon, 23 Dec 2019 19:49:52 GMT
Content-Type: application/json
Connection: close
Vary: Accept-Encoding
Cache-Control: no-cache, private
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
CF-Cache-Status: DYNAMIC
Strict-Transport-Security: max-age=0; includeSubDomains
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 549cdbe61f256e60-SJC
Content-Length: 49

{"success":1,"status":"Machine deployed to lab."}
```

```
/ap/machines/get/all
/api/machines/owns
/api/machines/difficulty
/api/machines/reviews
/api/machines/todo
/api/machines/expiry
/api/machines/spawned
/api/machines/terminating
/api/machines/assigned
/api/machines/resetting
/api/vm/vip/assign/218
```

# Ideal Commands
```
ListAllUserOwns()
ListAllRootOwns()
ListAllMachines()
StartMachine()
StopMachine()
SubmitUser()
SubmitRoot()
GetMachineStatus()
GetProfile()
```

https://github.com/QHpix/HackTheBox-python-api/blob/master/hackthebox.py
