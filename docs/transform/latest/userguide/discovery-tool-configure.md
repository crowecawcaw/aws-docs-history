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
- To access the discovery tool data directory at
  `/home/ec2-user/.local/share/DiscoveryTool`, we recommend
  switching to `ec2-user` by running `sudo su
 ec2-user`.

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
   - The target Windows servers on WinRM ports (5985 for HTTP,
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

###### To manually update the tool

1. Download the latest discovery tool image file (OVA for VMware or VHD for Hyper-V) from the provided link.
2. (Optional) We recommend that you delete the previous discovery tool image file before you deploy the latest one.
3. Follow the steps in the Deploy the discovery tool section to deploy the updated version.

## Revoking access

You can revoke access for each discovery source independently. When you revoke access for one source, data from other sources is not affected.

- **Revoking vCenter access** – Deletes vCenter credentials and VMware-collected data. Does not delete Hyper-V data, imported server data, or OS credentials.
- **Revoking Hyper-V access** – Deletes Hyper-V credentials and Hyper-V-collected data only.
- **Deleting imported servers** – Removes imported servers from inventory. Downstream collection data (network, database) that was collected from those servers is retained.
