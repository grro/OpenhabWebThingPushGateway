import pathlib
from os import system, remove
from string import Template

UNIT_TEMPLATE = Template('''
[Unit]
Description=$packagename
After=syslog.target

[Service]
Type=simple
ExecStart=$entrypoint --command listen --filename $filename
SyslogIdentifier=$packagename
StandardOutput=syslog
StandardError=syslog
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
''')


def register(packagename: str, entrypoint: str, filename: str):
    unit = UNIT_TEMPLATE.substitute(packagename=packagename, entrypoint=entrypoint, filename=filename)
    service = packagename + ".service"
    unit_file_fullname = str(pathlib.Path("/", "etc", "systemd", "system", service))
    with open(unit_file_fullname, "w") as file:
        file.write(unit)
    system("sudo systemctl daemon-reload")
    system("sudo systemctl enable " + service)
    system("sudo systemctl restart " + service)
    system("sudo systemctl status " + service)


def deregister(packagename: str):
    print("deregister " + packagename)

    service = packagename + ".service"
    unit_file_fullname = str(pathlib.Path("/", "etc", "systemd", "system", service))
    system("sudo systemctl stop " + service)
    system("sudo systemctl disable " + service)
    system("sudo systemctl daemon-reload")
    try:
        remove(unit_file_fullname)
    except Exception as e:
        pass

def printlog(packagename: str):
    service = packagename + ".service"
    system("sudo journalctl -f -u " + service)
