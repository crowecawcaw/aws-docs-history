# Viewing the cluster state

###### Topics

- [Operating system based](#_operating_system_based "#_operating_system_based")

## Operating system based

There are multiple operating system commands that can be run as root or as a user with appropriate permissions. The commands enable you to get an overview of the status of the cluster and its services.

```
# pcs status --full
```

Note: Omit the `--full` for a more concise output if you do not need to view the node attributes.

Sample output:

```
Cluster name: hacluster
Cluster Summary:
  * Stack: corosync
  * Current DC: hanahost02 (version 2.1.2-4.el9_0.5-ada5c3b36e2) - partition with quorum
  * Last updated: Tue Jun  3 15:47:15 2025
  * Last change:  Tue Jun  3 15:47:12 2025 by hacluster via crmd on hanahost02
  * 2 nodes configured
  * 6 resource instances configured

Node List:
  * Online: [ hanahost01 hanahost02 ]

Full List of Resources:
  * rsc_fence_aws       (stonith:fence_aws):     Started hanahost01
  * rsc_ip_HDB_HDB00    (ocf:heartbeat:aws-vpc-move-ip):         Stopped
  * Clone Set: rsc_SAPHanaTopology_HDB_HDB00-clone [rsc_SAPHanaTopology_HDB_HDB00]:
    * Started: [ hanahost01 hanahost02 ]
  * Clone Set: rsc_SAPHana_HDB_HDB00-clone [rsc_SAPHana_HDB_HDB00] (promotable):
    * Promoted: [ hanahost02 ]
    * Unpromoted: [ hanahost01 ]

Node Attributes:
  * Node: hanahost01 (1):
    * hana_hdb_clone_state              : PROMOTED
    * hana_hdb_op_mode                  : logreplay
    * hana_hdb_remoteHost               : hanavirt02
    * hana_hdb_roles                    : 4:P:master1:master:worker:master
    * hana_hdb_site                     : siteA
    * hana_hdb_srah                     : -
    * hana_hdb_srmode                   : syncmem
    * hana_hdb_sync_state               : PRIM
    * hana_hdb_version                  : 2.00.073.00
    * hana_hdb_vhost                    : hanavirt01
    * lpa_hdb_lpt                       : 1755493611
    * master-rsc_SAPHana_HDB_HDB00      : 150
  * Node: hanahost02 (2):
    * hana_hdb_clone_state              : DEMOTED
    * hana_hdb_op_mode                  : logreplay
    * hana_hdb_remoteHost               : hanavirt01
    * hana_hdb_roles                    : 4:S:master1:master:worker:master
    * hana_hdb_site                     : siteB
    * hana_hdb_srah                     : -
    * hana_hdb_srmode                   : syncmem
    * hana_hdb_sync_state               : SOK
    * hana_hdb_version                  : 2.00.073.00
    * hana_hdb_vhost                    : hanavirt02
    * lpa_hdb_lpt                       : 30
    * master-rsc_SAPHana_HDB_HDB00      : 100

Migration Summary:

Tickets:

PCSD Status:
  hanahost01: Online
  hanahost02: Online

Daemon Status:
  corosync: active/disabled
  pacemaker: active/disabled
  pcsd: active/enabled
```

The following table provides a list of useful commands.

| Command              | Description                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `crm_mon`            | Display cluster status on the console with updates as they occur                                                    |
| `crm_mon -1`         | Display cluster status on the console just once, and exit                                                           |
| `crm_mon -Arnf`      | -A Display node attributes -n Group resources by node -r Display inactive resources -f Display resource fail counts |
| `crm help`           | View more options                                                                                                   |
| `crm_mon --help-all` | View more options                                                                                                   |
