# Sample Upgrade

Following is a screen printout of a typical upgrade, showing the prompts and possible
responses.

```
[elemental@hostname ~]$ **sudo sh ./elemental\_production\_conductor\_live247\_3.25.4.12345.run --skip-all**
Verifying archive integrity... All good.
Uncompressing Elemental Installer............
Network device eth0 already initialized...
Stopping Apache..
Checking Elemental System Update
Starting system update
New system update version: 25101
Skipping System Update, version 25101 has already been applied
Installing Conductor Live 3.25.1.12345
Network device eth0 already initialized...
 
Welcome to the product installation utility!
Version information:
        Conductor Live (CPU) 3.25.4.12345
        -------------------------
        ruby 1.9.3p484 (2013-11-22 revision 43786) [x86_64-linux]
        Rails 3.2.17
        mysql  Ver 14.14 Distrib 5.1.73, for redhat-linux-gnu (x86_64) using readline 5.1
        Elemental Git revision 543f5b87
 
Checking license files.
IMPORTANT INFORMATION
.
.
.
Continue? [Y] y
 
2. LICENSE AND RESTRICTIONS.
.
.
.
Continue? [Y] y
 
TERM AND TERMINATION.  This Agreement is effective until terminated.  This
.
.
.
 
Continue? [Y] y
.
.
.
Do you agree to these terms? [N] y
```

The Conductor Live services and the database are stopped.

```
Stopping services...
Starting mysqld:                                           [  OK  ]
 
Stopping mysqld:                                           [  OK  ]
Starting mysqld:                                           [  OK  ]
```

The software is updated.

```
Creating/Updating database...
Running migrations - this could take a while.
Database updated!
Database creation complete!
Loading Rails environment...
Adding node to database...
Saving settings...
Adding cluster stat monitors...
Adding node stat monitors...
Adding cluster scheduled tasks...
Adding node scheduled tasks...
Adding licensing scheduled tasks...
```

Files are verified.

```
Checking hardware and license files...
[2014-08-29 22:24:31 +0000 SERVICE]: 8 CPU cores available, max CPU load: 21.12
 
Hardware and license check complete
Creating default directory structures and data
Setting server defaults...
Checking user presets...
Checking user profiles...
Changing permissions and ownership...
Cleaning elemental_ipc...
Removing tmp...
Removing cached files
Configuring Apache...
Adding Elemental service...
Configuring log rotation...
Configuring SNMP...
Configuring dynamic libraries...
Configuring NTP...
Setting sysctl configuration and adding to /etc/rc.local...
Configuring Avahi...
```

Services are started.

```
Shutting down SMB services:                                [  OK  ]
Starting SMB services:                                     [  OK  ]
 
Setting CPU scaling governorStarting services...
Starting system logger:                                    [  OK  ]
Starting httpd:                                            [  OK  ]
Starting ntpd:                                             [  OK  ]
Shutting down Avahi daemon:                                [  OK  ]
Starting Avahi daemon...                                   [  OK  ]
Starting snmpd:                                            [  OK  ]
```

The user is prompted to start elemental_se.

```
Would you like to start the Elemental service now? [Y] y
Starting elemental_se:                                     [  OK  ]
Starting elemental-issue:                                  [  OK  ]
 
Installation and configuration complete!
Please open a web browser and point it to http://10.4.136.91 to get to the web
interface.
Enjoy!
[elemental@hostname ~]$
```
