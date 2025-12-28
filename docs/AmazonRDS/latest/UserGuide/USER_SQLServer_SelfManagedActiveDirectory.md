# Requirements

Make sure you've met the following requirements before joining an RDS for SQL Server DB instance to your self-managed AD domain.

###### Topics

- [Configure your on-premises AD](#USER_SQLServer_SelfManagedActiveDirectory.Requirements.OnPremConfig "#USER_SQLServer_SelfManagedActiveDirectory.Requirements.OnPremConfig")
- [Configure your network connectivity](#USER_SQLServer_SelfManagedActiveDirectory.Requirements.NetworkConfig "#USER_SQLServer_SelfManagedActiveDirectory.Requirements.NetworkConfig")
- [Configure your AD domain service account](#USER_SQLServer_SelfManagedActiveDirectory.Requirements.DomainAccountConfig "#USER_SQLServer_SelfManagedActiveDirectory.Requirements.DomainAccountConfig")
- [Configuring secure communication over LDAPS](#USER_SQLServer_SelfManagedActiveDirectory.Requirements.LDAPS "#USER_SQLServer_SelfManagedActiveDirectory.Requirements.LDAPS")

## Configure your on-premises AD

Make sure that you have an on-premises or other self-managed Microsoft AD that you can join the Amazon RDS for SQL Server instance to.
Your on-premises AD should have the following configuration:

- If you have AD sites defined, make sure the subnets in the VPC associated with your RDS for SQL Server DB instance are defined in your AD site.
  Confirm there aren't any conflicts between the subnets in your VPC and the subnets in your other AD sites.
- Your AD domain controller has a domain functional level of Windows Server 2008 R2 or higher.
- Your AD domain name can't be in Single Label Domain (SLD) format. RDS for SQL Server does not support SLD domains.
- The fully qualified domain name (FQDN) for your AD can't exceed 47 characters.

## Configure your network connectivity

Make sure that you have met the following network configurations:

- Configure connectivity between the Amazon VPC where you want to create the RDS for SQL Server DB
  instance and your self-managed AD. You can set up connectivity
  using AWS Direct Connect, AWS VPN, VPC peering, or AWS Transit
  Gateway.
- For VPC security groups, the default security group for your default Amazon VPC is already added to your
  RDS for SQL Server DB instance in the console. Ensure that the security group and the VPC network ACLs for the subnet(s) where you're creating your
  RDS for SQL Server DB instance allow traffic on the ports and in the directions shown in the following diagram.

![Self-managed AD network configuration port rules.](images/SQLServer_SelfManagedActiveDirectory_Requirements_NetworkConfig.png)

The following table identifies the role of each port.

| Protocol | Ports            | Role                                                               |
| -------- | ---------------- | ------------------------------------------------------------------ |
| TCP/UDP  | 53               | Domain Name System (DNS)                                           |
| TCP/UDP  | 88               | Kerberos authentication                                            |
| TCP/UDP  | 464              | Change/Set password                                                |
| TCP/UDP  | 389              | Lightweight Directory Access Protocol (LDAP)                       |
| TCP      | 135              | Distributed Computing Environment / End Point Mapper (DCE / EPMAP) |
| TCP      | 445              | Directory Services SMB file sharing                                |
| TCP      | 636              | Lightweight Directory Access Protocol over TLS/SSL (LDAPS)         |
| TCP      | 49152<br>• 65535 | Ephemeral ports for RPC                                            |

- Generally, the domain DNS servers are located in the AD domain controllers.
  You do not need to configure the VPC DHCP option set to use this feature.
  For more information, see [DHCP option sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md")
  in the _Amazon VPC User Guide_.

###### Important

If you're using VPC network ACLs, you must also allow outbound traffic on dynamic ports (49152-65535)
from your RDS for SQL Server DB instance. Ensure that these traffic rules are also mirrored on the firewalls that apply to each
of the AD domain controllers, DNS servers, and RDS for SQL Server DB instances.

While VPC security groups require ports to be opened only in the direction that network traffic is initiated,
most Windows firewalls and VPC network ACLs require ports to be open in both directions.

## Configure your AD domain service account

Make sure that you have met the following requirements for an AD domain service account:

- Make sure that you have a domain service account in your self-managed AD domain with delegated permissions to join computers to the domain.
  A domain service account is a user account in your self-managed AD that has been delegated permission to perform certain tasks.
- The domain service account needs to be delegated the following permissions in the Organizational Unit (OU) that you're joining your RDS for SQL Server DB instance to:

      + Validated ability to write to the DNS host name
      + Validated ability to write to the service principal name
      + Create and delete computer objects

  These represent the minimum set of permissions that are required to join computer objects to your self-managed AD.
  For more information, see [Errors
  when attempting to join computers to a domain](https://learn.microsoft.com/en-US/troubleshoot/windows-server/identity/access-denied-when-joining-computers "https://learn.microsoft.com/en-US/troubleshoot/windows-server/identity/access-denied-when-joining-computers") in the Microsoft Windows Server documentation.

- To use Kerberos authentication, you need to provide Service Principal Names (SPNs) and
  DNS permissions to your AD domain service account:
  - **Write SPN**: Delegate the **Write
    SPN** permission to the AD domain service account in
    the OU where you need to join the RDS for SQL Server DB instance. This permissions is
    different from the validated write SPN.
  - **DNS permissions**: Provide the following permissions
    to the AD domain service account in the DNS manager at the server
    level for your domain controller:
    - List contents
    - Read all properties
    - Read permissions

###### Important

Do not move computer objects that RDS for SQL Server creates in the Organizational Unit after your DB instance is created. Moving the associated objects will cause your RDS for SQL Server DB instance to
become misconfigured. If you need to move the computer objects created by Amazon RDS, use the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") RDS API operation to modify the domain parameters
with the desired location of the computer objects.

## Configuring secure communication over LDAPS

Communication over LDAPS is recommended for RDS to query and access computer objects as
well as SPNs in the domain controller. To use secure LDAP, use a valid SSL
certificate on your domain controller that meets the requirements for secure LDAPS.
If a valid SSL certificate does not exist on the domain controller, the RDS for SQL Server
DB instance defaults to using LDAP. For more information on certificate validity, see
[Requirements for an LDAPS certificate](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/enable-ldap-over-ssl-3rd-certification-authority#requirements-for-an-ldaps-certificate "https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/enable-ldap-over-ssl-3rd-certification-authority#requirements-for-an-ldaps-certificate").
