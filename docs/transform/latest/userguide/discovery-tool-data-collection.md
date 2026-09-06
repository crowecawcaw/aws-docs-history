

# Data collection
<a name="discovery-tool-data-collection"></a>

## Discovery tool collection schedule
<a name="discovery-tool-scheduling"></a>

After your initial discovery collection, the discovery tool continues to run on a staggered schedule to avoid resource contention:
+ VMware discovery – every hour (at :00 UTC)
+ Hyper-V discovery – every hour (at :20 UTC)

The discovery tool also collects OS metrics through the following independent modules, each with its own staggered schedule:
+ Network metrics – every 15 seconds, might be less frequent for large environments
+ Server performance metrics – every 10 minutes (at :03, :13, :23, :33, :43, :53 UTC)
+ Storage performance metrics – every 10 minutes (at :07, :17, :27, :37, :47, :57 UTC)
+ Running processes – hourly (at :40 UTC)
+ Server provisioning data – daily (at 00:05 UTC)
+ Storage provisioning data – daily (at 00:35 UTC)
+ Network interfaces – daily (at 01:05 UTC)
+ SQL Server discovery – daily (at 03:05 UTC)
+ Oracle database discovery – daily (at 05:05 UTC)

You can independently start, stop, or trigger each OS metrics module by using **Collect data now**.

To manually run a collection, from the **Actions** menu choose:
+ **Start** – Enables the discovery module.
+ **Stop** – Disables the discovery module.
+ **Collect data now** – Starts discovery immediately. Use this option, for example, after you make a change in your network.

These actions apply per module. You can control OS metrics modules individually.

### OS data collection attempts
<a name="discovery-tool-os-collection-attempts"></a>

When a new server is discovered, the discovery tool attempts each configured credential for each IP address and the hostname. After the discovery tool finds a valid credential, it continues to use that credential unless you add a new credential.

After a collection failure, the discovery tool attempts to collect networking data for a server after 3 minutes, 30 minutes, 2 hours, and then 6 hours. After 4 failed attempts, the discovery tool continues to try all configured credentials once every 6 hours.

## How average, p95, and peak statistics are calculated
<a name="discovery-tool-statistics-basis"></a>

This section describes the average (`_avg`), 95th percentile (`_p95`), and peak (`_peak`) statistics in the *OS-collected* performance data: the columns in `server_performance_metrics.csv` and `server_storage_performance.csv`, and the `disk_*` statistic columns in `server_inventory.csv`. The VMware- and Hyper-V-sourced performance columns (for example, the MPA fields `avgCpuUsagePctDec` and `avgRamUtlPctDec`) are averaged on a different basis and carry no p95 or peak value.

**Window** – The statistics cover the entire export date range: the range you select at export time, up to the 30-day retention limit, or the tool's uptime if it is shorter.

