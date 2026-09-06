# Configure the discovery tool

## Access the discovery tool console

1. In a web browser access: `https://`ip_address`:5000`,
   where `ip_address` is the IP address of the discovery tool from
   Deploy Discovery Tool. The discovery tool uses a self-signed certificate for HTTPS connection which results in a security warning. Choose **Accept the risk and continue** to continue to the discovery tool console.
2. If you're accessing the discovery tool console for the first time, create a discovery tool login password. Create a password, which you will use for future logins.

###### Important

Remember this password - there is no password recovery mechanism.

## Accessing the discovery tool VM

- The discovery tool VM comes by default with a username and password ("discovery", "password").
  For strong security, we recommend that you update the password by using
  `sudo passwd discovery` after logging into the VM through your hypervisor's console (for example, vSphere Client for VMware or Hyper-V Manager for Hyper-V).
- SSH access is disabled by default. Users can use preconfigured `enablessh` and
  `disablessh` aliases to enable/disable SSH access to the
  discovery tool VM. Users can SSH into the VM via `ssh
 discovery@<VM-IP>` after enabling SSH access. Users are
  encouraged to keep SSH access disabled most of the times and enable it only
  while actively required. Password change is enforced when running
  `enablessh`.
- The discovery tool data directory is at
  `/home/discovery/.local/share/DiscoveryTool`. The default VM user is
  `discovery`, so you can access this directory after you sign in to the
  VM through your hypervisor's console.

## Configure Kerberos authentication

Kerberos authentication is the recommended method for connecting to Windows servers
from the discovery tool. The discovery tool VM uses native Amazon Linux 2023 Kerberos
libraries to authenticate against your Active Directory domain.

The following are key points about Kerberos authentication on the discovery tool VM:

- Use the `kinit` command to obtain a Kerberos ticket and
  `klist` to verify the ticket.
- The Kerberos configuration file is located at
  `/etc/krb5.conf`.
- Before you configure the discovery tool, verify that `kinit`
  succeeds from the CLI on the discovery tool VM.

### Kerberos prerequisites

Before you configure Kerberos authentication, verify that you have the following
information and network connectivity.

1. Obtain the following information from your Active Directory
   administrator:

   - The Kerberos realm name (typically your domain name in
     uppercase, for example, `EXAMPLE.COM`).
   - The hostname or IP address of the Key Distribution Center (KDC),
     which is typically a domain controller (for example,
     `dc01.example.com`).
   - A service account with permissions to authenticate against the
     target Windows servers.

2. Verify that the discovery tool VM has network connectivity to the
   following:

   - The KDC on port 88 (TCP and UDP) for Kerberos
     authentication.
   - The target Windows servers on Windows Remote Management (WinRM) ports (5985 for HTTP,
     5986 for HTTPS).

### Configure Kerberos

Complete the following steps to configure Kerberos authentication on the discovery
tool VM.

1. SSH to the discovery tool VM.

```
ssh discovery@<discovery-tool-vm-ip>
```

2. Edit the Kerberos configuration file at
   `/etc/krb5.conf`.

```
sudo nano /etc/krb5.conf
```

Add the following configuration, replacing the placeholder values with your
environment details.

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

###### Important

Kerberos is case-sensitive. The realm name must be in uppercase
(for example, `EXAMPLE.COM`, not `example.com`). The
domain name in the `[domain_realm]` section must be in
lowercase.

**Multiple Active Directory domains**

The discovery tool supports multiple Kerberos credentials for different
Active Directory domains. Each credential authenticates independently, so you
can configure multiple credentials normally and isolation is automatic.

If you have servers in multiple domains, add entries for each realm in your
`/etc/krb5.conf` file:

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

3. Verify that you can obtain a Kerberos ticket by running the
   `kinit` command.

```
kinit username@REALM.COM
```

Enter the password when prompted. If the command completes without errors,
authentication succeeded. 4. Verify the ticket by running the `klist` command.

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

5. Configure the discovery tool with the same case-sensitive principal that
   you used with `kinit` (for example,
   `username@REALM.COM`).

