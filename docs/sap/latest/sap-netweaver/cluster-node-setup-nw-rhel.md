# Cluster Node Setup

Establish cluster communication between nodes using Corosync and configure required authentication.

###### Topics

- [Change the hacluster Password](#change-hacluster-password-nw-rhel "#change-hacluster-password-nw-rhel")
- [Setup Passwordless Authentication](#setup-passwordless-auth-nw-rhel "#setup-passwordless-auth-nw-rhel")
- [Start and Enable the pcsd Service](#start-pcsd-service-nw-rhel "#start-pcsd-service-nw-rhel")
- [Authorize the Cluster](#configure-cluster-nodes-nw-rhel "#configure-cluster-nodes-nw-rhel")
- [Generate Corosync Configuration](#generate-corosync-config-nw-rhel "#generate-corosync-config-nw-rhel")
- [Start and Verify the Cluster](#start-cluster-nw-rhel "#start-cluster-nw-rhel")
- [Configure Cluster Services](#configure-cluster-services-nw-rhel "#configure-cluster-services-nw-rhel")
- [Verify Cluster Status](#verify-cluster-status-nw-rhel "#verify-cluster-status-nw-rhel")

## Change the hacluster Password

On all cluster nodes, change the password of the operating system user hacluster:

```
# passwd hacluster
```

## Setup Passwordless Authentication

Red Hat cluster tools provide comprehensive reporting and troubleshooting capabilities for cluster activity. Many of these tools require passwordless SSH access between nodes to collect cluster-wide information effectively. Red Hat recommends configuring passwordless SSH for the root user to enable seamless cluster diagnostics and reporting.

For more details, see Red Hat Documentation [How to setup SSH Key passwordless login in Red Hat Enterprise Linux](https://access.redhat.com/solutions/9194 "https://access.redhat.com/solutions/9194").

###### Warning

Review the security implications for your organization, including root access controls and network segmentation, before implementing this configuration.

## Start and Enable the pcsd Service

On all cluster nodes, enable and start the pcsd service:

```
# systemctl enable pcsd --now
```

## Authorize the Cluster

Run the following command to authenticate the cluster nodes. You will be prompted for the hacluster password you set earlier:

```
# pcs host auth <hostname_1> <hostname_2> -u hacluster -p <password>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs host auth rhxhost01 rhxhost02 -u hacluster -p <password>
```

## Generate Corosync Configuration

Corosync provides membership and member-communication needs for high availability clusters. Initial setup can be performed using the following command with dual network rings for redundant communication:

```
# pcs cluster setup <cluster_name> \
<hostname_1> addr=<host_ip_1> addr=<host_additional_ip_1> \
<hostname_2> addr=<host_ip_2> addr=<host_additional_ip_2>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs cluster setup myCluster rhxhost01 addr=10.1.10.1 addr=10.1.10.2 rhxhost02 addr=10.1.20.1 addr=10.1.20.2
Destroying cluster on hosts: 'rhxhost01', 'rhxhost02'...
rhxhost01: Successfully destroyed cluster
rhxhost02: Successfully destroyed cluster
Requesting remove 'pcsd settings' from 'rhxhost01', 'rhxhost02'
rhxhost01: successful removal of the file 'pcsd settings'
rhxhost02: successful removal of the file 'pcsd settings'
Sending 'corosync authkey', 'pacemaker authkey' to 'rhxhost01', 'rhxhost02'
rhxhost01: successful distribution of the file 'corosync authkey'
rhxhost01: successful distribution of the file 'pacemaker authkey'
rhxhost02: successful distribution of the file 'corosync authkey'
rhxhost02: successful distribution of the file 'pacemaker authkey'
Sending 'corosync.conf' to 'rhxhost01', 'rhxhost02'
rhxhost01: successful distribution of the file 'corosync.conf'
rhxhost02: successful distribution of the file 'corosync.conf'
Cluster has been successfully set up.
```

The timing parameters are optimized for AWS cloud environments. Update the token timeout to provide reliable cluster operation while accommodating normal cloud network characteristics:

```
# pcs cluster config update totem token=15000
```

## Start and Verify the Cluster

Start the cluster on all nodes:

```
# pcs cluster start --all
```

###### Note

By enabling the pacemaker service, the server automatically joins the cluster after a reboot. This ensures that your system is protected. Alternatively, you can start the pacemaker service manually on boot to investigate the cause of any failure.

Run the following command to check the cluster status:

```
# pcs status
```

Example output:

```
Cluster name: myCluster

WARNINGS:
No stonith devices and stonith-enabled is not false

Cluster Summary:
  * Stack: corosync
  * Current DC: rhxhost01 (version 2.1.2-4.el9_0.5-ada5c3b36e2) - partition with quorum
  * Last updated: Fri Oct 24 06:35:46 2025
  * Last change:  Fri Oct 24 06:26:38 2025 by hacluster via crmd on rhxhost01
  * 2 nodes configured
  * 0 resource instances configured

Node List:
  * Online: [ rhxhost01 rhxhost02 ]

Full List of Resources:
  * No resources

Daemon Status:
  corosync: active/disabled
  pacemaker: active/disabled
  pcsd: active/enabled
```

Both cluster nodes must show up as online. You can find the ring status and the associated IP addresses of the cluster with the corosync-cfgtool command:

```
# corosync-cfgtool -s
```

Example output:

```
Local node ID 1, transport knet
LINK ID 0 udp
        addr    = 10.1.10.114
        status:
                nodeid:          1:     localhost
                nodeid:          2:     connected
LINK ID 1 udp
        addr    = 10.1.10.215
        status:
                nodeid:          1:     localhost
                nodeid:          2:     connected
```

Both network rings should report "active with no faults". If either ring is missing, review the corosync configuration and check that `/etc/corosync/corosync.conf` changes have been synced to the secondary node. You may need to do this manually. Restart the cluster if needed.

## Configure Cluster Services

Enable pacemaker to start automatically after reboot:

```
# pcs cluster enable --all
```

Enabling pacemaker also handles corosync through service dependencies. The cluster will start automatically after reboot. For troubleshooting scenarios, you can choose to manually start services after boot instead.

## Verify Cluster Status

**1. Check pacemaker service status:**

```
# systemctl status pacemaker
```

**2. Verify cluster status:**

```
# pcs status
```

_Example output_:

```
Cluster name: myCluster
Cluster Summary:
  * Stack: corosync
  * Current DC: rhxhost01 (version 2.1.5+20221208.a3f44794f) - partition with quorum
  * 2 nodes configured
  * 0 resource instances configured

Node List:
  * Online: [ rhxhost01 rhxhost02 ]

Full List of Resources:
  * No resources
```
