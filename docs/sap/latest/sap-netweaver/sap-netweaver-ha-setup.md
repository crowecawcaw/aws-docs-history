# SAP and cluster setup

This section covers the following topics.

###### Topics

- [Install SAP](#install-sap "#install-sap")
- [Modify SAP control operations for cluster use](#modify-operations "#modify-operations")
- [Cluster prerequisites](#cluster-prerequisites "#cluster-prerequisites")
- [Create cluster and node associations](#associations "#associations")

## Install SAP

The following topics provide information about installing SAP on AWS Cloud in a highly available cluster. Review SAP Documentation for more details.

###### Topics

- [Use SWPM with high availability](#swpm-ha "#swpm-ha")
- [Install SAP instances](#sap-instances "#sap-instances")
- [Kernel upgrade and ENSA2 – optional](#kernel-ensa2 "#kernel-ensa2")
- [Check SAP host agent version](#host-agent-version "#host-agent-version")

### Use SWPM with high availability

Before running SAP Software Provisioning Manager (SWPM), ensure that the following prerequisites are met.

- If the operating system groups for SAP are pre-defined, ensure that the user identifier (UID) and group identifier values for `<sid>adm` and `sapsys` are consistent across both instances.
- You have downloaded the most recent version of Software Provisioning Manager for your SAP version. For more information, see SAP Documentation [Software Provisioning Manager](https://support.sap.com/en/tools/software-logistics-tools/software-provisioning-manager.html?anchorId=section "https://support.sap.com/en/tools/software-logistics-tools/software-provisioning-manager.html?anchorId=section").
- Ensure that routes, overlay IPs, and virtual host names are mapped to both instances. This is to ensure that the virtual hostname for ASCS is available on instance 1, and the virtual hostname for ERS is available on instance 2. For more information, see [IP and hostname resolution prerequisites](sles-setup.md#ip-prerequisites "sles-setup.md#ip-prerequisites").
- Ensure that shared file systems are available, either in `/etc/fstab` or using the mount command. For more information, see [File system prerequisites](sles-setup.md#filesystem-prerequisites "sles-setup.md#filesystem-prerequisites").

### Install SAP instances

The commands in this section use the example values provided in [Define reference parameters for setup](sles-setup.md#define-parameters "sles-setup.md#define-parameters").

Install ASCS instance on `slxhost01` with virtual hostname `slxascs`, using the high availability option of Software Provisioning Manager (SWPM) tool. You can use the `SAPINST_USE_HOSTNAME` parameter to install SAP using a virtual hostname.

```
<swpm location>/sapinst SAPINST_USE_HOSTNAME=<slxascs>
```

Install ERS instance on `slxhost02` with virtual hostname `slxers`, using the high availability option of Software Provisioning Manager (SWPM) tool. You can use the `SAPINST_USE_HOSTNAME` parameter to install SAP using a virtual hostname.

```
<swpm location>/sapinst SAPINST_USE_HOSTNAME=<slxers>
```

Once installation is complete, install and configure the database and SAP Primary Application Server (PAS). Optionally, you can also install and configure Additional Application Server (AAS). For more details on installing SAP NetWeaver, refer SAP Help Portal.

For additional information on unattended installation options, see [SAP Note 2230669 – System Provisioning Using an Input Parameter File](https://launchpad.support.sap.com/#/notes/2230669 "https://launchpad.support.sap.com/#/notes/2230669") (requires SAP portal access).

### Kernel upgrade and ENSA2 – _optional_

As of AS ABAP Release 7.53 (ABAP Platform 1809), the new Standalone Enqueue Server 2 (ENSA2) is installed by default. ENSA2 replaces the previous version – ENSA1.

If you have an older version of SAP NetWeaver, consider following the SAP guidance to upgrade the kernel and update the Enqueue Server configuration. An upgrade will allow you to take advantage of the features available in the latest version. For more information, see the following SAP Notes (require SAP portal access).

- [SAP Note 2630416 – Support for Standalone Enqueue Server 2](https://launchpad.support.sap.com/#/notes/2630416 "https://launchpad.support.sap.com/#/notes/2630416")
- [SAP Note 2711036 – Usage of the Standalone Enqueue Server 2 in an HA Environment](https://launchpad.support.sap.com/#/notes/2711036 "https://launchpad.support.sap.com/#/notes/2711036")

### Check SAP host agent version

This is applicable to both cluster nodes. The SAP host agent is used for system instance control and monitoring. This agent is used by SAP cluster resource agents and hooks. It is recommended that you have the latest version installed on both instances. For more details, see [SAP Note 2219592 – Upgrade Strategy of SAP Host Agent](https://launchpad.support.sap.com/#/notes/2219592 "https://launchpad.support.sap.com/#/notes/2219592").

Use the following command to check the version of the host agent.

```
/usr/sap/hostctrl/exe/saphostexec -version
```

## Modify SAP control operations for cluster use

This section covers the following topics.

###### Topics

- [Add sidadm to haclient group](#add-group "#add-group")
- [Modify SAP profiles for start operations and cluster hook](#modify-profiles "#modify-profiles")
- [Modify sapservices](#modify-services "#modify-services")
- [Align and disable SAP auto start services for systemd](#auto-disable "#auto-disable")
- [Enable sapping/sappong systemd services (simple-mount only)](#enable-services "#enable-services")

### Add `sidadm` to `haclient` group

This is applicable to both cluster nodes. An `haclient` operating system group is created when the cluster connector package is installed. Adding the `sidadm` user to this group ensures that your cluster has necessary access. Run the following command as root.

```
usermod -a -G haclient <slx>adm
```

### Modify SAP profiles for start operations and cluster hook

This action ensures that there is compatibility between SAP start framework and cluster actions. Modify SAP profiles to change the start behavior of the SAP instance and processes. Ensure that `sapcontrol` is aware that the system is being managed by a pacemaker cluster.

The following changes must be made in the instance profiles for ASCS and ERS. These profiles are created during install, and are located at `/usr/sap/<SID>/SYS/profile/`.

- ASCS profile example – `/usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs`
- ERS profile example – `/usr/sap/SLX/SYS/profile/SLX_ERS10_slxers`
  1.  **Program or process start behavior** – In case of failure, processes must be restarted. Determining where the process starts and in what order needs to be controlled by the cluster, and not SAP start framework behavior defined in the profiles. Your locks can be lost if this parameter is not changed.

  ENSA1

  **ASCS**

  ```
  #For ENSA1 (_EN)
  #Changing Restart to Start for Cluster compatibility
  #Old value: Restart_Program_XX = local $(_EN) pf=$(_PF)

  Start_Program_XX = local $(_EN) pf=$(_PF)
  ```

  **ERS**

  ```
  #For ENSA1 (_ER)
  #Changing Restart to Start for Cluster compatibility
  #Old value: Restart_Program_XX = local $(_ER) pf=$(_PFL)NR=$(SCSID)

  Start_Program_XX = local $(_ER) pf=$(_PFL) NR=$(SCSID)
  ```

  *`*XX*` indicates the start-up order. This value may be different in your install; retain the unchanged value.*

  ENSA2

  **ASCS**

  ```
  #For ENSA2 (_ENQ)
  #Changing Restart to Start for Cluster compatibility
  #Old value: Restart_Program_XX = local $(_ENQ) pf=$(_PF)

  Start_Program_XX = local $(_ENQ) pf=$(_PF)
  ```

  **ERS**

  ```
  #For ENSA2 (_ENQR)
  #Changing Restart to Start for Cluster compatibility
  #Old value: Restart_Program_XX = local $(_ENQR) pf=$(_PFL)NR=$(SCSID)

  Start_Program_XX = local $(_ENQR) pf=$(_PFL) NR=$(SCSID)
  ```

  *`*XX*` indicates the start order. This value may be different in your install; retain the unchanged value.* 2. **Disable instance auto start in both profiles** – When an instance restarts, SAP start framework should not start ASCS and ERS automatically. Add the following parameter on both profiles to prevent an auto start.

  ```
  Autostart = 0
  ```

  3.  **Add cluster connector details in both profilesP** – The connector integrates the SAP start and control frameworks of SAP NetWeaver with SUSE cluster to assist with maintenance and awareness of state. Add the following parameters on both profiles.

  ```
  #Added for Cluster Connectivity
  service/halib = $(DIR_CT_RUN)/saphascriptco.so
  service/halib_cluster_connector = /usr/bin/sap_suse_cluster_connector
  ```

  ###### Important

  RPM package `sap-suse-cluster-connector` has _dashes_. The executable `/usr/bin/sap_suse_cluster_connector` available after installation has _underscores_. Ensure that the correct name, that is executable `/usr/bin/sap_suse_cluster_connector`, is used in both profiles. 4. **Restart services** – Restart SAP services for ASCS and ERS to ensure that the preceding settings take effect. Adjust the system number to match the service.

  **ASCS**

  ```
  /usr/sap/hostctrl/exe/sapcontrol -nr <00> -function RestartService
  ```

  **ERS**

  ```
  /usr/sap/hostctrl/exe/sapcontrol -nr <10> -function RestartService
  ```

  5.  **Check integration using `sapcontrol`** – `sapcontrol` includes two functions: `HACheckConfig` and `HACheckFailoverConfig`. These functions can be used to check configuration, including awareness of the cluster connector.

  **ASCS**

  ```
  /usr/sap/hostctrl/exe/sapcontrol -nr <00> -function HACheckFailoverConfig
  /usr/sap/hostctrl/exe/sapcontrol -nr <00> -function HACheckConfig
  ```

### Modify `sapservices`

This is applicable to both cluster nodes. In older versions of SLES and SAP kernel, the `systemV init` service `sapinit` is responsible for starting SAP host agent and all `sapstartsrv` processes listed in `/usr/sap/sapservices`. In newer versions, native integration is available between `systemd` and SAP services. For more details, see the following SAP Notes (require SAP portal access).

- [SAP Note 3139184 – Linux: systemd integration for sapstartsrv and SAP Host Agent](https://launchpad.support.sap.com/#/notes/3139184 "https://launchpad.support.sap.com/#/notes/3139184")
- [SAP Note 3115048 – sapstartsrv with native Linux systemd support](https://launchpad.support.sap.com/#/notes/3115048 "https://launchpad.support.sap.com/#/notes/3115048")

Review if `systemV` or `systemd` integration is in place, and is consistent for ASCS and ERS by checking the `/usr/sap/services` file on both nodes.

```
cat /usr/sap/sapservices
```

See the following table for more details.

systemV
See the following example ASCS entry for older version with `systemV` integration.

```
LD_LIBRARY_PATH=/usr/sap/<SLX>/ASCS<00>/exe:$LD_LIBRARY_PATH;export LD_LIBRARY_PATH;/usr/sap/<SLX>/ASCS<00>/exe/sapstartsrv pf=/usr/sap/<SLX>/SYS/profile/<SLX>_ASCS<00>_<slxascs> -D -u <slxadm>
```

To ensure that SAP instance can be managed by the cluster and also manually during planned maintenance activities, add the missing entries for ASCS and ERS `sapstartsrv` service in `/usr/sap/sapservices` file on both cluster nodes (ASCS and ERS host). Copy the missing entry from both hosts. Post-modifications, the `/usr/sap/sapservices` file looks as follows on both hosts.

```
#!/bin/sh
LD_LIBRARY_PATH=/usr/sap/<SLX>/ASCS<00>/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/<SLX>/ASCS<00>/exe/sapstartsrv pf=/usr/sap/<SLX>/SYS/profile/<SLX>_ASCS<00>_<slxascs> -D -u <slxadm>

LD_LIBRARY_PATH=/usr/sap/<SLX>/ERS<10>/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/<SLX>/ERS<10>/exe/sapstartsrv pf=/usr/sap/<SLX>/SYS/profile/<SLX>_ERS<10>_<slxers> -D -u <slxadm>
```

systemd
See the following example ASCS entry for newer version with native `systemd` integration.

```
systemctl --no-ask-password start <SAPSLX>_<00> # sapstartsrv pf=/usr/sap/<SLX>/SYS/profile/SLX_ASCS<00>_<slxascs>
```

To ensure that SAP instance can be managed by the cluster and also manually during planned maintenance activities, add the missing entries for ASCS and ERS `sapstartsrv` service in `/usr/sap/sapservices` file on both cluster nodes (ASCS and ERS host). Copy the missing entry from both hosts. Post-modifications, the `/usr/sap/sapservices` file looks as follows on both hosts.

```
#!/bin/sh
systemctl --no-ask-password start <SAPSLX_00> # sapstartsrv pf=/usr/sap/<SLX>/SYS/profile/SLX_ASCS<00>_<slxascs>

systemctl --no-ask-password start <SAPSLX_10> # sapstartsrv pf=/usr/sap/<SLX>/SYS/profile/SLX_ERS<10>_<slxers>
```

### Align and disable SAP auto start services for `systemd`

This is applicable to both cluster nodes. For `systemd`, ensure SAP auto start services are aligned and disabled across nodes. If the installed version supports native integration with `systemd`, you must create services for ASCS and ERS on both nodes. This ensures that if you have revert to manual operations, there is no association and that both nodes are configured in the same manner.

You must disable auto start services to enable the cluster to manage stop/start.

**ASCS**

Register the missing ERS service on the node where you have installed ASCS.

Temporarily mount the ERS directory (classic only).

```
mount <nfs.fqdn>:/<SLX>_ERS<10>  /usr/sap/<SLX>/ERS10
```

Register the ERS service.

```
export LD_LIBRARY_PATH=/usr/sap/<SLX>/ERS10xe
/usr/sap/<SLX>/ERS10/exe/sapstartsrv pf=/usr/sap/<SLX>/SYS/profile/SLX_ERS10_slxers -reg

systemctl start SAPSLX_10
```

Check the existence and state of SAP services.

```
systemctl list-unit-files SAP*
UNIT FILESTATE VENDOR PRESET
SAPSLX_00.service disabled disabled
SAPSLX_10.service disabled disabled
SAP.slicestatic -
3 unit files listed.
```

If the state is not disabled, run the following command to disable `sapservices` integration for `SAP<SID>_<ascs_sys_nr>` and `SAP<SID>_<ers_sys_nr>` on both nodes.

###### Important

Stopping these services also stops the associated SAP instances.

```
systemctl stop SAP<SLX>_<00>.service
systemctl disable SAP<SLX>_<00>.service
systemctl stop SAP<SLX>_<10>.service
systemctl disable SAP<SLX>_<10>.service
```

Unmount the ERS directory (classic only).

```
umount /usr/sap/<SLX>/ERS

```

**ERS**

Register the missing ASCS service on the node where you have installed ERS.

Temporarily mount the ASCS directory (classic only).

```
mount <nfs.fqdn>:/SLX_ASCS00  /usr/sap/<SLX>/ASCS

```

Register the ASCS service.

```
export LD_LIBRARY_PATH=/usr/sap/<SLX>/ASCS<00>/exe
/usr/sap/<SLX>/ASCS<00>/exe/sapstartsrv pf=/usr/sap/<SLX>/SYS/profile/SLX_ASCS<00>_<slxascs> -reg
systemctl start SAP<SLX>_

```

Check the existence and state of SAP services.

```
systemctl list-unit-files SAP*
UNIT FILESTATE VENDOR PRESET
SAP<SLX>_<00>.service disabled disabled
SAP<SLX>_<10>.service disabled disabled
SAP.slicestatic -
3 unit files listed.
```

If the state is not disabled, run the following command to disable `sapservices` integration for `SAP<SID>_<ascs_sys_nr>` and `SAP<SID>_<ers_sys_nr>` on both nodes.

###### Important

Stopping these services also stops the associated SAP instances.

```
systemctl stop SAP<SLX>_<00>.service
systemctl disable SAP<SLX>_<00>.service
systemctl stop SAP<SLX>_<10>.service
systemctl disable SAP<SLX>_<10>.service
```

Unmount the ASCS directory (classic only).

```
umount /usr/sap/<SLX>/ASCS

```

For more details, see [SAP Note 3139184 – Linux: systemd integration for sapstartsrv and SAP Host Agent](https://launchpad.support.sap.com/#/notes/3139184 "https://launchpad.support.sap.com/#/notes/3139184").

### Enable `sapping`/`sappong` systemd services (simple-mount only)

In simple-mount architecture, the `sapstartsrv` resource is managed by the cluster. `sapstartsrv` should not be started by `sapinit` boot script during cluster nodes startup. The new services – `sapping` and `sappong` are used to mask and unmask the `/usr/sap/sapservices` file to meet this requirement.

These services are introduced by the `sapstartsrv` resource agent (located in the package `sapstartsrv-resource-agents`), and must exist in disabled state. If they do not exist, use the following command to check that you have installed the package.

```
zypper info sapstartsrv-resource-agents
```

Run the following command to enable `sapping` and `sappong` services on both nodes.

```
systemctl enable sapping
systemctl enable sappong
```

## Cluster prerequisites

This section covers the following topics.

###### Topics

- [Configure systemd for resource dependencies](#configure-systemd "#configure-systemd")
- [Update the hacluster password](#update-hacluster "#update-hacluster")
- [Setup passwordless authentication between nodes](#setup-authentication "#setup-authentication")
- [Create an authentication key for corosync](#corosync-authetication "#corosync-authetication")

### Configure `systemd` for resource dependencies

This is applicable to both cluster nodes. Some failure scenarios, such as an accidental shutdown of an Amazon EC2 instance, can result in unexpected fencing actions. This is caused by pacemaker dependencies that are not directly associated with cluster resources and constraints, but instead are a dependency for the pacemaker service.

If `systemd` is configured, create a config file that defines a dependency between pacemaker and SAP services.

```
mkdir -p /etc/systemd/system/resource-agents-deps.target.d/
cd /etc/systemd/system/resource-agents-deps.target.d/


cat > sap_systemd_<slx>.conf <<_EOF
[Unit]
Requires=sapinit.service
After=sapinit.service
After=SAP<SLX>_<00>.service
After=SAP<SLX>_<10>.service
_EOF


systemctl daemon-reload
```

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

Use `scp` or a temporary shared NFS location to copy an identical file on the second node at the same location. For example, on `slxhost01`.

```
scp -p /etc/corosync/authkey root@<slxhost02>:/etc/corosync
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
  # Enable and configure quorum subsystem (default: off)
  # see also corosync.conf.5 and votequorum.5
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
