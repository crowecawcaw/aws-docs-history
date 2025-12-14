# Cluster Node Setup

Establish cluster communication between nodes using Corosync and configure required authentication.

###### Topics

- [Change the hacluster Password](#change-hacluster-password-nw-sles "#change-hacluster-password-nw-sles")
- [Setup Passwordless Authentication](#setup-passwordless-auth-nw-sles "#setup-passwordless-auth-nw-sles")
- [Configure the Cluster Nodes](#configure-cluster-nodes-nw-sles "#configure-cluster-nodes-nw-sles")
- [Modify Generated Corosync Configuration](#modify-corosync-config-nw-sles "#modify-corosync-config-nw-sles")
- [Verify Corosync Configuration](#verify-corosync-config-nw-sles "#verify-corosync-config-nw-sles")
- [Configure Cluster Services](#configure-cluster-services-nw-sles "#configure-cluster-services-nw-sles")
- [Verify Cluster Status](#verify-cluster-status-nw-sles "#verify-cluster-status-nw-sles")

## Change the hacluster Password

On all cluster nodes, change the password of the operating system user hacluster:

```
# passwd hacluster
```

## Setup Passwordless Authentication

SUSE cluster tools provide comprehensive reporting and troubleshooting capabilities for cluster activity. Many of these tools require passwordless SSH access between nodes to collect cluster-wide information effectively. SUSE recommends configuring passwordless SSH for the root user to enable seamless cluster diagnostics and reporting.

EC2 instances typically have no root password set. Use the shared `/sapmnt` filesystem to exchange SSH keys:

**On the primary node (<hostname1>):**

```
# ssh-keygen -t rsa -b 4096 -f /root/.ssh/id_rsa -N ''
# cp /root/.ssh/id_rsa.pub /sapmnt/node1_key.pub
```

**On the secondary node (<hostname2>):**

```
# ssh-keygen -t rsa -b 4096 -f /root/.ssh/id_rsa -N ''
# cp /root/.ssh/id_rsa.pub /sapmnt/node2_key.pub
# cat /sapmnt/node1_key.pub >> /root/.ssh/authorized_keys
# chmod 600 /root/.ssh/authorized_keys
```

**Back on the primary node (<hostname1>):**

```
# cat /sapmnt/node2_key.pub >> /root/.ssh/authorized_keys
# chmod 600 /root/.ssh/authorized_keys
```

**Test connectivity from both nodes:**

```
# ssh root@<opposite_hostname> 'hostname'
```

**Clean up temporary files (from either node):**

```
# rm /sapmnt/node1_key.pub /sapmnt/node2_key.pub
```

An alternative is to review the SUSE Dcoumentation for [Running cluster reports without root access](https://documentation.suse.com/sle-ha/15-SP7/html/SLE-HA-all/app-crmreport-nonroot.html "https://documentation.suse.com/sle-ha/15-SP7/html/SLE-HA-all/app-crmreport-nonroot.html")

###### Warning

Review the security implications for your organization, including root access controls and network segmentation, before implementing this configuration.

## Configure the Cluster Nodes

Initialize the cluster framework on the first node to recognise both cluster nodes.

On the primary node as root, run:

```
# crm cluster init -u -n <cluster_name> -N <hostname_1> <hostname_2>
```

_Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm cluster init -u -y -n slx-sap-cluster -N slxhost01 -N slxhost02
INFO: Detected "amazon-web-services" platform
INFO: Loading "default" profile from /etc/crm/profiles.yml
INFO: "amazon-web-services" profile does not exist in /etc/crm/profiles.yml

INFO: Configuring csync2
INFO: Starting csync2.socket service on slxhost01
INFO: BEGIN csync2 checking files
INFO: END csync2 checking files
INFO: Configuring corosync (unicast)
WARNING: Not configuring SBD - STONITH will be disabled.
INFO: Hawk cluster interface is now running. To see cluster status, open:
INFO:   https://10.2.10.1:7630/
INFO: Log in with username 'hacluster'
INFO: Starting pacemaker.service on slxhost01
INFO: BEGIN Waiting for cluster
...........
INFO: END Waiting for cluster
INFO: Loading initial cluster configuration
INFO: Done (log saved to /var/log/crmsh/crmsh.log on slxhost01)
INFO: Adding node slxhost02 to cluster
INFO: Running command on slxhost02: crm cluster join -y  -c root@slxhost01
INFO: Configuring csync2
INFO: Starting csync2.socket service
INFO: BEGIN csync2 syncing files in cluster
INFO: END csync2 syncing files in cluster
INFO: Merging known_hosts
INFO: BEGIN Probing for new partitions
INFO: END Probing for new partitions
INFO: Hawk cluster interface is now running. To see cluster status, open:
INFO:   https://10.1.20.7:7630/
INFO: Log in with username 'hacluster'
INFO: Starting pacemaker.service on slxhost02
INFO: BEGIN Waiting for cluster
INFO: END Waiting for cluster
INFO: Set property "priority" in rsc_defaults to 1
INFO: BEGIN Reloading cluster configuration
INFO: END Reloading cluster configuration
INFO: Done (log saved to /var/log/crmsh/crmsh.log on slxhost02)
```

This command:

- Initializes a two-node cluster named `myCluster`
- Configures unicast communication (-u)
- Sets up the basic corosync configuration
- Automatically joins the second node to the cluster
- We do not configure SBD as an AWS Fencing Agent will be used for STONITH in AWS environments.
- QDevice configuration is possible but not covered in this document. Refer to [SUSE Linux Enterprise High Availability Documentation - QDevice and QNetD](https://documentation.suse.com/en-us/sle-ha/15-SP7/html/SLE-HA-all/cha-ha-qdevice.html "https://documentation.suse.com/en-us/sle-ha/15-SP7/html/SLE-HA-all/cha-ha-qdevice.html").

## Modify Generated Corosync Configuration

After initializing the cluster, the generated corosync configuration requires some modification to be optimised for cloud envrironments.

**1. Edit the corosync configuration:**

```
# vi /etc/corosync/corosync.conf
```

The generated file typically looks like this:

```
# Please read the corosync.conf.5 manual page
totem {
        version: 2
        cluster_name: myCluster
        clear_node_high_bit: yes
        interface {
                ringnumber: 0
                mcastport: 5405
                ttl: 1
        }

        transport: udpu
        crypto_hash: sha1
        crypto_cipher: aes256
        token: 5000     # This needs to be changed
        join: 60
        max_messages: 20
        token_retransmits_before_loss_const: 10
}

logging {
        fileline: off
        to_stderr: no
        to_logfile: yes
        logfile: /var/log/cluster/corosync.log
        to_syslog: yes
        debug: off
        timestamp: on
        logger_subsys {
                subsys: QUORUM
                debug: off
        }

}

nodelist {
    node {
        ring0_addr: <node1_primary_ip>    # Only single ring configured
        nodeid: 1
    }
    node {
        ring0_addr: <node2_primary_ip>    # Only single ring configured
        nodeid: 2
    }
}

quorum {

        # Enable and configure quorum subsystem (default: off)
        # see also corosync.conf.5 and votequorum.5
        provider: corosync_votequorum
        expected_votes: 2
        two_node: 1
}

totem {
    version: 2
    token: 5000             # This needs to be changed
    transport: udpu
    interface {
        ringnumber: 0
        mcastport: 5405
    }
}
```

**2. Modify the configuration to add the second ring and optimize settings:**

```
totem {
    token: 15000           # Changed from 5000 to 15000
    rrp_mode: passive      # Added for dual ring support
}

nodelist {
    node {
        ring0_addr: <node1_primary_ip>     # Primary network
        ring1_addr: <node1_secondary_ip>   # Added secondary network
        nodeid: 1
    }
    node {
        ring0_addr: <node2_primary_ip>     # Primary network
        ring1_addr: <node2_secondary_ip>   # Added secondary network
        nodeid: 2
    }
}
```

_Example IP configuration:_

| Network Interface | Node 1    | Node 2    |
| ----------------- | --------- | --------- |
| ring0_addr        | 10.2.10.1 | 10.2.20.1 |
| ring1_addr        | 10.2.10.2 | 10.2.20.2 |

**3. Synchronize the modified configuration to all nodes:**

```
# csync2 -xvF /etc/corosync/corosync.conf
```

**4. Restart the cluster**

```
# crm cluster restart
# ssh root@<hostname2> 'crm cluster restart'
```

## Verify Corosync Configuration

Verify network rings are active:

```
# corosync-cfgtool -s
```

_Example output_:

```
Printing ring status.
Local node ID 1
RING ID 0
        id      = 10.2.10.1
        status  = ring 0 active with no faults
RING ID 1
        id      = 10.2.10.2
        status  = ring 1 active with no faults
```

Both network rings should report "active with no faults". If either ring is missing, review the corosync configuration and check that `/etc/corosync/corosync.conf` changes have been synced to the secondary node. You may need to do this manually. Restart the cluster if needed.

## Configure Cluster Services

Enable pacemaker to start automatically after reboot:

```
# systemctl enable pacemaker
```

Enabling pacemaker also handles corosync through service dependencies. The cluster will start automatically after reboot. For troubleshooting scenarios, you can choose to manually start services after boot instead.

## Verify Cluster Status

**1. Check pacemaker service status:**

```
# systemctl status pacemaker
```

**2. Verify cluster status:**

```
# crm_mon -1
```

_Example output_:

```
Cluster Summary:
  * Stack: corosync
  * Current DC: slxhost01 (version 2.1.5+20221208.a3f44794f) - partition with quorum
  * 2 nodes configured
  * 0 resource instances configured

Node List:
  * Online: [ slxhost01 slxhost02 ]

Active Resources:
  * No active resources
```
