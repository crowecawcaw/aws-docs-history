# Enabling Conductor Live HA (high

availability)

If you have set up the cluster with a primary and a secondary
Conductor Live node, you must enable HA before you start running channels
and MPTSes in the cluster.

## The results of

enabling HA

When the enable HA (high availability), the following actions
occurs:

**The primary Conductor Live is
set**

The Conductor Live node where you enable HA becomes the primary
Conductor Live. The other Conductor Live node becomes the secondary
Conductor Live.

**The virtual IP (VIP) address
activates**

The virtual IP (VIP) address activates. The primary Conductor Live
registers with this VIP as the primary node. After this
occurs:

- The primary Conductor Live node becomes inaccessible
  through its local IP address and only accessible
  through the virtual IP (VIP) address. The web page
  you're using automatically redirects to the VIP as
  you are continue to access the primary Conductor Live
  node.
- The secondary Conductor Live node becomes completely
  inaccessible. If you enter the IP address of the
  secondary Conductor Live node, you are automatically
  redirected to the VIP. In other words, while you are
  accessing the primary Conductor Live node, you cannot access
  the secondary Conductor Live node.
- Any time that a Conductor Live failover of the primary
  node occurs, the Conductor Live node that's promoted to
  become the primary Conductor Live node re-registers with the
  VIP, effectively indicating “I’m the primary
  now.”
  **Information is copied over**

Information is copied over from the primary Conductor Live node to
the secondary Conductor Live node, and the secondary Conductor Live database
synchronizes itself with the primary Conductor Live database. The
following information that is copied over:

- Input device (SDI) configuration
- Mountpoint configuration
- Router configuration
- Time zone configuration

- Configuration of notification for alerts and
  SNMP
- User authentication and users
- Backup and restore configuration

###### To enable HA

1. Make sure that both of the Conductor Live nodes are on the same
   software version. If they are different, you will receive a
   validation error and HA won't get enabled.
2. If you're using a virtual machine (VM), take a snapshot
   before you enable HA. See the VMware VSphere help text for
   more information.
3. On the web interface for the primary Conductor Live node, go to
   the **Cluster** page and choose
   **Redundancy**. In the **High
   Availability** field, choose
   **Enable**.

###### To verify that HA is correctly enabled, follow these steps on

each Conductor Live node.

1. At your workstation, [start a
   remote terminal session](ready-conductor-live-config-access.md "ready-conductor-live-config-access.md") to the Conductor Live
   node.
2. Enter the following command to verify that Conductor Live HA is
   enabled:

```
[elemental@hostname log]$ **tail -F /opt/elemental\_se/web/log/conductor\_live247.output**
```

The conductor_live247.output log starts to scroll on the
screen and shows messages as they are occurring. Watch for
the following INFO lines on the primary Conductor Live node:

```
CONDUCTOR: Initializing environment
I, [2015-11-13T04:37:54.491204 #4978]  INFO -- : Configuring the HA environment
I, [2015-11-13T04:37:54.660644 #4978]  INFO -- : configuring keepalived
.
.
.
I, [2015-11-13T04:38:03.905069 #4978]  INFO -- : Elemental Conductor is ready
```

3. Press **Ctrl - C** to exit the tail
   command.
4. Enter the following commands:

```
[elemental@hostname ~]$ **sudo -s**
[elemental@hostname ~]$ **cd /data/pgsql/logs**
[elemental@hostname ~]$ **tail -F postgresql-`<day>`.log**
```

where <day> is today (the day you are upgrading), typed
with an initial capital letter: Mon, Tue, Wed, Thu, Fri,
Sat, Sun 5. Confirm that you see `database system is
 ready to accept connections` on the
primary Conductor Live, and `database system is ready
 to accept read only connections` on the
secondary Conductor Live. 6. Press **Ctrl - C** to exit the tail
command. 7. Type the following command to exit the session as the sudo
user:

```
[elemental@hostname ~]$ **exit**
```
