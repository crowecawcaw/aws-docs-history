# Setting up the discovery tool

## Prerequisites

The following are the prerequisites for using the AWS Transform discovery tool:

###### General prerequisites

- The tool requires 4 vCPU, 16 GB of RAM, and a hard disk of at least 35 GB. 35 GB is the default; larger inventories require more disk. For guidance, see [Disk sizing and management](discovery-tool-disk-sizing.md "discovery-tool-disk-sizing.md").
- The tool collects data by using a centralized approach. Servers in scope must allow inbound connectivity from the discovery tool VM (default ports, custom port configuration is supported):

  - Linux – SSH TCP/22
  - Windows – TCP/5985 for HTTP, TCP/5986 for HTTPS
  - SNMP – UDP/161 (used for network collection only, not OS metrics)

- For Linux, user accounts that can use SSH to connect to the server. The discovery tool runs commands over SSH for network collection and OS metrics. Most commands run as a regular user. A small number of commands attempt sudo and fall back automatically if sudo is unavailable: `dmidecode` (server UUID and manufacturer), `lvdisplay` (LVM detection), and `ss` or `netstat` (network connections with process information). Without sudo, the discovery tool still collects the majority of data but UUID, LVM, and process-level network details will be missing. We recommend configuring passwordless sudo for the SSH user to ensure complete data collection. For a full breakdown, see [Required permissions for the discovery tool](discovery-tool-permissions.md "discovery-tool-permissions.md").
- For OS-level collection (OS metrics, network connections, and database discovery), target servers must run a supported operating system. For the supported target operating systems, see [Requirements for OS-level collection](discovery-tool-configure.md#discovery-tool-os-supported-platforms "discovery-tool-configure.md#discovery-tool-os-supported-platforms").

###### Appliance (OVA and VHD) prerequisites

- DHCP must be available on the network segment that the appliance connects to. The prebuilt Open Virtualization Appliance (OVA) and Virtual Hard Disk (VHD) images obtain an IP address by DHCP on the first boot, and you use that address to open the discovery tool console.
- The OVA and VHD appliances run Amazon Linux 2023. Your VMware or Hyper-V host must meet the Amazon Linux 2023 host requirements. See [VMware host requirements for running AL2023 on VMware](../../../linux/al2023/ug/vmware-supported-configurations.md#vmware-host-requirements "../../../linux/al2023/ug/vmware-supported-configurations.md#vmware-host-requirements") or [Hyper-V host requirements for running AL2023 on Hyper-V](../../../linux/al2023/ug/hyperv-supported-configurations.md#hyperv-host-requirements "../../../linux/al2023/ug/hyperv-supported-configurations.md#hyperv-host-requirements") in the _Amazon Linux 2023 User Guide_.

###### VMware prerequisites

- VMware vCenter Server version 6.5, 6.7, 7.0, or 8.0.
- Permissions to deploy an OVA into your VMware vCenter.
- For VMware vCenter Server setup, a vCenter user with the Read-Only role assigned at the root datacenter level. For details, see [Required permissions for the discovery tool](discovery-tool-permissions.md "discovery-tool-permissions.md").
- VMware Tools must be installed and running in each guest virtual machine. The discovery tool reads the guest IP address, hostname, fully qualified domain name (FQDN), guest operating system, and per-partition disk usage from VMware Tools. For more information, see [Guest agent requirements for OS-level collection](#discovery-tool-guest-agent "#discovery-tool-guest-agent").

###### Hyper-V prerequisites

- Windows Server with the Hyper-V role enabled.
- WinRM enabled on Hyper-V hosts.
- A user account that is a member of the **Remote Management Users**, **Hyper-V Administrators**, and **Performance Monitor Users** groups on each Hyper-V host, with WMI read access to the `root\cimv2` namespace. For details, see [Required permissions for the discovery tool](discovery-tool-permissions.md "discovery-tool-permissions.md").
- Supported authentication: NTLM (HTTPS only) and Kerberos (HTTP or HTTPS).
- Hyper-V Integration Services must be running in each guest virtual machine. The discovery tool reads the guest hostname and FQDN from Integration Services through Key-Value Pair (KVP) exchange. If Integration Services is not running, or the virtual machine is powered off, this data is empty. For more information, see [Guest agent requirements for OS-level collection](#discovery-tool-guest-agent "#discovery-tool-guest-agent").
- When you create the Hyper-V virtual machine, you must select **Generation 1**. Generation 2 virtual machines do not support the VHD format.

###### Server import prerequisites

- A CSV file with server hostnames or IP addresses and the credential names (optional) that map to the friendly names of the OS credentials configured or to be configured on the discovery tool. The CSV must use the following headers:

```
hostname_or_ip,os_credential_name,oracle_credential_name
```

- Servers must be reachable from the discovery tool VM. Default ports: SSH port 22 for Linux, WinRM port 5985/5986 for Windows. Custom ports are supported.

###### Linux installer prerequisites

- A supported Linux distribution: Amazon Linux 2, Amazon Linux 2023, RHEL 8–9, Rocky Linux 8–9, AlmaLinux 9, Ubuntu 20.04–24.04, Debian 10–12, or SLES 15 SP5.
- Minimum 4 vCPU, 16 GB RAM, 35 GB available disk space.
- Port 5000 must be available (not in use by another service).
- systemd is required for service management.
- The discovery tool VM must have network access to your target infrastructure. Default ports: vCenter on port 443, Hyper-V hosts on port 5985/5986, servers on port 22. Custom ports are supported for SSH, WinRM, and SNMP.

###### Oracle Database prerequisites

- Network access from the discovery tool to Oracle hosts on port 1521 (or custom port).
- Supported Oracle versions: You can collect Oracle Database 12c Release 1 (12.1) and later through direct SQL connections. OS-level fallback detection works with all Oracle versions.
- A read-only Oracle service account with SELECT\_CATALOG\_ROLE grant. For details, see [Oracle Database (SQL)](discovery-tool-permissions.md#discovery-tool-permissions-oracle "discovery-tool-permissions.md#discovery-tool-permissions-oracle").
- For OS-level fallback detection: SSH or WinRM access to the Oracle host (uses existing OS credentials).

### Guest agent requirements for OS-level collection

The discovery tool discovers virtual machines from vCenter or Hyper-V without any agent
in the guest. However, OS-level collection — OS performance and storage metrics,
network connection tracking, and SQL Server and Oracle database discovery — requires
a network address to connect to the guest operating system. The discovery tool obtains that
address, along with other guest details, from the guest agent. The guest agent is
**VMware Tools** on VMware and
**Hyper-V Integration Services** on
Hyper-V.

###### What the discovery tool collects without the guest agent

Hypervisor-side inventory is still collected: CPU, RAM, and disk configuration; power
state; virtual disk utilization; and hypervisor performance counters.

###### What the discovery tool cannot collect without the guest agent

The guest IP address, hostname, FQDN, guest operating system, and per-partition free
space are unavailable. As a result, OS metrics, network connection, SQL Server, and Oracle
collection have no address to connect to, and Kerberos authentication has no FQDN for
service principal name (SPN) matching.

- **VMware** – The `guest.*` properties, including the guest FQDN, come from VMware Tools running in the guest. They are unavailable if VMware Tools is not installed or not running.
- **Hyper-V** – Guest OS detection uses Hyper-V KVP exchange and requires Integration Services running in the guest. It returns an empty value if Integration Services is not installed or the virtual machine is powered off.

If the guest agent is not available, you can supply each server's IP address directly by
importing servers from a CSV file, which bypasses the guest-agent dependency for OS-level
collection. For more information, see [Import servers](discovery-tool-configure.md#discovery-tool-bare-metal-import "discovery-tool-configure.md#discovery-tool-bare-metal-import").
