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
- Ensure that routes, overlay IPs, and virtual host names are mapped to both instances. This is to ensure that the virtual hostname for ASCS is available on instance 1, and the virtual hostname for ERS is available on instance 2. For more information, see [IP and hostname resolution prerequisites](rhel-setup.md#ip-prerequisites "rhel-setup.md#ip-prerequisites").
- Ensure that shared file systems are available, either in `/etc/fstab` or using the mount command. For more information, see [File system prerequisites](rhel-setup.md#filesystem-prerequisites "rhel-setup.md#filesystem-prerequisites").

### Install SAP instances

The commands in this section use the example values provided in [Define reference parameters for setup](rhel-setup.md#define-parameters "rhel-setup.md#define-parameters").

Install ASCS instance on `<rhxhost01>` with virtual hostname `rhxascs`, using the high availability option of Software Provisioning Manager (SWPM) tool. You can use the `SAPINST_USE_HOSTNAME` parameter to install SAP using a virtual hostname.

```
<swpm location>/sapinst SAPINST_USE_HOSTNAME=<rhxascs>
```

Install ERS instance on `<rhxhost02>` with virtual hostname `rhxers`, using the high availability option of Software Provisioning Manager (SWPM) tool. You can use the `SAPINST_USE_HOSTNAME` parameter to install SAP using a virtual hostname.

```
<swpm location>/sapinst SAPINST_USE_HOSTNAME=<rhxers>
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

### Add `sidadm` to `haclient` group

This is applicable to both cluster nodes. An `haclient` operating system group is created when the cluster connector package is installed. Adding the `sidadm` user to this group ensures that your cluster has necessary access. Run the following command as root.

```
usermod -a -G haclient <rhx>adm
```

### Modify SAP profiles for start operations and cluster hook

This action ensures that there is compatibility between SAP start framework and cluster actions. Modify SAP profiles to change the start behavior of the SAP instance and processes. Ensure that `sapcontrol` is aware that the system is being managed by a pacemaker cluster.

The following changes must be made in the instance profiles for ASCS and ERS. These profiles are created during install, and are located at `/usr/sap/<SID>/SYS/profile/`.

- ASCS profile example – `/usr/sap/RHX/SYS/profile/RHX_ASCS00_rhxascs`
- ERS profile example – `/usr/sap/RHX/SYS/profile/RHX_ERS10_rhxers`
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
  #Old value: Restart_Program_XX = local $(_ER) pf=$(_PF)NR=$(SCSID)

  Start_Program_XX = local $(_ER) pf=$(_PF) NR=$(SCSID)
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
  #Old value: Restart_Program_XX = local $(_ENQR) pf=$(_PF)NR=$(SCSID)

  Start_Program_XX = local $(_ENQR) pf=$(_PF) NR=$(SCSID)
  ```

  *`*XX*` indicates the start order. This value may be different in your install; retain the unchanged value.* 2. **Disable instance auto start in both profiles** – When an instance restarts, SAP start framework should not start ASCS and ERS automatically. Add the following parameter on both profiles to prevent an auto start.

  ```
  Autostart = 0
  ```

  3.  **Add cluster connector details in both profiles** – The connector integrates the SAP start and control frameworks of SAP NetWeaver with RHEL cluster to assist with maintenance and awareness of state. Add the following parameters on both profiles.

  ```
  Added for Cluster Connectivity
  service/halib = $(DIR_CT_RUN)/saphascriptco.so
  service/halib_cluster_connector = /usr/bin/sap_cluster_connector
  ```

  ###### Important

  The minimum version of `sap_cluster_connector` that complies with HA-Interface certification NW-HA-CLU 750 or S/4-HA-CLU 1.0 is 3.0.1-1.el7_6.5. A previous version of SAP cluster connector was delivered as part of the `resource-agents-sap` package and the name of the connector was `sap_cluster_connector`. 4. **Restart services** – Restart SAP services for ASCS and ERS to ensure that the preceding settings take effect. Adjust the system number to match the service.

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

  **ERS**

  ```
  /usr/sap/hostctrl/exe/sapcontrol -nr 10 -function HACheckFailoverConfig
  /usr/sap/hostctrl/exe/sapcontrol -nr 10 -function HACheckConfig
  ```

### Modify `sapservices`

This is applicable to both cluster nodes. In older versions of Red Hat and SAP kernel, the `systemV init` service `sapinit` is responsible for starting SAP host agent and all `sapstartsrv` processes listed in `/usr/sap/sapservices`. In newer versions, native integration is available between `systemd` and SAP services. For more details, see the following SAP Notes (require SAP portal access).

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
LD_LIBRARY_PATH=/usr/sap/<RHX>/ASCS<00>/exe:$LD_LIBRARY_PATH;export LD_LIBRARY_PATH;/usr/sap/<RHX>/ASCS<00>/exe/sapstartsrv pf=/usr/sap/<RHX>/SYS/profile/<RHX>_ASCS<00>_<rhxascs> -D -u <rhxadm>u
```

To ensure that SAP instance can be managed by the cluster and also manually during planned maintenance activities, add the missing entries for ASCS and ERS `sapstartsrv` service in `/usr/sap/sapservices` file on both cluster nodes (ASCS and ERS host). Copy the missing entry from both hosts. Post-modifications, the `/usr/sap/sapservices` file looks as follows on both hosts.

```
#!/bin/sh
LD_LIBRARY_PATH=/usr/sap/<RHX>/ASCS<00>/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/<RHX>/ASCS<00>/exe/sapstartsrv pf=/usr/sap/<RHX>/SYS/profile/<RHX>_ASCS<00>_<rhxascs> -D -u <rhxadm>

LD_LIBRARY_PATH=/usr/sap/<RHX>/ERS<10>/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/<RHX>/ERS<10>/exe/sapstartsrv pf=/usr/sap/<RHX>/SYS/profile/<RHX>_ERS<10>_ -D<rhxers> -u <rhxadm>
```

systemd

- See the following example ASCS entry for newer version with native `systemd` integration.

```
systemctl --no-ask-password start <SAPRHX_00> # sapstartsrv pf=/usr/sap/<RHX>/SYS/profile/<RHX>_ASCS<00>_<rhxascs>
```

To ensure that SAP instance can be managed by the cluster and also manually during planned maintenance activities, add the missing entries for ASCS and ERS `sapstartsrv` service in `/usr/sap/sapservices` file on both cluster nodes (ASCS and ERS host). Copy the missing entry from both hosts. Post-modifications, the `/usr/sap/sapservices` file looks as follows on both hosts.

```
#!/bin/sh
systemctl --no-ask-password start <SAPRHX_00> # sapstartsrv pf=/usr/sap/<RHX>/SYS/profile/<RHX>_ASCS<00>_<rhxascs>

systemctl --no-ask-password start <SAPRHX_10> # sapstartsrv pf=/usr/sap/<RHX>/SYS/profile/<RHX>_ERS<10>_<rhxers>
```

### Align and disable SAP auto start services for `systemd`

This is applicable to both cluster nodes. For `systemd`, ensure SAP auto start services are aligned and disabled across nodes. If the installed version supports native integration with `systemd`, you must create services for ASCS and ERS on both nodes. This ensures that if you have revert to manual operations, there is no association and that both nodes are configured in the same manner.

You must disable auto start services to enable the cluster to manage stop/start.

**ASCS**

Register the missing ERS service on the node where you have installed ASCS.

Temporarily mount the ERS directory.

```
mount <nfs.fqdn>:/<RHX>_ERS<10>  /usr/sap/<RHX>/ERS

```

Register the ERS service.

```
export LD_LIBRARY_PATH=/usr/sap/<RHX>/ERS<10>/exe
/usr/sap/<RHX>/ERS<10>/exe/sapstartsrv pf=/usr/sap/<RHX>/SYS/profile/<RHX>_ERS<10>_<rhxers> -reg

systemctl start <SAPRHX_10>
```

Check the existence and state of SAP services.

```
systemctl list-unit-files SAP*
UNIT FILESTATE VENDOR PRESET
<SAPRHX_00>.service disabled disabled
<SAPRHX_10>.service disabled disabled
SAP.slicestatic -
3 unit files listed.
```

If the state is not disabled, run the following command to disable `sapservices` integration for `SAP<SID>_<ascs_sys_nr>` and `SAP<SID>_<ers_sys_nr>` on both nodes.

###### Important

Stopping these services also stops the associated SAP instances.

```
systemctl stop <SAPRHX_00>.service
systemctl disable <SAPRHX_00>.service
systemctl stop <SAPRHX_10>.service
systemctl disable <SAPRHX_10>.service
```

Unmount the ERS directory (classic only).

```
umount /usr/sap/<RHX>/ERS

```

**ERS**

Register the missing ASCS service on the node where you have installed ERS.

Temporarily mount the ASCS directory (classic only).

```
mount <nfs.fqdn>:/<RHX>_ASCS<00>  /usr/sap/<RHX>/ASCS

```

Register the ASCS service.

```
export LD_LIBRARY_PATH=/usr/sap/<RHX>/ASCS<00>/exe
/usr/sap/<RHX>/ASCS<00>/exe/sapstartsrv pf=/usr/sap/<RHX>/SYS/profile/<RHX>_ASCS<00>_<rhxascs> -reg
systemctl start <SAPRHX_00>
```

Check the existence and state of SAP services.

```
systemctl list-unit-files SAP*
UNIT FILESTATE VENDOR PRESET
<SAPRHX_00>.service disabled disabled
<SAPRHX_10>.service disabled disabled
SAP.slicestatic -
3 unit files listed.
```

If the state is not disabled, run the following command to disable `sapservices` integration for `SAP<SID>_<ascs_sys_nr>` and `SAP<SID>_<ers_sys_nr>` on both nodes.

###### Important

Stopping these services also stops the associated SAP instances.

```
systemctl stop <SAPRHX_00>.service
systemctl disable <SAPRHX_00>.service
systemctl stop <SAPRHX_10>.service
systemctl disable <SAPRHX_10>.service
```

Unmount the ASCS directory (classic only).

```
umount /usr/sap/<RHX>/ASCS

```

For more details, see [SAP Note 3139184 – Linux: systemd integration for sapstartsrv and SAP Host Agent](https://launchpad.support.sap.com/#/notes/3139184 "https://launchpad.support.sap.com/#/notes/3139184").

## Cluster prerequisites

This section covers the following topics.

###### Topics

- [Configure systemd for resource dependencies](#configure-systemd "#configure-systemd")
- [Configure drop-in files for systemd](#configure-drop-in "#configure-drop-in")
- [Update the hacluster password](#update-hacluster "#update-hacluster")
- [Setup passwordless authentication between nodes](#setup-authentication "#setup-authentication")

### Configure `systemd` for resource dependencies

This is applicable to both cluster nodes. Some failure scenarios, such as an accidental shutdown of an Amazon EC2 instance, can result in unexpected fencing actions. This is caused by pacemaker dependencies that are not directly associated with cluster resources and constraints, but instead are a dependency for the pacemaker service.

If `systemd` is configured, create a config file that defines a dependency between pacemaker and SAP services.

```
mkdir -p /etc/systemd/system/resource-agents-deps.target.d/
cd /etc/systemd/system/resource-agents-deps.target.d/

cat > sap_systemd_<rhx>.conf <<_EOF
[Unit]
Requires=sapinit.service
After=sapinit.service
After=<SAPRHX_00>.service
After=<SAPRHX_10>.service
_EOF


systemctl daemon-reload
```

### Configure drop-in files for `systemd`

`systemd` has an inbuilt mechanism to restart a crashed service in a running system. In a cluster-controlled environment, it is recommended to prevent this from getting triggered, so that the cluster can completely manage the respective instances.

This is applicable on both cluster nodes. To prevent the automatic restart of crashed `systemd` based SAP service, create the drop-in files.

```
mkdir -p /etc/systemd/system/<SAPRHX_00>.service.d/
mkdir -p /etc/systemd/system/<SAPRHX_10>.service.d/

cd /etc/systemd/system/<SAPRHX_00>.service.d/

cat > HA.conf <<_EOF
[Service]
Restart=no
_EOF

cd /etc/systemd/system/<SAPRHX_10>.service.d/

cat > HA.conf <<_EOF
[Service]
Restart=no
_EOF

systemctl daemon-reload
```

### Update the `hacluster` password

This is applicable to both cluster nodes. Change the password of the operating system user `hacluster` using the following command.

```
passwd <hacluster>
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

This is applicable on both clsuter nodes. Run the following command to enable and start the cluster service `pcsd` (pacemaker/corosync configuration system daemon) on both, the primary and secondary node.

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

The following command authenticates `pcs` to the `pcs daemon` on cluster nodes. It should be run on only one of the cluster nodes. The username and password for the `pcs` user must be the same, and the username should be `hacluster`.

**RHEL 7.x**

```
pcs cluster auth <rhxhost01> <rhxhost02>
Username: <hacluster>
Password:
<rhxhost02>: Authorized
<rhxhost01>: Authorized
```

**RHEL 8.x**

```
pcs host auth <rhxhost01> <rhxhost02>
Username: <hacluster>
Password:
<rhxhost02>: Authorized
<rhxhost01>: Authorized
```

### Setup node configuration

The following command configures the `cluster configuration` file, and syncs the configuration on both nodes. It should be run on only one of the cluster nodes.

**RHEL 7.x**

```
pcs cluster setup --name <rhelha> <rhxhost01> <rhxhost02>
Destroying cluster on nodes: <rhxhost01>, <rhxhost02>...
<rhxhost02>: Stopping Cluster (pacemaker)...
<rhxhost01>: Stopping Cluster (pacemaker)...
<rhxhost02>: Successfully destroyed cluster
<rhxhost01>: Successfully destroyed cluster

Sending 'pacemaker_remote authkey' to '<rhxhost01>', '<rhxhost02>'
<rhxhost01>: successful distribution of the file 'pacemaker_remote authkey'
<rhxhost02>: successful distribution of the file 'pacemaker_remote authkey'
Sending cluster config files to the nodes...
<rhxhost01>: Succeeded
<rhxhost02>: Succeeded

Synchronizing pcsd certificates on nodes <rhxhost01>, <rhxhost02>...
<rhxhost01>: Success
<rhxhost02>: Success
Restarting pcsd on the nodes in order to reload the certificates...
<rhxhost01>: Success
<rhxhost02>: Success.
```

**RHEL 8.x**

```
#pcs cluster setup <rhelha> <rhxhost01> <rhxhost02>
No addresses specified for host '<rhxhost01>', using '<rhxhost01>'
No addresses specified for host '<rhxhost02>', using '<rhxhost02>'
Destroying cluster on hosts: '<rhxhost01>', '<rhxhost02>'...
<rhxhost01>: Successfully destroyed cluster
<rhxhost02>: Successfully destroyed cluster
Requesting remove 'pcsd settings' from '<rhxhost01>', '<rhxhost02>'
<rhxhost01>: successful removal of the file 'pcsd settings'
<rhxhost02>: successful removal of the file 'pcsd settings'
Sending 'corosync authkey', 'pacemaker authkey' to '<rhxhost01>', '<rhxhost02>'
<rhxhost01>: successful distribution of the file 'corosync authkey'
<rhxhost01>: successful distribution of the file 'pacemaker authkey'
<rhxhost02>: successful distribution of the file 'corosync authkey'
<rhxhost02>: successful distribution of the file 'pacemaker authkey'
Sending 'corosync.conf' to '<rhxhost01>', '<rhxhost02>'
<rhxhost01>: successful distribution of the file 'corosync.conf'
<rhxhost02>: successful distribution of the file 'corosync.conf'
Cluster has been successfully set up.
```
