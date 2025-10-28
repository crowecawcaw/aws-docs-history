# Step L: Disable high availability

###### To disable high availability

1. If you're using a virtual machine (VM), take a snapshot before disabling high availability.
   See the VMware VSphere help text for more information.
2. On the web interface for the primary Conductor Livenode, go to the **Cluster** page and
   choose **Redundancy**.
3. In the **High Availability** field, choose **Disable**.
4. Verify that high availability is disabled. From Linux prompts, access the
   primary and secondary Conductor Live nodes with the _elemental_ user credentials. For
   password assistance, contact your system administrator.
5. In the remote terminal session for each Conductor Live, enter the following
   command to verify that Conductor Live high availability is disabled:

```
[elemental@hostname log]$ **tail -F /opt/elemental\_se/web/log/conductor\_live247.output**
```

The conductor_live247.output log starts to scroll on the screen and shows
messages as they are occurring. Watch for the following INFO lines on the
primary Conductor Live node:

```
WARN -- : Disabling HA, elemental_se restarting…
.
.
.
I, [2015-11-13T04:37:54.491204 #4978] INFO -- : HA environment not enabled
.
.
.
I, [2015-11-13T04:38:03.905069 #4978] INFO -- : Elemental Conductor is ready
```

Ensure the secondary Conductor Live is also ready. 6. Press Ctrl+C to exit the tail command. 7. Enter the following commands:

```
[elemental@hostname ~]$ **sudo -s**
[elemental@hostname ~]$ **cd /data/pgsql/logs**
[elemental@hostname ~]$ **tail -F postgresql-`<day>`.log**
```

where <day> is today (the day you are upgrading), typed with an initial
capital letter: Mon, Tue, Wed, Thu, Fri, Sat, Sun 8. Confirm that you see `database system is ready to accept connections` on the secondary Conductor Live. 9. Press Ctrl+C to exit the tail command. 10. Type the following command to exit the session as the sudo user:

```
[elemental@hostname ~]$ **exit**
```
