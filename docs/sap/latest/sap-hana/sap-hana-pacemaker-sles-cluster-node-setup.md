# Cluster Node Setup

Establish cluster communication between nodes using Corosync and configure required authentication.

###### Topics

- [Deploy a Majority Maker Node (Scale-Out Clusters Only)](#_deploy_a_majority_maker_node_scale_out_clusters_only "#_deploy_a_majority_maker_node_scale_out_clusters_only")
- [Change the hacluster Password](#_change_the_hacluster_password "#_change_the_hacluster_password")
- [Setup Passwordless Authentication](#_setup_passwordless_authentication "#_setup_passwordless_authentication")
- [Configure the Cluster Nodes](#_configure_the_cluster_nodes "#_configure_the_cluster_nodes")
- [Modify Generated Corosync Configuration](#_modify_generated_corosync_configuration "#_modify_generated_corosync_configuration")
- [Verify Corosync Configuration](#_verify_corosync_configuration "#_verify_corosync_configuration")
- [Configure Cluster Services](#_configure_cluster_services "#_configure_cluster_services")
- [Verify Cluster Status](#_verify_cluster_status "#_verify_cluster_status")

## Deploy a Majority Maker Node (Scale-Out Clusters Only)

###### Note

Only required for clusters with more than two nodes.

When deploying an SAP HANA Scale-Out cluster in AWS, you must include a majority maker node in a third Availability Zone (AZ). The majority maker (tie-breaker) node ensures the cluster remains operational if one AZ fails by preserving the quorum. For the Scale-Out cluster to function, at least all nodes in one AZ plus the majority maker node must be running. If this minimum requirement is not met, the cluster loses its quorum state and any remaining SAP HANA nodes are fenced.

The majority maker requires a minimum EC2 instance configuration of 2 vCPUs, 2 GB RAM, and 50 GB disk space; this instance is exclusively used for quorum management and does not host an SAP HANA database or any other cluster resources.

## Change the hacluster Password

On all cluster nodes, change the password of the operating system user hacluster:

```
# passwd hacluster
```

## Setup Passwordless Authentication

For a more comprehensive and easily consumable view of cluster activity, SUSE provides additional reporting tools. Many of these tools require access to both nodes without entering a password. SUSE recommends performing this setup for root user.

For more details, see Configuration to collect cluster report as root with root SSH access between cluster nodes section in SUSE Documentation [Usage of hb_report for SLES HAE](https://www.suse.com/support/kb/doc/?id=000017501 "https://www.suse.com/support/kb/doc/?id=000017501").

###### Warning

Review the security implications for your organization, including root access controls and network segmentation, before implementing this configuration.

## Configure the Cluster Nodes

Initialize the cluster framework on the first node, including all known cluster nodes.

On the primary node as root, run:

```
# crm cluster init -u -n <cluster_name> -N <hostname_1> -N <hostname_2>
```

_Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_:

```
hanahost01:~ # crm cluster init -u -n myCluster -N hanahost01 -N hanahost02
INFO: Detected "amazon-web-services" platform
INFO: Loading "default" profile from /etc/crm/profiles.yml
INFO: Configure Corosync (unicast):
  This will configure the cluster messaging layer.  You will need
  to specify a network address over which to communicate (default
  is eth0's network, but you can use the network address of any
  active interface).

Address for ring0 [10.2.10.1]
Port for ring0 [5405]

Do you wish to use SBD (y/n)? n
WARNING: Not configuring SBD - STONITH will be disabled.

Do you wish to configure a virtual IP address (y/n)? n

Do you want to configure QDevice (y/n)? n
INFO: Done (log saved to /var/log/crmsh/crmsh.log)

INFO: Adding node hanahost02 to cluster
INFO: Running command on hanahost02: crm cluster join -y -c root@hanahost01
...
INFO: Done (log saved to /var/log/crmsh/crmsh.log)
```

This command:

- Initializes a two-node cluster named `myCluster`
- Configures unicast communication (-u)
- Sets up the basic corosync configuration
- Automatically joins the second node to the cluster
- We do not configure SBD as `fence_aws` will be used for STONITH in AWS environments.
- QDevice configuration is possible but not covered in this document. Refer to [SUSE Linux Enterprise High Availability Documentation - QDevice and QNetD](https://documentation.suse.com/en-us/sle-ha/15-SP7/html/SLE-HA-all/cha-ha-qdevice.html "https://documentation.suse.com/en-us/sle-ha/15-SP7/html/SLE-HA-all/cha-ha-qdevice.html").
- For clusters with more than two nodes, additional nodes can be added either during initialization with additional `-N <hostname_3>` parameters, or later using the following command on each new node:

```
# crm cluster join -c <hostname_1>
```

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
| ----------------- | --------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ring0_addr        | 10.2.10.1 | 10.2.20.1 |
| ring1_addr        | 10.2.10.2 | 10.2.20.2 | **3. Synchronize the modified configuration to all nodes:** `# csync2 -f /etc/corosync/corosync.conf` **4. Restart the cluster** `# crm cluster restart --all` ## Verify Corosync Configuration Verify network rings are active: `# corosync-cfgtool -s` _Example output_: `Printing ring status. Local node ID 1 RING ID 0 id      = 10.2.10.1 status  = ring 0 active with no faults RING ID 1 id      = 10.2.10.2 status  = ring 1 active with no faults` Both network rings should report "active with no faults". If either ring is missing, review the corosync configuration and check that `/etc/corosync/corosync.conf` changes have been synced to the secondary node. You may need to do this manually. Restart the cluster if needed. ## Configure Cluster Services Enable pacemaker to start automatically after reboot: `# systemctl enable pacemaker` Enabling pacemaker also handles corosync through service dependencies. The cluster will start automatically after reboot. For troubleshooting scenarios, you can choose to manually start services after boot instead. ## Verify Cluster Status **1. Check pacemaker service status:** `# systemctl status pacemaker` **2. Verify cluster status:** `# crm_mon -1` _Example output_: `Cluster Summary: <br>• Stack: corosync <br>• Current DC: hanahost01 (version 2.1.5+20221208.a3f44794f) - partition with quorum <br>• 2 nodes configured <br>• 0 resource instances configured Node List: <br>• Online: [ hanahost01 hanahost02 ] Active Resources: <br>• No active resources` |
