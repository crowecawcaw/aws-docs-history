# Setting up the discovery tool

## Installing the discovery tool

### Prerequisites

These are the prerequisites for using AWS Transform discovery tool:

- VMware vCenter Server version 6.5, 6.7, 7.0 or 8.0
- You should have permissions to deploy an OVA into your VMware vCenter
- For VMware vCenter Server setup, make sure that you can provide vCenter credentials with Read and View permissions set for the System group
- The tool requires 4 vCPU, 16GB of RAM, and a 35GB hard disk
- DHCP must be available in the network for the discovery tool VM
- The tool collects data using a centralized approach. VMs that are in scope must allow inbound connectivity from the discovery tool VM (default ports, custom port configuration is supported):
  - Linux – SSH TCP/22
  - Windows – TCP/5985 for HTTP, TCP/5986 for HTTPS
  - SNMP – UDP/161

- For Linux, user accounts that can SSH into the server. For SSH discovery, the tool uses ss -tnap.
- The SSH user must be able to execute the ss command using sudo. If ss is not available, the tool will fall back to netstat.

### Download the discovery tool

1. Sign in to vCenter as a VMware administrator and switch to the directory where you want to download the discovery tool OVA file.
2. Download the OVA file from this URL: https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.ova

### Deploy the discovery tool

