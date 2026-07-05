# Setting up the discovery tool

## Prerequisites

The following are the prerequisites for using the AWS Transform discovery tool:

**General prerequisites**

- The tool requires 4 vCPU, 16 GB of RAM, and a 35 GB hard disk.
- DHCP must be available in the network for the discovery tool VM.
- The tool collects data by using a centralized approach. Servers in scope must allow inbound connectivity from the discovery tool VM (default ports, custom port configuration is supported):

  - Linux – SSH TCP/22
  - Windows – TCP/5985 for HTTP, TCP/5986 for HTTPS
  - SNMP – UDP/161 (used for network collection only, not OS metrics)

- For Linux, user accounts that can use SSH to connect to the server. The discovery tool runs commands over SSH for network collection and OS metrics. Most commands run as a regular user. A small number of commands attempt sudo and fall back automatically if sudo is unavailable: `dmidecode` (server UUID and manufacturer), `lvdisplay` (LVM detection), and `ss` or `netstat` (network connections with process information). Without sudo, the discovery tool still collects the majority of data but UUID, LVM, and process-level network details will be missing. We recommend configuring passwordless sudo for the SSH user to ensure complete data collection. For a full breakdown, see [Required permissions for the discovery tool](discovery-tool-permissions.md "discovery-tool-permissions.md").

**VMware prerequisites**

- VMware vCenter Server version 6.5, 6.7, 7.0, or 8.0.
- Permissions to deploy an OVA into your VMware vCenter.
- For VMware vCenter Server setup, a vCenter user with the Read-Only role assigned at the root datacenter level. For details, see [Required permissions for the discovery tool](discovery-tool-permissions.md "discovery-tool-permissions.md").

**Hyper-V prerequisites**

- Windows Server with the Hyper-V role enabled.
- WinRM enabled on Hyper-V hosts.
- A user account that is a member of the **Remote Management Users**, **Hyper-V Administrators**, and **Performance Monitor Users** groups on each Hyper-V host, with WMI read access to the `root\cimv2` namespace. For details, see [Required permissions for the discovery tool](discovery-tool-permissions.md "discovery-tool-permissions.md").
- Supported authentication: NTLM (HTTPS only) and Kerberos (HTTP or HTTPS).

**Server import prerequisites**

- A CSV file with server hostnames or IP addresses and the credential names (optional) that map to the friendly names of the OS credentials configured or to be configured on the discovery tool. The CSV must use the following headers:

```
hostname_or_ip,os_credential_name,oracle_credential_name
```

- Servers must be reachable from the discovery tool VM. Default ports: SSH port 22 for Linux, WinRM port 5985/5986 for Windows. Custom ports are supported.

**Linux installer prerequisites**

- A supported Linux distribution: Amazon Linux 2, Amazon Linux 2023, RHEL 8–9, Rocky Linux 8–9, AlmaLinux 9, Ubuntu 20.04–24.04, Debian 10–12, or SLES 15 SP5.
- Minimum 4 vCPU, 16 GB RAM, 35 GB available disk space.
- Port 5000 must be available (not in use by another service).
- systemd is required for service management.
- The discovery tool VM must have network access to your target infrastructure. Default ports: vCenter on port 443, Hyper-V hosts on port 5985/5986, servers on port 22. Custom ports are supported for SSH, WinRM, and SNMP.

**Oracle Database prerequisites**

- Network access from the discovery tool to Oracle hosts on port 1521 (or custom port).
- Supported Oracle versions: You can collect Oracle Database 12c Release 1 (12.1) and later through direct SQL connections. OS-level fallback detection works with all Oracle versions.
- A read-only Oracle service account with SELECT\_CATALOG\_ROLE grant. For details, see [Oracle Database (SQL)](discovery-tool-permissions.md#discovery-tool-permissions-oracle "discovery-tool-permissions.md#discovery-tool-permissions-oracle").
- For OS-level fallback detection: SSH or WinRM access to the Oracle host (uses existing OS credentials).