An explicit `krb5.conf` configuration might not be required if your
environment has DNS SRV records configured for Kerberos service discovery. For more
information about Kerberos configuration options, see the [MIT
Kerberos krb5.conf documentation](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html "https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html") and the [sample
krb5.conf file](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html#sample-krb5-conf-file "https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html#sample-krb5-conf-file").

### Find Kerberos configuration from domain-joined machines

If you don't have the Kerberos configuration details, you can retrieve them from a
Windows machine that is joined to the domain. Run the following commands from a
command prompt on the domain-joined machine.

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

- **Realm** – Use the value from
  `%USERDNSDOMAIN%` in uppercase (for example,
  `EXAMPLE.COM`).
- **KDC** – Use the DC hostname
  from the `nltest` output (for example,
  `dc01.example.com`).

### Using Kerberos with IP addresses

Kerberos identifies each target server by a service principal name (SPN). The SPN is built from the server's fully qualified domain name (FQDN), such as `HTTP/server01.example.com`. Active Directory does not register SPNs for IP addresses.

When the discovery tool knows a server's FQDN, it uses the FQDN first for Kerberos credentials. The discovery tool learns the FQDN from guest metadata reported by VMware Tools on VMware, or by Integration Services on Hyper-V. Most servers that the discovery tool finds through VMware or Hyper-V discovery have an FQDN, so you do not need to do anything for those servers. A server that you import from a CSV file with only an IP address has no FQDN.

The discovery tool also tries any IP addresses it has for a server. An IP address works with Kerberos when the discovery tool can map that IP address to the FQDN with a reverse DNS lookup. Reverse DNS is a best-effort fallback, not a requirement. Set it up only if a server has no FQDN, and you want to use Kerberos with that server. The lookup needs one of the following:

- **A PTR record** – A PTR record for that IP address in your DNS or Active Directory. A PTR record maps an IP address to a host name. It is the reverse of the A record, which maps a host name to an IP address. Many Active Directory domains add PTR records for you when a server joins, so the record might already exist.
- **An `/etc/hosts` entry** – An entry in `/etc/hosts` on the discovery tool VM, in the form `<ip-address> <fqdn> <short-name>`. Use this when you cannot change DNS. You do not need a DNS administrator.

Reverse lookups must also be turned on for the VM. They are on by default. Do not set `rdns = false` or `dns_canonicalize_hostname = false` in `/etc/krb5.conf`. If either setting is already `false`, Kerberos keeps the IP address in the SPN instead of replacing it with the FQDN, and authentication fails with a `Server not found in Kerberos database` error even when the reverse mapping exists. Remove the setting, or set it to `true`.

To check reverse lookups, run the following command on the discovery tool VM.

```
getent hosts <target-ip>
```

The command returns the server's FQDN when reverse lookups work. It reads both `/etc/hosts` and DNS. If it does not return the FQDN, add a PTR record, add an `/etc/hosts` entry, or use the FQDN instead.

###### Note

If no reverse mapping exists, authentication fails with `Server not found in Kerberos database`. This is a principal lookup failure, not a rejected password. It does not count toward Active Directory account lockout.

## Configure vCenter access

1. On the **Discovery tool** page, under **Step 1. Configure discovery sources**, choose **Configure sources**.
2. On the **Configure discovery sources** page, provide the **Friendly name**, **vCenter FQDN/IP**, **Username**, and **Password**.
3. Choose **Save configuration**.

The discovery tool begins to collect vCenter information, as described in
[Discovered Inventory](discovery-tool-data-collection.md#discovery-tool-inventory "discovery-tool-data-collection.md#discovery-tool-inventory").

After initial configuration choose **Edit vCenter access** in the **Discovery tool status** frame to change your vCenter access settings.

The discovery tool collects from all configured vCenter servers in parallel. If one vCenter server is unreachable during collection, the tool reports partial success and continues collecting from the remaining vCenter servers.

If a VM appears on multiple vCenter servers (for example, due to shared ESXi hosts or cross-vCenter vMotion), the discovery tool automatically deduplicates VMs. Each unique VM appears only once in the inventory.

## Configure Hyper-V access

1. On the **Discovery tool** page, under **Step 1. Configure discovery sources**, choose **Configure sources**.
2. On the **Configure discovery sources** page, provide a **friendly name**, the **host FQDN or IP address**, the **authentication type (NTLM or Kerberos)**, the **WinRM username**, and the **WinRM password**.
3. Choose **Save configuration**.

The discovery tool begins to collect Hyper-V information, as described in
[Discovered inventory](discovery-tool-data-collection.md#discovery-tool-inventory "discovery-tool-data-collection.md#discovery-tool-inventory").

Collection begins automatically after you save the credentials.

For Hyper-V failover clusters, you can add multiple hosts in the same cluster. The tool automatically deduplicates VMs that appear on more than one host.

## Import servers

1. Navigate to the **Import servers** page from the Discovery tool homepage.
2. Prepare a CSV file with the following columns: `hostname_or_ip` (required), `os_credential_name` (optional), and `oracle_credential_name` (optional).

   - The `hostname_or_ip` value must be a valid IPv4 address or a fully qualified domain name (FQDN).
   - The `os_credential_name` value, if provided, must match the friendly name of an OS credential that you already configured (SSH, WinRM, or SNMP). Leave empty for servers where you have not yet configured an OS credential.
   - The `oracle_credential_name` value, if provided, must match the friendly name of an Oracle credential that you already configured.

3. Upload the CSV file. The tool validates all rows and rejects the file if any row is invalid.

After a successful import, the tool automatically begins database, network and OS metrics collection for the imported servers, if OS credentials are configured. If you upload another CSV file, existing records are updated without creating duplicates and new records are merged into the inventory.

## Import a self-signed certificate authority into the discovery tool (Optional)

This is required when you use WinRM over HTTPS and target servers using WinRM HTTPS certificates signed by a self-signed Certificate Authority (CA), and you want to enable "Validate server SSL certificate" on the discovery tool.

### Prerequisites

1. Self-signed CA certificate that was used to sign the WinRM HTTPS certificates on target servers
2. Certificate in PEM format (.pem or .crt extension)

To import a self-signed certificate authority on the discovery tool VM:

1. Ssh to Discovery tool VM
2. Place the CA certificate(s) that signed your target servers' WinRM certificates into trust store directory `/etc/pki/ca-trust/source/anchors/` on the discovery tool VM. For example: `sudo cp winrm-ca.pem /etc/pki/ca-trust/source/anchors/winrm-ca.pem`. Note: If your target servers use certificates signed by different CAs, copy all relevant CA certificates to this directory.
3. Update the certificate trust store: `sudo update-ca-trust`
4. Reboot the VM
5. (Optional) To verify that certificates have been successfully imported, you can run the following command. `sudo trust list —filter=ca-anchors | grep -A 5 "<certificate_name>"`

See [Installation and configuration for Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management "https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management")

## Configure the discovery tool for OS access

Configure OS access so that the discovery tool can:

- Discover databases to perform database assessment and to assist in VM migration,
- Track network connections between servers in your inventory, including the process associated with each connection, to assist in application dependency mapping and wave planning. Only connections where both endpoints are in the discovery tool's inventory are included.

###### Enable discovery tool OS Access

1. Navigate to the **Set up OS access** page to provide Windows and Linux credentials.
2. Choose a protocol that you want to add credentials for.
3. Provide the required credentials for the selected protocol.
4. Select **Auto-connect** to enable the discovery tool to try all provided credentials on discovered servers until matching credentials are found for each server.

See [Using Auto-Connect Feature With Caution](discover-tool-security.md#auto-connect-caution "discover-tool-security.md#auto-connect-caution") for important security recommendations regarding the auto-connect feature. 5. Choose **Set up and connect**.

When the OS matching process is completed, you see a message that the data collection is in progress, and an error regarding servers for which a credentials match was not found.

### Requirements for OS-level collection

OS-level collection — server and storage performance metrics, network connection
tracking, and SQL Server and Oracle database discovery — runs remotely against your
target servers. The discovery tool installs no agent or software on them. The following are
the requirements for a target server to be collected.

###### Note

These requirements apply to the servers you are collecting data
_from_. They are separate from the Linux distributions supported for
the host you install the discovery tool _on_, which are listed in
[Supported distributions for the installer host](discovery-tool-deploy-linux.md#discovery-tool-linux-supported-distros "discovery-tool-deploy-linux.md#discovery-tool-linux-supported-distros").

The following list describes the connectivity and account requirements for each type of
target server.

Linux
SSH reachable from the discovery tool VM on TCP/22 (or a custom port), and
an account that can run shell commands. Network connection tracking can also use
SNMP on UDP/161 instead of SSH. `sudo` is optional. Without
it, the discovery tool still collects most data, but the server UUID, LVM
detection, and process-level network connection details are missing. For
details, see [Linux servers (SSH)](discovery-tool-permissions.md#discovery-tool-permissions-linux "discovery-tool-permissions.md#discovery-tool-permissions-linux").

Windows
WinRM enabled and reachable on TCP/5985 (HTTP) or TCP/5986 (HTTPS), or a
custom port. The discovery tool runs all Windows commands through PowerShell
remoting, so PowerShell must be present on the target server. PowerShell 3.0 or
later provides full data coverage. For details,
see [Windows servers (WinRM) — OS metrics](discovery-tool-permissions.md#discovery-tool-permissions-windows-os "discovery-tool-permissions.md#discovery-tool-permissions-windows-os").

Because collection uses standard operating system commands rather than an agent, the
discovery tool works across a wide range of operating system versions, including older
ones. The following operating systems are validated end to end. Other versions that meet
the requirements in the preceding list are also collected.

- **Linux** – Amazon Linux 2, Amazon Linux 2023, RHEL 7.9, Rocky Linux 9.7, AlmaLinux 9.7, SLES 12 SP5, Debian 11, Ubuntu 16.04, and Ubuntu 22.04
- **Windows** – Windows Server 2012 R2, 2016, 2019, and 2022

###### Reduced data coverage on older operating systems

On older operating systems, the discovery tool substitutes alternative commands and some
fields can be empty:

- Linux distributions released before `/etc/os-release` became
  standard — such as RHEL 6, CentOS 6, SLES 11, Ubuntu 14.04 and earlier, and
  Amazon Linux 1 — are identified from `/etc/*-release` or
  `uname` instead, which can report less detail.
- Windows Server 2003 does not include PowerShell. Because the discovery tool
  runs all Windows commands through PowerShell remoting, it collects no OS-level data from
  these servers unless you install PowerShell and WinRM on them.
- On servers that provide only PowerShell 2.0, such as Windows Server 2008,
  `Get-CimInstance` is unavailable. The discovery tool falls back to
  `Get-WmiObject` for basic server identity, but most other data, including
  performance and storage metrics, is unavailable.
- Servers whose SSH service offers only legacy key exchange or host key
  algorithms, which is common on RHEL 6 and other distributions of that era, can refuse
  the connection. If a server cannot be reached over SSH but is reachable manually,
  verify which algorithms its SSH service offers.

### Supported protocols setup

You must set up WinRM, SSH, and SNMP protocols on target servers for the discovery tool to communicate with them.

#### Set up WinRM and WMI

WinRM is automatically installed with all currently-supported versions of the Windows operating system.

To verify or edit WinRM configuration, use the `winrm` command line tool:

- Verify installed WinRM listeners: `winrm enumerate winrm/config/listener`
- Verify WinRM configurations: `winrm get winrm/config`
- Example command to set up WinRM: `winrm quickconfig -transport:https`

**Listener Ports**

Default HTTP port is 5985; HTTPS is 5986. You can use other ports as needed. The ports must be open between the discovery tool and target servers.

**Encryption**

The discovery tool uses encrypted WinRM communication. We recommend that WinRM
listeners on target servers also use encryption: `winrm set
 winrm/config/service '@{AllowUnencrypted="false"}'`

**NTLM vs Kerberos**

WinRM authentication protocols Kerberos and NTLM are supported by the discovery tool. NTLM can be used only with HTTPS and Kerberos can be used with both HTTP or HTTPS.

**WMI Requirements**

The discovery tool queries the following WMI namespaces. The WinRM account needs
read access to each namespace relevant to your collection modules:

| WMI namespace                                  | Used by                                                  |
| ---------------------------------------------- | -------------------------------------------------------- |
| `root\cimv2`                                   | OS metrics, Hyper-V host metadata, SQL Server collection |
| `root\virtualization\v2`                       | Hyper-V VM inventory                                     |
| `root\StandardCIMV2`                           | Network collection                                       |
| `root\Microsoft\SqlServer\ComputerManagement*` | SQL Server collection                                    |
| `root\Microsoft\SqlServer\ReportServer\*`      | SQL Server collection (SSRS)                             |

For network collection, ensure these conditions are met:

- Allow network connectivity via ICMP
- Allow network connectivity via TCP port 135 + ephemeral TCP port range (49152 - 65535)
- Disable UAC
- Remote DCOM permissions are set up
- Create a dedicated service account with minimal required permissions
- WMI namespace permissions are set up for Windows accounts with namespaces: `\\root\\standardcimv2`, `MSFT_NetTCPConnection` class

For SQL Server collection, a Windows account (local or domain) belonging to the **Local Administrator Group** is required because of complex WMI objects permission requirements.

### Set up SSH

- The default port is 22. Custom ports are supported. The configured port must be open between the discovery tool and target servers.
- For SSH network collection to work properly, provide a user configured for passwordless sudo.
- Ensure that the following commands are available on target Linux servers (installed by default on most distributions): `ss` or `netstat` for network collection, and `lsblk`, `iostat`, `dmidecode`, `smartctl`, `top`, `ps`, `free`, `ip`, and `df` for OS metrics collection.

The discovery tool supports two authentication methods for SSH:

**Option 1: Username and password**

Provide the SSH username and password. This is the default authentication method.

**Option 2: SSH private key**

Provide the SSH username and a private key in PEM format. To use this option, choose **SSH Key** from the **Authentication type** dropdown when configuring SSH credentials. If the private key is encrypted with a passphrase, enter the passphrase in the optional **Key Passphrase** field.

The following key formats are supported:

- RSA
- ECDSA
- Ed25519
- OpenSSH format
- PKCS#8 format

Both authentication methods support auto-connect. Credentials are stored encrypted at rest.

### Set up SNMP

- The default port is 161/UDP. Custom ports are supported. The configured port must be open between the discovery tool and target servers.
- For SNMP v2: Provide a read-only community string that can access TCP connection OIDs.
- For SNMP v3: Provide username/password and auth/privacy details with read-only permission that can access TCP connection OIDs

The discovery tool requires access to:

- `"1.3.6.1.2.1.6.13.1.1." (tcpConnState)`
- `"1.3.6.1.2.1.6.19.1.8." (tcpConnectionProcess)`
- `"1.3.6.1.2.1.25.4.2.1.2." (hrSWRunName)`

## Configure Oracle database access

Configure Oracle database access to collect detailed Oracle database metadata
directly through SQL connections. Collected metadata includes CDB and PDB topology, feature
usage, and installed options. This data helps you plan Oracle database migrations more
accurately. You can collect Oracle Database 12c Release 1 (12.1) and later through
direct SQL connections. OS-level fallback detection works with all Oracle
versions.

**Configure Oracle credentials in the discovery tool**

1. On the **Discovery tool** page, in the sidebar, choose **Database access**.
2. Choose **Add Oracle credential**.
3. Provide the following information:

   - **Friendly name** – A descriptive name for this credential (for example, `Oracle Production`).
   - **Port** – The Oracle listener port (default 1521).
   - **Service name** – The Oracle service name for the target database.
   - **Username** – The Oracle service account username.
   - **Password** – The Oracle service account password.
   - **Auto-connect** – Turn on this option to try the credential against all servers in your inventory. Turn off this option to manually assign the credential to specific servers.

4. To add more credentials (for example, for different Oracle environments), choose **Add Oracle credential** again.
5. Choose **Save**.

**Credential modes**

When you configure Oracle credentials, you can choose between two modes:

- **Manual** – Pin a credential to a
  specific server. The discovery tool uses that credential exclusively for that server. If the connection
  fails, no fallback occurs. Fix the credential configuration to resolve the
  issue.
- **Auto-connect** – The discovery tool
  tries each auto-connect credential against every server in your inventory. When a
  credential succeeds for a server, the discovery tool uses that credential for all
  subsequent collection rounds.

**Detection flow**

When you configure Oracle credentials, the discovery tool first tries a direct SQL
connection. If all database credentials fail, the tool falls back to OS-level detection
through SSH or WinRM, so you can still discover Oracle installations without database
access.

## Updating the discovery tool

The discovery tool does not have an automatic updates feature however you will
receive a reminder notification after 30 days of installation to update. It is recommended
to keep the application up-to-date to receive the latest features and security
patches.

There are two ways to update:

- **Update in place** – Updates the application inside your existing VM with the Linux installer. Your collected inventory, credentials, and configuration are preserved. This method needs operating system access to the discovery tool VM. We recommend this method.
- **Redeploy from a new image** – Deploys a new VM from the latest OVA for VMware or VHD for Hyper-V. A new deployment starts with an empty database. Your existing data and configuration are not carried over unless you migrate them yourself.

### Updating in place with the Linux installer

This method runs on the existing VM. It keeps your database, which holds your collected data, discovery sources, and credentials, and it keeps the database encryption key. Use this method when you want to keep your existing configuration and collected data.

###### Note

This method updates only the discovery tool application. It does not update anything on the VM host, such as the operating system version, the preconfigured shell aliases, or the networking and firewall rules. To get host updates, redeploy from a new image instead. For more information, see [Redeploying from a new image](#discovery-tool-updating-redeploy "#discovery-tool-updating-redeploy").

###### Important

Complete the backup step before you update, so that you can restore your data if the update does not finish.

###### To update the discovery tool in place

1. Access the discovery tool VM through your hypervisor console, or through SSH after you run `enablessh`. For more information, see [Accessing the discovery tool VM](#discovery-tool-vm-access "#discovery-tool-vm-access").
2. Back up the data directory so that you can restore it if you need to.

```
sudo tar czf /home/ec2-user/discovery-tool-backup-$(date +%F).tar.gz \
  -C /home/ec2-user/.local/share DiscoveryTool
```

The installer keeps the database encryption key. It does not change the key during an update. 3. Download the latest installer script to the VM and make it executable.

```
curl -O https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.sh
chmod +x AWS-Transform-discovery-tool.sh
```

4. Stop the discovery tool service.

```
sudo ./AWS-Transform-discovery-tool.sh stop
```

5. Run the installer. It detects the existing installation and updates it in place, keeping your data directory, encryption key, and service user. It also installs any required system packages.

```
sudo ./AWS-Transform-discovery-tool.sh install
```

6. Start the discovery tool service.

```
sudo ./AWS-Transform-discovery-tool.sh start
```

7. Verify the update. Open `https://`ip_address`:5000` in a web browser, sign in, and confirm that the version is updated and that your discovery sources, credentials, and inventory are present.

### Redeploying from a new image

Use this method if you do not have operating system access to the VM, or if you prefer to deploy a new appliance. A redeployed VM starts with an empty database.

###### To redeploy the discovery tool from a new image

1. Download the latest image file: the OVA for VMware or the VHD for Hyper-V.
2. (Optional) Delete the previous discovery tool image file before you deploy the latest one.
3. Deploy the new version. For VMware, see [Deploy on VMware](discovery-tool-deploy-vmware.md "discovery-tool-deploy-vmware.md"). For Hyper-V, see [Deploy on Hyper-V](discovery-tool-deploy-hyperv.md "discovery-tool-deploy-hyperv.md").
4. Configure your discovery sources, credentials, and server imports again on the new VM.

###### Note

If you want to deploy a new discovery tool and keep the data and configuration that you already collected, contact AWS Support before you begin.

## Revoking access

You can revoke access for each discovery source independently. When you revoke access for one source, data from other sources is not affected.

- **Revoking vCenter access** – Deletes vCenter credentials and VMware-collected data. Does not delete Hyper-V data, imported server data, or OS credentials.
- **Revoking Hyper-V access** – Deletes Hyper-V credentials and Hyper-V-collected data only.
- **Deleting imported servers** – Removes imported servers from inventory. Downstream collection data (network, database) that was collected from those servers is retained.
