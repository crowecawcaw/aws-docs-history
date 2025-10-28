# Step Q: Re-enable high

availability

1. If you're using a virtual machine (VM), take a snapshot before you enable HA.
   See the VMware VSphere help text for more information.
2. On the web interface for the primary Conductor Live node, go to the
   **Cluster** page and choose
   **Redundancy**. In the **High Availability**
   field, choose **Enable**.

###### To verify that HA is correctly enabled, follow these steps on each Conductor Live

node.

1. At your workstation, start a remote terminal session to the Conductor Live
   node.
2. Enter the following command to verify that Conductor Live HA is enabled:

```
[elemental@hostname log]$ **tail -F /opt/elemental\_se/web/log/conductor\_live247.output**
```

The conductor_live247.output log starts to scroll on the screen and shows
messages as they are occurring. Watch for the following INFO lines on the
primary Conductor Live node:

```
CONDUCTOR: Initializing environment
I, [2015-11-13T04:37:54.491204 #4978]  INFO -- : Configuring the HA environment
I, [2015-11-13T04:37:54.660644 #4978]  INFO -- : configuring keepalived
.
.
.
I, [2015-11-13T04:38:03.905069 #4978]  INFO -- : Elemental Conductor is ready
```

3. Press **Ctrl - C** to exit the tail command.
4. Enter the following commands:

```
[elemental@hostname ~]$ **sudo -s**
[elemental@hostname ~]$ **cd /data/pgsql/logs**
[elemental@hostname ~]$ **tail -F postgresql-`<day>`.log**
```

where <day> is today (the day you are upgrading), typed with an initial
capital letter: Mon, Tue, Wed, Thu, Fri, Sat, Sun 5. Confirm that you see `database system is ready to accept
 connections` on the primary Conductor Live, and
`database system is ready to accept read only
 connections` on the secondary Conductor Live. 6. Press **Ctrl - C** to exit the tail command. 7. Type the following command to exit the session as the sudo user:

```
[elemental@hostname ~]$ **exit**
```
