# SAP HANA Setup and HSR

Prepare SAP HANA for System Replication (HSR) by configuring parameters and creating required backups.

###### Topics

- [Review AWS and SAP Installation Guides](#review_guides "#review_guides")
- [Check global.ini parameters](#global_ini "#global_ini")
- [Create a SAP HANA Backup on the Primary System](#pre_setup_backup "#pre_setup_backup")
- [Configure System Replication on Primary and Secondary Systems](#register_hsr "#register_hsr")
- [Check SAP Host Agent Version](#sap_host_agent "#sap_host_agent")

###### Important

This guide assumes that SAP HANA Platform has been installed either as a scale-up configuration with two EC2 instances in different availability zones, or as a scale-out configuration with multiple EC2 instances in two availability zones, following the guidance from AWS and SAP.

## Review AWS and SAP Installation Guides

- AWS Documentation - [SAP HANA Environment Setup on AWS](std-sap-hana-environment-setup.md "std-sap-hana-environment-setup.md")
- SAP Documentation - [SAP HANA Server Installation and Update Guide](https://help.sap.com/docs/SAP_HANA_PLATFORM/2c1988d620e04368aa4103bf26f17727/7eb0167eb35e4e2885415205b8383584.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/2c1988d620e04368aa4103bf26f17727/7eb0167eb35e4e2885415205b8383584.html")

SAP provides documentation on how to configure SAP HANA System Replication using the SAP HANA Cockpit, SAP HANA Studio or `hdbnsutil` on the command line.
Review the documentation for your SAP HANA Version to ensure no changes to the guidance or to use a method other than command line.

- SAP Documentation: [Configuring SAP HANA System Replication](https://help.sap.com/docs/SAP_HANA_PLATFORM/4e9b18c116aa42fc84c7dbfd02111aba/442bf027937746248f69701aa9b94112.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/4e9b18c116aa42fc84c7dbfd02111aba/442bf027937746248f69701aa9b94112.html")

## Check global.ini parameters

Run the following as <sid>adm. These commands will prompt for the system password for the SYSTEMDB database.

###### Check log_mode is set to normal

Ensure that the configuration parameter log_mode is set to `normal` in the persistence section of the global.ini file:

```
 hdbsql -jx -i <hana_sys_nr> -u system -d SYSTEMDB "SELECT VALUE FROM M_INIFILE_CONTENTS WHERE FILE_NAME = 'global.ini' AND SECTION = 'persistence' AND KEY = 'log_mode';"
```

For example:

```
 hdbadm> hdbsql -jx -i 00 -u system -d SYSTEMDB "SELECT VALUE FROM M_INIFILE_CONTENTS WHERE FILE_NAME = 'global.ini' AND SECTION = 'persistence' AND KEY = 'log_mode';"
VALUE
"normal"
```

###### Review global.ini file replication

SAP HANA System Replication requires consistent configuration between primary and secondary systems to ensure proper operation, especially during failover scenarios. The `inifile_checker/replicate` parameter in global.ini provides an automated solution to this requirement. When enabled on the primary system, any configuration changes made to ini files on the primary are automatically synchronized to the secondary site. This removes the need for manual configuration replication and helps prevent configuration mismatches that could impact system availability. The parameter only needs to be configured on the primary system, as the secondary system will receive these configuration changes through the normal System Replication process.

Add the following to `global.ini`:

```
 [inifile_checker]
replicate = true
```

See SAP Note [2978895 - Changing parameters on Primary and Secondary site of SAP HANA system](https://me.sap.com/notes/2978895 "https://me.sap.com/notes/2978895")

## Create a SAP HANA Backup on the Primary System

**Get a list of all active databases:**

```
 hdbsql -jx -i <hana_sys_nr> -u system -d SYSTEMDB "SELECT DATABASE_NAME,ACTIVE_STATUS from M_DATABASES"
```

For example:

```
 hdbadm> hdbsql -jx -i 00 -u system -d SYSTEMDB "SELECT DATABASE_NAME,ACTIVE_STATUS from M_DATABASES"
Password:
DATABASE_NAME,ACTIVE_STATUS
"SYSTEMDB","YES"
"HDB","YES"
```

###### Create a backup of the SYSTEMDB and each tenant database:

The following commands are examples for file based backups. Backups can be performed using your preferred tool and location. If using a filesystem (e.g. /backup) ensure there is sufficient space for a full backup.

Backint
For the SystemDB

```
 hdbsql -i 00 -u SYSTEM  -d SYSTEMDB "BACKUP DATA USING BACKINT ('initial_hsr_db_SYSTEMDB') COMMENT 'Initial backup for HSR'";
```

For each Tenant DB

```
 hdbsql -i 00 -u SYSTEM  -d <TENANT_DB> "BACKUP DATA USING BACKINT ('initial_hsr_db_<TENANT_DB>') COMMENT 'Initial backup for HSR'";
```

- Run as <sid>adm
- Ensure that backint has been configured correctly
- You will be prompted to provide a password or alternatively can use `-p password`

File
For the SystemDB

```
 hdbsql -i <hana_sys_nr> -u system -d SYSTEMDB "BACKUP DATA USING FILE ('/<backup location>/initial_hsr_db_SYSTEMDB') COMMENT 'Initial backup for HSR'";
```

For each Tenant DB

```
 hdbsql -i <hana_sys_nr> -u system -d <TENANT_DB> "BACKUP DATA USING FILE ('/<backup location>/initial_hsr_db_<TENANT_DB>') COMMENT 'Initial backup for HSR'";
```

- Run as <sid>adm
- Ensure that a backup location exists with sufficient space and the correct file permissions
- You will be prompted to provide a password or alternatively can use `-p password`

### Stop the Secondary System and Copy System PKI Keys

###### Stop the secondary system

Stop the hana application on the secondary, as <sid>adm

```
 sapcontrol -nr <hana_sys_nr> -function StopSystem <SID>
```

###### Copy the system PKI keys

Copy the following system PKI SSFS key and data files from the primary system to the same location on the secondary system using scp, a shared file system, or an S3 bucket:

```
 /usr/sap/<SID>/SYS/global/security/rsecssfs/data/SSFS_<SID>.DAT
/usr/sap/<SID>/SYS/global/security/rsecssfs/key/SSFS_<SID>.KEY
```

For example using scp:

```
 hdbadm>scp -p /usr/sap/HDB/SYS/global/security/rsecssfs/data/SSFS_HDB.DAT hdbadm@hanahost02:/usr/sap/HDB/SYS/global/security/rsecssfs/data/SSFS_HDB.DAT
hdbadm>scp -p /usr/sap/HDB/SYS/global/security/rsecssfs/key/SSFS_HDB.KEY hdbadm@hanahost02:/usr/sap/HDB/SYS/global/security/rsecssfs/key/SSFS_HDB.KEY
```

## Configure System Replication on Primary and Secondary Systems

###### Enable System Replication on the Primary System

Ensure the primary SAP HANA system is **started**, then as <sid>adm, enable system replication using a unique site name:

```
 hdbnsutil -sr_enable --name=<site_1>
```

For example:

```
 hdbadm> hdbnsutil -sr_enable --name=siteA
```

###### Register System Replication on the Secondary System

Ensure the secondary SAP HANA system is **stopped**, then as <sid>adm, enable system replication using a unique site name, the connection details of the primary system and preferred replication options.

```
 hdbnsutil -sr_register \
 --name=<site_2> \
 --remoteHost=<hostname_1> \
 --remoteInstance=<hana_sys_nr> \
 --replicationMode=[sync|syncmem] \
 --operationMode=[logreplay|logreplay_readenabled]
```

For example:

```
 hdbadm> hdbnsutil -sr_register --name=siteB --remoteHost=hanahost01 --remoteInstance=00 --replicationMode=syncmem --operationMode=logreplay
```

Alternatively, if your setup requires active/active read-enabled access to the secondary:

```
 hdbadm> hdbnsutil -sr_register --name=siteB --remoteHost=hanahost01 --remoteInstance=00 --replicationMode=syncmem --operationMode=logreplay_readenabled
```

- `hostname_1` is the hostname used to install SAP HANA, which may be a virtual name.
- The replication mode can be either `sync` or `syncmem`.
- For replication to support a clustered system and a hot standby, the operation mode must be `logreplay` or `logreplay_readenabled`.
- For more information review the SAP Documentation
  - SAP Documentation: [Replication Modes for SAP HANA System Replication](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/c039a1a5b8824ecfa754b55e0caffc01.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/c039a1a5b8824ecfa754b55e0caffc01.html")
  - SAP Documentation: [Operaton Modes for SAP HANA System Replication](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/627bd11e86c84ec2b9fcdf585d24011c.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/627bd11e86c84ec2b9fcdf585d24011c.html")
  - SAP Documentation: [SAP HANA System Replication - Active/Active (Read Enabled)](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/fe5fc53706a34048bf4a3a93a5d7c866.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/fe5fc53706a34048bf4a3a93a5d7c866.html")

## Check SAP Host Agent Version

The SAP host agent is used for SAP instance control and monitoring. This agent is used by SAP cluster resource agents and hooks. It is recommended that you have the latest version installed on all instances. For more details, see [SAP Note 2219592 – Upgrade Strategy of SAP Host Agent](https://me.sap.com/notes/2219592 "https://me.sap.com/notes/2219592").

Use the following command to check the version of the host agent, repeat on all SAP HANA nodes:

```
 # /usr/sap/hostctrl/exe/saphostexec -version
```
