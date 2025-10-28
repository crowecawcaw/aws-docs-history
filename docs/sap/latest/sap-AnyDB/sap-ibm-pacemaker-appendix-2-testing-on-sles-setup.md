# Appendix 2: Testing on SLES Setup

## Test Case 1: Manual Failover

**Procedure**: Use the command `crm resource move <Db2 primary resource name> force` to move the primary Db2 instance to standby node.

```
     dbprim00:  crm resource move msl_db2_db2stj_STJ force
     INFO: Move constraint created for rsc_db2_db2stj_STJ
```

**Expected result**: The Db2 primary node is moved from the primary node (`dbprim00`) to the standby node (`dbsec00`).

```
     dbprim00:~  crm status
     Stack: corosync
     Current DC: dbsec00 (version 1.1.19+20181105.ccd6b5b10-3.16.1-1.1.19+20181105.ccd6b5b10) - partition with quorum
     Last updated: Sat Apr 25 19:03:20 2020
     Last change: Sat Apr 25 19:02:26 2020 by root via crm_resource on dbprim00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     res_AWS_STONITH        (stonith:external/ec2): Started dbsec00
     Master/Slave Set: msl_db2_db2stj_STJ [rsc_db2_db2stj_STJ]
         Masters: [ dbsec00 ]
         Stopped: [ dbprim00 ]
     res_AWS_IP     (ocf::suse:aws-vpc-move-ip):    Started dbsec00
```

**Follow-up actions**: Start the Db2 instance as standby on the new standby node, logged in as `db2<sid>`. Clean up the error logged in as root.

```
     db2stj> db2start
     04/25/2020 19:05:27     0   0   SQL1063N  DB2START processing was successful.
     SQL1063N  DB2START processing was successful.

     db2stj> db2 start hadr on database STJ as standby
     DB20000I  The START HADR ON DATABASE command completed successfully.
```

**Remove location constraint**: When using a manual command to move the resource, there is a location constraint created on the node (in this case primary node) which is run, preventing the Db2 resource from running in standby mode.

Use the following command to remove the location constraint.

```
       dbprim00:  crm resource clear msl_db2_db2stj_STJ
```

Once the constraint is removed, the standby instance starts automatically.

```
       dbprim00:  crm status
     Stack: corosync
     Current DC: dbsec00 (version 1.1.19+20181105.ccd6b5b10-3.16.1-1.1.19+20181105.ccd6b5b10) - partition with quorum
     Last updated: Sat Apr 25 19:05:29 2020
     Last change: Sat Apr 25 19:05:18 2020 by root via crm_resource on dbprim00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     res_AWS_STONITH        (stonith:external/ec2): Started dbsec00
     Master/Slave Set: msl_db2_db2stj_STJ [rsc_db2_db2stj_STJ]
          Masters: [ dbsec00 ]
         Slaves: [ dbprim00 ]
     res_AWS_IP     (ocf::suse:aws-vpc-move-ip):    Started dbsec00
```

## Test Case 2: Shut Down the Primary EC2 Instance

**Procedure**: Using AWS console or CLI, stop the EC2 instance to simulate EC2 failure.

Expected Result: The Db2 primary node is moved to a standby server (`dbsec00`).

```
     dbsec00:~  crm status
     Stack: corosync
     Current DC: dbsec00 (version 1.1.19+20181105.ccd6b5b10-3.16.1-1.1.19+20181105.ccd6b5b10) - partition with quorum
     Last updated: Sat Apr 25 19:19:32 2020
     Last change: Sat Apr 25 19:18:16 2020 by root via crm_resource on dbprim00

     2 nodes configured
     4 resources configured

     Online: [ dbsec00 ]
     OFFLINE: [ dbprim00 ]

     Full list of resources:

     res_AWS_STONITH        (stonith:external/ec2): Started dbsec00
     Master/Slave Set: msl_db2_db2stj_STJ [rsc_db2_db2stj_STJ]
         Masters: [ dbsec00 ]
         Stopped: [ dbprim00 ]
     res_AWS_IP     (ocf::suse:aws-vpc-move-ip):    Started dbsec00
```

**Follow-up action**: Start the EC2 instance and the standby node should start on `dbprim00`.

## Test Case 3: Stop the Db2 Instance on the Primary Instance

**Procedure**: Log in to the Db2 primary instance (`dbprim00`) as `db2<sid> (db2stj)` and run db2stop force.

```
     db2stj> db2stop force
     02/12/2020 12:40:03     0   0   SQL1064N  DB2STOP processing was successful.
     SQL1064N  DB2STOP processing was successful.
```

**Expected result**: The Db2 primary node will failover on primary instance. The standby remains on the standby instance. There is a failed resource alert.

```
     dbsec00:~  crm status
     Stack: corosync
     Current DC: dbsec00 (version 1.1.19+20181105.ccd6b5b10-3.16.1-1.1.19+20181105.ccd6b5b10) - partition with quorum
     Last updated: Sat Apr 25 19:29:38 2020
     Last change: Sat Apr 25 19:23:04 2020 by root via crm_resource on dbprim00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     res_AWS_STONITH        (stonith:external/ec2): Started dbprim00
     Master/Slave Set: msl_db2_db2stj_STJ [rsc_db2_db2stj_STJ]
         Masters: [ dbprim00 ]
         Slaves: [ dbsec00 ]
     res_AWS_IP     (ocf::suse:aws-vpc-move-ip):    Started dbprim00

    Failed Resource Actions:
    * rsc_db2_db2stj_STJ_demote_0 on dbprim00 'unknown error' (1): call=74, status=complete, exitreason='',
    last-rc-change='Sat Apr 25 19:27:21 2020', queued=0ms, exec=175ms
```

