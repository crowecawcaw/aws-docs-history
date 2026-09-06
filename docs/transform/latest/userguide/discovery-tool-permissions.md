

# Required permissions for the discovery tool
<a name="discovery-tool-permissions"></a>

The discovery tool connects to your infrastructure using several protocols. Each protocol and collection module requires specific account permissions. This section describes the minimum permissions needed for complete data collection, and what data you lose if certain permissions are unavailable.

## VMware vCenter
<a name="discovery-tool-permissions-vmware"></a>

The discovery tool connects to VMware vCenter Server on port 443 (HTTPS) and performs read-only operations. No changes are made to your vCenter environment.

**Minimum required role:** Read-Only, assigned at the vCenter root level.

The Read-Only role provides all the access the discovery tool needs to collect VM inventory (name, UUID, CPU, memory, disk, network, power state, guest OS) and performance metrics (CPU utilization, memory utilization, disk IOPS and throughput).

**Recommendation:** Create a dedicated vCenter user with the built-in Read-Only role at the root datacenter level.

## Hyper-V hosts (Windows)
<a name="discovery-tool-permissions-hyperv"></a>

The discovery tool connects to Hyper-V hosts over WinRM (port 5985 for HTTP, port 5986 for HTTPS) and runs PowerShell commands to collect VM inventory, host metadata, and storage performance.

**Minimum required group memberships** on each Hyper-V host:


| Windows group | Why it's needed | 
| --- | --- | 
| Remote Management Users | Baseline WinRM remote access | 
| Hyper-V Administrators | VM inventory collection (VM list, disk, network, memory, guest OS) | 
| Performance Monitor Users | Storage I/O performance counters (read/write IOPS and throughput per VM) | 

The account also needs WMI read access to the `root\cimv2` namespace for host OS version and hardware UUID. This access is granted by default for local administrators but must be configured explicitly for non-administrator accounts.

**Recommendation:** Create a dedicated domain service account and add it to the Remote Management Users, Hyper-V Administrators, and Performance Monitor Users groups on each Hyper-V host. Avoid using domain administrator accounts.

## Linux servers (SSH)
<a name="discovery-tool-permissions-linux"></a>

The discovery tool connects to Linux servers over SSH (port 22) to collect OS metrics, network connections, and server inventory. Most data collection runs as a regular user. A small number of commands attempt `sudo` and automatically fall back if sudo is unavailable.

**Minimum required access:** An SSH user account that can log in to the target server.

**Recommended access:** The same SSH user configured with passwordless sudo for complete data collection.

**What requires sudo and what happens without it:**


| Data collected | Sudo needed? | What you lose without sudo | 
| --- | --- | --- | 
| Server name, OS, CPU, memory, IP, disk count | No | Nothing — collected as regular user | 
| CPU, memory, and network utilization | No | Nothing — collected as regular user | 
| Disk IOPS, throughput, and space | No | Nothing — collected as regular user | 
| Network interface configuration | No | Nothing — collected as regular user | 
| Running processes (name, PID, command) | No | Nothing — collected as regular user | 
| Server UUID and SMBIOS UUID | Yes | UUID fields are empty in the export | 
| Hardware manufacturer (physical vs. virtual detection) | Yes | Resource type detection is less accurate on older distributions | 
| LVM logical volume detection | Yes | LVM volumes not detected; volume type may show as "Unknown" | 
| Network connections with process name and PID | Yes | Connections are still collected, but without process attribution (PID and process name columns are empty) | 
| Oracle Database OS-level detection (fallback when Oracle credentials are not configured) | Yes | Basic Oracle presence detection (oratab, process monitor) works without sudo. Detailed collection (opatch, lsnrctl, ASM, Grid Infrastructure) requires passwordless sudo -u oracle access to the Oracle home binaries. | 

**Note**  
The discovery tool never fails entirely due to lack of sudo. It collects what it can and reports partial results. However, for the most complete data — especially network dependency mapping with process names — we recommend passwordless sudo.

**Required utilities on target servers:** The following commands should be available (installed by default on most Linux distributions): `ss` or `netstat`, `lsblk`, `top`, `ps`, `free`, `ip`, `df`, `hostname`, `cat`, `nproc`, and `grep`. Optional for additional data: `iostat` (disk I/O detail), `dmidecode` (hardware UUID), `smartctl` (disk interface type), `lvdisplay` (LVM detection).

## Windows servers (WinRM) — OS metrics
<a name="discovery-tool-permissions-windows-os"></a>

The discovery tool connects to Windows servers over WinRM to collect OS metrics (server inventory, performance, storage, network interfaces, and running processes).

**Minimum required access:** A WinRM-enabled user account with remote access to the target server.

**Recommended access:** A user in the local Administrators group for complete data collection.


