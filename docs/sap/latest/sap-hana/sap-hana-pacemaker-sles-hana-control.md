# SAP HANA Service Control

Modify how SAP HANA services are managed to enable cluster takeover and operation.

###### Topics

- [Add sidadm to haclient Group](#_add_sidadm_to_haclient_group "#_add_sidadm_to_haclient_group")
- [Modify SAP Profile for HANA](#_modify_sap_profile_for_hana "#_modify_sap_profile_for_hana")
- [Configure SAPHanaSR Cluster Hook for Optimized Cluster Response](#hook_saphanasr "#hook_saphanasr")
- [Configure susTkOver Cluster Hook to Ensure Cluster Awareness of Manual Takeover](#hook_sustkover "#hook_sustkover")
- [(Optional) Configure susChkSrv Cluster Hook (Fast Dying Index Server)](#hook_suschksrv "#hook_suschksrv")
- [(Optional) Configure Fast Start Option](#_optional_configure_fast_start_option "#_optional_configure_fast_start_option")
- [Review systemd Integration](#_review_systemd_integration "#_review_systemd_integration")

## Add sidadm to haclient Group

The pacemaker software creates a haclient operating system group. To ensure proper cluster access permissions, add the sidadm user to this group on all cluster nodes. Run the following command as root:

```
 # usermod -a -G haclient hdbadm
```

## Modify SAP Profile for HANA

To prevent automatic SAP HANA startup by the SAP start framework when an instance restarts, modify the SAP HANA instance profiles on all nodes. These profiles are located at `/usr/sap/<SID>/SYS/profile/`.

As <sid>adm, edit the SAP HANA profile `<SID>_HDB<hana_sys_nr>_<hostname>` and modify or add the Autostart parameter, ensuring it is set to 0:

```
 Autostart = 0
```

## Configure SAPHanaSR Cluster Hook for Optimized Cluster Response

The SAPHanaSR hook provides immediate notification to the cluster if system replication fails, complementing the standard cluster polling mechanism. This optimization can significantly improve failover response time.

Follow these steps to configure the SAPHanaSR hook:

1. **Verify Cluster Package**

The hook configuration varies based on the resource agents in use (see [Deployment Guidance](sap-hana-pacemaker-rhel-references.md#deployments-rhel "sap-hana-pacemaker-rhel-references.md#deployments-rhel") for details).

SAPHanaSR
Check the expected package is installed

```
 # rpm -qa SAPHanaSR
```

Review the man pages for more details.

```
 # man SAPHanaSR
# man SAPHanaSR.py
```

SAPHanaSR-angi
Check the expected package is installed

```
 # rpm -qa SAPHanaSR-angi
```

Review the man pages for more details

```
 # man SAPHanaSR-angi
# man SAPHanaSR.py
```

2. **Confirm Hook Location**

By default the package is installed in `/usr/share/SAPHanaSR-angi` or `/usr/share/SAPHanaSR`. We suggest using the default location but optionally you can copy it to a custom directory; for example, `/hana/share/myHooks`. The hook must be available on all SAP HANA cluster nodes. 3. **Configure global.ini**

Update the `global.ini` file located at `/hana/shared/<SID>/global/hdb/custom/config/` on each SAP HANA cluster node. Make a backup copy before proceeding.

SAPHanaSR

```
 [ha_dr_provider_SAPHanaSR]
provider = SAPHanaSR
path = /usr/share/SAPHanaSR
execution_order = 1

[trace]
ha_dr_saphanasr = info
```

###### Note

Update the path if you have modified the package location.

SAPHanaSR-angi

```
 [ha_dr_provider_sushanasr]
provider = susHanaSR
path = /usr/share/SAPHanaSR-angi
execution_order = 1

[trace]
ha_dr_sushanasr = info
```

###### Note

Update the path if you have modified the package location. 4. **Configure Sudo Privileges**

The SAPHanaSR Python hook requires sudo privileges for the <sid>adm user to access cluster attributes:

    1. Create a new sudoers file as root user in `/etc/sudoers.d/`, for example `60-SAPHanaSR-hook`
    2. Use visudo to safely edit the new file `visudo /etc/sudoers.d/60-SAPHanaSR-hook`
    3. Add the following configuration, replacing <sid> with lowercase system ID and <SID> with uppercase system ID:



    ```
     Cmnd_Alias SITE_SOK = /usr/sbin/crm_attribute -n hana_<sid>_site_srHook_[a-zA-Z0-9_]* -v SOK -t crm_config -s SAPHanaSR
    Cmnd_Alias SITE_SFAIL = /usr/sbin/crm_attribute -n hana_<sid>_site_srHook_[a-zA-Z0-9_]* -v SFAIL -t crm_config -s SAPHanaSR
    Cmnd_Alias HOOK_HELPER  = /usr/sbin/SAPHanaSR-hookHelper --sid=<SID> --case=checkTakeover
    <sid>adm ALL=(ALL) NOPASSWD: SITE_SOK, SITE_SFAIL, HOOK_HELPER
    ```

    For example:



    ```
     Cmnd_Alias SITE_SOK = /usr/sbin/crm_attribute -n hana_hdb_site_srHook_[a-zA-Z0-9_]* -v SOK -t crm_config -s SAPHanaSR
    Cmnd_Alias SITE_SFAIL = /usr/sbin/crm_attribute -n hana_hdb_site_srHook_[a-zA-Z0-9_]* -v SFAIL -t crm_config -s SAPHanaSR
    Cmnd_Alias HOOK_HELPER  = /usr/sbin/SAPHanaSR-hookHelper --sid=HDB --case=checkTakeover
    hdbadm ALL=(ALL) NOPASSWD: SITE_SOK, SITE_SFAIL, HOOK_HELPER
    ```

    ###### Note

    The syntax uses a glob expression which allows it to adapt to different HSR site names whilst avoiding the use of wild cards. This ensures flexibility and security. A modification is still required if the SID changes. Replace the `<sid>` with a lowercase `sid` and `<SID>` with an uppercase `SID` which matches your installation.

5. **Reload Configuration**

As <sid>adm reload the changes to `global.ini` using either a HANA restart or the command:

```
 hdbadm> hdbnsutil -reconfig
```

6. **Verify Hook Configuration**

As <sid>adm, verify the hook is loaded:

```
 hdbadm> cdtrace
hdbadm> grep "loading HA/DR Provider" nameserver*
```

7. **Replicate Configuration to Secondary**
   1. Confirm that global.ini changes have been replicated to the secondary system
   2. Create corresponding sudoers.d file on the secondary system

## Configure susTkOver Cluster Hook to Ensure Cluster Awareness of Manual Takeover

susTkOver.py prevents a manual takeover of the HANA primary if the SAP HANA multi-state resource (managed by SAPHana or SAPHanaController) is active, unless the cluster is set into maintenance mode or the Linux cluster is stopped.

For more details:

```
 # man susTkOver.py
```

In addition to the steps for the previous hook, add an additional entry in the global.ini on each node. It is necessary to restart Hana:

```
 [ha_dr_provider_susTkOver]
provider = susTkOver
path = /usr/share/SAPHanaSR
execution_order = 2
sustkover_timeout = 30

[trace]
ha_dr_sustkover = info
```

## (Optional) Configure susChkSrv Cluster Hook (Fast Dying Index Server)

In the default configuration, a failure of the SAP HANA IndexServer will result in the process being restarted locally even when protected by a cluster. The time taken to stop the process and reload the memory can impact both the Recovery Time Objective (RTO) and performance. The SAP HANA hook susChksrv provides an option to trigger an action, such as a fencing or shutdown based on the HA/DR provider hook method srServiceStateChanged(), which in turn will trigger a failover.

###### Important

As this hook can be configured using several different options. We suggest consulting the man page or SUSE documentation, and evaluating the best option for your setup.

```
 # man susChksrv.py
```

Test the scenario with a Production Sized system to assess whether the time to resume operations aligns with your non functional requirements.

For more information, see SUSE Blog: [Emergency Braking for SAP HANA Dying Index Server](https://www.suse.com/c/emergency-braking-for-sap-hana-dying-indexserver/ "https://www.suse.com/c/emergency-braking-for-sap-hana-dying-indexserver/")

## (Optional) Configure Fast Start Option

Although out of scope of this document, the SAP HANA Fast Restart option uses tmpfs file systems to preserve and reuse MAIN data fragments to speed up SAP HANA restarts. This is effective in cases where the operating system is not restarted including local restarts of the Index Server.

Fast Start Option may be an alternative to the susChkSrv hook.

For more information, see SAP Documentation: [SAP HANA Fast Restart Option](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ce158d28135147f099b761f8b1ee43fc.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ce158d28135147f099b761f8b1ee43fc.html")

## Review systemd Integration

Review SAP HANA version and systemd version to determine whether the prerequisites for systemd are available:

```
 sidadm> systemctl --version
```

###### Operating System versions

- SUSE Linux Enterprise Server 15 (systemd version 234)

###### SAP HANA Revisions

- SAP HANA SPS07 revision 70

When using an SAP HANA version with systemd integration (SPS07 and later), you must run the following steps to prevent the nodes from being fenced when Amazon EC2 instances are intentionally stopped.
See Note [3189534 - Linux: systemd integration for sapstartsrv and SAP HANA](https://me.sap.com/notes/3189534 "https://me.sap.com/notes/3189534")

1. Verify if SAP HANA is integrated with systemd. If it is integrated, a systemd service name, such as `SAP<SID>_<hana_sys_nr>.service` is present. For example, for SID HDB and instance number 00, `SAPHDB_00.service` is the service name.

Use the following command as root to find SAP systemd services:

```
 # systemctl list-unit-files | grep -i sap
```

2. Create a pacemaker service drop-in file:

```
 # mkdir -p /etc/systemd/system/pacemaker.service.d/
```

3. Create the file /etc/systemd/system/pacemaker.service.d/50-saphana.conf with the following content:

```
 [Unit]
Description=pacemaker needs SAP instance service
Documentation=man:SAPHanaSR_basic_cluster(7)
Wants=SAP<SID>_<hana_sys_nr>.service
After=SAP<SID>_<hana_sys_nr>.service
```

4. Enable the drop-in file by reloading systemd:

```
 # systemctl daemon-reload
```

5. Verify that the change is active:

```
 # systemctl show pacemaker.service | grep SAP<SID>_<hana_sys_nr>
```

For example, for SID HDB and instance number 00, the following output is expected:

```
# systemctl show pacemaker.service | grep SAPHDB_00
Wants=SAPHDB_00.service resource-agents-deps.target dbus.service
After=system.slice network.target corosync.service resource-agents-deps.target basic.target rsyslog.service SAPHDB_00.service systemd-journald.socket sysinit.target time-sync.target dbus.service sbd.service
```
