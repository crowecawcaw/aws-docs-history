# Disabling Conductor Live HA

(high availability)

The main reason to disable HA is to make a change to the
configuration of one or both Conductor Live nodes. You must disable HA to
make these configuration changes:

- Configure DNS
- Configure Ethernet interfaces

- Bond Ethernet interfaces

- Configure the firewall or ports
- Enable user authentication

###### Important

Disabling HA occurs immediately, but enabling always involves
a wait. Don't disable without a good reason!

###### To disable HA

1. If you're using a virtual machine (VM), take a snapshot
   before you disable HA. See the VMware VSphere help text for
   more information.
2. On the web interface for the primary Conductor Live node, go to
   the **Cluster** page and choose
   **Redundancy**.
3. Note the values in **Virtual IP Address**
   and **Virtual Route Identifier**. You will
   use these when you re-enable HA.
4. In the **High Availability** field,
   choose **Disable**.

###### To verify that HA is disabled

1. At your workstation, [start a
   remote terminal session](ready-conductor-live-config-access.md "ready-conductor-live-config-access.md") to each Conductor Live
   node.
2. In the session for each Conductor Live, enter the following
   command to verify that Conductor Live HA is disabled:

```
[elemental@hostname log]$ **tail -F /opt/elemental\_se/web/log/conductor\_live247.output**
```

The conductor_live247.output log starts to scroll on the
screen and shows messages as they are occurring. Watch for
the following INFO lines on the primary Conductor Live node:

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

Make sure that the secondary Conductor Live is also ready. 3. Press **Ctrl - C** to exit the tail
command. 4. Enter the following commands:

```
[elemental@hostname ~]$ **sudo -s**
[elemental@hostname ~]$ **cd /data/pgsql/logs**
[elemental@hostname ~]$ **tail -F postgresql-`<day>`.log**
```

where <day> is today (the day you are upgrading), typed
with an initial capital letter: Mon, Tue, Wed, Thu, Fri,
Sat, Sun 5. Confirm that you see `database system is
 ready to accept connections` on the
secondary Conductor Live. 6. Press **Ctrl - C** to exit the tail
command. 7. Type the following command to exit the session as the sudo
user:

```
[elemental@hostname ~]$ **exit**
```
