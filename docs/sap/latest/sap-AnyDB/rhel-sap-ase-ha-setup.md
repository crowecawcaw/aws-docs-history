# SAP and cluster setup

This section covers the following topics.

###### Topics

- [Install SAP](#install-sap "#install-sap")
- [Cluster prerequisites](#cluster-prerequisites "#cluster-prerequisites")
- [Create cluster and node associations](#associations "#associations")

## Install SAP

The following topics provide information about installing SAP ASE database on AWS Cloud in a highly available cluster. Review SAP Documentation for more details.

###### Topics

- [Use SWPM with high availability](#swpm-ha "#swpm-ha")
- [Install SAP database instance](#sap-instances "#sap-instances")
- [Check SAP host agent version](#host-agent-version "#host-agent-version")

### Use SWPM with high availability

Before running SAP Software Provisioning Manager (SWPM), ensure that the following prerequisites are met.

- If the operating system groups for SAP are pre-defined, ensure that the user identifier (UID) and group identifier (GID) values for `<syb>adm`, `sapadm`, and `sapsys` are consistent across both instances.
- You have downloaded the most recent version of Software Provisioning Manager for your SAP version. For more information, see SAP Documentation [Software Provisioning Manager](https://support.sap.com/en/tools/software-logistics-tools/software-provisioning-manager.html?anchorId=section "https://support.sap.com/en/tools/software-logistics-tools/software-provisioning-manager.html?anchorId=section").
- Ensure that routes, overlay IPs, and virtual host names are mapped to the instance where the installation will run. This is to ensure that the virtual hostname for SAP ASE database is available on the primary instance. For more information, see [IP and hostname resolution prerequisites](../sap-netweaver/sles-setup.md#ip-prerequisites "../sap-netweaver/sles-setup.md#ip-prerequisites").
- Ensure that FSx for ONTAP mount points are available, either in `/etc/fstab` or using the mount command. For more information, see [File system prerequisites](../sap-netweaver/sles-setup.md#filesystem-prerequisites "../sap-netweaver/sles-setup.md#filesystem-prerequisites"). If you are adding the entries in `/etc/fstab`, ensure that they are removed before configuring the cluster.

### Install SAP database instance

The commands in this section use the example values provided in [Define reference parameters for setup](../sap-netweaver/sles-setup.md#define-parameters "../sap-netweaver/sles-setup.md#define-parameters").

Install SAP ASE database on `<rhxdbhost01>` with virtual hostname `rhxvdb`, using the high availability option of Software Provisioning Manager (SWPM) tool. You can use the `SAPINST_USE_HOSTNAME` parameter to install SAP using a virtual hostname.

```
<swpm location>/sapinst SAPINST_USE_HOSTNAME=<rhxvdb>
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

### Update the `hacluster` password

This is applicable to both cluster nodes. Change the password of the operating system user `hacluster` using the following command.

```
passwd hacluster
```

### Setup passwordless authentication between nodes

For a more comprehensive and easily consumable view of cluster activity, Red Hat provides additional reporting tools. Many of these tools require access to both nodes without entering a password. Red Hat recommends performing this setup for root user.

For more details, see Red Hat documentation [How to setup SSH Key passwordless login in Red Hat Enterprise Linux?](https://access.redhat.com/solutions/9194 "https://access.redhat.com/solutions/9194")

## Create cluster and node associations

This section covers the following topics.

###### Topics

- [Start pcsd service](#start-pcsd "#start-pcsd")
- [Reset configuration – optional](#reset-configuration "#reset-configuration")
- [Authenticate pcs with user hacluster](#autheticate-pcs "#autheticate-pcs")
- [Setup node configuration](#node-configuration "#node-configuration")

### Start `pcsd` service

This is applicable on both cluster nodes. Run the following command to enable and start the cluster service `pcsd` (pacemaker/corosync configuration system daemon) on both, the primary and secondary node.

```
systemctl start pcsd.service
systemctl enable pcsd.service
```

Run the following command to check the status of cluster service.

```
systemctl status pcsd.service
● pcsd.service - PCS GUI and remote configuration interface
   Loaded: loaded (/usr/lib/systemd/system/pcsd.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-01-13 14:15:32 IST; 7min ago
     Docs: man:pcsd(8)
           man:pcs(8)
 Main PID: 1445 (pcsd)
    Tasks: 1 (limit: 47675)
   Memory: 27.1M
   CGroup: /system.slice/pcsd.service
           └─1445 /usr/libexec/platform-python -Es /usr/sbin/pcsd
```

### Reset configuration – _optional_

###### Note

The following instructions help you reset the complete configuration. Run these commands only if you want to start setup from the beginning. You can make minor changes with the `crm edit` command.

Run the following command to back up the current configuration for reference.

```
pcs config show > /tmp/pcsconfig_backup.txt
```

Run the following command to clear the current configuration.

```
pcs cluster destroy
```

### Authenticate `pcs` with user `hacluster`

The following command authenticates `pcs` to the `pcs daemon` on cluster nodes. It should be run on only one of the cluster nodes. The username and password for the `pcs` user must be the same, and the username should be `<hacluster>`.

**RHEL 7.x**

```
pcs cluster auth <rhxdbhost01> <rhxdbhost02>
Username: <hacluster>
Password:
rhxhost02: Authorized
rhxhost01: Authorized
```

**RHEL 8.x**

```
pcs host auth <rhxdbhost01> <rhxdbhost02>
Username: <hacluster>
Password:
rhxhost02: Authorized
rhxhost01: Authorized
```

### Setup node configuration

The following command configures the `cluster configuration` file, and syncs the configuration on both nodes. It should be run on only one of the cluster nodes.

**RHEL 7.x**

```
pcs cluster setup --name <rhelha> <rhxdbhost01> <rhxdbhost02>
Destroying cluster on nodes: <rhxdbhost01>, <rhxdbhost02>...
<rhxdbhost02>: Stopping Cluster (pacemaker)...
<rhxdbhost01>: Stopping Cluster (pacemaker)...
<rhxdbhost02>: Successfully destroyed cluster
<rhxdbhost01>: Successfully destroyed cluster

Sending 'pacemaker_remote authkey' to '<rhxdbhost01>', '<rhxdbhost02>'
<rhxdbhost01>: successful distribution of the file 'pacemaker_remote authkey'
<rhxdbhost02>: successful distribution of the file 'pacemaker_remote authkey'
Sending cluster config files to the nodes...
<rhxdbhost01>: Succeeded
<rhxdbhost02>: Succeeded

Synchronizing pcsd certificates on nodes <rhxdbhost01>, <rhxdbhost02>...
<rhxdbhost01>: Success
<rhxdbhost02>: Success
Restarting pcsd on the nodes in order to reload the certificates...
<rhxdbhost01>: Success
<rhxdbhost02>: Success.
```

**RHEL 8.x**

```
pcs cluster setup <rhelha> <rhxdbhost01> <rhxdbhost02>
        No addresses specified for host '<rhxdbhost01>', using '<rhxdbhost01>'
        No addresses specified for host '<rhxdbhost02>', using '<rhxdbhost02>'
        Destroying cluster on hosts: '<rhxdbhost01>', '<rhxdbhost02>'...
        <rhxdbhost01>: Successfully destroyed cluster
        <rhxdbhost02>: Successfully destroyed cluster
        Requesting remove 'pcsd settings' from '<rhxdbhost01>', '<rhxdbhost02>'
        <rhxdbhost01>: successful removal of the file 'pcsd settings'
        <rhxdbhost02>: successful removal of the file 'pcsd settings'
        Sending 'corosync authkey', 'pacemaker authkey' to '<rhxdbhost01>', '<rhxdbhost02>'
        <rhxdbhost01>: successful distribution of the file 'corosync authkey'
        <rhxdbhost01>: successful distribution of the file 'pacemaker authkey'
        <rhxdbhost02>: successful distribution of the file 'corosync authkey'
        <rhxdbhost02>: successful distribution of the file 'pacemaker authkey'
        Sending 'corosync.conf' to '<rhxdbhost01>', '<rhxdbhost02>'
        <rhxdbhost01>: successful distribution of the file 'corosync.conf'
        <rhxdbhost02>: successful distribution of the file 'corosync.conf'
        Cluster has been successfully set up.
```
