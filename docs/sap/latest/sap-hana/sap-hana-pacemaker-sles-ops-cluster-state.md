# Viewing the cluster state

You can view the state of the cluster in two ways - based on your operating system or with a web based console provided by SUSE.

###### Topics

- [Operating system based](#_operating_system_based "#_operating_system_based")
- [SUSE Hawk2](#_suse_hawk2 "#_suse_hawk2")

## Operating system based

There are multiple operating system commands that can be run as root or as a user with appropriate permissions. The commands enable you to get an overview of the status of the cluster and its services. See the following commands for more details.

```
# crm status
```

Sample output:

```
Cluster Summary:
  * Stack: corosync
  * Current DC: sapsecdb (version 2.0.5+20201202.ba59be712-150300.4.45.2-2.0.5+20201202.ba59be712) - partition with quorum
  * Last updated: Wed Aug 20 14:05:19 2025
  * Last change:  Wed Aug 20 14:04:54 2025 by root via crm_attribute on hanahost01
  * 2 nodes configured
  * 6 resource instances configured

Node List:
  * Online: [ hanahost01 hanahost02  ]

Full List of Resources:
  * rsc_AWS_STONITH     (stonith:external/ec2):  Started sapsecdb
  * rsc_ip_HDB_HDB00    (ocf::heartbeat:aws-vpc-move-ip):        Started hanahost01
  * Clone Set: cln_SAPHanaTopology_HDB_HDB00 [rsc_SAPHanaTopology_HDB_HDB00]:
    * Started: [ hanahost01 hanahost02 ]
  * Clone Set: msl_SAPHana_HDB_HDB00 [rsc_SAPHana_HDB_HDB00] (promotable):
    * Masters: [ hanahost01 ]
    * Slaves: [ hanahost02 ]
```

The following table provides a list of useful commands.

| Command              | Description                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `crm_mon`            | Display cluster status on the console with updates as they occur                                                             |
| `crm_mon -1`         | Display cluster status on the console just once, and exit                                                                    |
| `crm_mon -Arnf`      | -A Display node attributes<br>-n Group resources by node<br>-r Display inactive resources<br>-f Display resource fail counts |
| `crm help`           | View more options                                                                                                            |
| `crm_mon --help-all` | View more options                                                                                                            |

## SUSE Hawk2

Hawk2 is a web-based graphical user interface for managing and monitoring pacemaker highly availability clusters. It must be enabled on every node in the cluster, to point your web browser on any node for accessing it. Use the following command to enable Hawk2.

```
# systemctl enable --now hawk
# systemctl status hawk
```

Use the following URL to check security groups for access on port 7630 from your administrative host.

```
https://your-server:7630/

e.g https://hanahost01:7630
```

For more information, see [Configuring and Managing Cluster Resources with Hawk2](https://documentation.suse.com/sle-ha/12-SP5/html/SLE-HA-all/cha-conf-hawk2.html "https://documentation.suse.com/sle-ha/12-SP5/html/SLE-HA-all/cha-conf-hawk2.html") in the SUSE Documentation.
