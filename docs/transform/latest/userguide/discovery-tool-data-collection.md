# Data collection

## Discovery tool collection schedule

After your initial discovery collection, the discovery tool continues to run on a staggered schedule to avoid resource contention:

- VMware discovery – every hour (at :00 UTC)
- Hyper-V discovery – every hour (at :20 UTC)

The discovery tool also collects OS metrics through the following independent modules, each with its own staggered schedule:

- Database discovery – once a day
- Network metrics – every 15 seconds, might be less frequent for large environments
- Server performance metrics – every 10 minutes (at :03, :13, :23, :33, :43, :53 UTC)
- Storage performance metrics – every 10 minutes (at :07, :17, :27, :37, :47, :57 UTC)
- Server provisioning data – daily (at 00:05 UTC)
- Storage provisioning data – daily (at 00:35 UTC)
- Network interfaces – daily (at 01:05 UTC)
- Running processes – hourly (at :40 UTC)

You can independently start, stop, or trigger each OS metrics module by using **Collect data now**.

To manually run a collection, from the **Actions** menu
choose:

- **Start** – Enables the discovery module.
- **Stop** – Disables the discovery module.
- **Collect data now** – Starts discovery immediately. Use this option, for example,
  after you make a change in your network.

These actions apply per module. You can control OS metrics modules individually.

### OS data collection attempts

When a new server is discovered, the discovery tool attempts each configured credential for each IP address and the hostname. After the discovery tool finds a valid credential, it continues to use that credential unless you add a new credential.

After a collection failure, the discovery tool attempts to collect networking data for a server after 3 minutes, 30 minutes, 2 hours, and then 6 hours. After 4 failed attempts, the discovery tool continues to try all configured credentials once every 6 hours.

## Discovered inventory

After you configure a discovery source, the **Number of discovered servers** value in the **Discovery tool status** frame begins to increment. The discovery status for the configured source changes to **Enabled** in the **Collection module** frame. The inventory page shows servers from all configured sources: VMware VMs, Hyper-V VMs, and imported servers. Each server shows its source and collection status per module.

Navigate to the **Discovered inventory** page to see the servers that the discovery tool has found. From this page, choose **Download inventory** to download a ZIP file (`discovery_tool_export.zip`) that contains up to 30 days of collected data, including MPA files for all configured sources, performance utilization data, database information, and server-to-server communication information.

You can download the ZIP file while the discovery tool continues to work, and obtain partial
results. Upload this file to [Migration assessment](transform-app-assessments.md "transform-app-assessments.md") to obtain a business
case for migration.

### Export options

When exporting data, you can customize the export with the following options:

**Date range**

Select a start date and end date to export only data collected within that time period. Both dates are inclusive. The maximum date range is 30 days.

###### Note

The discovery tool stores up to 30 days of collected data. If you need data spanning more than 30 days, run incremental exports every 30 days to capture all data.

**Module selection**

Choose which data modules to include in the export. You can export all modules or select specific ones:

| Module                     | Description                                    |
| -------------------------- | ---------------------------------------------- |
| VMware data                | Virtual machine inventory from vCenter servers |
| Hyper-V data               | Virtual machine inventory from Hyper-V hosts   |
| Network data               | Network connections between servers            |
| Database data              | SQL Server database inventory                  |
| Server inventory           | Server hardware and OS information             |
| Server performance metrics | CPU, memory, and network utilization           |
| Server storage performance | Disk IOPS and throughput                       |
| Storage config             | Disk and volume configuration                  |
| Network interfaces         | Network adapter details                        |
| Process metrics            | Running processes                              |

If you don't select any modules, the discovery tool exports all available data.

### Data points collected

The discovery tool gathers comprehensive data across VMware, Hyper-V, OS metrics, database, and network components. The following sections detail the specific data points collected for each component.

#### VMware data collection

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

#### Hyper-V data collection

This table describes the Hyper-V virtual machine information collected by the discovery tool:

