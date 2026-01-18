# Cluster Node Setup

Establish cluster communication between nodes using Corosync and configure required authentication.

###### Topics

- [Deploy a Majority Maker Node (Scale-Out Clusters Only)](#_deploy_a_majority_maker_node_scale_out_clusters_only "#_deploy_a_majority_maker_node_scale_out_clusters_only")
- [Setup Passwordless Authentication](#_setup_passwordless_authentication "#_setup_passwordless_authentication")
- [Start and Enable the pcsd service](#_start_and_enable_the_pcsd_service "#_start_and_enable_the_pcsd_service")
- [Authorize the Cluster](#_authorize_the_cluster "#_authorize_the_cluster")
- [Generate Corosync Configuration](#_generate_corosync_configuration "#_generate_corosync_configuration")
- [Verify Configuration](#_verify_configuration "#_verify_configuration")

## Deploy a Majority Maker Node (Scale-Out Clusters Only)

###### Note

Only required for clusters with more than two nodes.

When deploying an SAP HANA Scale-Out cluster in AWS, you must include a majority maker node in a third Availability Zone (AZ). The majority maker (tie-breaker) node ensures the cluster remains operational if one AZ fails by preserving the quorum. For the Scale-Out cluster to function, at least all nodes in one AZ plus the majority maker node must be running. If this minimum requirement is not met, the cluster loses its quorum state and any remaining SAP HANA nodes are fenced.

The majority maker requires a minimum EC2 instance configuration of 2 vCPUs, 2 GB RAM, and 50 GB disk space; this instance is exclusively used for quorum management and does not host an SAP HANA database or any other cluster resources.
=== Change the hacluster Password

On all cluster nodes, change the password of the operating system user hacluster:

```
 # passwd hacluster
```

## Setup Passwordless Authentication

Red Hat cluster tools provide comprehensive reporting and troubleshooting capabilities for cluster activity. Many of these tools require passwordless SSH access between nodes to collect cluster-wide information effectively. Red Hat recommends configuring passwordless SSH for the root user to enable seamless cluster diagnostics and reporting.

See Redhat Documentation [How to setup SSH Key passwordless login in Red Hat Enterprise Linux](https://access.redhat.com/solutions/9194 "https://access.redhat.com/solutions/9194")

See [Accessing the Red Hat Knowledge base portal](../../../systems-manager/latest/userguide/fleet-manager-red-hat-knowledge-base-access.md "../../../systems-manager/latest/userguide/fleet-manager-red-hat-knowledge-base-access.md")

###### Warning

Review the security implications for your organization, including root access controls and network segmentation, before implementing this configuration.

## Start and Enable the pcsd service

```
 # systemctl enable pcsd --now
```

## Authorize the Cluster

Run the following command to enable and start the pacemaker cluster service on both nodes:

```
 # pcs host auth <hostname_1> <hostname_2> -u hacluster -p <password>
```

- You will be prompted for the hacluster password you set earlier.

## Generate Corosync Configuration

Corosync provides membership and member-communication needs for high availability clusters.

Initial setup can be performed using the following command

```
 # pcs cluster setup <cluster_name> \
<hostname_1> addr=<host_ip_1> addr=<host_additional_ip_1> \
<hostname_2> addr=<host_ip_2> addr=<host_additional_ip_2>
```

- Example

```
# pcs cluster setup hana_cluster hanahost01 addr=10.1.20.1 addr=10.1.20.2 hanahost02 addr=10.2.20.1 addr=10.2.20.2
```

| IP address type        | Example   |
| ---------------------- | --------- |
| <host_ip_1>            | 10.2.10.1 |
| <host_additional_ip_1> | 10.2.10.2 |
| <host_ip_2>            | 10.2.20.1 |
| <host_additional_ip_2> | 10.2.20.2 |

The timing parameters are optimized for AWS cloud environments:

- Increasing the value of totem token to 15s provides reliable cluster operation while accommodating normal cloud network characteristics. These settings prevent unnecessary failovers during brief network variations
- When scaling beyond two nodes, remove the two_node parameter from the quorum section. The timing parameters will automatically adjust using the token_coefficient feature to maintain appropriate failure detection as nodes are added.

```
 # pcs cluster config update totem token=15000
```

## Verify Configuration

```
 # pcs cluster start --all
```

By enabling the pacemaker service, the server automatically joins the cluster after a reboot. This ensures that your system is protected. Alternatively, you can start the pacemaker service manually on boot. You can then investigate the cause of failure.

Run the following command to check the status of the pacemaker service:

```
 # systemctl status pacemaker
```

Example output:

```
 ● pacemaker.service - Pacemaker High Availability Cluster Manager
     Loaded: loaded (/usr/lib/systemd/system/pacemaker.service; enabled; vendor preset: disabled)
     Active: active (running) since Mon 2025-06-02 13:27:48 AEST; 39s ago
       Docs: man:pacemakerd
             https://clusterlabs.org/pacemaker/doc/
   Main PID: 38554 (pacemakerd)
      Tasks: 7
     Memory: 31.3M
        CPU: 136ms
     CGroup: /system.slice/pacemaker.service
             ├─38554 /usr/sbin/pacemakerd
             ├─38555 /usr/libexec/pacemaker/pacemaker-based
             ├─38556 /usr/libexec/pacemaker/pacemaker-fenced
             ├─38557 /usr/libexec/pacemaker/pacemaker-execd
             ├─38558 /usr/libexec/pacemaker/pacemaker-attrd
             ├─38559 /usr/libexec/pacemaker/pacemaker-schedulerd
             └─38560 /usr/libexec/pacemaker/pacemaker-controld
```

Once the cluster service pacemaker is started, check the cluster status with pcs command, as shown in the following example:

```
 # pcs status
```

Example output:

```
 # pcs status
Cluster name: hana_cluster

WARNINGS:
No stonith devices and stonith-enabled is not false

Cluster Summary:
  * Stack: corosync
  * Current DC: hanahost02 (version 2.0.5-9.el8_4.8-ba59be7122) - partition with quorum
  * Last updated: Mon May 12 12:59:35 2025
  * Last change:  Mon May 12 12:59:25 2025 by hacluster via crmd on hanahost02
  * 2 nodes configured
  * 0 resource instances configured

Node List:
  * Online: [ hanahost01 hanahost02 ]

Full List of Resources:
  * No resources

Daemon Status:
  corosync: active/disabled
  pacemaker: active/disabled
  pcsd: active/enabled
```

The primary (hanahost01) and secondary (hanahost02) must show up as online.
You can find the ring status and the associated IP address of the cluster with corosync-cfgtool command, as shown in the following example:

```
 # corosync-cfgtool -s
```

Example output:

```
 Local node ID 1, transport knet
LINK ID 0 udp
        addr    = 10.2.10.1
        status:
                nodeid:          1:     localhost
                nodeid:          2:     connected
LINK ID 1 udp
        addr    = 10.2.10.2
        status:
                nodeid:          1:     localhost
                nodeid:          2:     connected
```
