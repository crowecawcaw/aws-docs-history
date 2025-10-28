# Appendix 1: Testing on RHEL Setup

## Test Case 1: Manual Failover

**Procedure**: Use the command `pcs resource move <Db2 master resource name>`.

```
     [root@dbprim00 profile] pcs resource move Db2_HADR_STJ-master
     Warning: Creating location constraint cli-ban-Db2_HADR_STJ-master-on-dbprim00 with a score of -INFINITY for resource
     Db2_HADR_STJ-master on-dbprim00 with a score of -INFINITY for resource Db2_HADR_STJ-
     master on node dbprim00.
     This will prevent Db2_HADR_STJ-master from running on dbprim00
     until the constraint is removed. This will be the case even if
     dbprim00 is the last node in the cluster.
     [root@dbprim00 profile]
```

**Expected result**: The Db2 primary node is moved from primary node to standby node.

```
     [root@dbprim00 profile] pcs status
     Cluster name: db2ha
     Stack: corosync
     Current DC: dbsec00 (version 1.1.18-11.el7_5.4-2b07d5c5a9) - partition with quorum
     Last updated: Sat Feb  8 08:54:04 2020
     Last change: Sat Feb  8 08:53:02 2020 by root via crm_resource on dbprim00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     clusterfence   (stonith:fence_aws):    Started dbprim00
         Master/Slave Set: Db2_HADR_STJ-master [Db2_HADR_STJ]
         Masters: [ dbsec00 ]
     Stopped: [ dbprim00 ]
     db2-oip        (ocf::heartbeat:aws-vpc-move-ip):       Started dbsec00

     Daemon Status:
     corosync: active/enabled
     pacemaker: active/enabled
     pcsd: active/enabled
     [root@dbprim00 profile]
```

**Followup actions**: Remove the location constraint.

When using a manual command for moving the resource, there is location constraint created on the node (in this case, the primary node) that prevents running the Db2 resource in standby mode.

**To remove the location constraint:**

1. Use the following command to remove the location constraint:

```
      pcs config show
     Location Constraints:
     Resource: Db2_HADR_STJ-master
     Disabled on: dbprim00 (score:-INFINITY) (role: Started) (id:cli-ban-Db2_HADR_STJ-master-on-dbprim00)

     [root@dbprim00 profile] pcs constraint delete cli-ban-Db2_HADR_STJ-master-on-dbprim00
```

2. Start the Db2 instance as standby on the new standby node, logged in as `db2<sid>`. Next, clean up the error logged in as root.

```
     db2stj> db2start
     02/08/2020 09:11:29     0   0   SQL1063N  DB2START processing was successful.
     SQL1063N  DB2START processing was successful.

     db2stj> db2 start hadr on database STJ as standby
     DB20000I  The START HADR ON DATABASE command completed successfully.

     [root@dbprim00 ~] pcs resource cleanup
     Cleaned up all resources on all nodes
     [root@dbprim00 ~] pcs status
     Cluster name: db2ha
     Stack: corosync
     Current DC: dbsec00 (version 1.1.18-11.el7_5.4-2b07d5c5a9) - partition with quorum
     Last updated: Sat Feb  8 09:13:17 2020
     Last change: Sat Feb  8 09:12:26 2020 by hacluster via crmd on dbprim00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     clusterfence   (stonith:fence_aws):    Started dbprim00
     Master/Slave Set: Db2_HADR_STJ-master [Db2_HADR_STJ]
          Masters: [ dbsec00 ]
          Slaves: [ dbprim00 ]
     db2-oip        (ocf::heartbeat:aws-vpc-move-ip):       Started dbsec00

     Daemon Status:
          corosync: active/enabled
          pacemaker: active/enabled
          pcsd: active/enabled
     [root@dbprim00 ~]
```

## Test Case 2: Shut Down the Primary EC2 Instance

**Procedure**: Using AWS Console or CLI to stop the EC2 instance and simulate EC2 failure.

**Expected result**: The Db2 primary node is moved to the standby server.

```
     [root@dbsec00 db2stj] pcs status
     Cluster name: db2ha
     Stack: corosync
     Current DC: dbsec00 (version 1.1.18-11.el7_5.4-2b07d5c5a9) - partition with quorum
     Last updated: Sat Feb  8 09:44:16 2020
     Last change: Sat Feb  8 09:31:39 2020 by hacluster via crmd on dbsec00

     2 nodes configured
     4 resources configured

     Online: [ dbsec00 ]
     OFFLINE: [ dbprim00 ]

     Full list of resources:

     clusterfence   (stonith:fence_aws):    Started dbsec00
     Master/Slave Set: Db2_HADR_STJ-master [Db2_HADR_STJ]
          Masters: [ dbsec00 ]
          Stopped: [ dbprim00 ]
     db2-oip        (ocf::heartbeat:aws-vpc-move-ip):       Started dbsec00

     Daemon Status:
          corosync: active/enabled
          pacemaker: active/enabled
          pcsd: active/enabled
```