| Name             | Type    | Category | Sample Value                           |
| ---------------- | ------- | -------- | -------------------------------------- |
| vm_name          | String  | VM Info  | "win2022-hyperv-test-01"               |
| vm_id            | String  | VM Info  | "a1b2c3d4-e5f6-7890-abcd-ef1234567890" |
| powerstate       | String  | VM Info  | "Running"                              |
| cpus             | Integer | VM Info  | 4                                      |
| memory_mb        | Integer | VM Info  | 8192                                   |
| disk_paths       | String  | Disk     | "C:\\VMs\\disk1.vhdx"                  |
| disk_size_gb     | Float   | Disk     | 127.0                                  |
| network_adapters | String  | Network  | "00:15:5D:01:02:03"                    |
| ip_addresses     | String  | Network  | "10.0.1.50"                            |
| host_name        | String  | Host     | "hyperv-host-01.example.com"           |
| host_os_version  | String  | Host     | "Windows Server 2022 Datacenter"       |
| cluster_name     | String  | Host     | "FailoverCluster01"                    |
| hypervisor       | String  | VM Info  | "Hyper-V"                              |

#### Imported server data

Imported servers are not auto-discovered. They are imported through a CSV file. The discovery tool does not collect hypervisor-level data for imported servers. Instead, it collects database, network, and OS metrics data by using the OS credentials associated with each server during import.

## Discovery tool's OS-related data

### OS metrics data collection

The discovery tool collects OS-level metrics from servers through SSH (Linux) and WinRM (Windows). Data is collected across six sub-modules and exported into six CSV files.

#### Server inventory (server_inventory.csv)

Combines server provisioning (hardware and OS configuration) with aggregated storage performance. Collected every 24 hours.

| Name                            | Type    | Category            | Sample Value                           |
| ------------------------------- | ------- | ------------------- | -------------------------------------- |
| server_id                       | String  | Server Info         | "vm-web-server-01"                     |
| server_name                     | String  | Server Info         | "web-server-01"                        |
| resource_type                   | String  | Server Info         | "virtual_machine"                      |
| power_state                     | String  | Server Info         | "Running"                              |
| os_type                         | String  | Server Info         | "Linux"                                |
| os_name                         | String  | Server Info         | "Amazon Linux"                         |
| os_version                      | String  | Server Info         | "2023"                                 |
| primary_hostname                | String  | Server Info         | "web-server-01.example.com"            |
| primary_ip_address              | String  | Server Info         | "10.0.2.101"                           |
| netmask                         | String  | Server Info         | "255.255.255.0"                        |
| total_num_network_cards         | Integer | Server Info         | 2                                      |
| total_num_disks                 | Integer | Server Info         | 1                                      |
| cpu_count                       | Integer | Server Info         | 4                                      |
| total_memory_gb                 | Float   | Server Info         | 15.88                                  |
| server_uuid                     | String  | Server Info         | "4201ecf8-cc44-ee7e-01da-34dfb2acf6c0" |
| smbios_uuid                     | String  | Server Info         | "4201ecf8-cc44-ee7e-01da-34dfb2acf6c0" |
| cluster_name                    | String  | Server Info         | "production-cluster-01"                |
| hypervisor_object_id            | String  | Server Info         | "vm-30920"                             |
| hypervisor_type                 | String  | Server Info         | "VMware"                               |
| hypervisor_version              | String  | Server Info         | "8.0.0"                                |
| hypervisor_hostname             | String  | Server Info         | "esxi-node1.example.com"               |
| hypervisor_host_id              | String  | Server Info         | "host-1234"                            |
| hypervisor_id                   | String  | Server Info         | "4201ecf8-cc44-ee7e-01da-34dfb2acf6c0" |
| disk_read_iops_avg              | Float   | Storage Performance | 12.5                                   |
| disk_read_iops_peak             | Float   | Storage Performance | 245.0                                  |
| disk_write_iops_avg             | Float   | Storage Performance | 8.3                                    |
| disk_write_iops_peak            | Float   | Storage Performance | 180.0                                  |
| disk_total_iops_avg             | Float   | Storage Performance | 20.8                                   |
| disk_total_iops_peak            | Float   | Storage Performance | 425.0                                  |
| disk_read_throughput_avg_mbps   | Float   | Storage Performance | 1.2                                    |
| disk_read_throughput_peak_mbps  | Float   | Storage Performance | 24.5                                   |
| disk_write_throughput_avg_mbps  | Float   | Storage Performance | 0.8                                    |
| disk_write_throughput_peak_mbps | Float   | Storage Performance | 18.0                                   |
| disk_total_throughput_avg_mbps  | Float   | Storage Performance | 2.0                                    |
| disk_total_throughput_peak_mbps | Float   | Storage Performance | 42.5                                   |

#### Server performance metrics (server_performance_metrics.csv)

CPU, memory, and network throughput utilization. Sampled every 10 minutes, aggregated over 30 days.

