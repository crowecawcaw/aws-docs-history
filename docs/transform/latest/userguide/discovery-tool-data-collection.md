# Data collection

## Scheduling the discovery tool

After your initial discovery collection, the discovery tool continues to run on this schedule:

- VMware discovery - every hour
- Database discovery - once a day
- Network metrics - every 15 seconds, may be less frequent for large environments

To manually run a collection, from the **Actions** menu
choose:

- **Start** - enable the discovery module
- **Stop** - disable the discovery module
- **Collect data now** - use this to start discovery right away, for example,
  after making a change in your network.

**OS data collection attempts**

When a new server is discovered, the discovery tool attempts each configured credential for each IP address and the hostname. After the discovery tool finds a valid credential, it will continue to use that credential unless a new credential is added.

After a collection failure, the discovery tool attempts to collect networking data for a server after 3 minutes, 30 minutes, 2 hours, and then 6 hours. After 4 failed attempts, the discovery tool continues to try all configured credentials once every 6 hours.

## Discovered VMware Inventory

After you set up the vCenter Access, the **Number of discovered VMs** displayed in the **Discovery tool status** frame begins to increment,
and the **VMware discovery** status is shown as **Enabled** in the **Collection module** frame.

You can navigate to the **Discovered inventory** page and see the
servers that are being discovered by the discovery tool. From this page, you can choose
**Download inventory** to download a zip file containing MPA files
listing the VMs that have been discovered with performance utilization data, database
information, and server to server communication information.

You can download the zip file while the discovery tool continues to work, and obtain partial
results. Upload this file to [Migration assessment](transform-app-assessments.md "transform-app-assessments.md") to obtain a business
case for migration.

### Data Points Collected

The discovery tool gathers comprehensive data across VMware, Database, and Network components. These sections detail the specific data points collected for each component.

#### VMware Data Collection

This table describes the VMware virtual machine information collected by the discovery tool:

| Name                                   | Type    | Category       | Sample Value                                      |
| -------------------------------------- | ------- | -------------- | ------------------------------------------------- |
| vm_name                                | String  | VM Info        | "w2k22-snmpd-v2-en-us-mssql-2022-testcase4-1"     |
| vm_id                                  | String  | VM Info        | "vm-30920"                                        |
| vm_uuid                                | String  | VM Info        | "4201ecf8-cc44-ee7e-01da-34dfb2acf6c0"            |
| powerstate                             | String  | VM Info        | "poweredOn"                                       |
| host                                   | String  | VM Info        | "esxi-70-node1.testlab.local"                     |
| primary_ip_address                     | String  | VM Info        | "192.168.0.52"                                    |
| cpus                                   | Integer | VM Info        | 2                                                 |
| memory                                 | Integer | VM Info        | 4096                                              |
| total_disk_capacity_mib                | Integer | VM Info        | 32768                                             |
| os_according_to_the_configuration_file | String  | VM Info        | "Microsoft Windows Server 2016 or later (64-bit)" |
| max_cpu_usage_pct_dec                  | Float   | VM Performance | 79.33                                             |
| avg_cpu_usage_pct_dec                  | Float   | VM Performance | 45.06                                             |
| max_ram_usage_pct_dec                  | Float   | VM Performance | 63.99                                             |
| avg_ram_utl_pct_dec                    | Float   | VM Performance | 29.27                                             |

## Discovery tool's OS-related data

### Network collection

The Network collection module makes it possible for you to discover dependencies among servers in your on-premises data center. This network data accelerates your migration planning by providing visibility into how applications communicate across servers.

This module collects network data for the server inventory that comes from the VMware collection. It uses WinRM to collect data from Windows servers and uses SSH, SNMPv2, and SNMPv3 to collect data from Linux servers.

#### Network Data Collection

The Network collection module captures TCP IPv4 connections in ESTABLISHED or TIME_WAIT state. These data points are collected:

- Source IP, port, process ID, and process name
- Target IP, port, process ID, and process name
- State (ESTABLISHED and TIME_WAIT)
- Transport protocol (TCP)
- IP version (IPv4)
- Count (number of times this unique connection was observed)

### Database collection

The Database collection module gathers database (SQL Server) information from Windows servers. The module uses WinRM protocol to remotely connect to each Windows server and run PowerShell queries to get information about all installed SQL Server services (components) on the server using WMI namespaces, registry, and file properties.

A SQL Server component is a specific service or feature instance installed as part of
a SQL Server deployment on a Windows server. The discovery tool collects Database
Engine, Analysis Services, Reporting Services, and Integration Services.

#### Database Data Collection

The Database collection module gathers SQL Server component information. This table describes key database data points collected:

| Name                 | Type    | Category      | Sample Value                                     |
| -------------------- | ------- | ------------- | ------------------------------------------------ |
| Engine Type          | String  | Component     | sql_server                                       |
| Is Engine Component  | Boolean | Component     | Y                                                |
| Status               | String  | Service       | Running, Stopped, StartPending                   |
| Version              | String  | Service       | 2015.131.5026.0                                  |
| Edition              | String  | Service       | Developer Edition (64-bit)                       |
| SQL Service Name     | String  | Service       | MsDtsServer130, Mssql                            |
| SQL Service Type     | String  | Service       | SQL Server service, Integration Services service |
| Instance Name        | String  | Instance      | MSSQLSERVER                                      |
| Display Name         | String  | Service       | SQL Server (MSSQLSERVER2017)                     |
| Start Mode           | String  | Service       | Automatic, Manual, Disabled                      |
| Service Account Name | String  | Service       | NT Service/MsDtsServer130                        |
| Is Clustered         | Boolean | Configuration | N                                                |

**Note:** Full format includes all service types. MPA format includes only database engine components. Not all fields are available depending on the SQL service type and configuration.
