

# Enabling or disabling high availability (HA)
<a name="migrate-topic-disable-ha"></a>

To enable or disable HA in a cluster, follow these steps.

1. If you're using a virtual machine (VM), take a snapshot before disabling high availability. See the VMware VSphere help text for more information. 

1. On the web interface for the primary Conductor node, choose the **Cluster** page, then choose **Redundancy**. In the **High Availability** field, select **Enable** or **Disable**.

1. Verify that high availability is enabled or disabled. From the Linux prompt, use the **elemental** user start a remote terminal session with the primary and with the secondary Conductor nodes. 

   Then, in the remote terminal session for each Conductor, enter the following command: 

   ```
   [elemental@hostname ~]$ tail -F /opt/elemental_se/web/log/conductor_live247.output
   ```

   The conductor\_live247.output log starts to scroll on the screen and shows messages as they are occurring. 

   If you enabled HA, watch for the following INFO lines on the primary Conductor node:

   ```
   CONDUCTOR: Initializing environment
   I, [2015-11-13T04:37:54.491204 #4978]  INFO -- : Configuring the HA environment
   I, [2015-11-13T04:37:54.660644 #4978]  INFO -- : configuring keepalived
   .
   .
   .
   I, [2015-11-13T04:38:03.905069 #4978]  INFO -- : Elemental Conductor is ready
   ```

   If you disabled HA, watch for the following INFO lines on the primary Conductor node:

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

1. Press Ctrl\+C to exit the tail command.

1. Enter the following commands:

   ```
   [elemental@hostname ~]$ sudo -s
   [elemental@hostname ~]$ cd /data/pgsql/logs
   [elemental@hostname ~]$ tail -F postgresql-{{<day>}}.log
   ```

   where <day> is today (the day you are upgrading), typed with an initial capital letter: Mon, Tue, Wed, Thu, Fri, Sat, Sun

1. Confirm the message that appears.

   If you enabled HA, look for `database system is ready to accept connections` on the primary Conductor, and `database system is ready to accept read only connections` on the secondary Conductor.

   If you disabled HA, look for `database system is ready to accept connections` on the secondary Conductor.

1. Press Ctrl\+C to exit the tail command.

1. Type the following command to exit the session as the sudo user:

   ```
   [elemental@hostname ~]$ exit
   ```