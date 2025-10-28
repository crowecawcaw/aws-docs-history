# Enabling or disabling high

availability (HA)

Disable high availability prior to performing any changes on the Conductor
nodes.

**To disable high availability on a conductor**:

1. From the Linux prompt, log in to the conductor node with the
   _elemental_ user credentials.
2. Enter the following command to configure the primary Conductor node for
   HA.

```
[elemental@hostname ~]$ sudo /opt/elemental_se/.support_utils/dbrepl disable
```

3. Restart the service using the following commands.

```
[elemental@hostname ~]$ sudo systemctl restart postgresql-15
[elemental@hostname ~]$ sudo systemctl restart elemental_se
```

4. Enter the following command to verify that Conductor high availability is
   disabled.

```
[elemental@hostname ~]$ tail -F /opt/elemental_se/web/log/conductor.output
```

The conductor.output log starts to scroll on the screen and shows messages as
they are occurring. Watch for the following INFO lines on the primary Conductor
node.

```
CONDUCTOR: Initializing environment
I, [2024-06-04T23:07:54.439807 #131824]  INFO -- : HA environment not enabled
[2024-06-04 23:08:00 UTC SERVICE]: Elemental Conductor File 2.18.x.x
```

5. Enter **Ctrl+C** to exit the tail command.
6. Enter the following command, where <day> is today (the day you are
   upgrading), typed with an initial capital letter: Mon, Tue, Wed, Thu, Fri, Sat,
   Sun:

```
[elemental@hostname ~]$ sudo tail -F /data/pgsql/logs/postgresql-<day>.log
```

7. Confirm that you see this line.

```
database system is ready to accept connections.
```

If the elemental_se or postgres process has already started when you starting
tailing the logs, you might not see the **ready to accept
connections** message. Instead, you could see **rejects connection for host messages** until you upgrade the
worker nodes. 8. Enter Ctrl+C to exit the tail command.
You must re-enable high availability on the Conductor nodes, to put the nodes back
into a redundant configuration. If you have only one Conductor File node, skip this
step.

**To enable high availability on the primary
Conductor**

1. From the Linux prompt, log in to the primary Conductor node with the _elemental_ user credentials.
2. Enter the following command to configure the primary Conductor node for high
   availability. Where _<dbrepl_config_file_name>_ is your dbrepl_config.yml
   file.

```
[elemental@hostname ~]$ sudo /opt/elemental_se/.support_utils/dbrepl configure <dbrepl_config_file_name> primary
```

3. Restart the elemental_se service.

```
[elemental@hostname ~] sudo systemctl restart elemental_se
```

4. Enter the following command to verify that the service is running.

```
[elemental@hostname ~] tail -F /opt/elemental_se/web/log/conductor.output
```

The conductor.output log starts to scroll on the screen and shows messages as
they are occurring. Watch for the following three INFO lines on the primary
Conductor node.

```
CONDUCTOR: Initializing environment
I, [2024-06-04T20:58:01.073149 #9844] INFO -- : Configuring the HA environment
I, [2024-06-04T20:58:03.170375 #9844] INFO -- : Preparing database as replication master
...
[2024-06-04 20:58:09 UTC SERVICE]: Elemental Conductor File 2.18.x.x
```

5. Enter Ctrl+C to exit the tail command.
6. Enter the following command, where <day> is today (the day you are
   upgrading), typed with an initial capital letter: Mon, Tue, Wed, Thu, Fri, Sat,
   Suns.

```
[elemental@hostname ~]$ sudo -s
[elemental@hostname ~]$ cd /data/pgsql/logs
[elemental@hostname ~]$ tail -F postgresql-<day>.log
```

7. Confirm that you see this line.

```
database system is ready to accept connections.
```

If the elemental_se or postgres process has already started when you starting
tailing the logs, you might not see the **ready to accept
connections message**. Instead, you could see **rejects connection for host messages** until you upgrade the
worker nodes. 8. Enter Ctrl+C to exit the tail command. 9. Type the following command to exit the session as the sudo user.

```
[elemental@hostname ~]$ exit
```

**On the secondary Conductor**

Repeat high availability steps on the secondary Conductor but use the following
command instead.

```
[elemental@hostname ~]$ sudo /opt/elemental_se/.support_utils/dbrepl configure <dbrepl_config_file_name> secondary
```