| Name                        | Type    | Category    | Sample Value       |
| --------------------------- | ------- | ----------- | ------------------ |
| server_id                   | String  | Server Info | "vm-web-server-01" |
| data_source                 | String  | Server Info | "OS"               |
| cpu_utilization_avg_pct     | Float   | CPU         | 45.06              |
| cpu_utilization_peak_pct    | Float   | CPU         | 79.33              |
| cpu_count                   | Integer | CPU         | 4                  |
| memory_total_gb             | Float   | Memory      | 15.88              |
| memory_utilization_avg_pct  | Float   | Memory      | 29.27              |
| memory_utilization_peak_pct | Float   | Memory      | 63.99              |
| network_in_avg_mbps         | Float   | Network     | 0.52               |
| network_in_peak_mbps        | Float   | Network     | 12.3               |
| network_out_avg_mbps        | Float   | Network     | 0.31               |
| network_out_peak_mbps       | Float   | Network     | 8.7                |
| network_total_avg_mbps      | Float   | Network     | 0.83               |
| network_total_peak_mbps     | Float   | Network     | 21.0               |

#### Storage performance (server_storage_performance.csv)

Per-volume disk I/O and space utilization. Sampled every 10 minutes, aggregated over 30 days.

| Name                            | Type   | Category        | Sample Value       |
| ------------------------------- | ------ | --------------- | ------------------ |
| server_id                       | String | Server Info     | "vm-web-server-01" |
| data_source                     | String | Server Info     | "OS"               |
| disk_volume_id                  | String | Volume Info     | "/dev/nvme0n1p1"   |
| disk_mount_point                | String | Volume Info     | "/"                |
| file_system                     | String | Volume Info     | "xfs"              |
| disk_total_gb                   | Float  | Disk Space      | 30.0               |
| disk_used_gb                    | Float  | Disk Space      | 12.5               |
| disk_free_gb                    | Float  | Disk Space      | 17.5               |
| disk_read_iops_avg              | Float  | Disk I/O        | 12.5               |
| disk_read_iops_peak             | Float  | Disk I/O        | 245.0              |
| disk_write_iops_avg             | Float  | Disk I/O        | 8.3                |
| disk_write_iops_peak            | Float  | Disk I/O        | 180.0              |
| disk_total_iops_avg             | Float  | Disk I/O        | 20.8               |
| disk_total_iops_peak            | Float  | Disk I/O        | 425.0              |
| disk_read_throughput_avg_mbps   | Float  | Disk Throughput | 1.2                |
| disk_read_throughput_peak_mbps  | Float  | Disk Throughput | 24.5               |
| disk_write_throughput_avg_mbps  | Float  | Disk Throughput | 0.8                |
| disk_write_throughput_peak_mbps | Float  | Disk Throughput | 18.0               |
| disk_total_throughput_avg_mbps  | Float  | Disk Throughput | 2.0                |
| disk_total_throughput_peak_mbps | Float  | Disk Throughput | 42.5               |

#### Storage configuration (storage_config.csv)

Physical disk hardware details. Collected every 24 hours.

| Name                | Type   | Category    | Sample Value         |
| ------------------- | ------ | ----------- | -------------------- |
| server_id           | String | Server Info | "vm-web-server-01"   |
| disk_controller_id  | String | Disk Info   | "/dev/sda"           |
| vmdk_vhd_file_name  | String | Disk Info   | "web-server-01.vmdk" |
| disk_volume_type    | String | Disk Info   | "Virtual"            |
| disk_provisioned_gb | Float  | Disk Info   | 30.0                 |
| disk_device_type    | String | Disk Info   | "SCSI HDD"           |
| disk_interface_type | String | Disk Info   | "SCSI"               |
| disk_protocol       | String | Disk Info   | "LSI Logic SAS"      |

#### Network interfaces (network_interfaces.csv)

Network adapter configuration. Collected every 24 hours.