**Followup action**: Start the EC2 instance and then start Db2 as standby on the standby instance as you did in [Test Case 1](#sap-ibm-pacemaker-test-case-1-manual-failover "#sap-ibm-pacemaker-test-case-1-manual-failover"). Do not include location constraint removal this time.

## Test Case 3: Stop the Db2 Instance on the Primary Instance

**Procedure**: Log in to the Db2 primary instance as `db2<sid> (db2stj)` and run `db2stop force`.

```
     db2stj> db2stop force
     02/12/2020 12:40:03     0   0   SQL1064N  DB2STOP processing was successful.
     SQL1064N  DB2STOP processing was successful.
```

**Expected result**: The Db2 primary node is failed over to standby server. The standby node continues to be on the old primary in a stopped state. There is a failed monitoring action.

```
     [root@dbsec00 db2stj] pcs status
     Cluster name: db2ha
     Stack: corosync
     Current DC: dbsec00 (version 1.1.18-11.el7_5.4-2b07d5c5a9) - partition with quorum
     Last updated: Wed Feb 12 16:55:56 2020
     Last change: Wed Feb 12 13:58:11 2020 by hacluster via crmd on dbsec00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     clusterfence   (stonith:fence_aws):    Started dbsec00
     Master/Slave Set: Db2_HADR_STJ-master [Db2_HADR_STJ]
         Masters: [ dbsec00 ]
         Stopped: [ dbprim00 ]
     db2-oip        (ocf::heartbeat:aws-vpc-move-ip):       Started dbsec00

    Failed Actions:
    * Db2_HADR_STJ_start_0 on dbprim00 'unknown error' (1): call=34, status=complete, exitreason='',
    last-rc-change='Wed Feb 12 16:55:32 2020', queued=1ms, exec=6749ms


    Daemon Status:
       corosync: active/enabled
       pacemaker: active/enabled
    pcsd: active/enabled
    [root@dbsec00 db2stj]
```

**Followup action**: Start the EC2 instance, then start Db2 as standby on the standby instance as you did in [Test Case 2](#sap-ibm-pacemaker-test-case-2-shut-down-the-primary-ec2-instance "#sap-ibm-pacemaker-test-case-2-shut-down-the-primary-ec2-instance"). Clear the failed monitoring error.

## Test Case 4: End the Db2 Process (db2sysc) on the Node that Runs the Primary Database

**Procedure**: Log in to the Db2 primary instance as root and then run `ps –ef|grep db2sysc`. Note the process ID (PID) and then end it.

```
     [root@dbprim00 ~] ps -ef|grep db2sysc
     root      5809 30644  0 18:54 pts/1    00:00:00 grep --color=auto
     db2sysc
     db2stj   26982 26980  0 17:12 pts/0    00:00:28 db2sysc 0
     [root@dbprim00 ~] kill -9 26982
```

**Expected result**: The Db2 primary node is failed over to the standby server. The standby node is in the old primary in a stopped state.

```
     [root@dbprim00 ~] pcs status
     Cluster name: db2ha
     Stack: corosync
     Current DC: dbsec00 (version 1.1.18-11.el7_5.4-2b07d5c5a9) - partition with quorum
     Last updated: Wed Feb 12 18:54:50 2020
     Last change: Wed Feb 12 18:53:12 2020 by hacluster via crmd on dbsec00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     clusterfence   (stonith:fence_aws):    Started dbsec00
     Master/Slave Set: Db2_HADR_STJ-master [Db2_HADR_STJ]
         Masters: [ dbsec00 ]
         Stopped: [ dbprim00 ]
     db2-oip        (ocf::heartbeat:aws-vpc-move-ip):       Started dbsec00

     Failed Actions:
     * Db2_HADR_STJ_start_0 on dbprim00 'unknown error' (1): call=57, status=complete, exitreason='',
    last-rc-change='Wed Feb 12 18:54:37 2020', queued=0ms, exec=6777ms


     Daemon Status:
        corosync: active/enabled
        pacemaker: active/enabled
        pcsd: active/enabled
```

**Followup action**: Start the EC2 instance and start Db2 as standby on the standby instance, as you did in [Test Case 2](#sap-ibm-pacemaker-test-case-2-shut-down-the-primary-ec2-instance "#sap-ibm-pacemaker-test-case-2-shut-down-the-primary-ec2-instance"). Clear the failed monitoring alert.

## Test Case 5: End the Db2 Process (db2sysc) on the Node that Runs the Standby Database

**Procedure**: Log in to the Db2 standby instance as root and run `ps –ef|grep db2sysc`. Note the PID and then end it.

```
     [root@dbsec00 db2stj] ps -ef|grep db2sysc
     db2stj   24194 24192  1 11:55 pts/1    00:00:01 db2sysc 0
     root     26153  4461  0 11:57 pts/0    00:00:00 grep --color=auto
     db2sysc
     [root@dbsec00 db2stj] kill -9 24194
```

**Expected result**: The `db2sysc` process is restarted on the Db2 standby instance. There is a monitoring failure event record in the cluster.

```
     [root@dbprim00 ~] pcs status
     Cluster name: db2ha
     Stack: corosync
     Current DC: dbsec00 (version 1.1.18-11.el7_5.4-2b07d5c5a9) - partition with quorum
     Last updated: Fri Feb 14 11:59:22 2020
     Last change: Fri Feb 14 11:55:54 2020 by hacluster via crmd on dbsec00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     clusterfence   (stonith:fence_aws):    Started dbsec00
     Master/Slave Set: Db2_HADR_STJ-master [Db2_HADR_STJ]
         Masters: [ dbprim00 ]
         Slaves: [ dbsec00 ]
     db2-oip        (ocf::heartbeat:aws-vpc-move-ip):       Started dbprim00

     Failed Actions:
     * Db2_HADR_STJ_monitor_20000 on dbsec00 'not running' (7): call=345, status=complete, exitreason='',
    last-rc-change='Fri Feb 14 11:57:57 2020', queued=0ms, exec=0ms


     Daemon Status:
        corosync: active/enabled
        pacemaker: active/enabled
        pcsd: active/enabled


     [root@dbsec00 db2stj] ps -ef|grep db2sysc
     db2stj   26631 26629  1 11:57 ?        00:00:01 db2sysc 0
     root     27811  4461  0 11:58 pts/0    00:00:00 grep --color=auto db2sysc
```

**Follow-up action**: Clear the monitoring error.

## Test Case 6: Simulating a Crash of the Node that Runs the Primary Db2

**Procedure**: Log in to the Db2 primary instance as root and run `echo 'c' > /proc/sysrq-trigger`.

```
     [root@dbprim00 ~] echo 'c' > /proc/sysrq-trigger
     ───────────────────────────────────────────────────────────────────────────────────────────────────────

     Session stopped
         - Press <return> to exit tab
         - Press R to restart session
         - Press S to save terminal output to file

     Network error: Software caused connection abort
```

**Expected result**: The primary Db2 should failover to standby node. The standby is in a stopped state on the previous primary.

```
     [root@dbsec00 ~] pcs status
     Cluster name: db2ha
     Stack: corosync
     Current DC: dbsec00 (version 1.1.18-11.el7_5.4-2b07d5c5a9) - partition with quorum
     Last updated: Fri Feb 21 15:38:43 2020
     Last change: Fri Feb 21 15:33:17 2020 by hacluster via crmd on dbsec00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

      clusterfence   (stonith:fence_aws):    Started dbsec00
      Master/Slave Set: Db2_HADR_STJ-master [Db2_HADR_STJ]
         Masters: [ dbsec00 ]
         Stopped: [ dbprim00 ]
      db2-oip        (ocf::heartbeat:aws-vpc-move-ip):       Started dbsec00

     Failed Actions:
     * Db2_HADR_STJ_start_0 on dbprim00 'unknown error' (1): call=15, status=complete, exitreason='',
     last-rc-change='Fri Feb 21 15:38:31 2020', queued=0ms, exec=7666ms


     Daemon Status:
        corosync: active/enabled
        pacemaker: active/enabled
        pcsd: active/enabled
```

**Followup action**: Start the EC2 instance and then start Db2 as standby on the standby instance as you did in [Test Case 2](#sap-ibm-pacemaker-test-case-2-shut-down-the-primary-ec2-instance "#sap-ibm-pacemaker-test-case-2-shut-down-the-primary-ec2-instance"). Clear the monitoring error.