**Sampling** – The discovery tool records one sample per metric per collection cycle. CPU, memory, and network samples come from the server performance module, and disk IOPS and throughput samples come from the storage performance module. Both modules run every 10 minutes, which is about 144 samples per metric per day, or about 4,320 over 30 days. For the full schedule, see [Discovery tool collection schedule](#discovery-tool-scheduling).

**Computation** – Samples accumulate each day during collection. At export, all samples in the selected window are pooled, and the statistics are computed over that full set:
+ **Average** – the mean of the pooled samples.
+ **p95** – the 95th percentile, computed with the inclusive method (equivalent to the Excel `PERCENTILE.INC` function). It never exceeds the maximum sample observed.
+ **Peak** – for CPU, memory, network, and the per-volume rows in `server_storage_performance.csv`, the peak is the highest single sample observed. For the server-level `disk_*` columns in `server_inventory.csv`, the peak is the sum of each volume's peak.

The discovery tool computes the statistics from all samples in the window. A shorter window contains fewer samples. A 2-day export therefore produces different average and p95 values than a 30-day export.

## Discovered inventory
<a name="discovery-tool-inventory"></a>

After you configure a discovery source, the **Number of discovered servers** value in the **Discovery tool status** frame begins to increment. The discovery status for the configured source changes to **Enabled** in the **Collection module** frame. The inventory page shows servers from all configured sources: VMware VMs, Hyper-V VMs, and imported servers. Each server shows its source and collection status per module.

Navigate to the **Discovered inventory** page to see the servers that the discovery tool has found. From this page, choose **Download inventory** to download a ZIP file (`discovery_tool_export.zip`) that contains up to 30 days of collected data, including MPA files for all configured sources, performance utilization data, database information, and server-to-server communication information.

You can download the ZIP file while the discovery tool continues to work, and obtain partial results. Upload this file to [Migration assessment ](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html)to obtain a business case for migration.

### Export options
<a name="discovery-tool-export-options"></a>

When exporting data, you can customize the export with the following options:

**Date range**

Select a start date and end date to export only data collected within that time period. Both dates are inclusive. The maximum date range is 30 days.

**Note**  
The discovery tool stores up to 30 days of collected data. If you need data spanning more than 30 days, run incremental exports every 30 days to capture all data.

**Module selection**

Choose which data modules to include in the export. You can export all modules or select specific ones:


| Module | Description | 
| --- | --- | 
| VMware data | Virtual machine inventory from vCenter servers | 
| Hyper-V data | Virtual machine inventory from Hyper-V hosts | 
| Network data | Network connections between servers | 
| Server inventory | Server hardware and OS information | 
| Server performance metrics | CPU, memory, and network utilization | 
| Server storage performance | Disk IOPS and throughput | 
| Storage config | Disk and volume configuration | 
| Network interfaces | Network adapter details | 
| Process metrics | Running processes | 
| SQL Server data | SQL Server database inventory | 
| Oracle Database data | Oracle database inventory – CDBs, PDBs, features, options, and components | 

If you don't select any modules, the discovery tool exports all available data.

### Data points collected
<a name="discovery-tool-data-points"></a>

The discovery tool gathers comprehensive data across VMware, Hyper-V, OS metrics, database, and network components. The following sections detail the specific data points collected for each component.

#### VMware data collection
<a name="discovery-tool-vmware-data"></a>

This table describes the VMware virtual machine information collected by the discovery tool:


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| vm\_name | String | VM Info | "w2k22-snmpd-v2-en-us-mssql-2022-testcase4-1" | 
| vm\_id | String | VM Info | "vm-30920" | 
| vm\_uuid | String | VM Info | "4201ecf8-cc44-ee7e-01da-34dfb2acf6c0" | 
| powerstate | String | VM Info | "poweredOn" | 
| host | String | VM Info | "esxi-70-node1.testlab.local" | 
| primary\_ip\_address | String | VM Info | "192.168.0.52" | 
| cpus | Integer | VM Info | 2 | 
| memory | Integer | VM Info | 4096 | 
| total\_disk\_capacity\_mib | Integer | VM Info | 32768 | 
| os\_according\_to\_the\_configuration\_file | String | VM Info | "Microsoft Windows Server 2016 or later (64-bit)" | 
| max\_cpu\_usage\_pct\_dec | Float | VM Performance | 79.33 | 
| avg\_cpu\_usage\_pct\_dec | Float | VM Performance | 45.06 | 
| max\_ram\_usage\_pct\_dec | Float | VM Performance | 63.99 | 
| avg\_ram\_utl\_pct\_dec | Float | VM Performance | 29.27 | 

#### Hyper-V data collection
<a name="discovery-tool-hyperv-data"></a>

This table describes the Hyper-V virtual machine information collected by the discovery tool:


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| vm\_name | String | VM Info | "win2022-hyperv-test-01" | 
| vm\_id | String | VM Info | "a1b2c3d4-e5f6-7890-abcd-ef1234567890" | 
| powerstate | String | VM Info | "Running" | 
| cpus | Integer | VM Info | 4 | 
| memory\_mb | Integer | VM Info | 8192 | 
| disk\_paths | String | Disk | "C:\\\\VMs\\\\disk1.vhdx" | 
| disk\_size\_gb | Float | Disk | 127.0 | 
| network\_adapters | String | Network | "00:15:5D:01:02:03" | 
| ip\_addresses | String | Network | "10.0.1.50" | 
| host\_name | String | Host | "hyperv-host-01.example.com" | 
| host\_os\_version | String | Host | "Windows Server 2022 Datacenter" | 
| cluster\_name | String | Host | "FailoverCluster01" | 
| hypervisor | String | VM Info | "Hyper-V" | 

#### Imported server data
<a name="discovery-tool-bare-metal-data"></a>

Imported servers are not auto-discovered. They are imported through a CSV file. The discovery tool does not collect hypervisor-level data for imported servers. Instead, it collects database, network, and OS metrics data by using the OS credentials associated with each server during import.

## Discovery tool's OS-related data
<a name="discovery-tool-os-data"></a>

The discovery tool collects server inventory, performance, storage, network interface, and process data through SSH (Linux) and WinRM (Windows). The following tables describe the data points collected.

### Server inventory (server\_inventory.csv)
<a name="discovery-tool-os-server-inventory"></a>

Combines server provisioning (hardware and OS configuration) with aggregated storage performance. Collected every 24 hours.

Disk throughput columns end in `_mibps` and are reported in mebibytes per second (MiBps). The `_p95` columns hold the 95th percentile of the samples in the export window.


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| server\_id | String | Server Info | "vm-web-server-01" | 
| server\_name | String | Server Info | "web-server-01" | 
| resource\_type | String | Server Info | "virtual\_machine" | 
| power\_state | String | Server Info | "Running" | 
| os\_type | String | Server Info | "Linux" | 
| os\_name | String | Server Info | "Amazon Linux" | 
| os\_version | String | Server Info | "2023" | 
| primary\_hostname | String | Server Info | "web-server-01.example.com" | 
| primary\_ip\_address | String | Server Info | "10.0.2.101" | 
| netmask | String | Server Info | "255.255.255.0" | 
| total\_num\_network\_cards | Integer | Server Info | 2 | 
| total\_num\_disks | Integer | Server Info | 1 | 
| cpu\_count | Integer | Server Info | 4 | 
| total\_memory\_gb | Float | Server Info | 15.88 | 
| server\_uuid | String | Server Info | "4201ecf8-cc44-ee7e-01da-34dfb2acf6c0" | 
| smbios\_uuid | String | Server Info | "4201ecf8-cc44-ee7e-01da-34dfb2acf6c0" | 
| cluster\_name | String | Server Info | "production-cluster-01" | 
| hypervisor\_object\_id | String | Server Info | "vm-30920" | 
| hypervisor\_type | String | Server Info | "VMware" | 
| hypervisor\_version | String | Server Info | "8.0.0" | 
| hypervisor\_hostname | String | Server Info | "esxi-node1.example.com" | 
| hypervisor\_host\_id | String | Server Info | "host-1234" | 
| hypervisor\_id | String | Server Info | "4201ecf8-cc44-ee7e-01da-34dfb2acf6c0" | 
| disk\_read\_iops\_avg | Float | Storage Performance | 12.5 | 
| disk\_read\_iops\_p95 | Float | Storage Performance | 198.0 | 
| disk\_read\_iops\_peak | Float | Storage Performance | 245.0 | 
| disk\_write\_iops\_avg | Float | Storage Performance | 8.3 | 
| disk\_write\_iops\_p95 | Float | Storage Performance | 142.0 | 
| disk\_write\_iops\_peak | Float | Storage Performance | 180.0 | 
| disk\_total\_iops\_avg | Float | Storage Performance | 20.8 | 
| disk\_total\_iops\_p95 | Float | Storage Performance | 340.0 | 
| disk\_total\_iops\_peak | Float | Storage Performance | 425.0 | 
| disk\_read\_throughput\_avg\_mibps | Float | Storage Performance | 1.2 | 
| disk\_read\_throughput\_p95\_mibps | Float | Storage Performance | 19.8 | 
| disk\_read\_throughput\_peak\_mibps | Float | Storage Performance | 24.5 | 
| disk\_write\_throughput\_avg\_mibps | Float | Storage Performance | 0.8 | 
| disk\_write\_throughput\_p95\_mibps | Float | Storage Performance | 14.2 | 
| disk\_write\_throughput\_peak\_mibps | Float | Storage Performance | 18.0 | 
| disk\_total\_throughput\_avg\_mibps | Float | Storage Performance | 2.0 | 
| disk\_total\_throughput\_p95\_mibps | Float | Storage Performance | 34.0 | 
| disk\_total\_throughput\_peak\_mibps | Float | Storage Performance | 42.5 | 

### Server performance metrics (server\_performance\_metrics.csv)
<a name="discovery-tool-os-server-performance"></a>

CPU, memory, and network throughput utilization. Sampled every 10 minutes, aggregated over 30 days.

The `_p95` columns hold the 95th percentile of the samples in the export window. Network throughput columns end in `_mbps` and are reported in megabits per second (Mbps).


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| server\_id | String | Server Info | "vm-web-server-01" | 
| data\_source | String | Server Info | "OS" | 
| cpu\_utilization\_avg\_pct | Float | CPU | 45.06 | 
| cpu\_utilization\_p95\_pct | Float | CPU | 72.14 | 
| cpu\_utilization\_peak\_pct | Float | CPU | 79.33 | 
| cpu\_count | Integer | CPU | 4 | 
| memory\_total\_gb | Float | Memory | 15.88 | 
| memory\_utilization\_avg\_pct | Float | Memory | 29.27 | 
| memory\_utilization\_p95\_pct | Float | Memory | 58.42 | 
| memory\_utilization\_peak\_pct | Float | Memory | 63.99 | 
| network\_in\_avg\_mbps | Float | Network | 0.52 | 
| network\_in\_p95\_mbps | Float | Network | 9.84 | 
| network\_in\_peak\_mbps | Float | Network | 12.3 | 
| network\_out\_avg\_mbps | Float | Network | 0.31 | 
| network\_out\_p95\_mbps | Float | Network | 6.95 | 
| network\_out\_peak\_mbps | Float | Network | 8.7 | 
| network\_total\_avg\_mbps | Float | Network | 0.83 | 
| network\_total\_p95\_mbps | Float | Network | 16.79 | 
| network\_total\_peak\_mbps | Float | Network | 21.0 | 

### Storage performance (server\_storage\_performance.csv)
<a name="discovery-tool-os-storage-performance"></a>

Per-volume disk I/O and space utilization. Sampled every 10 minutes, aggregated over 30 days.

Disk throughput columns end in `_mibps` and are reported in mebibytes per second (MiBps). The `_p95` columns hold the 95th percentile of the samples in the export window.


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| server\_id | String | Server Info | "vm-web-server-01" | 
| data\_source | String | Server Info | "OS" | 
| disk\_volume\_id | String | Volume Info | "/dev/nvme0n1p1" | 
| disk\_mount\_point | String | Volume Info | "/" | 
| file\_system | String | Volume Info | "xfs" | 
| disk\_total\_gb | Float | Disk Space | 30.0 | 
| disk\_used\_gb | Float | Disk Space | 12.5 | 
| disk\_free\_gb | Float | Disk Space | 17.5 | 
| disk\_read\_iops\_avg | Float | Disk I/O | 12.5 | 
| disk\_read\_iops\_p95 | Float | Disk I/O | 198.0 | 
| disk\_read\_iops\_peak | Float | Disk I/O | 245.0 | 
| disk\_write\_iops\_avg | Float | Disk I/O | 8.3 | 
| disk\_write\_iops\_p95 | Float | Disk I/O | 142.0 | 
| disk\_write\_iops\_peak | Float | Disk I/O | 180.0 | 
| disk\_total\_iops\_avg | Float | Disk I/O | 20.8 | 
| disk\_total\_iops\_p95 | Float | Disk I/O | 340.0 | 
| disk\_total\_iops\_peak | Float | Disk I/O | 425.0 | 
| disk\_read\_throughput\_avg\_mibps | Float | Disk Throughput | 1.2 | 
| disk\_read\_throughput\_p95\_mibps | Float | Disk Throughput | 19.8 | 
| disk\_read\_throughput\_peak\_mibps | Float | Disk Throughput | 24.5 | 
| disk\_write\_throughput\_avg\_mibps | Float | Disk Throughput | 0.8 | 
| disk\_write\_throughput\_p95\_mibps | Float | Disk Throughput | 14.2 | 
| disk\_write\_throughput\_peak\_mibps | Float | Disk Throughput | 18.0 | 
| disk\_total\_throughput\_avg\_mibps | Float | Disk Throughput | 2.0 | 
| disk\_total\_throughput\_p95\_mibps | Float | Disk Throughput | 34.0 | 
| disk\_total\_throughput\_peak\_mibps | Float | Disk Throughput | 42.5 | 

### Unmapped storage devices (unmapped\_storage\_devices.csv)
<a name="discovery-tool-os-unmapped-storage"></a>

The discovery tool cannot always match a storage device to a mounted file system, and some devices report no usable capacity. The discovery tool does not omit these devices or report their capacity as zero. It writes them to `unmapped_storage_devices.csv` instead, and still reports performance data for them. Only the capacity columns are blank.

This file has the same columns as `server_storage_performance.csv`, in the same order, plus a `reason` column. The `reason` column can hold the following values.


| Value | Meaning | 
| --- | --- | 
| no\_mounted\_filesystem\_match | The discovery tool cannot match the device to a mounted file system. | 
| mounted\_but\_capacity\_unavailable | The device is mounted, but it does not report usable capacity. | 

When you export the storage performance module, the export includes both files.

**Note**  
When you upload the export to AWS Transform, the assessments agent ignores unmapped storage devices unless you specifically instruct it to include them.

### Storage configuration (storage\_config.csv)
<a name="discovery-tool-os-storage-config"></a>

Physical disk hardware details. Collected every 24 hours.


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| server\_id | String | Server Info | "vm-web-server-01" | 
| disk\_controller\_id | String | Disk Info | "/dev/sda" | 
| vmdk\_vhd\_file\_name | String | Disk Info | "web-server-01.vmdk" | 
| disk\_volume\_type | String | Disk Info | "Virtual" | 
| disk\_provisioned\_gb | Float | Disk Info | 30.0 | 
| disk\_device\_type | String | Disk Info | "SCSI HDD" | 
| disk\_interface\_type | String | Disk Info | "SCSI" | 
| disk\_protocol | String | Disk Info | "LSI Logic SAS" | 

### Network interfaces (network\_interfaces.csv)
<a name="discovery-tool-os-network-interfaces"></a>

Network adapter configuration. Collected every 24 hours.


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| server\_id | String | Server Info | "vm-web-server-01" | 
| interface\_name | String | Interface Info | "eth0" | 
| interface\_index | Integer | Interface Info | 2 | 
| mac\_address | String | Interface Info | "0A:1B:2C:3D:4E:5F" | 
| adapter\_type | String | Interface Info | "vmxnet3" | 
| virtual\_network\_name | String | Interface Info | "VM Network" | 
| virtual\_network\_id | String | Interface Info | "dvportgroup-1234" | 
| virtual\_switch | String | Interface Info | "vSwitch0" | 
| ipv4\_address | String | IP Config | "10.0.2.101" | 
| ipv4\_subnet\_mask | String | IP Config | "255.255.255.0" | 
| ipv4\_gateway | String | IP Config | "10.0.2.1" | 
| ipv6\_address | String | IP Config | "fe80::a1b:2cff:fe3d:4e5f" | 
| ipv6\_prefix\_length | Integer | IP Config | 64 | 
| ipv6\_gateway | String | IP Config | "fe80::1" | 
| dns\_servers | String | IP Config | "10.0.0.2" | 
| dhcp\_enabled | Boolean | IP Config | false | 
| interface\_status | String | Interface Info | "Up" | 
| vlan\_id | Integer | Interface Info | 100 | 
| is\_primary | Boolean | Interface Info | true | 

### Running processes (process\_metrics.csv)
<a name="discovery-tool-os-running-processes"></a>

Snapshot of running processes. Collected every hour, deduplicated over 30 days.


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| server\_id | String | Server Info | "vm-web-server-01" | 
| process\_name | String | Process Info | "sshd" | 
| process\_id | Integer | Process Info | 1234 | 
| process\_command\_line | String | Process Info | "/usr/sbin/sshd -D" | 
| process\_user | String | Process Info | "root" | 

### Network collection
<a name="discovery-tool-network-collection"></a>

The Network collection module helps you discover dependencies among servers in your on-premises data center. This network data accelerates your migration planning by providing visibility into how applications communicate across servers.

This module collects network data for servers from all configured sources, including VMware, Hyper-V, and imported servers. It uses WinRM to collect data from Windows servers and uses SSH, SNMPv2, and SNMPv3 to collect data from Linux servers.

#### Network data collection
<a name="discovery-tool-network-data"></a>

The Network collection module captures TCP IPv4 connections in ESTABLISHED or TIME\_WAIT state between servers in your discovered inventory. A connection appears in the output only when both the source and target IP addresses belong to servers that the discovery tool has discovered or that you have imported. Connections to or from IP addresses outside your inventory — such as external services, cloud endpoints, or servers not yet added to the discovery tool — are not included.

This design focuses the network data on server-to-server dependencies within your environment, which is the information needed for application dependency mapping and migration wave planning.

These data points are collected for each connection:


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| Source IP | String | Connection | "192.168.1.10" | 
| Source port | Integer | Connection | 49152 | 
| Source process ID | Integer | Process | 1234 | 
| Source process name | String | Process | "java" | 
| Target IP | String | Connection | "192.168.1.20" | 
| Target port | Integer | Connection | 5432 | 
| Target process ID | Integer | Process | 5678 | 
| Target process name | String | Process | "postgres" | 
| State | String | Connection | "ESTABLISHED" | 
| Transport protocol | String | Connection | "TCP" | 
| IP version | String | Connection | "IPv4" | 
| Count | Integer | Connection | 42 | 

**Tip**  
To maximize the completeness of your network dependency map, configure all discovery sources (VMware, Hyper-V, and server CSV import) and add OS credentials before reviewing network data. The more servers in your inventory, the more connections the network module can capture.

#### Private address network collection
<a name="discovery-tool-private-address-collection"></a>

By default, the Network collection module only captures connections where both endpoints are servers in your discovered inventory. You can enable private address collection to also capture connections to and from RFC 1918 private IP addresses (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) that are not in your inventory.

**To start private address collection**

1. On the **Collector configuration** page, locate the **Collection modules** section.

1. Find **Network connections discovery** under **Application discovery**.

1. Open the **Actions** dropdown.

1. Choose **Start private address collection**.

1. If the module status was **Enabled**, you can see it change to **Enabled · Private Address on**.

To stop private address collection, open the **Actions** dropdown and choose **Stop private address collection**. Previously collected private address data is retained even after stopping.

Private address connections appear only in the full CSV export (inside the ZIP file), not in the MPA CSV files. If an IP address belongs to a server already in your inventory, it is always identified by its discovered server ID regardless of this setting.

This setting persists across restarts. You can start or stop private address collection at any time. Previously collected private address data is exported regardless of the current setting.

### SQL Server collection
<a name="discovery-tool-database-collection"></a>

The SQL Server collection module gathers SQL Server information from Windows servers across all configured sources, including VMware, Hyper-V, and imported servers. The module uses WinRM to remotely connect to each Windows server and run PowerShell queries. It collects information about all installed SQL Server services (components) by using WMI namespaces, registry, and file properties.

A SQL Server component is a specific service or feature instance installed as part of a SQL Server deployment on a Windows server. The discovery tool collects Database Engine, Analysis Services, Reporting Services, and Integration Services.

#### SQL Server data collection
<a name="discovery-tool-database-data"></a>

The SQL Server collection module gathers SQL Server component information. This table describes key data points collected:


| Name | Type | Category | Sample value | 
| --- | --- | --- | --- | 
| Engine Type | String | Component | sql\_server | 
| Is Engine Component | Boolean | Component | Y | 
| Status | String | Service | Running, Stopped, StartPending | 
| Version | String | Service | 2015.131.5026.0 | 
| Edition | String | Service | Developer Edition (64-bit) | 
| SQL Service Name | String | Service | MsDtsServer130, Mssql | 
| SQL Service Type | String | Service | SQL Server service, Integration Services service | 
| Instance Name | String | Instance | MSSQLSERVER | 
| Display Name | String | Service | SQL Server (MSSQLSERVER2017) | 
| Start Mode | String | Service | Automatic, Manual, Disabled | 
| Service Account Name | String | Service | NT Service/MsDtsServer130 | 
| Is Clustered | Boolean | Configuration | N | 

**Note**  
Full format includes all service types. MPA format includes only database engine components. Not all fields are available depending on the SQL service type and configuration.

### Oracle Database collection
<a name="discovery-tool-oracle-collection"></a>

With Oracle Database collection, you can discover Oracle database instances across all configured sources, including VMware, Hyper-V, and imported servers. The module collects the following data:
+ Container database (CDB) and pluggable database (PDB) enumeration
+ Version and edition
+ Installed options
+ Feature usage statistics
+ Component inventory (DBA\_REGISTRY)
+ Datafile sizing
+ Topology flags (RAC, Data Guard, and multitenant architecture)

**Database-connected (SQL)**

When you configure Oracle credentials, the discovery tool connects directly to the Oracle database using the read-only service account. This provides full SQL-level collection including PDB details, feature usage, and installed options. All CSV files contain complete data.

**OS-level fallback**

If you have not configured database credentials, or if the connection fails, the discovery tool uses SSH or WinRM to detect Oracle installations. It discovers Oracle homes, listeners, patches, version, and edition without database access. For OS-detected hosts, the exported CDB CSV contains instance name, host name, version, and edition. The PDB, features, options, and components CSV files contain no rows.

The Oracle collection produces the following CSV files in the export ZIP. Each table describes the data points collected per file.

#### CDB data (oracle\_data\_cdbs\_full.csv)
<a name="discovery-tool-oracle-cdb-data"></a>

One row per CDB instance. This table describes the CDB data points collected:


| Name | Type | Category | Sample value | Source | 
| --- | --- | --- | --- | --- | 
| Instance Name | String | Identity | "ORCL" | SQL, OS | 
| Host Name | String | Identity | "oracledb01.example.com" | SQL, OS | 
| DB Name | String | Identity | "ORCL" | SQL only | 
| DB Unique Name | String | Identity | "ORCL\_PRIMARY" | SQL only | 
| DBID | Integer | Identity | 1234567890 | SQL only | 
| Version | String | Version | "19.0.0.0" | SQL, OS | 
| Version Full | String | Version | "19.21.0.0.0" | SQL only | 
| Edition | String | Version | "Enterprise Edition" | SQL, OS | 
| Database Type | String | Configuration | "SINGLE" | SQL only | 
| Database Role | String | Configuration | "PRIMARY" | SQL only | 
| Open Mode | String | Configuration | "READ WRITE" | SQL only | 
| Log Mode | String | Configuration | "ARCHIVELOG" | SQL only | 
| Platform | String | Configuration | "Linux x86 64-bit" | SQL only | 
| CDB Flag | String | Configuration | "YES" | SQL only | 
| Is RAC | String | Topology | "YES" or "NO" | SQL only | 
| Is Data Guard Standby | String | Topology | "YES" or "NO" | SQL only | 
| Protection Mode | String | Topology | "MAXIMUM PERFORMANCE" | SQL only | 
| Data Guard Broker | String | Topology | "ENABLED" | SQL only | 
| NLS Characterset | String | Configuration | "AL32UTF8" | SQL only | 
| PDB Count | Integer | Sizing | 3 | SQL only | 
| Flashback On | String | Configuration | "YES" | SQL only | 
| Detection Path | String | Metadata | "phase2" or "phase1b" | SQL, OS | 

#### PDB data (oracle\_data\_pdbs\_full.csv)
<a name="discovery-tool-oracle-pdb-data"></a>

One row per PDB (pluggable database). This table describes the PDB data points collected:

**Note**  
PDB data requires Oracle database credentials (SQL connection). OS-level fallback does not populate this CSV.


| Name | Type | Category | Sample value | Source | 
| --- | --- | --- | --- | --- | 
| CDB Instance Name | String | Identity | "ORCL" | SQL only | 
| PDB Name | String | Identity | "APPPDB1" | SQL only | 
| Open Mode | String | Status | "READ WRITE" | SQL only | 
| Lifecycle Status | String | Status | "NORMAL" | SQL only | 
| Tablespace Count | Integer | Sizing | 5 | SQL only | 
| Datafile Count | Integer | Sizing | 12 | SQL only | 
| Total Size Bytes | Integer | Sizing | 5368709120 | SQL only | 
| User Schema Count | Integer | Sizing | 8 | SQL only | 
| DB Link Count | Integer | Connectivity | 2 | SQL only | 
| Components Installed | String | Configuration | "APEX;JVM;XML" | SQL only | 
| Encrypted Tablespace Count | Integer | Security | 1 | SQL only | 

#### Feature usage data (oracle\_data\_features\_full.csv)
<a name="discovery-tool-oracle-features-data"></a>

One row per feature usage entry from DBA\_FEATURE\_USAGE\_STATISTICS. This table describes the feature usage data points collected:

**Note**  
Feature usage data requires Oracle database credentials (SQL connection). OS-level fallback does not populate this CSV.


| Name | Type | Category | Sample value | Source | 
| --- | --- | --- | --- | --- | 
| CDB Instance Name | String | Identity | "ORCL" | SQL only | 
| Name | String | Feature | "Partitioning (user)" | SQL only | 
| Detected Usages | Integer | Usage | 42 | SQL only | 
| Currently Used | String | Usage | "TRUE" | SQL only | 
| First Usage Date | DateTime | Usage | "2024-01-15T00:00:00" | SQL only | 
| Last Usage Date | DateTime | Usage | "2026-06-01T00:00:00" | SQL only | 

#### Options data (oracle\_data\_options\_full.csv)
<a name="discovery-tool-oracle-options-data"></a>

One row per V$OPTION entry per CDB. This table describes the installed options data points collected:

**Note**  
Options data requires Oracle database credentials (SQL connection). OS-level fallback does not populate this CSV.


| Name | Type | Category | Sample value | Source | 
| --- | --- | --- | --- | --- | 
| CDB Instance Name | String | Identity | "ORCL" | SQL only | 
| Option Name | String | Option | "Advanced Analytics" | SQL only | 
| Is Installed | String | Option | "TRUE" | SQL only | 
| Container ID | Integer | Option | 0 | SQL only | 

#### Components data (oracle\_data\_components\_full.csv)
<a name="discovery-tool-oracle-components-data"></a>

One row per DBA\_REGISTRY component. This table describes the component data points collected:

**Note**  
Components data requires Oracle database credentials (SQL connection). OS-level fallback does not populate this CSV.


| Name | Type | Category | Sample value | Source | 
| --- | --- | --- | --- | --- | 
| CDB Instance Name | String | Identity | "ORCL" | SQL only | 
| PDB Name | String | Identity | "APPPDB1" | SQL only | 
| Component ID | String | Component | "APEX" | SQL only | 
| Component Name | String | Component | "Oracle Application Express" | SQL only | 
| Version | String | Component | "22.1.0.15.0" | SQL only | 
| Status | String | Component | "VALID" | SQL only | 
| Schema | String | Component | "APEX\_220100" | SQL only | 