| Name                 | Type    | Category       | Sample Value               |
| -------------------- | ------- | -------------- | -------------------------- |
| server_id            | String  | Server Info    | "vm-web-server-01"         |
| interface_name       | String  | Interface Info | "eth0"                     |
| interface_index      | Integer | Interface Info | 2                          |
| mac_address          | String  | Interface Info | "0A:1B:2C:3D:4E:5F"        |
| adapter_type         | String  | Interface Info | "vmxnet3"                  |
| virtual_network_name | String  | Interface Info | "VM Network"               |
| virtual_network_id   | String  | Interface Info | "dvportgroup-1234"         |
| virtual_switch       | String  | Interface Info | "vSwitch0"                 |
| ipv4_address         | String  | IP Config      | "10.0.2.101"               |
| ipv4_subnet_mask     | String  | IP Config      | "255.255.255.0"            |
| ipv4_gateway         | String  | IP Config      | "10.0.2.1"                 |
| ipv6_address         | String  | IP Config      | "fe80::a1b:2cff:fe3d:4e5f" |
| ipv6_prefix_length   | Integer | IP Config      | 64                         |
| ipv6_gateway         | String  | IP Config      | "fe80::1"                  |
| dns_servers          | String  | IP Config      | "10.0.0.2"                 |
| dhcp_enabled         | Boolean | IP Config      | false                      |
| interface_status     | String  | Interface Info | "Up"                       |
| vlan_id              | Integer | Interface Info | 100                        |
| is_primary           | Boolean | Interface Info | true                       |

#### Running processes (process_metrics.csv)

Snapshot of running processes. Collected every hour, deduplicated over 30 days.

| Name                 | Type    | Category     | Sample Value        |
| -------------------- | ------- | ------------ | ------------------- |
| server_id            | String  | Server Info  | "vm-web-server-01"  |
| process_name         | String  | Process Info | "sshd"              |
| process_id           | Integer | Process Info | 1234                |
| process_command_line | String  | Process Info | "/usr/sbin/sshd -D" |
| process_user         | String  | Process Info | "root"              |

### Network collection

The Network collection module helps you discover dependencies among servers in your on-premises data center. This network data accelerates your migration planning by providing visibility into how applications communicate across servers.

This module collects network data for servers from all configured sources, including VMware, Hyper-V, and imported servers. It uses WinRM to collect data from Windows servers and uses SSH, SNMPv2, and SNMPv3 to collect data from Linux servers.

#### Network data collection

The Network collection module captures TCP IPv4 connections in ESTABLISHED or
TIME_WAIT state between servers in your discovered inventory. A connection
appears in the output only when both the source and target IP addresses belong
to servers that the discovery tool has discovered or that you have imported.
Connections to or from IP addresses outside your inventory — such as
external services, cloud endpoints, or servers not yet added to the discovery
tool — are not included.

This design focuses the network data on server-to-server dependencies within
your environment, which is the information needed for application dependency
mapping and migration wave planning.

These data points are collected for each connection:

- Source IP, port, process ID, and process name
- Target IP, port, process ID, and process name
- State (ESTABLISHED and TIME_WAIT)
- Transport protocol (TCP)
- IP version (IPv4)
- Count (number of times this unique connection was observed)

###### Tip

To maximize the completeness of your network dependency map, configure all
discovery sources (VMware, Hyper-V, and server CSV import) and add OS
credentials before reviewing network data. The more servers in your
inventory, the more connections the network module can capture.

#### Private address network collection

By default, the Network collection module only captures connections where both endpoints are servers in your discovered inventory. You can enable private address collection to also capture connections to and from RFC 1918 private IP addresses (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) that are not in your inventory.

###### To start private address collection

1. On the **Collector configuration** page, locate the **Collection modules** section.
2. Find **Network connections discovery** under **Application discovery**.
3. Open the **Actions** dropdown.
4. Choose **Start private address collection**.
5. If the module status was **Enabled**, you can see it change to **Enabled · Private Address on**.

To stop private address collection, open the **Actions** dropdown and choose **Stop private address collection**. Previously collected private address data is retained even after stopping.

Private address connections appear only in the full CSV export (inside the ZIP file), not in the MPA CSV files. If an IP address belongs to a server already in your inventory, it is always identified by its discovered server ID regardless of this setting.

This setting persists across restarts. You can start or stop private address collection at any time. Previously collected private address data is exported regardless of the current setting.

### Database collection

The Database collection module gathers database (SQL Server) information from Windows servers across all configured sources, including VMware, Hyper-V, and imported servers. The module uses the WinRM protocol to remotely connect to each Windows server and run PowerShell queries to get information about all installed SQL Server services (components) on the server by using WMI namespaces, registry, and file properties.

A SQL Server component is a specific service or feature instance installed as part of
a SQL Server deployment on a Windows server. The discovery tool collects Database
Engine, Analysis Services, Reporting Services, and Integration Services.

#### Database data collection

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

###### Note

Full format includes all service types. MPA format includes only database engine components. Not all fields are available depending on the SQL service type and configuration.
