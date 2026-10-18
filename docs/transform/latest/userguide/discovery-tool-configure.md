

# Configure the discovery tool
<a name="discovery-tool-configure"></a>

## Access the discovery tool console
<a name="discovery-tool-access-console"></a>

1. In a web browser access: `https://{{ip_address}}:5000`, where {{ip\_address}} is the IP address of the discovery tool from Deploy Discovery Tool. The discovery tool uses a self-signed certificate for HTTPS connection which results in a security warning. Choose **Accept the risk and continue** to continue to the discovery tool console.

1. If you're accessing the discovery tool console for the first time, create a discovery tool login password. Create a password, which you will use for future logins.
**Important**  
Remember this password - there is no password recovery mechanism.

## Accessing the discovery tool VM
<a name="discovery-tool-vm-access"></a>
+ The discovery tool VM comes by default with a username and password ("discovery", "password"). For strong security, we recommend that you update the password by using `sudo passwd discovery` after logging into the VM through your hypervisor's console (for example, vSphere Client for VMware or Hyper-V Manager for Hyper-V).
+ SSH access is disabled by default. Users can use preconfigured `enablessh` and `disablessh` aliases to enable/disable SSH access to the discovery tool VM. Users can SSH into the VM via `ssh discovery@<VM-IP>` after enabling SSH access. Users are encouraged to keep SSH access disabled most of the times and enable it only while actively required. Password change is enforced when running `enablessh`.
+ The discovery tool data directory is at `/home/discovery/.local/share/DiscoveryTool` on the standard OVA and VHD appliance, where the default VM user is `discovery`. On a Linux installer deployment, the data directory is under the home directory of whichever user ran the installer, not necessarily `discovery`. To find the exact path on any deployment, run `systemctl show discovery-tool -p Environment` and look for `DT_DATA_DIR`. If `DT_DATA_DIR` is not listed, the data directory is `.local/share/DiscoveryTool` under the home directory of the user that runs the service.

## Configure Kerberos authentication
<a name="security-kerberos"></a>

Kerberos authentication is the recommended method for connecting to Windows servers from the discovery tool. The discovery tool VM uses native Amazon Linux 2023 Kerberos libraries to authenticate against your Active Directory domain.

The following are key points about Kerberos authentication on the discovery tool VM:
+ Use the `kinit` command to obtain a Kerberos ticket and `klist` to verify the ticket.
+ The Kerberos configuration file is located at `/etc/krb5.conf`.
+ Before you configure the discovery tool, verify that `kinit` succeeds from the CLI on the discovery tool VM.

### Kerberos prerequisites
<a name="kerberos-prerequisites"></a>

Before you configure Kerberos authentication, verify that you have the following information and network connectivity.

1. Obtain the following information from your Active Directory administrator:
   + The Kerberos realm name (typically your domain name in uppercase, for example, `EXAMPLE.COM`).
   + The hostname or IP address of the Key Distribution Center (KDC), which is typically a domain controller (for example, `dc01.example.com`).
   + A service account with permissions to authenticate against the target Windows servers.

1. Verify that the discovery tool VM has network connectivity to the following:
   + The KDC on port 88 (TCP and UDP) for Kerberos authentication.
   + The target Windows servers on Windows Remote Management (WinRM) ports (5985 for HTTP, 5986 for HTTPS).

### Configure Kerberos
<a name="kerberos-configuration"></a>

Complete the following steps to configure Kerberos authentication on the discovery tool VM.

1. SSH to the discovery tool VM.

   ```
   ssh discovery@<discovery-tool-vm-ip>
   ```

1. Edit the Kerberos configuration file at `/etc/krb5.conf`.

   ```
   sudo nano /etc/krb5.conf
   ```

   Add the following configuration, replacing the placeholder values with your environment details.

   ```
   [libdefaults]
       default_realm = EXAMPLE.COM
       dns_lookup_realm = false
       dns_lookup_kdc = true
   
   [realms]
       EXAMPLE.COM = {
           kdc = dc01.example.com
       }
   
   [domain_realm]
       .example.com = EXAMPLE.COM
       example.com = EXAMPLE.COM
   ```
**Important**  
Kerberos is case-sensitive. The realm name must be in uppercase (for example, `EXAMPLE.COM`, not `example.com`). The domain name in the `[domain_realm]` section must be in lowercase.

   **Multiple Active Directory domains**

   The discovery tool supports multiple Kerberos credentials for different Active Directory domains. Each credential authenticates independently, so you can configure multiple credentials normally and isolation is automatic.

   If you have servers in multiple domains, add entries for each realm in your `/etc/krb5.conf` file:

   ```
   [libdefaults]
       default_realm = DEV.COMPANY.COM
       dns_lookup_realm = false
       dns_lookup_kdc = true
   
   [realms]
       DEV.COMPANY.COM = {
           kdc = dc01.dev.company.com
       }
       PROD.COMPANY.COM = {
           kdc = dc01.prod.company.com
       }
   
   [domain_realm]
       .dev.company.com = DEV.COMPANY.COM
       dev.company.com = DEV.COMPANY.COM
       .prod.company.com = PROD.COMPANY.COM
       prod.company.com = PROD.COMPANY.COM
   ```

