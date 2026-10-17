import time
import random
from datetime import datetime
import os

class CommandExecutor:
    def __init__(self, filesystem):
        self.filesystem = filesystem
        self.commands = {
            'help': self.cmd_help,
            'cls': self.cmd_cls,
            'clear': self.cmd_cls,
            'cd': self.cmd_cd,
            'dir': self.cmd_dir,
            'ls': self.cmd_dir,
            'pwd': self.cmd_pwd,
            'echo': self.cmd_echo,
            'date': self.cmd_date,
            'time': self.cmd_time,
            'systeminfo': self.cmd_systeminfo,
            'ipconfig': self.cmd_ipconfig,
            'tasklist': self.cmd_tasklist,
            'taskkill': self.cmd_taskkill,
            'type': self.cmd_type,
            'copy': self.cmd_copy,
            'del': self.cmd_del,
            'mkdir': self.cmd_mkdir,
            'rmdir': self.cmd_rmdir,
            'ren': self.cmd_ren,
            'move': self.cmd_move,
            'tree': self.cmd_tree,
            'chdir': self.cmd_cd,
            'ver': self.cmd_ver,
            'exit': self.cmd_exit,
            'ping': self.cmd_ping,
            'netstat': self.cmd_netstat,
            'whoami': self.cmd_whoami,
            'wmic': self.cmd_wmic,
            'powershell': self.cmd_powershell,
            'cmd': self.cmd_cmd,
            'diskpart': self.cmd_diskpart,
            'format': self.cmd_format,
            'chkdsk': self.cmd_chkdsk,
            'attrib': self.cmd_attrib,
            'findstr': self.cmd_findstr,
            'find': self.cmd_find,
            'more': self.cmd_more,
            'fc': self.cmd_fc,
            'comp': self.cmd_comp,
        }
    
    def execute(self, cmd_name, args, current_path):
        """Выполняет команду"""
        if cmd_name in self.commands:
            return self.commands[cmd_name](args, current_path)
        else:
            return {
                'success': False,
                'output': '',
                'error': f"'{cmd_name}' is not recognized as an internal or external command,\noperable program or batch file."
            }
    
    # ============== ОСНОВНЫЕ КОМАНДЫ ==============
    
    def cmd_help(self, args, current_path):
        """Справка по командам"""
        output = """For more information on a specific command, type:  HELP command-name

ASSOC          Displays or modifies file extension associations.
ATTRIB         Displays or changes file attributes.
BREAK          Sets or clears extended CTRL+C checking.
BCDEDIT        Sets properties in boot database to control boot loading.
CACLS          Displays or modifies access control lists (ACLs) of files.
CALL           Calls one batch program from another.
CD             Displays the name of or changes the current directory.
CHCP           Displays or sets the active code page number.
CHDIR          Displays the name of or changes the current directory.
CHKDSK         Checks a disk and displays a status report.
CHKNTFS        Displays or modifies the checking of disk at boot time.
CLS            Clears the screen.
CMD            Starts a new instance of the Windows command interpreter.
CMDKEY         Creates, lists, and deletes stored user names and passwords.
COLOR          Sets the default console foreground and background colors.
COMP           Compares the contents of two files or sets of files.
COMPACT        Displays or alters the compression of files on NTFS partitions.
CONVERT        Converts FAT volumes to NTFS.
COPY           Copies one or more files to another location.
DATE           Displays or sets the date.
DEL            Deletes one or more files.
DELIMS         Sets the delimiter for a command set.
DIR            Displays a list of files and subdirectories in a directory.
DISKPART       Invokes the diskpart script interpreter.
DOSKEY         Edits command lines, recalls Windows commands, and creates macros.
DRIVERQUERY    Displays the status of all installed device drivers.
ECHO           Displays messages, or turns command echoing on or off.
ENDLOCAL       Ends localization of environment changes in a batch file.
ERASE          Deletes one or more files.
EXIT           Quits the CMD.EXE program (command interpreter).
FC             Compares two files or sets of files, and displays the differences between them.
FIND           Searches for a text string in a file or files.
FINDSTR        Searches for strings in files.
FOR            Runs a specified command for each file in a set of files.
FORFILES      Selects files in a folder for batch processing.
FORMAT         Formats a disk for use with Windows.
FSUTIL         Displays or configures the file system properties.
FTYPE          Displays or modifies file types used in file extension associations.
GETMAC         Displays the media access control (MAC) address of all the network adapters on a computer.
GO             This command is not supported on this version of Windows.
GOTO           Directs the Windows command interpreter to a labeled line in a batch program.
GPRESULT       Displays Group Policy information for a computer and user.
GRAFTABL       Enables Windows to display an extended character set in graphics mode.
HELP           Provides Help information for Windows commands.
HOSTNAME       Prints the name of the host computer.
ICACLS         Display, modify, backup, or restore ACLs for files and directories.
IF             Performs conditional processing in batch programs.
IPCONFIG       Displays all current TCP/IP network configuration values.
LABEL          Creates, changes, or deletes the volume label of a disk.
LOGMAN         Create and manage Event Trace Session and performance logs.
LOGOFF         Logs off a user.
MORE           Displays output one screen at a time.
MOVE           Moves one or more files from one directory to another directory.
OPENFILES      Displays files opened by remote users for a file share.
PATH           Displays or sets a search path for executable files.
PAUSE          Suspends processing of a batch file and displays a message.
PING           Pings a host to verify that the host is reachable.
POPD           Restores the previous value of the current directory.
PRINT          Prints a text file.
PRNCNFG        Configure or display configuration information about a printer.
PRNMNGR        Adds, deletes, or lists printers or printer connections.
PROMPT         Changes the Windows command prompt.
PUSHD          Saves the current directory then changes it.
RD             Removes a directory.
RECOVER        Recovers readable information from a bad or defective disk.
REM            Records comments (remarks) in batch files or CONFIG.SYS.
REN            Renames a file or files.
RENAME         Renames a file or files.
REPLACE        Replaces files.
RESET          Resets the session subsystem software to its initial state.
RMDIR          Removes a directory.
ROBOCOPY       Advanced utility to copy files and directory trees
RUNAS          Runs a program under a different user account.
RWINSTA        (Reset Session) resets the session subsystem hardware and software to initial values.
SCHTASKS       Schedules commands and programs to run on a computer.
SETLOCAL       Begins localization of environment changes in a batch file.
SETX           Sets environment variables.
SHIFT          Shifts the position of replaceable parameters in batch files.
SHUTDOWN       Allows proper local or remote shutdown of machine.
SORT           Sorts input.
START          Starts a separate window to run a specified program or command.
SUBST          Associates a path with a drive letter.
SYSTEMINFO    Displays detailed configuration information about a computer and its operating system.
TASKLIST       Displays all currently running processes with their Process IDs (PID).
TASKKILL       Kill or stop a running process or application.
TIME           Displays or sets the system time.
TITLE          Sets the window title for a CMD.EXE session.
TREE           Graphically displays the directory structure of a drive or path.
TYPE           Displays the contents of a text file or files.
TZUTIL         Displays Time Zone Utility.
UMASK          Sets or displays file creation mode mask.
VERIFY         Tells Windows whether to verify that your files are written correctly to a disk.
VER            Displays the Windows version.
VOL            Displays a disk volume label and serial number.
XCOPY          Copies files and directory trees.
WMIC           Displays WMI information inside interactive command shell.
WHOAMI         Displays user, group and privileges information.

Type HELP <command> for more information on a command.
"""
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_cls(self, args, current_path):
        """Очистка экрана"""
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': '', 'error': ''}
    
    def cmd_cd(self, args, current_path):
        """Смена директории"""
        if not args:
            return {'success': True, 'output': current_path + '\n', 'error': '', 'new_path': current_path}
        
        new_path = args[0]
        
        # Обработка специальных путей
        if new_path == '..':
            parts = current_path.split('\\')
            if len(parts) > 1:
                new_path = '\\'.join(parts[:-1])
            else:
                new_path = current_path
        elif new_path == '.':
            return {'success': True, 'output': '', 'error': '', 'new_path': current_path}
        elif new_path.startswith('C:') or new_path.startswith('D:'):
            if not self.filesystem.path_exists(new_path):
                return {'success': False, 'output': '', 'error': f"The system cannot find the path specified."}
        else:
            if not new_path.startswith('\\'):
                new_path = current_path + '\\' + new_path
            
            if not self.filesystem.path_exists(new_path):
                return {'success': False, 'output': '', 'error': f"The system cannot find the path specified."}
        
        return {'success': True, 'output': '', 'error': '', 'new_path': new_path}
    
    def cmd_dir(self, args, current_path):
        """Список файлов"""
        path = current_path if not args else args[0]
        
        if not self.filesystem.path_exists(path):
            return {'success': False, 'output': '', 'error': f"The system cannot find the path specified."}
        
        items = self.filesystem.list_directory(path)
        
        output = f"\n Directory of {path}\n\n"
        output += f"{'[.]':<30} {'':>20}\n"
        output += f"{'[..]':<30} {'':>20}\n"
        
        for item in items:
            if self.filesystem.is_directory(f"{path}\\{item}"):
                output += f"[{item}]".ljust(30) + f"{'<DIR>':>20}\n"
            else:
                output += f"{item}".ljust(30) + f"{'1,234 bytes':>20}\n"
        
        output += f"\n         {len(items)} File(s)\n"
        output += f"  {random.randint(100, 500)} GB(s) free\n"
        
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_pwd(self, args, current_path):
        """Текущая директория"""
        return {'success': True, 'output': current_path + '\n', 'error': ''}
    
    def cmd_echo(self, args, current_path):
        """Вывод текста"""
        if not args:
            return {'success': True, 'output': 'ECHO is on.\n', 'error': ''}
        
        text = ' '.join(args)
        return {'success': True, 'output': text + '\n', 'error': ''}
    
    def cmd_date(self, args, current_path):
        """Текущая дата"""
        now = datetime.now()
        date_str = now.strftime('%a %m/%d/%Y')
        output = f"\nThe current date is: {date_str}\nEnter the new date: (mm-dd-yy) \n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_time(self, args, current_path):
        """Текущее время"""
        now = datetime.now()
        time_str = now.strftime('%H:%M:%S.%f')[:-3]
        output = f"\nThe current time is: {time_str}\nEnter the new time: (hh:mm:ss) \n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_systeminfo(self, args, current_path):
        """Информация о системе"""
        output = """
Host Name:                 DESKTOP-ABC123
OS Name:                   Microsoft Windows 10 Pro
OS Version:                10.0.19045 Build 19045
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
System Boot Time:          12/15/2024, 8:45:30 AM
System Manufacturer:       Dell Inc.
System Model:              XPS 13 9370
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 142 Stepping 10
                                 GenuineIntel ~2300 Mhz
BIOS Version:              Dell Inc. 2.21.0, 11/8/2024
Windows Directory:         C:\\Windows
System Directory:          C:\\Windows\\system32
Boot Device:               \\Device\\HarddiskVolume1
System Locale:             en-US; English (United States)
Input Locale:              en-US; English (United States)
UTC Offset:                -05:00
Time Zone:                 Eastern Standard Time
Daylight Saving Time:      In effect
Installed RAM:             16.0 GB
Available Physical Memory: 8.2 GB
Total Virtual Memory:      18.5 GB
Available Virtual Memory:  10.3 GB
Page File Space:           2.5 GB
Domain:                    WORKGROUP
Logon Server:              \\\\DESKTOP-ABC123
Logon User:                Admin
Network Card(s):           2 NIC(s) Installed.
                           [01]: Name : Ethernet
                                 Connection Name : Ethernet
                                 Status : Connected
                           [02]: Name : Wi-Fi
                                 Connection Name : Wi-Fi
                                 Status : Disconnected
Hyper-V:                   Yes
"""
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_ipconfig(self, args, current_path):
        """Конфигурация IP"""
        output = """
Windows IP Configuration

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : 
   Link-local IPv6 Address . . . . . : fe80::1c50:f64e:4c4c:5f3e%11
   IPv4 Address. . . . . . . . . . . : 192.168.1.105
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1
   DHCPv4 DHCP Server . . . . . . . : 192.168.1.1
   DHCPv4 Lease Obtained. . . . . . : Saturday, December 14, 2024 11:30:45 PM
   DHCPv4 Lease Expires . . . . . . : Sunday, December 15, 2024 11:30:45 PM
   DNS Servers . . . . . . . . . . . : 192.168.1.1
                                       8.8.8.8
   NetBIOS over Tcpip. . . . . . . . : Enabled

Wireless LAN adapter Wi-Fi:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 
"""
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_tasklist(self, args, current_path):
        """Список задач"""
        processes = [
            ("System", 4),
            ("csrss.exe", 516),
            ("wininit.exe", 528),
            ("services.exe", 660),
            ("lsass.exe", 668),
            ("svchost.exe", 772),
            ("svchost.exe", 836),
            ("svchost.exe", 940),
            ("fontdrvhost.exe", 1004),
            ("dwm.exe", 1248),
            ("explorer.exe", 1640),
            ("chrome.exe", 2156),
            ("Code.exe", 2840),
            ("python.exe", 3012),
            ("notepad.exe", 3456),
            ("cmd.exe", 3888),
        ]
        
        output = "Image Name                     PID Session Name        Session#    Mem Usage\n"
        output += "========================= ======== ================ ========== ============\n"
        
        for name, pid in processes:
            mem = random.randint(1, 500)
            output += f"{name:<29} {pid:<8} Console              1       {mem:>6,} K\n"
        
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_taskkill(self, args, current_path):
        """Завершение задачи"""
        if not args:
            return {'success': False, 'output': '', 'error': 'Invalid parameter. Type "TASKKILL /?" for usage.'}
        
        output = "SUCCESS: Sent termination signal to the process.\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_type(self, args, current_path):
        """Вывод содержимого файла"""
        if not args:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        file_path = args[0]
        content = self.filesystem.get_file_content(file_path)
        
        if content is None:
            return {'success': False, 'output': '', 'error': 'The system cannot find the file specified.'}
        
        return {'success': True, 'output': content + '\n', 'error': ''}
    
    def cmd_copy(self, args, current_path):
        """Копирование файла"""
        if len(args) < 2:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        output = f"        1 file(s) copied.\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_del(self, args, current_path):
        """Удаление файла"""
        if not args:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        output = f"{args[0]} deleted.\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_mkdir(self, args, current_path):
        """Создание директории"""
        if not args:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        return {'success': True, 'output': '', 'error': ''}
    
    def cmd_rmdir(self, args, current_path):
        """Удаление директории"""
        if not args:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        return {'success': True, 'output': '', 'error': ''}
    
    def cmd_ren(self, args, current_path):
        """Переименование"""
        if len(args) < 2:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        return {'success': True, 'output': '', 'error': ''}
    
    def cmd_move(self, args, current_path):
        """Перемещение"""
        if len(args) < 2:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        output = f"        1 file(s) moved.\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_tree(self, args, current_path):
        """Дерево директорий"""
        output = """C:\\
├── Users
│   └── Admin
│       ├── Desktop
│       ├── Documents
│       │   ├── Project.txt
│       │   └── Notes.txt
│       └── Downloads
├── Windows
│   └── System32
└── Program Files
    ├── Python
    └── Git
"""
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_ver(self, args, current_path):
        """Версия Windows"""
        output = "\nMicrosoft Windows [Version 10.0.19045]\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_exit(self, args, current_path):
        """Выход"""
        import sys
        sys.exit(0)
    
    def cmd_ping(self, args, current_path):
        """Ping"""
        if not args:
            return {'success': False, 'output': '', 'error': 'Usage: ping [-t] [-a] [-n count] [-l size] [-f] [-i TTL] [-v TOS] [-r count] [-s count] [-j computer-list] | [-k host-list] [-w timeout] [-R] [-S srcaddr] [-4] [-6] target_name'}
        
        target = args[0]
        output = f"\nPinging {target} [192.168.1.{random.randint(1, 254)}] with 32 bytes of data:\n"
        
        for i in range(4):
            time_val = random.randint(20, 100)
            output += f"Reply from 192.168.1.{random.randint(1, 254)}: bytes=32 time={time_val}ms TTL=64\n"
        
        total_time = random.randint(80, 400)
        output += f"\nPing statistics for {target}:\n"
        output += f"    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\n"
        output += f"Approximate round trip times in milli-seconds:\n"
        output += f"    Minimum = 24ms, Maximum = 98ms, Average = {total_time//4}ms\n"
        
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_netstat(self, args, current_path):
        """Netstat"""
        output = """Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING
  TCP    127.0.0.1:49664        0.0.0.0:0              LISTENING
  TCP    192.168.1.105:56273    142.251.41.14:443      ESTABLISHED
  TCP    192.168.1.105:56274    142.251.41.14:443      ESTABLISHED
  TCP    192.168.1.105:56275    172.217.14.206:443     TIME_WAIT
  TCP    [::]:135               [::]:0                 LISTENING
  TCP    [::]:445               [::]:0                 LISTENING
  TCP    [::1]:49664            [::]:0                 LISTENING
  UDP    0.0.0.0:123            *:*
  UDP    0.0.0.0:5353           *:*
  UDP    192.168.1.105:137      *:*
  UDP    192.168.1.105:138      *:*
"""
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_whoami(self, args, current_path):
        """Текущий пользователь"""
        output = "DESKTOP-ABC123\\Admin\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_wmic(self, args, current_path):
        """WMI Command"""
        if args and args[0].lower() == 'logicaldisk':
            output = """
Node   : DESKTOP-ABC123
Class  : Win32_LogicalDisk
Name   : C:
Size   : 512110190592
FreeSpace : 176319709184
"""
            return {'success': True, 'output': output, 'error': ''}
        
        return {'success': False, 'output': '', 'error': 'Invalid WMIC command'}
    
    def cmd_powershell(self, args, current_path):
        """Попытка запустить PowerShell"""
        output = "Windows PowerShell\nCopyright (C) Microsoft Corporation. All rights reserved.\n\n"
        output += "Try the new cross-platform PowerShell https://aka.ms/pscore6\n\n"
        output += "PS C:\\> "
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_cmd(self, args, current_path):
        """Вложенный CMD"""
        output = "Starting a nested instance of CMD...\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_diskpart(self, args, current_path):
        """DiskPart"""
        output = """Microsoft DiskPart version 10.0.19045

Copyright (C) Microsoft Corporation.
On computer: DESKTOP-ABC123

DISKPART> 
"""
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_format(self, args, current_path):
        """Форматирование"""
        if not args:
            return {'success': False, 'output': '', 'error': 'Invalid parameter. Type "FORMAT /?" for usage.'}
        
        output = f"Formatting {args[0]}...\n"
        output += "100% complete.\n"
        output += "Format complete.\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_chkdsk(self, args, current_path):
        """Проверка диска"""
        drive = args[0] if args else 'C:'
        output = f"""The type of the file system is NTFS.
Volume label is OS.
Volume Serial Number is 1A2B-3C4D

Chkdsk is verifying files and folders...

File and folder verification is complete.

0 large allocation units allocated to user files.
0 small allocation units allocated to user files.
0 bad sectors encountered.

Status code returned by Chkdsk: 0
"""
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_attrib(self, args, current_path):
        """Атрибуты файла"""
        output = "A  C:\\Users\\Admin\\Documents\\Project.txt\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_findstr(self, args, current_path):
        """Поиск строк"""
        if len(args) < 2:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        output = f"C:\\Documents\\example.txt:1:Found: {args[0]}\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_find(self, args, current_path):
        """Find (поиск)"""
        if not args:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        return {'success': True, 'output': '', 'error': ''}
    
    def cmd_more(self, args, current_path):
        """More (постраничный вывод)"""
        if not args:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        return {'success': True, 'output': '', 'error': ''}
    
    def cmd_fc(self, args, current_path):
        """Сравнение файлов"""
        if len(args) < 2:
            return {'success': False, 'output': '', 'error': 'Insufficient number of parameters'}
        
        output = f"Comparing files {args[0]} and {args[1]}...\nNo differences encountered.\n"
        return {'success': True, 'output': output, 'error': ''}
    
    def cmd_comp(self, args, current_path):
        """Compare (сравнение)"""
        if len(args) < 2:
            return {'success': False, 'output': '', 'error': 'The syntax of the command is incorrect.'}
        
        output = "Files are identical\n"
        return {'success': True, 'output': output, 'error': ''}
