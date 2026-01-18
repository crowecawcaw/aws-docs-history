# Viewing the cluster state

You can view the state of the cluster in two ways - based on your operating system or with a web based console provided by Red Hat.

###### Topics

- [Operating system based](#os-based-nw-rhel "#os-based-nw-rhel")
- [Red Hat Cockpit](#rhel-cockpit "#rhel-cockpit")

## Operating system based

There are multiple operating system commands that can be run as root or as a user with appropriate permissions. The commands enable you to get an overview of the status of the cluster and its services. See the following commands for more details.

```
 # pcs status
```

Sample output:

```
 rhxhost01:~ # pcs status
Cluster name: rhx-cluster
Cluster Summary:
  * Stack: corosync
  * Current DC: rhxhost01 (version 2.1.0-8.el8-7c3f660707) - partition with quorum
  * Last updated: Tue Nov  1 13:41:58 2022
  * Last change:  Fri Oct 28 08:55:43 2022 by root via crm_attribute on rhxhost02
  * 2 nodes configured
  * 7 resource instances configured

Node List:
  * Online: [ rhxhost01 rhxhost02 ]

Full List of Resources:
  * Resource Group: grp_RHX_ASCS00:
    * rsc_ip_RHX_ASCS00 (ocf::heartbeat:aws-vpc-move-ip):        Started rhxhost01
    * rsc_sapstart_RHX_ASCS00   (ocf::heartbeat:SAPStartSrv):         Started rhxhost01
    * rsc_sap_RHX_ASCS00        (ocf::heartbeat:SAPInstance):    Started rhxhost01
  * res_AWS_STONITH     (stonith:fence_aws):  Started rhxhost02
  * Resource Group: grp_RHX_ERS10:
    * rsc_ip_RHX_ERS10  (ocf::heartbeat:aws-vpc-move-ip):        Started rhxhost02
    * rsc_sapstart_RHX_ERS10    (ocf::heartbeat:SAPStartSrv):         Started rhxhost02
    * rsc_sap_RHX_ERS10 (ocf::heartbeat:SAPInstance):    Started rhxhost02
```

The following table provides a list of useful commands.

| Command                | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| `pcs status`           | Display cluster status on the console                        |
| `pcs status --full`    | Display detailed cluster status including inactive resources |
| `pcs status nodes`     | Display node status and attributes                           |
| `pcs status resources` | Display resource status and fail counts                      |
| `pcs cluster status`   | Display cluster daemon status                                |
| `pcs help`             | View more options                                            |
| `pcs status --help`    | View more options                                            |

## Red Hat Cockpit

Cockpit is a web-based graphical user interface for managing and monitoring Red Hat Enterprise Linux systems, including pacemaker highly availability clusters. It must be enabled on every node in the cluster, to point your web browser on any node for accessing it. Use the following command to enable Cockpit.

```
 # systemctl enable --now cockpit.socket
# systemctl status cockpit.socket
```

Use the following URL to check security groups for access on port 9090 from your administrative host.

```
https://your-server:9090/

e.g https://rhxhost01:9090
```

For more information, see [Configuring and Managing High Availability Clusters](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_high_availability_clusters/managing-cluster-resources_configuring-and-managing-high-availability-clusters "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_high_availability_clusters/managing-cluster-resources_configuring-and-managing-high-availability-clusters") in the Red Hat Documentation.