1. Verify that you can obtain a Kerberos ticket by running the `kinit` command.

   ```
   kinit username@REALM.COM
   ```

   Enter the password when prompted. If the command completes without errors, authentication succeeded.

1. Verify the ticket by running the `klist` command.

   ```
   klist
   ```

   The expected output is similar to the following.

   ```
   Ticket cache: FILE:/tmp/krb5cc_1000
   Default principal: username@REALM.COM
   
   Valid starting       Expires              Service principal
   01/01/2025 12:00:00  01/01/2025 22:00:00  krbtgt/REALM.COM@REALM.COM
   ```

1. Configure the discovery tool with the same case-sensitive principal that you used with `kinit` (for example, `username@REALM.COM`).

An explicit `krb5.conf` configuration might not be required if your environment has DNS SRV records configured for Kerberos service discovery. For more information about Kerberos configuration options, see the [MIT Kerberos krb5.conf documentation](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html) and the [sample krb5.conf file](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html#sample-krb5-conf-file).

### Find Kerberos configuration from domain-joined machines
<a name="kerberos-find-config"></a>

If you don't have the Kerberos configuration details, you can retrieve them from a Windows machine that is joined to the domain. Run the following commands from a command prompt on the domain-joined machine.

To find the domain name, run the following command.

```
echo %USERDNSDOMAIN%
```

Example output:

```
EXAMPLE.COM
```

To find the domain controller hostname, run the following command.

```
nltest /dsgetdc:EXAMPLE.COM
```

Example output:

```
           DC: \\dc01.example.com
      Address: \\10.0.1.100
     Dom Guid: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
     Dom Name: EXAMPLE.COM
  Forest Name: example.com
 Dc Site Name: Default-First-Site-Name
Our Site Name: Default-First-Site-Name
        Flags: 0xe00033fd
The command completed successfully
```

Map the output to your `krb5.conf` configuration as follows:
+ **Realm** – Use the value from `%USERDNSDOMAIN%` in uppercase (for example, `EXAMPLE.COM`).
+ **KDC** – Use the DC hostname from the `nltest` output (for example, `dc01.example.com`).

### Using Kerberos with IP addresses
<a name="kerberos-ip-addresses"></a>

Kerberos identifies each target server by a service principal name (SPN). The SPN is built from the server's fully qualified domain name (FQDN), such as `WSMAN/server01.example.com`. If the server does not recognize the `WSMAN` SPN, the discovery tool falls back to `HTTP/server01.example.com`. Active Directory does not register SPNs for IP addresses.

When the discovery tool knows a server's FQDN, it uses the FQDN first for Kerberos credentials. The discovery tool learns the FQDN from guest metadata reported by VMware Tools on VMware, or by Integration Services on Hyper-V. Most servers that the discovery tool finds through VMware or Hyper-V discovery have an FQDN, so you do not need to do anything for those servers. A server that you import from a CSV file with only an IP address has no FQDN.

The discovery tool also tries any IP addresses it has for a server. An IP address works with Kerberos when the discovery tool can map that IP address to the FQDN with a reverse DNS lookup. Reverse DNS is a best-effort fallback, not a requirement. Set it up only if a server has no FQDN, and you want to use Kerberos with that server. The lookup needs one of the following:
+ **A PTR record** – A PTR record for that IP address in your DNS or Active Directory. A PTR record maps an IP address to a host name. It is the reverse of the A record, which maps a host name to an IP address. Many Active Directory domains add PTR records for you when a server joins, so the record might already exist.
+ **An `/etc/hosts` entry** – An entry in `/etc/hosts` on the discovery tool VM, in the form `<ip-address> <fqdn> <short-name>`. Use this when you cannot change DNS. You do not need a DNS administrator.

Reverse lookups must also be turned on for the VM. They are on by default. Do not set `rdns = false` or `dns_canonicalize_hostname = false` in `/etc/krb5.conf`. If either setting is already `false`, Kerberos keeps the IP address in the SPN instead of replacing it with the FQDN, and authentication fails with a `Server not found in Kerberos database` error even when the reverse mapping exists. Remove the setting, or set it to `true`.

To check reverse lookups, run the following command on the discovery tool VM.

```
getent hosts <target-ip>
```

The command returns the server's FQDN when reverse lookups work. It reads both `/etc/hosts` and DNS. If it does not return the FQDN, add a PTR record, add an `/etc/hosts` entry, or use the FQDN instead.

**Note**  
If no reverse mapping exists, authentication fails with `Server not found in Kerberos database`. This is a principal lookup failure, not a rejected password. It does not count toward Active Directory account lockout.

## Configure vCenter access
<a name="discovery-tool-vcenter-config"></a>

1. On the **Discovery tool** page, under **Step 1. Configure discovery sources**, choose **Configure sources**.

1. On the **Configure discovery sources** page, provide the **Friendly name**, **vCenter FQDN/IP**, **Username**, and **Password**.

1. Choose **Save configuration**.

   The discovery tool begins to collect vCenter information, as described in [Discovered Inventory](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool-data-collection.html#discovery-tool-inventory).

After initial configuration choose **Edit vCenter access** in the **Discovery tool status** frame to change your vCenter access settings. 

The discovery tool collects from all configured vCenter servers in parallel. If one vCenter server is unreachable during collection, the tool reports partial success and continues collecting from the remaining vCenter servers.

If a VM appears on multiple vCenter servers (for example, due to shared ESXi hosts or cross-vCenter vMotion), the discovery tool automatically deduplicates VMs. Each unique VM appears only once in the inventory.

## Configure Hyper-V access
<a name="discovery-tool-hyperv-config"></a>

1. On the **Discovery tool** page, under **Step 1. Configure discovery sources**, choose **Configure sources**.

1. On the **Configure discovery sources** page, provide a **friendly name**, the **host FQDN or IP address**, the **authentication type (NTLM or Kerberos)**, the **WinRM username**, and the **WinRM password**.

1. Choose **Save configuration**.

   The discovery tool begins to collect Hyper-V information, as described in [Discovered inventory](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool-data-collection.html#discovery-tool-inventory).

Collection begins automatically after you save the credentials.

For Hyper-V failover clusters, you can add multiple hosts in the same cluster. The tool automatically deduplicates VMs that appear on more than one host.

## Import servers
<a name="discovery-tool-bare-metal-import"></a>

1. Navigate to the **Import servers** page from the Discovery tool homepage.

1. Prepare a CSV file with the following columns: `hostname_or_ip` (required), `os_credential_name` (optional), and `oracle_credential_name` (optional).
   + The `hostname_or_ip` value must be a valid IPv4 address or a fully qualified domain name (FQDN).
   + The `os_credential_name` value, if provided, must match the friendly name of an OS credential that you already configured (SSH, WinRM, or SNMP). Leave empty for servers where you have not yet configured an OS credential.
   + The `oracle_credential_name` value, if provided, must match the friendly name of an Oracle credential that you already configured.

1. Upload the CSV file. The tool validates all rows and rejects the file if any row is invalid.

After a successful import, the tool automatically begins database, network and OS metrics collection for the imported servers, if OS credentials are configured. If you upload another CSV file, existing records are updated without creating duplicates and new records are merged into the inventory.

## Import a self-signed certificate authority into the discovery tool (Optional)
<a name="security-certificate-authority"></a>

This is required when you use WinRM over HTTPS and target servers using WinRM HTTPS certificates signed by a self-signed Certificate Authority (CA), and you want to enable "Validate server SSL certificate" on the discovery tool.

### Prerequisites
<a name="certificate-prerequisites"></a>

1. Self-signed CA certificate that was used to sign the WinRM HTTPS certificates on target servers

1. Certificate in PEM format (.pem or .crt extension)

To import a self-signed certificate authority on the discovery tool VM:

1. Ssh to Discovery tool VM

1. Place the CA certificate(s) that signed your target servers' WinRM certificates into trust store directory `/etc/pki/ca-trust/source/anchors/` on the discovery tool VM. For example: `sudo cp winrm-ca.pem /etc/pki/ca-trust/source/anchors/winrm-ca.pem`. Note: If your target servers use certificates signed by different CAs, copy all relevant CA certificates to this directory.

1. Update the certificate trust store: `sudo update-ca-trust`

1. Reboot the VM

1. (Optional) To verify that certificates have been successfully imported, you can run the following command. `sudo trust list —filter=ca-anchors | grep -A 5 "<certificate_name>"`

See [Installation and configuration for Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management)

## Configure the discovery tool for OS access
<a name="discovery-tool-os-access"></a>

Configure OS access so that the discovery tool can: 
+ Discover databases to perform database assessment and to assist in VM migration, 
+ Track network connections between servers in your inventory, including the process associated with each connection, to assist in application dependency mapping and wave planning. Only connections where both endpoints are in the discovery tool's inventory are included.

**Enable discovery tool OS Access**

1. Navigate to the **Set up OS access** page to provide Windows and Linux credentials.

1. Choose a protocol that you want to add credentials for.

1. Provide the required credentials for the selected protocol.

1. Select **Auto-connect** to enable the discovery tool to try all provided credentials on discovered servers until matching credentials are found for each server.

   See [Using Auto-Connect Feature With Caution](discover-tool-security.md#auto-connect-caution) for important security recommendations regarding the auto-connect feature.

1. Choose **Set up and connect**.

When the OS matching process is completed, you see a message that the data collection is in progress, and an error regarding servers for which a credentials match was not found.

### Requirements for OS-level collection
<a name="discovery-tool-os-supported-platforms"></a>

OS-level collection — server and storage performance metrics, network connection tracking, and SQL Server and Oracle database discovery — runs remotely against your target servers. The discovery tool installs no agent or software on them. The following are the requirements for a target server to be collected.

**Note**  
These requirements apply to the servers you are collecting data *from*. They are separate from the Linux distributions supported for the host you install the discovery tool *on*, which are listed in [Supported distributions for the installer host](discovery-tool-deploy-linux.md#discovery-tool-linux-supported-distros).

The following list describes the connectivity and account requirements for each type of target server.

Linux  
SSH reachable from the discovery tool VM on TCP/22 (or a custom port), and an account that can run shell commands. Network connection tracking can also use SNMP on UDP/161 instead of SSH. `sudo` is optional. Without it, the discovery tool still collects most data, but the server UUID, LVM detection, and process-level network connection details are missing. For details, see [Linux servers (SSH)](discovery-tool-permissions.md#discovery-tool-permissions-linux).

Windows  
WinRM enabled and reachable on TCP/5985 (HTTP) or TCP/5986 (HTTPS), or a custom port. The discovery tool runs all Windows commands through PowerShell remoting, so PowerShell must be present on the target server. PowerShell 3.0 or later provides full data coverage. For details, see [Windows servers (WinRM) — OS metrics](discovery-tool-permissions.md#discovery-tool-permissions-windows-os).  
If Windows PowerShell Transcription logging is enabled on your target servers, the discovery tool's frequent PowerShell commands can generate thousands of transcript files each day on each server. This can fill the target server's system disk quickly. See [Set up WinRM and WMI](#discovery-tool-winrm-setup) for the recommended mitigation before enabling collection on Windows targets.

Because collection uses standard operating system commands rather than an agent, the discovery tool works across a wide range of operating system versions, including older ones. The following operating systems are validated end to end. Other versions that meet the requirements in the preceding list are also collected.
+ **Linux** – Amazon Linux 2, Amazon Linux 2023, RHEL 7.9, Rocky Linux 9.7, AlmaLinux 9.7, SLES 12 SP5, Debian 11, Ubuntu 16.04, and Ubuntu 22.04
+ **Windows** – Windows Server 2012 R2, 2016, 2019, and 2022

On older operating systems, the discovery tool substitutes alternative commands and some fields can be empty:
+ Linux distributions released before `/etc/os-release` became standard — such as RHEL 6, CentOS 6, SLES 11, Ubuntu 14.04 and earlier, and Amazon Linux 1 — are identified from `/etc/*-release` or `uname` instead, which can report less detail.
+ Windows Server 2003 does not include PowerShell. Because the discovery tool runs all Windows commands through PowerShell remoting, it collects no OS-level data from these servers unless you install PowerShell and WinRM on them.
+ On servers that provide only PowerShell 2.0, such as Windows Server 2008, `Get-CimInstance` is unavailable. The discovery tool falls back to `Get-WmiObject` for basic server identity, but most other data, including performance and storage metrics, is unavailable.
+ Servers whose SSH service offers only legacy key exchange or host key algorithms, which is common on RHEL 6 and other distributions of that era, can refuse the connection. If a server cannot be reached over SSH but is reachable manually, verify which algorithms its SSH service offers.

### Supported protocols setup
<a name="discovery-tool-os-access-protocols"></a>

You must set up WinRM, SSH, and SNMP protocols on target servers for the discovery tool to communicate with them.

#### Set up WinRM and WMI
<a name="discovery-tool-winrm-setup"></a>

WinRM is automatically installed with all currently-supported versions of the Windows operating system.

To verify or edit WinRM configuration, use the `winrm` command line tool:
+ Verify installed WinRM listeners: `winrm enumerate winrm/config/listener`
+ Verify WinRM configurations: `winrm get winrm/config`
+ Example command to set up WinRM: `winrm quickconfig -transport:https`

**Listener Ports**

Default HTTP port is 5985; HTTPS is 5986. You can use other ports as needed. The ports must be open between the discovery tool and target servers.

**Encryption**

The discovery tool uses encrypted WinRM communication. We recommend that WinRM listeners on target servers also use encryption: `winrm set winrm/config/service '@{AllowUnencrypted="false"}'`

**NTLM vs Kerberos**

WinRM authentication protocols Kerberos and NTLM are supported by the discovery tool. NTLM can be used only with HTTPS and Kerberos can be used with both HTTP or HTTPS.

**WMI Requirements**

The discovery tool queries the following WMI namespaces. The WinRM account needs read access to each namespace relevant to your collection modules:


| WMI namespace | Used by | 
| --- | --- | 
| root\\cimv2 | OS metrics, Hyper-V host metadata, SQL Server collection | 
| root\\virtualization\\v2 | Hyper-V VM inventory | 
| root\\StandardCIMV2 | Network collection | 
| root\\Microsoft\\SqlServer\\ComputerManagement\* | SQL Server collection | 
| root\\Microsoft\\SqlServer\\ReportServer\\\* | SQL Server collection (SSRS) | 

For network collection, ensure these conditions are met:
+ Allow network connectivity via ICMP
+ Allow network connectivity via TCP port 135 \+ ephemeral TCP port range (49152 - 65535)
+ Disable UAC
+ Remote DCOM permissions are set up
+ Create a dedicated service account with minimal required permissions
+ WMI namespace permissions are set up for Windows accounts with namespaces: `\\root\\standardcimv2`, `MSFT_NetTCPConnection` class

For SQL Server collection, a Windows account (local or domain) belonging to the **Local Administrator Group** is required because of complex WMI objects permission requirements.

**PowerShell Transcription logging**

If Windows PowerShell Transcription logging is enabled on your target servers, every command that the discovery tool sends writes a transcript file to that server's local disk. The Group Policy key `HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\Transcription` controls this behavior, and a value of `EnableTranscripting = 1` turns it on. By default, transcription writes transcript files to the service account's Documents folder. If the Group Policy sets an `OutputDirectory`, transcription writes them to that path instead.

To check whether transcription is enabled on a target server, run the following command on that server in PowerShell:

```
Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\Transcription" -ErrorAction SilentlyContinue
```

If the command returns no output, transcription is not enabled by Group Policy. If it returns a property named `EnableTranscripting` with a value of `1`, transcription is active.

The discovery tool communicates with Windows targets approximately every 15 seconds for network data collection, generating thousands of transcript files each day on each server. This can fill the target server's system disk quickly, causing OS or application failures on monitored machines.

**Important**  
**Recommended mitigation:** Before enabling collection on Windows targets, ask your IT or domain administrator to create an exemption for the Windows service account used by the discovery tool from the **Turn on PowerShell Transcription** Group Policy setting (**Computer Configuration** > **Administrative Templates** > **Windows Components** > **Windows PowerShell**). The specific exemption mechanism depends on your domain's Group Policy structure. For User Configuration policies, security group filtering can target the account directly. For Computer Configuration policies, OU-scoped targeting is the typical approach.

If transcription logging is a compliance requirement, implement periodic cleanup of the transcript output directory to prevent disk exhaustion. In the default configuration, transcripts are written to the service account's Documents folder (`%USERPROFILE%\Documents`).

### Set up SSH
<a name="discovery-tool-ssh-setup"></a>
+ The default port is 22. Custom ports are supported. The configured port must be open between the discovery tool and target servers.
+ For SSH network collection to work properly, provide a user configured for passwordless sudo.
+ Ensure that the following commands are available on target Linux servers (installed by default on most distributions): `ss` or `netstat` for network collection, and `lsblk`, `iostat`, `dmidecode`, `smartctl`, `top`, `ps`, `free`, `ip`, and `df` for OS metrics collection.

The discovery tool supports two authentication methods for SSH:

**Option 1: Username and password**

Provide the SSH username and password. This is the default authentication method.

**Option 2: SSH private key**

Provide the SSH username and a private key in PEM format. To use this option, choose **SSH Key** from the **Authentication type** dropdown when configuring SSH credentials. If the private key is encrypted with a passphrase, enter the passphrase in the optional **Key Passphrase** field.

The following key formats are supported:
+ RSA
+ ECDSA
+ Ed25519
+ OpenSSH format
+ PKCS\#8 format

Both authentication methods support auto-connect. Credentials are stored encrypted at rest.

### Set up SNMP
<a name="discovery-tool-snmp-setup"></a>
+ The default port is 161/UDP. Custom ports are supported. The configured port must be open between the discovery tool and target servers.
+ For SNMP v2: Provide a read-only community string that can access TCP connection OIDs.
+ For SNMP v3: Provide username/password and auth/privacy details with read-only permission that can access TCP connection OIDs

The discovery tool requires access to:
+ `"1.3.6.1.2.1.6.13.1.1." (tcpConnState)`
+ `"1.3.6.1.2.1.6.19.1.8." (tcpConnectionProcess)`
+ `"1.3.6.1.2.1.25.4.2.1.2." (hrSWRunName)`

## Configure Oracle database access
<a name="discovery-tool-oracle-access"></a>

Configure Oracle database access to collect detailed Oracle database metadata directly through SQL connections. Collected metadata includes CDB and PDB topology, feature usage, and installed options. This data helps you plan Oracle database migrations more accurately. You can collect Oracle Database 12c Release 1 (12.1) and later through direct SQL connections. OS-level fallback detection works with all Oracle versions.

**Configure Oracle credentials in the discovery tool**

1. On the **Discovery tool** page, in the sidebar, choose **Database access**.

1. Choose **Add Oracle credential**.

1. Provide the following information:
   + **Friendly name** – A descriptive name for this credential (for example, `Oracle Production`).
   + **Port** – The Oracle listener port (default 1521).
   + **Service name** – The Oracle service name for the target database.
   + **Username** – The Oracle service account username.
   + **Password** – The Oracle service account password.
   + **Auto-connect** – Turn on this option to try the credential against all servers in your inventory. Turn off this option to manually assign the credential to specific servers.

1. To add more credentials (for example, for different Oracle environments), choose **Add Oracle credential** again.

1. Choose **Save and collect**. The discovery tool immediately starts a full Oracle collection round for all servers in your inventory.

**Credential modes**

When you configure Oracle credentials, you can choose between two modes:
+ **Manual** – Pin a credential to a specific server. The discovery tool uses that credential exclusively for that server. If the connection fails, no fallback occurs. Fix the credential configuration to resolve the issue.
+ **Auto-connect** – The discovery tool tries each auto-connect credential against every server in your inventory. When a credential succeeds for a server, the discovery tool uses that credential for all subsequent collection rounds.

**Detection flow**

When you configure Oracle credentials, the discovery tool first tries a direct SQL connection. If all database credentials fail, the tool falls back to OS-level detection through SSH or WinRM, so you can still discover Oracle installations without database access.

## Configure SQL Server database access
<a name="discovery-tool-sql-server-access"></a>

Configure SQL Server database credentials to collect additional information directly from SQL Server, such as database count, high-availability topology, and cluster role. Without database credentials, the discovery tool collects SQL Server information using your Windows credentials only.

**Prerequisites**
+ The SQL Server instance must be configured for SQL Server authentication (mixed-mode authentication). The discovery tool uses SQL authentication only. Windows domain logins are not supported.
+ The discovery tool appliance must have TCP access to the SQL Server port (default 1433) on each target server. Named instances on dynamic ports are not supported — the discovery tool connects by port number only.
+ Only Windows servers are attempted. Linux servers are skipped and report "OS not supported" even when a SQL Server credential is assigned.
+ SQL Server connections in this release are unencrypted. Servers with "Force Encryption" enabled cannot be collected using database credentials.

**Required SQL Server grants**

Create a dedicated SQL Server login with the following read-only grants:
+ `VIEW SERVER STATE` – Required to read high-availability topology data. A missing grant leaves the HA fields blank with a **Warning** status.
+ `VIEW ANY DEFINITION` – Required to read Always On availability group information. A missing grant causes the collection round to show a **Warning** status, with a message indicating the grant is likely missing.
+ `VIEW ANY DATABASE` – Required to enumerate databases. A missing grant silently undercounts databases without raising an error.

Run the following statements on the SQL Server instance to create the login. Replace `YourStrongPassword` with a strong, unique password:

```
USE master;
CREATE LOGIN atx_discovery WITH PASSWORD = 'YourStrongPassword';
GRANT VIEW SERVER STATE TO atx_discovery;
GRANT VIEW ANY DEFINITION TO atx_discovery;
GRANT VIEW ANY DATABASE TO atx_discovery;
```

**Configure SQL Server credentials in the discovery tool**

1. On the **Discovery tool** page, in the sidebar, choose **Database access**.

1. Choose **Add SQL Server credential**.

1. Provide the following information:
   + **Friendly name** – A descriptive name for this credential (for example, `SQL Server Production`).
   + **Port** – The SQL Server port (default 1433).
   + **Username** – The SQL Server login name.
   + **Password** – The SQL Server login password.
   + **Auto-connect** – Turn on to try the credential against all Windows servers in your inventory. Turn off to assign the credential to specific servers manually.

1. To add more credentials, choose **Add SQL Server credential** again.

1. Choose **Save and collect**. The discovery tool immediately starts a full SQL Server collection round for all Windows servers in your inventory.

You can monitor the collection result for each server on the **Discovered inventory** page.

SQL Server database credentials use the same auto-connect and manual assignment modes as Oracle credentials. For details, see [Using Auto-Connect Feature With Caution](discover-tool-security.md#auto-connect-caution).

## Updating the discovery tool
<a name="discovery-tool-updating"></a>

You can update the discovery tool using the built-in self-update feature, or manually by updating in place or redeploying a new appliance image.

### Self-update
<a name="discovery-tool-self-update"></a>

The discovery tool can update itself to a newer version without redeploying the appliance. A self-update preserves all collected data, discovery source configuration, and credentials. Collection is paused during the update and resumes automatically when it completes.

**Important**  
Self-update requires outbound internet access from the discovery tool appliance to download updates. It is disabled by default. If your appliance cannot reach the internet, use the manual update method described in [Manual update](#discovery-tool-manual-update).

**Prerequisites**
+ Outbound HTTPS access to the discovery tool's release location, `s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/`. If outbound traffic is restricted, allow this location. Because the discovery tool uses path-style Amazon S3 URLs, a filter that matches only on host name cannot scope below `s3.us-east-1.amazonaws.com`; use a filter that matches on the full URL path to limit access to this location. Path-based filtering requires a firewall that performs TLS inspection; because the discovery tool validates the server certificate against the appliance's trust store, that firewall's certificate authority must be trusted on the appliance, or self-update fails with a TLS error. No proxy configuration is supported.
+ Sufficient free disk space. The discovery tool checks available space before starting and refuses the update with an "insufficient space" error if there is not enough room for the installer, a database snapshot, and a safety margin. Free up disk space if you see this error.

**Enabling self-update**

1. On the **Discovery tool** page, choose **Software updates** in the sidebar.

1. Turn on **Automatically check for software updates**.

1. Make sure the discovery tool appliance has outbound internet access. No additional credentials are required to download updates.

**Note**  
If self-update is not enabled or your appliance cannot reach the internet, the discovery tool shows a reminder banner after 30 days to prompt you to update manually.

**Updating to a new version**

1. When a new version is available, an **Update available** banner appears on the dashboard. Choose **Review update**.

1. On the **Software updates** page, review the available version and release date. 
**Note**  
For major version updates, **Update now** is disabled until you confirm three readiness checkboxes: that you have exported a backup, that you understand collection halts during the update, and that you will not power off the appliance during the update.

1. Choose **Update now**. The discovery tool stops collection, installs the new version, and restarts. The **Software updates** page shows progress through each stage.

1. When the update completes, sign in again. The discovery tool resumes collection automatically.
**Note**  
If you see the banner "Update to version X failed. The appliance restored version Y" — the update failed but the discovery tool automatically restored the previous version. Your collected data is intact. Choose **Open update page** to retry.
**Important**  
If the page shows **Recovery required** — the browser timed out waiting for the update to complete. Choose **Reload page**. If the discovery tool is still not reachable after reloading, contact support.

**Automatic rollback**

If the new version fails to start correctly after installation, the discovery tool automatically restores the previous version. Your previously collected data is intact. The discovery tool does not offer the failed version again until you clear it. To clear it and retry, choose **Retry update** on the **Software updates** page.

### Manual update
<a name="discovery-tool-manual-update"></a>

If self-update is not available (for example, on appliances with no internet access, sometimes called air-gapped), you can update manually.

There are two ways to update:
+ **Update in place** – Updates the application inside your existing VM with the Linux installer. Your collected inventory, credentials, and configuration are preserved. This method needs operating system access to the discovery tool VM. We recommend this method.
+ **Redeploy from a new image** – Deploys a new VM from the latest OVA for VMware or VHD for Hyper-V. A new deployment starts with an empty database. Your existing data and configuration are not carried over unless you migrate them yourself.

Not every discovery tool version can update in place to every newer version. See [Minimum version for each update method](#discovery-tool-updating-min-version) for the minimum version each update method supports.

#### Updating in place with the Linux installer
<a name="discovery-tool-updating-in-place"></a>

This method runs on the existing VM. It keeps your database, which holds your collected data, discovery sources, and credentials, and it keeps the database encryption key. Use this method when you want to keep your existing configuration and collected data.

**Note**  
This method updates only the discovery tool application. It does not update anything on the VM host, such as the operating system version, the preconfigured shell aliases, or the networking and firewall rules. To get host updates, redeploy from a new image instead. For more information, see [Redeploying from a new image](#discovery-tool-updating-redeploy).

**Important**  
Complete the backup step before you update, so that you can restore your data if the update does not finish.

**To update the discovery tool in place**

1. Access the discovery tool VM through your hypervisor console, or through SSH after you run `enablessh`. For more information, see [Accessing the discovery tool VM](#discovery-tool-vm-access).

1. Get the latest installer script onto the VM, and make it executable. Choose one of the following:
   + If the VM has outbound internet access, download it directly:

     ```
     curl -O https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.sh
     ```
   + If the VM has no outbound internet access (for example, an air-gapped appliance), download the installer script on a machine that does have internet access, and then transfer it over SSH into the home directory of the discovery tool service user on the VM. If SSH access is disabled, first run `enablessh` on the discovery tool VM (see [Accessing the discovery tool VM](#discovery-tool-vm-access)).

   ```
   chmod +x AWS-Transform-discovery-tool.sh
   ```

1. Stop the discovery tool service so that the backup in the next step captures a consistent snapshot of the database.

   ```
   sudo ./AWS-Transform-discovery-tool.sh stop
   ```

1. Back up the data directory so that you can restore it if you need to. This command reads the data directory from the service's own configuration, so it works whether you are on the standard OVA/VHD appliance or a standalone Linux-installer host.

   ```
   SVC=discovery-tool.service
   DATA_DIR=$(systemctl show -p Environment --value "$SVC" | tr ' ' '\n' | sed -n 's/^DT_DATA_DIR=//p')
   if [ -z "$DATA_DIR" ]; then
     SVC_USER=$(systemctl show -p User --value "$SVC")
     DATA_DIR="$(getent passwd "$SVC_USER" | cut -d: -f6)/.local/share/DiscoveryTool"
   fi
   echo "Discovery Tool data directory: $DATA_DIR"
   if [ ! -d "$DATA_DIR" ]; then
     echo "ERROR: data dir not found - do NOT proceed"
   else
     BACKUP="$HOME/discovery-tool-backup-$(date +%F).tar.gz"
     sudo tar czf "$BACKUP" -C "$(dirname "$DATA_DIR")" "$(basename "$DATA_DIR")"
     echo "Backup created: $BACKUP ($(du -h "$BACKUP" | cut -f1))"; tar tzf "$BACKUP" | head
   fi
   ```

   The installer keeps the database encryption key. It does not change the key during an update.

1. Run the installer. It detects the existing installation and updates it in place, keeping your data directory, encryption key, and service user. The `--install-deps` flag installs any system packages that the new version requires and that are not already present, using your OS package manager (`yum`, `dnf`, `apt-get`, or `zypper`).
**Note**  
On an update, the installer always installs required system packages regardless of whether you pass `--install-deps`. This step only reaches out to your OS package repository if a required package is missing; it does not need network access if your appliance already has the required packages installed, which is typically the case on an appliance that is already running. If a package manager call does need network access and your appliance has none, host the packages in a local or mirrored repository that your package manager is configured to use, or install the missing packages manually before you run the installer.

   ```
   sudo ./AWS-Transform-discovery-tool.sh install --install-deps
   ```

1. Start the discovery tool service.

   ```
   sudo ./AWS-Transform-discovery-tool.sh start
   ```

1. Verify the update. Open `https://{{ip_address}}:5000` in a web browser, sign in, and confirm that the version is updated and that your discovery sources, credentials, and inventory are present.

#### Redeploying from a new image
<a name="discovery-tool-updating-redeploy"></a>

Use this method if you do not have operating system access to the VM, or if you prefer to deploy a new appliance. A redeployed VM starts with an empty database.

**To redeploy the discovery tool from a new image**

1. Download the latest image file: the OVA for VMware or the VHD for Hyper-V.

1. (Optional) Delete the previous discovery tool image file before you deploy the latest one.

1. Deploy the new version. For VMware, see [Deploy on VMware](discovery-tool-deploy-vmware.md). For Hyper-V, see [Deploy on Hyper-V](discovery-tool-deploy-hyperv.md).

1. Configure your discovery sources, credentials, and server imports again on the new VM.

**Note**  
If you want to deploy a new discovery tool and keep the data and configuration that you already collected, contact AWS Support before you begin.

#### Minimum version for each update method
<a name="discovery-tool-updating-min-version"></a>

Not every version of the discovery tool can update in place to every newer version. Some older versions renamed internal configuration keys without carrying old values forward, so updating in place from a version older than the minimum shown below can silently drop collected data or settings. The following table shows, for each update method, the oldest version you can update **from**.


| Update method | Minimum version to update from | Notes | 
| --- | --- | --- | 
| Redeploy from a new image | 1.0.0 | Always available. Starts with an empty database, so nothing to preserve. | 
| Manual update (in place) | 1.0.2325 | Updating in place from a version older than 1.0.2325 can silently stop scheduled collection for one or more modules, or cause the discovery tool to fail to start, depending on your starting version. If you are on an older version, redeploy from a new image instead. | 
| Self-update | 1.0.2810 | Self-update is available starting in 1.0.2810. Appliances on an earlier version do not have the self-update feature and must update manually or redeploy. | 

## Revoking access
<a name="discovery-tool-revoking"></a>

You can revoke access for each discovery source independently. When you revoke access for one source, data from other sources is not affected.
+ **Revoking vCenter access** – Deletes vCenter credentials and VMware-collected data. Does not delete Hyper-V data, imported server data, or OS credentials.
+ **Revoking Hyper-V access** – Deletes Hyper-V credentials and Hyper-V-collected data only.
+ **Deleting imported servers** – Removes imported servers from inventory. Downstream collection data (network, database) that was collected from those servers is retained.