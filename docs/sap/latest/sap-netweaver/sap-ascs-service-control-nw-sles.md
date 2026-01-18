# Configure SAP for Cluster Control

Modify SAP service configurations, user permissions, and system integration settings to enable proper cluster control of ASCS and ERS instances.

###### Topics

- [Add <sid>adm to haclient group](#add-sidadm-haclient-nw-sles "#add-sidadm-haclient-nw-sles")
- [Modify SAP profiles for start operations and cluster hook](#modify-sap-profiles-nw-sles "#modify-sap-profiles-nw-sles")
- [Enable sapping and sappong Services (Simple-Mount Only)](#sapping-sappong-services-nw-sles "#sapping-sappong-services-nw-sles")
- [Ensure ASCS and ERS SAP Services can run on either node (systemd)](#modify-sapservices-nw-sles "#modify-sapservices-nw-sles")
- [Configure dependencies for Pacemaker and SAP services (systemd)](#configure-systemd-deps-nw-sles "#configure-systemd-deps-nw-sles")
- [(Alternative) Ensure ASCS and ERS SAP Services can run on either node (sysV)](#modify-sapservices-sysv-nw-sles "#modify-sapservices-sysv-nw-sles")

## Add <sid>adm to haclient group

This is applicable to both cluster nodes. An `haclient` operating system group is created when the cluster connector package is installed. Adding the `<sid>adm` user to this group ensures that your cluster has necessary access. Run the following command as root:

```
 # usermod -a -G haclient <sid>adm
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
 # usermod -a -G haclient slxadm
```

## Modify SAP profiles for start operations and cluster hook

This action ensures that there is compatibility between the SAP start framework and cluster actions. Modify SAP profiles to change the start behavior of the SAP instance and processes. Ensure that `sapcontrol` is aware that the system is being managed by a pacemaker cluster.

- ASCS profile – `/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>`
- ERS profile – `/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>`

The profile directory /usr/sap/<SID>/SYS/profile/ is typically a symbolic link to /sapmnt/<SID>/profile/ on the shared NFS filesystem. This
means profile modifications made on one node are immediately visible on all cluster nodes. You can modify the profiles from either node.

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:
  - ASCS profile example – `/usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs`
  - ERS profile example – `/usr/sap/SLX/SYS/profile/SLX_ERS10_slxers`

Follow the procedure outlined below to make the necessary changes:

1. **Program or process start behavior** – In case of failure, processes must be restarted. Determining where the process starts and in what order needs to be controlled by the cluster, and not SAP start framework behavior defined in the profiles. Your locks can be lost if this parameter is not changed. In newer SAP installations, the profiles may already contain `Start_Program_XX` instead of `Restart_Program_XX`. If `Start_Program_XX` is already present, no changes are needed for this step.

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

_`XX` indicates the start-up order. This value may be different in your install; retain the unchanged value._

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

_`XX` indicates the start order. This value may be different in your install; retain the unchanged value._ 2. **Disable instance auto start in both profiles** – When an instance restarts, SAP start framework should not start ASCS and ERS automatically. Add the following parameter on both profiles to prevent an auto start:

```
 # Disable instance auto start
Autostart = 0
```

3. **Add cluster connector details in both profiles** – The connector integrates the SAP start and control frameworks of SAP NetWeaver with SUSE cluster to assist with maintenance and awareness of state. Add the following parameters on both profiles:

```
 # Added for Cluster Connectivity
service/halib = $(DIR_EXECUTABLE)/saphascriptco.so
service/halib_cluster_connector = /usr/bin/sap_suse_cluster_connector
```

###### Important

RPM package `sap-suse-cluster-connector` has _dashes_. The executable `/usr/bin/sap_suse_cluster_connector` available after installation has _underscores_. Ensure that the correct name, that is executable `/usr/bin/sap_suse_cluster_connector`, is used in both profiles. 4. **Restart services** – Restart SAP services for ASCS and ERS to ensure that the preceding settings take effect. Adjust the system number to match the service.

**ASCS**

```
 # /usr/sap/hostctrl/exe/sapcontrol -nr <ascs_sys_nr> -function RestartService
```

**ERS**

```
 # /usr/sap/hostctrl/exe/sapcontrol -nr <ers_sys_nr> -function RestartService
```

    * *Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")*:



    **ASCS**




    ```
     # /usr/sap/hostctrl/exe/sapcontrol -nr 00 -function RestartService
    ```


    **ERS**




    ```
     # /usr/sap/hostctrl/exe/sapcontrol -nr 10 -function RestartService
    ```

5. **Check integration using `sapcontrol`** – `sapcontrol` includes functions: `HACheckConfig` and `HACheckFailoverConfig`. These functions can be used to check configuration, including awareness of the cluster connector.
   These checks have limited value before the cluster is configured, but you can run HACheckFailoverConfig to ensure the base configuration is in place.

**ASCS**

```
 # /usr/sap/hostctrl/exe/sapcontrol -nr <ascs_sys_nr> -function HACheckFailoverConfig
```

    * *Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")*:



    **ASCS**




    ```
     # /usr/sap/hostctrl/exe/sapcontrol -nr 00 -function HACheckFailoverConfig

    10.10.2025 01:23:55
    HACheckFailoverConfig
    OK
    state, category, description, comment
    SUCCESS, SAP CONFIGURATION, SAPInstance RA sufficient version, SAPInstance includes is-ers patch
    ```

## Enable sapping and sappong Services (Simple-Mount Only)

For simple-mount architecture, enable the sapping and sappong systemd services on both cluster nodes. These services ensure proper SAP instance startup coordination between systemd and the cluster.

The sapping service runs before sapinit during boot and temporarily hides the `/usr/sap/sapservices` file to prevent automatic SAP instance startup. The sappong service runs after sapinit and restores the sapservices file, making it available for cluster management while maintaining compatibility with SAP management tools.

```
 # systemctl enable sapping
# systemctl enable sappong
```

Verify the services are enabled:

```
 # systemctl status sapping
# systemctl status sappong
```

###### Note

Both services will show "inactive (dead)" status, which is normal for one-shot services that only run during system boot.

## Ensure ASCS and ERS SAP Services can run on either node (systemd)

This is applicable to both cluster nodes.

To ensure that the cluster can orchestrate availability by starting and stopping instances on either cluster node, the SAP Services must be registerd on both nodes and auto-start should be disabled.

In recent Operating System and SAP kernel versions, SAP offers systemd integration for sapstartsrv which controls how SAP instances are stopped and started. This is the recommended configuration and a requirement for Simple Mount Configuration.

For more details, see the following SAP Notes (require SAP portal access):

- [SAP Note 3139184 – Linux: systemd integration for sapstartsrv and SAP Host Agent](https://me.sap.com/notes/3139184 "https://me.sap.com/notes/3139184")
- [SAP Note 3115048 – sapstartsrv with native Linux systemd support](https://me.sap.com/notes/3115048 "https://me.sap.com/notes/3115048")

You can confirm whether systemd is in place by running the following command. Systemd is in place if SAP Services (e.g., SAPSLX_00.service, SAPSLX_10.service) are listed.

```
 # systemctl list-unit-files SAP*
```

If you have installed an ASCS or ERS on this host but no SAP Services are returned, the classic SysV init may be in use. In that case you can skip to section [(Alternative) Ensure ASCS and ERS SAP Services can run on either node (sysV)](#modify-sapservices-sysv-nw-sles "#modify-sapservices-sysv-nw-sles")

1. **On the instance where the ASCS was installed**

Register the missing ERS service on the node where you have installed ASCS.

    1. Temporarily mount the ERS directory (classic only):



    ```
     # mount <nfs.fqdn>:/<SID>_ERS<ers_sys_nr>  /usr/sap/<SID>/ERS<ers_sys_nr>
    ```
    2. Register the ERS service:



    ```
     # export LD_LIBRARY_PATH=/usr/sap/<SID>/ERS<ers_sys_nr>/exe
    # /usr/sap/<SID>/ERS<ers_sys_nr>/exe/sapstartsrv pf=/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname> -reg
    # systemctl start SAP<SID>_<ers_sys_nr>
    ```
    3. Check the existence and state of SAP services (example):



    ```
     # systemctl list-unit-files SAP*
    UNIT FILE                    STATE   VENDOR PRESET
    SAPSLX.service            disabled disabled
    SAPSLX.service            disabled disabled
    SAP.slice                   static   -
    3 unit files listed.
    ```
    4. If the state is not disabled, run the following command to disable `sapservices` integration for `SAP<SID>_<ascs_sys_nr>` and `SAP<SID>_<ers_sys_nr>` on both nodes:


    ###### Important

    Stopping these services also stops the associated SAP instances.



    ```
     # systemctl stop SAP<SID>_<ascs_sys_nr>.service
    # systemctl disable SAP<SID>_<ascs_sys_nr>.service
    # systemctl stop SAP<SID>_<ers_sys_nr>.service
    # systemctl disable SAP<SID>_<ers_sys_nr>.service
    ```
    5. Unmount the ERS directory (classic only):



    ```
     # umount /usr/sap/<SID>/ERS<ers_sys_nr>
    ```



    	* *Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")*:



    	```
    	 # mount <nfs.fqdn>:/SLX_ERS10  /usr/sap/SLX/ERS10
    	# export LD_LIBRARY_PATH=/usr/sap/SLX/ERS10/exe
    	# /usr/sap/SLX/ERS10/exe/sapstartsrv pf=/usr/sap/SLX/SYS/profile/SLX_ERS10_slxers -reg
    	# systemctl start SAPSLX_10
    	# systemctl stop SAPSLX_00.service
    	# systemctl disable SAPSLX_00.service
    	# systemctl stop SAPSLX_10.service
    	# systemctl disable SAPSLX_10.service
    	# umount /usr/sap/SLX/ERS10
    	```

2. **On the instance where the ERS was installed**

Register the missing ASCS service on the node where you have installed ERS.

    1. Temporarily mount the ASCS directory (classic only):



    ```
     # mount <nfs.fqdn>:/<SID>_ASCS<ascs_sys_nr> /usr/sap/<SID>/ASCS<ascs_sys_nr>
    ```
    2. Register the ASCS service:



    ```
     # export LD_LIBRARY_PATH=/usr/sap/<SID>/ASCS<ascs_sys_nr>/exe
    # /usr/sap/<SID>/ASCS<ascs_sys_nr>/exe/sapstartsrv pf=/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname> -reg
    # systemctl start SAP<SID>_<ascs_sys_nr>
    ```
    3. Check the existence and state of SAP services (example):



    ```
     # systemctl list-unit-files SAP*
    UNIT FILE                    STATE   VENDOR PRESET
    SAPSLX00.service           disabled disabled
    SAPSLX00.service           disabled disabled
    SAP.slice                   static   -
    3 unit files listed.
    ```
    4. If the state is not disabled, run the following command to disable `sapservices` integration for `SAP<SID>_<ascs_sys_nr>` and `SAP<SID>_<ers_sys_nr>` on both nodes:


    ###### Important

    Stopping these services also stops the associated SAP instances.



    ```
     # systemctl stop SAP<SID>_<ascs_sys_nr>.service
    # systemctl disable SAP<SID>_<ascs_sys_nr>.service
    # systemctl stop SAP<SID>_<ers_sys_nr>.service
    # systemctl disable SAP<SID>_<ers_sys_nr>.service
    ```
    5. Unmount the ASCS directory (classic only):



    ```
     # umount /usr/sap/<SID>/ASCS<ascs_sys_nr>
    ```



    	* *Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")*:



    	```
    	 # mount <nfs.fqdn>:/SLX_ASCS00 /usr/sap/SLX/ASCS00
    	# export LD_LIBRARY_PATH=/usr/sap/SLX/ASCS00/exe
    	# /usr/sap/SLX/ASCS00/exe/sapstartsrv pf=/usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs -reg
    	# systemctl start SAPSLX_00
    	# systemctl stop SAPSLX_00.service
    	# systemctl disable SAPSLX_00.service
    	# systemctl stop SAPSLX_10.service
    	# systemctl disable SAPSLX_10.service
    	# umount /usr/sap/SLX/ASCS00
    	```

## Configure dependencies for Pacemaker and SAP services (systemd)

This step is required on both cluster nodes when using systemd integration.

When an EC2 instance shuts down unexpectedly, Pacemaker (the cluster resource manager) may trigger unnecessary fencing actions because it cannot distinguish between planned SAP service shutdowns and system failures. To prevent this, configure systemd dependencies that inform Pacemaker about the relationship between SAP services and cluster operations.

Create a systemd drop-in configuration for the `resource-agents-deps.target`, which is a systemd target that Pacemaker uses to understand external service dependencies:

```
 # mkdir -p /etc/systemd/system/resource-agents-deps.target.d/
# cd /etc/systemd/system/resource-agents-deps.target.d/

# cat > sap_systemd_<sid>.conf <<_EOF
[Unit]
Requires=sapinit.service
After=sapinit.service
After=SAP<SID>_<ascs_sys_nr>.service
After=SAP<SID>_<ers_sys_nr>.service
_EOF

# systemctl daemon-reload
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
 # cat > sap_systemd_slx.conf <<_EOF
[Unit]
Requires=sapinit.service
After=sapinit.service
After=SAPSLX_00.service
After=SAPSLX_10.service
_EOF

# systemctl daemon-reload
```

## (Alternative) Ensure ASCS and ERS SAP Services can run on either node (sysV)

This is only applicable for if systemd integration is not in place.

To ensure that SAP instance can be managed by the cluster and also manually during planned maintenance activities, add the missing entries for ASCS and ERS `sapstartsrv` service in `/usr/sap/sapservices` file on both cluster nodes (ASCS and ERS host). Copy the missing entry from both hosts. Post-modifications, the `/usr/sap/sapservices` file looks as follows on both hosts:

```
 #!/bin/sh
LD_LIBRARY_PATH=/usr/sap/<SID>/ASCS<ascs_sys_nr>/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/<SID>/ASCS<ascs_sys_nr>/exe/sapstartsrv pf=/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname> -D -u <sid>adm
LD_LIBRARY_PATH=/usr/sap/<SID>/ERS<ers_sys_nr>/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/<SID>/ERS<ers_sys_nr>/exe/sapstartsrv pf=/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname> -D -u <sid>adm
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
 #!/bin/sh
LD_LIBRARY_PATH=/usr/sap/SLX/ASCS00/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/SLX/ASCS00/exe/sapstartsrv pf=/usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs -D -u slxadm
LD_LIBRARY_PATH=/usr/sap/SLX/ERS10/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/SLX/ERS10/exe/sapstartsrv pf=/usr/sap/SLX/SYS/profile/SLX_ERS10_slxers -D -u slxadm
```