**Followup action**: Clear the failed cluster action.

```
     dbsec00:~  crm resource cleanup
     Waiting for 1 reply from the CRMd. OK
```

## Test Case 4: End the Db2 Process (db2sysc) on the Node that Runs the Primary Database

**Procedure**: Log in to the Db2 primary instance as root and run `ps –ef|grep db2sysc`. Note the PID and then end it.

```
     dbprim00:~  ps -ef|grep db2sysc
     db2stj   11690 11688  0 19:27 ?        00:00:02 db2sysc 0
     root     15814  4907  0 19:31 pts/0    00:00:00 grep --color=auto db2sysc
     [root@dbprim00 ~] kill -9 11690
```

**Expected result**: The Db2 primary node is restarted on the primary instance. The standby node remains on the standby instance. There is a failed resource alert.

```
     dbsec00:~  crm status
     Stack: corosync
     Current DC: dbsec00 (version 1.1.19+20181105.ccd6b5b10-3.16.1-1.1.19+20181105.ccd6b5b10) - partition with quorum
     Last updated: Sat Apr 25 19:29:38 2020
     Last change: Sat Apr 25 19:23:04 2020 by root via crm_resource on dbprim00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     res_AWS_STONITH        (stonith:external/ec2): Started dbprim00
     Master/Slave Set: msl_db2_db2stj_STJ [rsc_db2_db2stj_STJ]
         Masters: [ dbprim00 ]
         Slaves: [ dbsec00 ]
     res_AWS_IP     (ocf::suse:aws-vpc-move-ip):    Started dbprim00

     Failed Resource Actions:
     * rsc_db2_db2stj_STJ_demote_0 on dbprim00 'unknown error' (1): call=74, status=complete, exitreason='',
    last-rc-change='Sat Apr 25 19:27:21 2020', queued=0ms, exec=175ms
```

**Followup action**: Clear the failed cluster action.

```
     dbsec00:~  crm resource cleanup
     Waiting for 1 reply from the CRMd. OK
```

## Test Case 5: End the Db2 Process (db2sysc) on the Node that Runs the Standby Database

**Procedure**: Log in to the standby DB instance (`dbsec00`) as root, then run `ps –ef|grep db2sysc`. Note the PID and then end it.

```
     dbsec00:~  ps -ef| grep db2sysc
     db2stj   16245 16243  0 19:23 ?        00:00:04 db2sysc 0
     root     28729 28657  0 19:38 pts/0    00:00:00 grep --color=auto db2sysc
     dbsec00:~  kill -9 16245
```

**Expected result**: The `db2sysc` process is restarted on the standby DB instance. There is a monitoring failure event recorded in the cluster.

```
     dbsec00:~  crm status
     Stack: corosync
     Current DC: dbsec00 (version 1.1.19+20181105.ccd6b5b10-3.16.1-1.1.19+20181105.ccd6b5b10) - partition with quorum
     Last updated: Sat Apr 25 19:40:23 2020
     Last change: Sat Apr 25 19:23:04 2020 by root via crm_resource on dbprim00

     2 nodes configured
     4 resources configured

     Online: [ dbprim00 dbsec00 ]

     Full list of resources:

     res_AWS_STONITH        (stonith:external/ec2): Started dbprim00
     Master/Slave Set: msl_db2_db2stj_STJ [rsc_db2_db2stj_STJ]
         Masters: [ dbprim00 ]
         Slaves: [ dbsec00 ]
     res_AWS_IP     (ocf::suse:aws-vpc-move-ip):    Started dbprim00

     Failed Resource Actions:
     * rsc_db2_db2stj_STJ_monitor_30000 on dbsec00 'not running' (7): call=387, status=complete, exitreason='',
    last-rc-change='Sat Apr 25 19:39:24 2020', queued=0ms, exec=0ms
```

**Followup action**: Clear the monitoring error.

```
     dbsec00:~  crm resource cleanup
     Waiting for 1 reply from the CRMd. OK
```

## Test Case 6: Simulating a Crash of the Node that Runs the Primary Db2

**Procedure**: Log in to the Db2 primary instance as root, then run `echo 'c' > /proc/sysrq-trigger`.

```
     dbprim00:~  echo 'c' > /proc/sysrq-trigger
     Session stopped
         - Press <return> to exit tab
         - Press R to restart session
         - Press S to save terminal output to file

     Network error: Software caused connection abort
```

**Expected result**: The primary Db2 should failover to standby node.vThe standby is in a stopped state on the previous primary (`dbprim00`).

```
     [root@dbsec00 ~] crm status
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

**Followup action**: Start the EC2 instance and then start Db2 as standby on the standby instance as you did in [Test Case 2](sap-ibm-pacemaker-appendix-1-testing-on-rhel-setup.md#sap-ibm-pacemaker-test-case-2-shut-down-the-primary-ec2-instance "sap-ibm-pacemaker-appendix-1-testing-on-rhel-setup.md#sap-ibm-pacemaker-test-case-2-shut-down-the-primary-ec2-instance").
