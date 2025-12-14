# Viewing the cluster state

You can view the state of the cluster in two ways - based on your operating system or with a web based console provided by SUSE.

###### Topics

- [Operating system based](#os-based-nw-sles "#os-based-nw-sles")
- [SUSE Hawk2](#suse-hawk "#suse-hawk")

## Operating system based

There are multiple operating system commands that can be run as root or as a user with appropriate permissions. The commands enable you to get an overview of the status of the cluster and its services. See the following commands for more details.

```
# crm status
```

Sample output:

```
slxhost01:~ # crm status
Cluster Summary:
  * Stack: corosync
  * Current DC: slxhost01 (version 2.0.5+20201202.ba59be712-150300.4.24.1-2.0.5+20201202.ba59be712) - partition with quorum
  * Last updated: Tue Nov  1 13:41:58 2022
  * Last change:  Fri Oct 28 08:55:43 2022 by root via crm_attribute on slxhost02
  * 2 nodes configured
  * 7 resource instances configured

Node List:
  * Online: [ slxhost01 slxhost02 ]

Full List of Resources:
  * Resource Group: grp_SLX_ASCS00:
    * rsc_ip_SLX_ASCS00 (ocf::heartbeat:aws-vpc-move-ip):        Started slxhost01
    * rsc_sapstart_SLX_ASCS00   (ocf::suse:SAPStartSrv):         Started slxhost01
    * rsc_sap_SLX_ASCS00        (ocf::heartbeat:SAPInstance):    Started slxhost01
  * res_AWS_STONITH     (stonith:external/ec2):  Started slxhost02
  * Resource Group: grp_SLX_ERS10:
    * rsc_ip_SLX_ERS10  (ocf::heartbeat:aws-vpc-move-ip):        Started slxhost02
    * rsc_sapstart_SLX_ERS10    (ocf::suse:SAPStartSrv):         Started slxhost02
    * rsc_sap_SLX_ERS10 (ocf::heartbeat:SAPInstance):    Started slxhost02
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

e.g https://slxhost01:7630
```

For more information, see [Configuring and Managing Cluster Resources with Hawk2](https://documentation.suse.com/sle-ha/12-SP5/html/SLE-HA-all/cha-conf-hawk2.html "https://documentation.suse.com/sle-ha/12-SP5/html/SLE-HA-all/cha-conf-hawk2.html") in the SUSE Documentation.
