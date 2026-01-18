# SAP HANA Service Control

Modify how SAP HANA services are managed to enable cluster takeover and operation.

###### Topics

- [Add sidadm to haclient Group](#_add_sidadm_to_haclient_group "#_add_sidadm_to_haclient_group")
- [Modify SAP Profile for HANA](#_modify_sap_profile_for_hana "#_modify_sap_profile_for_hana")
- [Configure SAPHanaSR Cluster Hook for Optimized Cluster Response](#hook_saphanasr "#hook_saphanasr")
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
 # rpm -qa resource-agents-sap-hana
```

SAPHanaSR-angi
Check the expected package is installed

```
 # rpm -qa sap-hana-ha
```

2. **Confirm Hook Location**

By default the package is installed in `/usr/share/sap-hana-ha/` or `/usr/share/SAPHanaSR/srHook`. We suggest using the default location but optionally you can copy it to a custom directory; for example, `/hana/share/myHooks`. The hook must be available on all SAP HANA cluster nodes. 3. **Configure global.ini**

Update the `global.ini` file located at `/hana/shared/<SID>/global/hdb/custom/config/` on each SAP HANA cluster node. Make a backup copy before proceeding.

SAPHanaSR

```
 [ha_dr_provider_SAPHanaSR]
provider = SAPHanaSR
path = /usr/share/SAPHanaSR/srHook
execution_order = 1

[trace]
ha_dr_saphanasr = info
```

###### Note

Update the path if you have modified the package location.

sap-hana-ha (newer agent)

```
 [ha_dr_provider_sushanasr]
provider = HanaSR
path = /usr/share/sap-hana-ha/
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
    hdbadm ALL=(ALL) NOPASSWD: SITE_SOK, SITE_SFAIL, HOOK_HELPER
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

## (Optional) Configure Fast Start Option

Although out of scope of this document, the SAP HANA Fast Restart option uses tmpfs file systems to preserve and reuse MAIN data fragments to speed up SAP HANA restarts. This is effective in cases where the operating system is not restarted including local restarts of the Index Server.

Fast Start Option may be an alternative to the susChkSrv hook.

For more information, see SAP Documentation: [SAP HANA Fast Restart Option](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ce158d28135147f099b761f8b1ee43fc.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ce158d28135147f099b761f8b1ee43fc.html")

## Review systemd Integration

Review HANA version and systemd version to determine whether the prerequisites for systemd are available:

```
 sidadm> systemctl --version
```

###### OS versions

- Red Hat Enterprise Linux 8 (systemd version 239)

###### SAP HANA Revisions

- SAP HANA SPS07 revision 70

When using an SAP HANA version with systemd integration (SPS07 and later), you must run the following steps to prevent the nodes from being fenced when Amazon EC2 instances are intentionally stopped.
See Note [3189534 - Linux: systemd integration for sapstartsrv and SAP HANA](https://me.sap.com/notes/3189534 "https://me.sap.com/notes/3189534")

1. Verify if SAP HANA is integrated with systemd. If it is integrated, a systemd service name, such as SAP<SID>\_<hana_sys_nr>.service is present. For example, for SID HDB and instance number 00, SAPHDB_00.service is the service name.

Use the following command as root to find SAP systemd services:

```
 # systemctl list-unit-files | grep -i sap
```

2. Create a pacemaker service drop-in file:

```
 # mkdir -p /etc/systemd/system/pacemaker.service.d/
```

3. Create the file `/etc/systemd/system/pacemaker.service.d/50-saphana.conf` with the following content:

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
