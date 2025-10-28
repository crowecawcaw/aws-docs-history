# Sample install of AWS Elemental Conductor Live

Following is a screen printout of a typical install of AWS Elemental Conductor Live, showing the prompts
and possible responses.

```
[elemental@hostname ~] **sudo sh ./elemental\_production\_conductor\_live247\_3.25.5.4.12345.run -l -z -t**
Verifying archive integrity... All good.
Uncompressing Elemental Installer  100%
/tmp/selfgz1160911216/elemental_system_update/rpms /tmp/selfgz1160911216
Non-fatal POSTIN scriptlet failure in rpm package 1:logstash-6.5.4-1.noarch
/tmp/selfgz1160911216
Stopping Services
..
.
Checking Elemental System Update
Starting system update
New system update version: 3150008
System packages are now being updated and modified!
Please DO NOT interrupt the installer after this point!
.

Initializing RPM repo......
Cleaning up old kernels
...

Installing RPMs............................................................
..
Installing MOTD
Installing /etc/issue
.............................
..............................
Reload the systemd manager configuration
.
Installing logstash-forwarder plugin for logstash
Installing gems......................................................................
Running scripts......................................................................
Starting plat-api.
.Created symlink from /etc/systemd/system/multi-user.target.wants/plat-api.service to /usr/lib/systemd/system/plat-api.service.

Initializing postgres
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.UTF-8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /data/pgsql/data94 ... ok
creating subdirectories ... ok
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting dynamic shared memory implementation ... posix
creating configuration files ... ok
creating template1 database in /data/pgsql/data94/base/1 ... ok
initializing pg_authid ... ok
initializing dependencies ... ok
creating system views ... ok
loading system objects' descriptions ... ok
creating collations ... ok
creating conversions ... ok
creating dictionaries ... ok
setting privileges on built-in objects ... ok
creating information schema ... ok
loading PL/pgSQL server-side language ... ok
vacuuming database template1 ... ok
copying template1 to template0 ... ok
copying template1 to postgres ... ok
syncing data to disk ... ok

WARNING: enabling "trust" authentication for local connections
You can change this by editing pg_hba.conf or using the option -A, or
--auth-local and --auth-host, the next time you run initdb.

Success. You can now start the database server using:

    /usr/pgsql-9.4/bin/postgres -D /data/pgsql/data94
or
    /usr/pgsql-9.4/bin/pg_ctl -D /data/pgsql/data94 -l logfile start

Setting up config files
Starting the database service
Created symlink from /etc/systemd/system/multi-user.target.wants/postgresql-9.4.service to /usr/lib/systemd/system/postgresql-9.4.service.
Setting password for default user 'postgres'
ALTER ROLE
Tightening Postgres access security
Reloading Postgres
Redirecting to /bin/systemctl reload postgresql-9.4.service
Welcome to the product installation utility!
Version information:
   Conductor Live 3.25.0.12345
   -------------------------
    ruby 2.3.7p456 (2018-03-28 revision 63024) [x86_64-linux]
    Rails 3.2.22.5
    psql (PostgreSQL) 9.4.19
    Elemental Git revision 0290c91c
```

You are prompted to read and accept the EULA.

```
Checking license files.
IMPORTANT INFORMATION
.
.
.
Continue? [Y] `y`
.
.
.
Continue? [Y] `y`
.
.
.
Continue? [Y] `y`
.
.
.
Do you agree to these terms? [N] `y`
```

You are prompted to configure the network.

```
Enter this server's Hostname: [elemental@hostname ~]live-3-01
Detected 2 ethernet devices
Configuring eth0

Does eth0 use DHCP to get its IP address? [Y]
Would you like to configure eth1? [N]
The firewall for this system is currently enabled. Would you like to disable it? [N]


```

Services are stopped (note that actually no services are running) and interfaces are shut down.

```
Stopping services...
Restarting network services
Redirecting to /bin/systemctl start postgresql-9.4.service
Creating user 'elemental'
Creating database 'web_production'
Granting all privileges on 'web_production' to user 'elemental'
```

Interfaces are configured with the new information.

```
Bringing up loopback interface:    [  OK  ]
Bringing up interface eth0:  
Determining IP information for eth0... done.
   [  OK  ] Bringing up interface eth1:  
Determining IP information for eth1... done.
  [  OK  ]
```

The Conductor Live software is configured.

```
Creating/Updating database...
Running migrations - this could take a while.
Database creation complete!
Loading Rails environment...
Adding node to database...
Saving settings...
Adding cluster stat monitors...
Adding node stat monitors...
Adding cluster scheduled tasks...
Adding node scheduled tasks...
Adding licensing scheduled tasks...
Hardware and license check complete
Creating default directory structures and data
```

You are prompted for the time zone and user authentication.

```
Configuring time zone...
...
Select time zone ('n' for more) [Pacific Time (US & Canada)]
Selected: Pacific Time (US & Canada)
Do you wish to enabled authentication [N]
```

The installation continues.

```
Changing permissions and ownership...
Cleaning elemental_ipc...
Removing tmp...
Removing cached files
Configuring Apache...
Adding Elemental service...
Configuring log rotation...
Configuring apache...

..Configuring SNMP...
Configuring dynamic libraries...
Configuring NTP...
Setting sysctl configuration and adding to /etc/rc.local...
Shutting down SMB services: [60G[[0;32m  OK  [0;39m]
Starting SMB services: [60G[[0;32m  OK  [0;39m]
 
Configuring RabbitMQ.........
 
Setting CPU scaling governor
Starting services...
Starting system logger: [60G[[0;32m  OK  [0;39m]
Starting httpd: httpd.worker: Could not reliably determine the server's fully qualified domain name, using ::1 for ServerName
[60G[[0;32m  OK  [0;39m]
Starting ntpd:
Starting snmpd: [60G[[0;32m  OK  [0;39m]
```

You are prompted to start elemental_se.

```
Would you like to start the Elemental service now? [Y]
Starting elemental_se:     [  OK  ]
Starting elemental-motd:   [60G[[0;32m  OK  [0;39m]
Starting elemental-issue:  [  OK  ]
 
Installation and configuration complete!
Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
Enjoy!
```
