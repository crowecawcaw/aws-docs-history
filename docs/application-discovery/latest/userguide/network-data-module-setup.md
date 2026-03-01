AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Setting up the Network Data Collection module

The Network Data Collection module collects network data for the server inventory that
comes from the VMware vCenter module. Therefore, to use the Network Data Collection
module, first set up the VMware vCenter module. For instructions, follow the guidance in
the following topics:

1. [Deploying Application Discovery Service Agentless Collector](agentless-collector-deploying.md "agentless-collector-deploying.md")
2. [Accessing the Agentless Collector console](agentless-collector-gs-access-console.md "agentless-collector-gs-access-console.md")
3. [Configuring Agentless Collector](agentless-collector-gs-configure.md "agentless-collector-gs-configure.md")
4. [Using the VMware vCenter Agentless Collector data collection module](agentless-collector-gs-data-collection-vcenter.md "agentless-collector-gs-data-collection-vcenter.md")

###### To set up the Network Data Collection module

1. On the Agentless Collector dashboard, in the **Network Data
   Collection** section, choose **View network
   connections**.
2. On the **Network connections** page, choose **Edit
   collector**.
3. In the credentials section, enter at least one set of credentials. You can
   enter up to 10 sets of credentials. The first time the module attempts to
   collect data for a server, it tries all of the credentials until it finds a set
   of credentials that works; it then saves that set and uses it again in
   subsequent attempts. For information about setting up credentials, see [Setting up credentials](#network-data-module-credentials-setup "#network-data-module-credentials-setup").
4. In the **Data collection preferences** section, to
   automatically start collecting data when a server reboots, select
   **Start data collection automatically**.
5. If you haven't set up WinRM certificates, select **Disable WinRM
   certificate checks**.
6. Choose **Save**.
7. Collection happens on the servers every 15 seconds. To see the details of the
   collection attempts for a given server, select the checkbox to the left of the
   server in the **Servers** table.

## Setting up credentials

The Network Data Collection module uses WinRM to collect data from Windows
servers. It uses SNMPv2 and SNMPv3 to collect data from Linux servers.

**WinRM credentials:**

- Specify the username and password of a Windows account that has the
  following:
  - Read access to the `\root\standardcimv2`
    namespace
  - Read permissions for `MSFT_NetTCPConnection`
    class
  - Remote WMI access

- We recommend that you create a dedicated service account with minimal
  required permissions.
- Avoid using domain administrator or local administrator accounts.
- Port 5986 (HTTPS) must be open between collector and target
  servers.
- Avoid disabling WinRM certificate check. For information about setting up
  WinRM certificates, see [Addressing self-signed certification problems when configuring WinRM certificates](agentless-collector-troubleshooting.md#agentless-collector-address-self-signed-certification-problems "agentless-collector-troubleshooting.md#agentless-collector-address-self-signed-certification-problems").

**SNMPv2 credentials:**

- Provide a read-only community string that can access 1.3.6.1.2.1.6.13.\*
  OID
- SNMPv3 is preferable to SNMPv2 because of the improved security in
  SNMPv3
- Port 161/UDP must be open between collector and target servers
- Use complex, non-default community strings
- Avoid common strings like "public" or "private"
- Treat community strings like passwords

**SNMPv3 credentials**

- Provide a username/password and auth/privacy details with read-only
  permission that can access 1.3.6.1.2.1.6.13.\* OID.
- Port 161/UDP must be open between collector and target servers
- Enable both authentication and privacy
- Use strong authentication protocols (SHA preferred over MD5)
- Use strong encryption protocols (AES preferred over DES)
- Use complex passwords for both auth and privacy
- Use unique usernames (avoid common names)

**General best practices for Credential
Management**

- Store credentials securely
- Regularly rotate all credentials
- Use password managers or secure vaults
- Monitor credential usage
- Follow the principle of least privilege and only grant the minimum
  necessary permissions needed