1.  Sign in to vCenter as a VMware administrator.
2.  Use one of these ways to install the OVA file:
    1. **Use the UI:** Choose **File**, choose **Deploy OVF Template**, select the collector OVA file you downloaded in the previous section, and then complete the wizard. Ensure the proxy settings in the server management dashboard are configured correctly.
    2. **Use the command line:** To install the collector OVA file from the command line, download and use the VMware Open Virtualization Format Tool (ovftool).
       To download ovftool, select a release from the [OVF Tool Documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/ovf-tool-user-s-guide/using-ovf-tool-commands/command-line-options.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/ovf-tool-user-s-guide/using-ovf-tool-commands/command-line-options.html") page. This is an example of using the ovftool command line tool to install the collector OVA file.

    ```
    ovftool --acceptAllEulas --name='discovery tool' --datastore=datastore1 -dm=thin ATX-Transform-discovery-tool.ova 'vi://username:password@vcenterurl/Datacenter/host/esxi/'
    ```

    Descriptions of the replaceable values in the example:

        * The name is the name that you want to use for your discovery tool VM.
        * The datastore is the name of the datastore in your vCenter.
        * The OVA file name is the name of the downloaded collector OVA file.
        * The username/password are your vCenter credentials.
        * The vcenterurl is the URL of your vCenter.
        * The vi path is the path to your VMware ESXi host.

3.  Locate the deployed discovery tool in your vCenter. Right-click the VM, and then choose **Power**, **Power On**.
4.  After a few minutes, the IP address of the collector displays in vCenter. You use this IP address to connect to the collector.

#### Discovery tool virtual machine specifications

- **Operating System** – Amazon Linux 2023
- **RAM** – 16 GB
- **CPU** – 4 cores
- **Disks** - 35 GB
- **VMware requirements** – See [VMware host requirements for running AL2023 on VMware](../../../linux/al2023/ug/vmware-supported-configurations.md#vmware-host-requirements "../../../linux/al2023/ug/vmware-supported-configurations.md#vmware-host-requirements")

### Accessing the discovery tool VM

- The collector VM comes by default with a username and password ("discovery", "collector"). For strong security users are highly encouraged to update the password using `sudo passwd discovery` after logging into the VM through vSphere Client → Discovery Tool VM → "Launch Web Console".
- SSH access is disabled by default. Users can use preconfigured `enablessh` and `disablessh` aliases to enable/disable
  SSH access to the collector VM. Users can SSH into the VM via `ssh discovery@<VM-IP>` after enabling SSH access.
  Users are encouraged to keep SSH access disabled most of the times and enable it only while actively required. Password change is enforced when running `enablessh`.
- To access collector data directory at `/home/ec2-user/.local/share/DiscoveryCollector`, we recommend switching to `ec2-user` by running `sudo su ec2-user`.

## Configure krb5.conf For Kerberos Authentication

Protocol (optional)

krb5.conf configuration may not be required if your environment has proper DNS SRV records configured for Kerberos service discovery. However, explicit configuration is recommended for: Environments without DNS-based Kerberos discovery, Custom or non-standard Kerberos setups.

To configure the Kerberos authentication protocol on your collector VM:

1. Ssh to Discovery Collector VM
2. Open krb5.conf configuration file in the `/etc` folder. To do so, you can use the following example `sudo nano /etc/krb5.conf`
3. Update the krb5.conf configuration file with at least the following information.

```

[realms]
<KERBEROS_REALM> = {
kdc = <KDC_hostname>
default_domain = <domain_name>
}
[domain_realm]
.<domain_name> = <KERBEROS_REALM>
<domain_name> = <KERBEROS_REALM>

```

Replace the placeholders with your actual values:

- `<KERBEROS_REALM>` - Your Kerberos realm (all uppercase, e.g., COLLECTOR.EXAMPLE.COM)
- `<KDC_hostname>` - Hostname or IP address of your Key Distribution Center (e.g., domain-controller.example.com)
- `<domain_name>` - Your domain name (e.g., example.com)

For detailed configuration options, refer to [the MIT Kerberos krb5.conf
documentation](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html "https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html") and [Sample krb5.conf file](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html#sample-krb5-conf-file "https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html#sample-krb5-conf-file")

Verify kerberos setup is working in the collector VM by running `kinit <principal>` and `klist` to obtain and view the ticket. `<principal>` = username@DOMAIN (DOMAIN in all caps) e.g., testuser@EXAMPLE.COM).

Upon verifying, provide the principal and password in the collector UI.

## Import a self-signed certificate authority into the collector (Optional)

This is required when you use WinRM over HTTPS and target servers using WinRM HTTPS certificates signed by a self-signed Certificate Authority (CA), and you want to enable "Validate server SSL certificate" on the collector.

### Prerequisites

1. Self-signed CA certificate that was used to sign the WinRM HTTPS certificates on target servers
2. Certificate in PEM format (.pem or .crt extension)

To import a self-signed certificate authority on the collector VM:

1. Ssh to Discovery Collector VM
2. Place the CA certificate(s) that signed your target servers' WinRM certificates into trust store directory `/etc/pki/ca-trust/source/anchors/` on the collector VM. For example: `sudo cp winrm-ca.pem /etc/pki/ca-trust/source/anchors/winrm-ca.pem`. Note: If your target servers use certificates signed by different CAs, copy all relevant CA certificates to this directory.
3. Update the certificate trust store: `sudo update-ca-trust`
4. Reboot the VM
5. (Optional) To verify that certificates have been successfully imported, you can run the following command. `sudo trust list —filter=ca-anchors | grep -A 5 "<certificate_name>"`

See [Installation and configuration for Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management "https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management")

## Configure discovery tool access to vCenter

###### To configure discovery tool to access VCenter

1. In a web browser access: `https://`ip_address`:5000`,
   where `ip_address` is the IP address of the discovery tool from
   Deploy Discovery Tool. The discovery tool uses a self-signed certificate for HTTPS connection which results in a security warning. Choose **Accept the risk and continue** to continue to the discovery tool console.
2. If you're accessing the discovery tool console for the first time, create a discovery tool login password. Create a password, which you will use for future logins.

###### Important

Remember this password - there is no password recovery mechanism. 3. On the **Discovery tool** page, under **Step 1. Set up vCenter access**, choose **Set up access**. 4. On the **Set up vCenter access** page, provide the **vCenter URL/IP**, the **vCenter username** and **vCenter password** and choose **Set up and connect**.

The discovery tool begins to collect vCenter information, as described in
[Discovered VMware Inventory](discovery-tool-data-collection.md#discovery-tool-inventory "discovery-tool-data-collection.md#discovery-tool-inventory").

After initial configuration choose **Edit vCenter access** in the **Discovery tool status** frame to change your vCenter access settings.

## Configure the collector for OS access

Configure OS access so that the discovery tool can:

- Discover databases to perform database assessment and to assist in VM migration,
- Track network connections, including the process associated with the connection, to assist in application dependency mapping and wave planning.

###### Enable discovery tool OS Access

1. Navigate to the **Set up OS access** page to provide Windows and Linux credentials.
2. Choose a protocol from the dropdown menu.
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

Proper WMI access permissions are needed for remote PowerShell WMI query execution.

For network collection, ensure these conditions are met:

- Allow network connectivity via ICMP
- Allow network connectivity via TCP port 135 + ephemeral TCP port range (49152 - 65535)
- Disable UAC
- Remote DCOM permissions are set up
- Create a dedicated service account with minimal required permissions
- WMI namespace permissions are set up for Windows accounts with namespaces: `\\root\\standardcimv2`, `MSFT_NetTCPConnection` class

For database (SQL Server) collection, a Windows account (local or domain) belonging to the **Local Administrator Group** is required due to complex WMI objects permission requirements.

### Set up SSH

- Port 22 must be open between the discovery tool and target servers
- For SSH network collection to work properly, provide a user configured for passwordless sudo
- Ensure either the `ss` or `netstat` command are available on the machines (should come installed by default)

### Set up SNMP

- Port 161/UDP must be open between the discovery tool and target servers
- For SNMP v2: Provide a read-only community string that can access TCP connection OIDs.
- For SNMP v3: Provide username/password and auth/privacy details with read-only permission that can access TCP connection OIDs

The discovery tool requires access to:

- `"1.3.6.1.2.1.6.13.1.1." (tcpConnState)`
- `"1.3.6.1.2.1.6.19.1.8." (tcpConnectionProcess)`
- `"1.3.6.1.2.1.25.4.2.1.2." (hrSWRunName)`

## Updating the discovery tool

The discovery tool does not have an automatic updates feature however you will
receive a reminder notification after 30 days of installation to update. It is recommended
to keep the application up-to-date to receive the latest features and security
patches.

###### To manually update the tool

1. Obtain the latest discovery tool Open Virtualization Archive (OVA) file by downloading it from the provided link.
2. (Optional) We recommend that you delete the previous discovery tool OVA file, before you deploy the latest one.
3. Follow the steps in the Deploy discovery tool section to deploy the updated version.

## Revoking vCenter access

Editing vCenter access to change only the **vCenter URL/IP** or to choose **Revoke access** deletes all of the data discovered by the discovery tool, including OS access configuration and discovered inventory.