| Permission level | What it enables | What you lose without it | 
| --- | --- | --- | 
| Remote Management Users (WinRM access) | All Windows data collection | No data collected from the server | 
| WMI read access to root\\cimv2 | Server name, OS version, memory, UUID, BIOS serial, disk space | Server inventory fields are empty | 
| Performance Monitor Users | CPU utilization, network throughput, disk IOPS and throughput | Performance metrics not collected | 
| Local Administrator | Running process owner names | Process list collected but the user/owner column is empty | 

**Note**  
Local Administrator membership implicitly grants Performance Monitor Users access and WMI read access, so it satisfies all requirements above.

**Note**  
Oracle Database OS-level fallback detection on Windows uses registry queries and `Get-Service` and `Get-Process` commands when Oracle credentials are not configured. These commands require only standard Remote Management Users access. No additional permissions beyond OS metrics requirements are needed.

## Windows servers (WinRM) — SQL Server collection
<a name="discovery-tool-permissions-windows-db"></a>

SQL Server collection discovers SQL Server instances, Reporting Services (SSRS), and Integration Services (SSIS) on Windows servers.

**Recommended access:** A user in the local Administrators group on each target Windows server.

Local Administrator is recommended because SQL Server discovery queries multiple WMI namespaces and requires elevated access for some operations:


| What is discovered | Permission needed | What you lose without it | 
| --- | --- | --- | 
| SQL Server Database Engine instances (version, edition, status) | WMI read access to root\\Microsoft\\SqlServer\\ComputerManagement\* namespaces | SQL Server instances not discovered | 
| SQL Server Reporting Services (SSRS) | WMI read access to root\\Microsoft\\SqlServer\\ReportServer namespaces | SSRS components not discovered | 
| SSRS URL and port configuration | Elevated privileges (Local Admin) | SSRS URL reservation details missing | 
| SQL Server Integration Services (SSIS) | Registry read access (HKLM) | SSIS version and edition missing | 
| Port-to-service association | Access to TCP listener enumeration | Cannot associate listening ports with SQL Server services | 

**Note**  
SQL Server collection is Windows-only. The discovery tool skips Linux servers for SQL Server discovery.

## Oracle Database (SQL)
<a name="discovery-tool-permissions-oracle"></a>

Oracle Database collection connects directly to Oracle instances on port 1521 (or a custom port) to collect database metadata. The discovery tool does not require DBA or SYSDBA privileges.

**Minimum required access:** A read-only Oracle service account with the SELECT\_CATALOG\_ROLE grant.

The discovery tool does not access Diagnostics Pack or Tuning Pack views, so no additional Oracle license is required for data collection.

**SQL to create the account:**

```
CREATE USER discovery_user IDENTIFIED BY <password>;
GRANT CREATE SESSION TO discovery_user;
GRANT SELECT_CATALOG_ROLE TO discovery_user;
```

**OS-level fallback:** If database credentials are not configured or the connection fails, the discovery tool uses existing SSH or WinRM OS credentials to detect Oracle installations. No additional Oracle-specific OS permissions are needed beyond what the OS metrics module requires.

## Network collection
<a name="discovery-tool-permissions-network"></a>

Network collection uses different protocols depending on the server's operating system:


| Server OS | Protocol | Permissions needed | 
| --- | --- | --- | 
| Linux | SSH | Regular user for connection data. Passwordless sudo recommended for process-level details (PID and process name). | 
| Linux | SNMPv2 | A read-only community string with access to the TCP MIB (tcpConnState, tcpConnectionProcess) and Host Resources MIB (hrSWRunName). | 
| Linux | SNMPv3 | A USM user with read access to the same MIBs as SNMPv2. Supports noAuthNoPriv, authNoPriv, and authPriv security levels. | 
| Windows | WinRM | WMI read access to the root\\StandardCIMV2 namespace (MSFT\_NetTCPConnection class). | 

## Quick reference: Minimum permissions by use case
<a name="discovery-tool-permissions-quick-ref"></a>


| Use case | Account type | Minimum permissions | 
| --- | --- | --- | 
| VMware VM discovery | vCenter user | Read-Only role at root datacenter level | 
| Hyper-V VM discovery | Windows domain or local account | Remote Management Users \+ Hyper-V Administrators \+ Performance Monitor Users on each host | 
| Linux OS metrics — full data | SSH user | Passwordless sudo | 
| Linux OS metrics — partial data | SSH user | Regular user (no sudo). UUID, manufacturer, LVM, and network process info will be missing. | 
| Windows OS metrics — full data | WinRM user | Local Administrator | 
| Windows OS metrics — basic data | WinRM user | Remote Management Users \+ WMI read access to root\\cimv2 | 
| SQL Server database discovery | WinRM user | Local Administrator | 
| Oracle database discovery (SQL) | Oracle service account | SELECT\_CATALOG\_ROLE (read-only, no DBA or SYSDBA) | 
| Network collection — Linux (SSH) | SSH user | Passwordless sudo for process-level data; regular user for connection data only | 
| Network collection — Linux (SNMP) | SNMP community string or USM user | Read access to TCP and Host Resources MIBs | 
| Network collection — Windows | WinRM user | WMI read access to root\\StandardCIMV2 | 