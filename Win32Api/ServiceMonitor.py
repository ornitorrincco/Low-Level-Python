import win32con
import win32api
import win32security
import wmi
import sys
import os

def logToFile(message):
    fd = open('Process Monitor Log.csv','ab')
    fd.write(bytes(message, encoding= 'utf-8'))
    fd.close()
    return

# create a log file header
logToFile('Time, User, Executable, CommandLine, PID, Parent PID, Privileges')

# instantiate the WMI interfaces
c = wmi.WMI()

# create our process Monitor TODO(ornitorrincco): is this a function?
processWatcher = c.Win32_Process.watch_for('creation')

while True:
    try:
        newProcess = processWatcher()
        print(newProcess)
        processOwner = newProcess.GetOwner()
        print(processOwner)
        createDate = newProcess.CreationDate
        print(createDate)
        executable = newProcess.ExecutablePath
        print(executable)
        cmdline = newProcess.CommandLine
        print(cmdline)
        pid = newProcess.ProcessId
        print(pid)
        parentPid = newProcess.ParentProcessId
        print(parentPid)
        privileges = 'N/A'
        print("%s,%s,%s,%s,%s,%s,%s\r\n" % (create_date, "%s\\%s" % (proc_owner[0],proc_owner[2]), executable, cmdline, pid, parent_pid, privileges))
    except:
        pass
