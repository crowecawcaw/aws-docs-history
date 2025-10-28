# SAP ASE and cluster setup

This section covers the following topics.

###### Topics

- [Install SAP ASE database](#install-sap-ase "#install-sap-ase")
- [Cluster prerequisites](#cluster-prerequisites "#cluster-prerequisites")
- [Create cluster and node associations](#associations "#associations")

## Install SAP ASE database

The following topics provide information about installing SAP ASE database on AWS Cloud in a highly available cluster. Review SAP Documentation for more details.

###### Topics

- [Use SWPM](#swpm "#swpm")
- [Install SAP database instance](#sap-instances "#sap-instances")
- [Check SAP host agent version](#host-agent-version "#host-agent-version")

### Use SWPM

Before running SAP Software Provisioning Manager (SWPM), ensure that the following prerequisites are met.

- If the operating system groups for SAP are pre-defined, ensure that the user identifier (UID) and group identifier values for `sapadm`, `<syb>adm`, and `sapsys` are consistent across both instances.
- You have downloaded the most recent version of Software Provisioning Manager for your SAP version. For more information, see SAP Documentation [Software Provisioning Manager](https://support.sap.com/en/tools/software-logistics-tools/software-provisioning-manager.html?anchorId=section "https://support.sap.com/en/tools/software-logistics-tools/software-provisioning-manager.html?anchorId=section").
- Ensure that routes, overlay IPs, and virtual host names are mapped to the instance where the installation is run. This is to ensure that the virtual hostname for SAP ASE database is available on the primary instance. For more information, see [IP and hostname resolution prerequisites](../sap-netweaver/sles-setup.md#ip-prerequisites "../sap-netweaver/sles-setup.md#ip-prerequisites").
- Ensure that FSx for ONTAP mount points are available, either in `/etc/fstab` or using the mount command. For more information, see [File system prerequisites](../sap-netweaver/sles-setup.md#filesystem-prerequisites "../sap-netweaver/sles-setup.md#filesystem-prerequisites"). If you are adding the entries in `/etc/fstab`, ensure that they are removed before configuring the cluster.

### Install SAP database instance

The commands in this section use the example values provided in [Define reference parameters for setup](../sap-netweaver/sles-setup.md#define-parameters "../sap-netweaver/sles-setup.md#define-parameters").

Install SAP ASE database on `slxdbhost01` with virtual hostname `slxvdb`, using the high availability option of Software Provisioning Manager (SWPM) tool. You can use the `SAPINST_USE_HOSTNAME` parameter to install SAP using a virtual hostname.

```
<swpm location>/sapinst SAPINST_USE_HOSTNAME=<slxvdb>
```

###### Note

Before installing SAP ASE database, ASCS and ERS must be installed, and the `/sapmnt` directory must be available on the database server.

### Check SAP host agent version

The SAP host agent is used for ASE database instance control and monitoring. This agent is used by SAP cluster resource agents and hooks. It is recommended that you have the latest version installed on both instances. For more details, see [SAP Note 2219592 – Upgrade Strategy of SAP Host Agent](https://launchpad.support.sap.com/#/notes/2219592 "https://launchpad.support.sap.com/#/notes/2219592").

Use the following command to check the version of the host agent.

```
/usr/sap/hostctrl/exe/saphostexec -version
```

## Cluster prerequisites

This section covers the following topics.

###### Topics

- [Update the hacluster password](#update-hacluster "#update-hacluster")
- [Setup passwordless authentication between nodes](#setup-authentication "#setup-authentication")
- [Create an authentication key for corosync](#corosync-authetication "#corosync-authetication")

### Update the `hacluster` password

This is applicable to both cluster nodes. Change the password of the operating system user `hacluster` using the following command.

```
passwd hacluster
```

### Setup passwordless authentication between nodes

For a more comprehensive and easily consumable view of cluster activity, SUSE provides additional reporting tools. Many of these tools require access to both nodes without entering a password. SUSE recommends performing this setup for root user. For more details, see _Configuration to collect cluster report as root with root SSH access between cluster nodes_ section in SUSE Documentation [https://www.suse.com/support/kb/doc/?id=000017501#:~:text=The%20hb_report%20utility%20(on%20newer,an%20incident%20to%20be%20investigated](https://www.suse.com/support/kb/doc/?id=000017501#:~:text=The%20hb_report%20utility%20(on%20newer,an%20incident%20to%20be%20investigated "https://www.suse.com/support/kb/doc/?id=000017501#:~:text=The%20hb_report%20utility%20(on%20newer,an%20incident%20to%20be%20investigated").[Usage of hb\_report for SLES HAE].

### Create an authentication key for `corosync`

If you want to configure `corosync` to use cryptographic techniques for ensuring authenticity and privacy of the messages, you need to generate a private key. The executable `corosync-keygen` creates this key and writes it to `/etc/corosync/authkey`.

Use the following command on Node 1 as root.

```
corosync-keygen
```

Use `scp` or a temporary shared NFS location to copy an identical file on the second node at the same location. For example, on `slxdbhost01`.

```
scp -p /etc/corosync/authkey root@<slxdbhost02>:/etc/corosync
```

## Create cluster and node associations

This section covers the following topics.

###### Topics

- [Stop services for initial configuration](#stop-services "#stop-services")
- [File modifications and key values](#file-modifications "#file-modifications")
- [Sample corosync.conf file](#sample-file "#sample-file")

### Stop services for initial configuration

This is applicable to both cluster nodes. The cluster service `pacemaker` must be in a stopped state when performing cluster configuration.

Run the following command to check if `pacemaker` is running.

```
systemctl status pacemaker
```

Run the following command to stop `pacemaker`.

```
systemctl stop pacemaker
```

### File modifications and key values

`corosync.conf` is the configuration file for the `corosync` executable. Copy the contents of the [Sample corosync.conf file](#sample-file "#sample-file") to `/etc/corosync/corosync.conf` on both nodes.

Ensure the following when copying the file.

- Ensure that the node list IP addresses match the primary and secondary IPs on each host (not the overlay IP)
- Ensure that the file is same on both nodes, with the exception of `bindnetaddr` that should match the relevant local primary IP address on each node.
- Ensure that the token value is set to 30000. This timeout specifies the time taken in milliseconds until a token loss is declared after not receiving a token. This is important for the stability of the cluster.

### Sample `corosync.conf` file

The following is a sample `corosync.conf` file.

Ensure that the file is same on both nodes, with the exception of `bindnetaddr` that should match the relevant local primary IP address on each node.

```
#Read the corosync.conf.5 manual page
totem {
  version: 2
  rrp_mode: passive
  token: 30000
  consensus: 36000
  token_retransmits_before_loss_const: 10
  max_messages: 20
  crypto_cipher: aes256
  crypto_hash: sha1
  clear_node_high_bit: yes
  interface {
    ringnumber: 0
    bindnetaddr: <local_ip>
    mcastport: 5405
    ttl: 1
 }
  transport: udpu
}
 logging {
      fileline: off
      to_logfile: yes
      to_syslog: yes
      logfile: /var/log/cluster/corosync.log
      debug: off
      timestamp: on
      logger_subsys {
         subsys: QUORUM
         debug: off
     }
}
nodelist {
  node {
  ring0_addr: <primary_host_ip>
  ring1_addr: <primary_host_additional_ip>
  nodeid: 1
  }
  node {
  ring0_addr: <secondary_host_ip>
  ring1_addr: <secondary_host_additional_ip>
  nodeid: 2
  }
}

quorum {
  #Enable and configure quorum subsystem (default: off)
  #see also corosync.conf.5 and votequorum.5
  provider: corosync_votequorum
  expected_votes: 2
  two_node: 1
}
```

The following table displays example substitutions for IP addresses using the sample IP addresses provided in this document. The <local_ip> configuration differs between hosts.

| IP address type                | Primary host  | Secondary host |
| ------------------------------ | ------------- | -------------- |
| <local_ip>                     | **10.1.10.1** | **10.1.20.1**  |
| <primary_host_ip>              | 10.1.10.1     | 10.1.10.1      |
| <primary_host_additional_ip>   | 10.1.10.2     | 10.1.10.2      |
| <secondary_host_ip>            | 10.1.20.1     | 10.1.20.1      |
| <secondary_host_additional_ip> | 10.1.20.2     | 10.1.20.2      |
