

# What gets created with your AWS Managed Microsoft AD
<a name="ms_ad_getting_started_what_gets_created"></a>

When you create an Active Directory with AWS Managed Microsoft AD, Directory Service performs the following tasks on your behalf:
+ Automatically creates and associates an elastic network interface (ENI) with each of your domain controllers. Each of these ENIs are essential for connectivity between your VPC and Directory Service domain controllers and should never be deleted. You can identify all network interfaces reserved for use with Directory Service by the description: "AWS created network interface for directory *directory-id*". For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide*. The default DNS Server of the AWS Managed Microsoft AD Active Directory is the VPC DNS server at Classless Inter-Domain Routing (CIDR)\+2. For more information, see [Amazon DNS server](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#AmazonDNS) in *Amazon VPC User Guide*.
**Note**  
Domain controllers are deployed across two Availability Zones in a region by default and connected to your Amazon VPC (VPC). Backups are automatically taken once per day, and the Amazon EBS (EBS) volumes are encrypted to ensure that data is secured at rest. Domain controllers that fail are automatically replaced in the same Availability Zone using the same IP address, and a full disaster recovery can be performed using the latest backup.
+ Provisions Active Directory within your VPC using two domain controllers for fault tolerance and high availability. More domain controllers can be provisioned for higher resiliency and performance after the directory has been successfully created and is [Active](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_status.html). For more information, see [Deploying additional domain controllers for your AWS Managed Microsoft AD](ms_ad_deploy_additional_dcs.md).
**Note**  
AWS does not allow the installation of monitoring agents on AWS Managed Microsoft AD domain controllers.
+ Creates an [AWS Security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) {{sg-1234567890abcdef0}} that establishes network rules for traffic in and out of your domain controllers. The default outbound rule permits all traffic to all IPv4 and/or IPv6 addresses. The default inbound rules allows only traffic through ports that are required by Active Directory from the primary IPv4 CIDR block, or IPv6 CIDR block associated with the VPC hosting for your AWS Managed Microsoft AD. For additional security, the ENIs that are created do not have Elastic IPs attached to them and you do not have permission to attach an Elastic IP to those ENIs. Therefore by default, the only inbound traffic that can communicate with your AWS Managed Microsoft AD is local VPC. You can change the security group rules to allow additional traffic sources, for example from other peered VPCs or CIDRs reachable via VPN. Use extreme caution if you attempt to change these rules as you may break your ability to communicate with your domain controllers. For more information, see [AWS Managed Microsoft AD best practices](ms_ad_best_practices.md) and [Enhancing your AWS Managed Microsoft AD network security configuration](ms_ad_network_security.md).

  You can use [prefix lists]() to manage your CIDR blocks within the security group rules. Prefix lists make it easier to manage and configure security groups and route tables. You can consolidate multiple CIDR blocks with the same port and protocols to scale your network traffic.
  + In a Windows environment, clients often communicate via [Server Message Block (SMB)](https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview) or port 445. This protocol facilitates various actions like file and printer sharing and general network communication. You will see clients traffic on port 445 to management interfaces of your AWS Managed Microsoft AD domain controllers.

    This traffic occurs as SMB clients rely on DNS (port 53) and NetBIOS (port 138) name resolution to locate your AWS Managed Microsoft AD domain resources. These clients are directed to any available interface on the domain controllers when locating domain resources. This behavior is expected and often occurs in environments with multiple network adapters and where [SMB Multichannel](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn610980(v=ws.11)) allows clients to establish connections across different interfaces for enhanced performance and redundancy.

  The following AWS Security group rules are created by default:

  **Inbound Rules**



<table>
<thead>
  <tr><th>Protocol</th><th>Port range</th><th>Source</th><th>Type of traffic</th><th>Active Directory usage</th></tr>
</thead>
<tbody>
  <tr><td>ICMP</td><td>N/A</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>Ping</td><td>LDAP Keep Alive, DFS</td></tr>
  <tr><td>TCP &amp; UDP</td><td>53</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>DNS</td><td>User and computer authentication, name resolution, trusts </td></tr>
  <tr><td>TCP &amp; UDP</td><td>88</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>Kerberos</td><td>User and computer authentication, forest level trusts</td></tr>
  <tr><td>TCP &amp; UDP</td><td>389</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>LDAP</td><td>Directory, replication, user and computer authentication group policy, trusts</td></tr>
  <tr><td>TCP &amp; UDP</td><td>445</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>SMB / CIFS</td><td>Replication, user and computer authentication, group policy, trusts</td></tr>
  <tr><td>TCP &amp; UDP</td><td>464</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>Kerberos change / set password</td><td>Replication, user and computer authentication, trusts</td></tr>
  <tr><td>TCP</td><td>135</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>Replication</td><td>RPC, EPM</td></tr>
  <tr><td>TCP</td><td>636</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>LDAP SSL</td><td>Directory, replication, user and computer authentication, group policy, trusts</td></tr>
  <tr><td>TCP</td><td>1024 - 65535</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>RPC</td><td>Replication, user and computer authentication, group policy, trusts</td></tr>
  <tr><td>TCP</td><td>3268 - 3269</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>LDAP GC &amp; LDAP GC SSL</td><td>Directory, replication, user and computer authentication, group policy, trusts</td></tr>
  <tr><td>UDP</td><td>123</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>Windows Time</td><td>Windows Time, trusts</td></tr>
  <tr><td>UDP</td><td>138</td><td>AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR</td><td>DFSN &amp; NetLogon</td><td>DFS, group policy</td></tr>
  <tr><td>All</td><td>All</td><td>AWS created security group for domain controllers ({{sg-1234567890abcdef0}})</td><td>All Traffic</td><td></td></tr>
</tbody>
</table>


  **Outbound Rules**



<table>
<thead>
  <tr><th>Protocol</th><th>Port range</th><th>Destination</th><th>Type of traffic</th><th>Active Directory usage</th></tr>
</thead>
<tbody>
  <tr><td>All</td><td>All</td><td>0.0.0.0/0 or ::/0</td><td>All Traffic</td><td></td></tr>
</tbody>
</table>

+ For more information about the ports and protocols used by Active Directory, see [Service overview and network port requirements for Windows](https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements#system-services-ports) in Microsoft documentation.
+ Creates a directory administrator account with the user name Admin and the specified password. This account is located under the Users OU (For example, Corp > Users). You use this account to manage your directory in the AWS Cloud. For more information, see [AWS Managed Microsoft AD Administrator account and group permissions](ms_ad_getting_started_admin_account.md).
**Important**  
Be sure to save this password. Directory Service does not store this password, and it cannot be retrieved. However, you can reset a password from the Directory Service console or by using the [ResetUserPassword](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html) API.
+ Creates the following three organizational units (OUs) under the domain root:



<table>
<thead>
  <tr><th>OU name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>AWS Delegated Groups</td><td>Stores all of the groups that you can use to delegate AWS specific permissions to your users. </td></tr>
  <tr><td>AWS Reserved</td><td>Stores all AWS management specific accounts.</td></tr>
  <tr><td>&lt;<i>yourdomainname</i>&gt; </td><td>The name of this OU is based off of the NetBIOS name you typed when you created your directory. If you did not specify a NetBIOS name, it will default to the first part of your Directory DNS name (for example, in the case of corp.example.com, the NetBIOS name would be <i>corp</i>). This OU is owned by AWS and contains all of your AWS-related directory objects, which you are granted Full Control over. Two child OUs exist under this OU by default; Computers and Users. For example:<ul><li> Corp <ul><li> Computers </li><li> Users </li></ul> </li></ul></td></tr>
</tbody>
</table>

+ Creates the following groups in the AWS Delegated Groups OU:



<table>
<thead>
  <tr><th>Group name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>AWS Delegated Account Operators</td><td>Members of this security group have limited account management capability such as password resets</td></tr>
  <tr><td>AWS Delegated Active Directory Based Activation Administrators</td><td>Members of this security group can create Active Directory volume licensing activation objects, which enables enterprises to activate computers through a connection to their domain.</td></tr>
  <tr><td>AWS Delegated Add Workstations To Domain Users</td><td>Members of this security group can join 10 computers to a domain.</td></tr>
  <tr><td>AWS Delegated Administrators</td><td>Members of this security group can manage AWS Managed Microsoft AD, have full control of all the objects in your OU and can manage groups contained in the AWS Delegated Groups OU.</td></tr>
  <tr><td>AWS Delegated Allowed to Authenticate Objects</td><td>Members of this security group are provided the ability to authenticate to computer resources in the AWS Reserved OU (Only needed for on-premises objects with Selective Authentication enabled Trusts).</td></tr>
  <tr><td>AWS Delegated Allowed to Authenticate to Domain Controllers</td><td>Members of this security group are provided the ability to authenticate to computer resources in the Domain Controllers OU (Only needed for on-premises objects with Selective Authentication enabled Trusts).</td></tr>
  <tr><td>AWS Delegated Deleted Object Lifetime Administrators</td><td>Members of this security group can modify the msDS-DeletedObjectLifetime object, which defines how long a deleted object will be available to recover from the AD Recycle Bin.</td></tr>
  <tr><td>AWS Delegated Distributed File System Administrators</td><td>Members of this security group can add and remove FRS, DFS-R, and DFS name spaces.</td></tr>
  <tr><td>AWS Delegated Domain Name System Administrators</td><td>Members of this security group can manage Active Directory integrated DNS.</td></tr>
  <tr><td>AWS Delegated Dynamic Host Configuration Protocol Administrators</td><td>Members of this security group can authorize Windows DHCP servers in the enterprise.</td></tr>
  <tr><td>AWS Delegated Enterprise Certificate Authority Administrators</td><td>Members of this security group can deploy and manage Microsoft Enterprise Certificate Authority infrastructure.</td></tr>
  <tr><td>AWS Delegated Fine Grained Password Policy Administrators</td><td>Members of this security group can modify precreated fine-grained password policies.</td></tr>
  <tr><td>AWS Delegated FSx Administrators</td><td>Members of this security group are provided the ability to manage Amazon FSx resources.</td></tr>
  <tr><td>AWS Delegated Group Policy Administrators</td><td>Members of this security group can perform group policy management tasks (create, edit, delete, link).</td></tr>
  <tr><td>AWS Delegated Kerberos Delegation Administrators</td><td>Members of this security group can enable delegation on computer and user account objects.</td></tr>
  <tr><td>AWS Delegated Managed Service Account Administrators</td><td>Members of this security group can create and delete Managed Service Accounts.</td></tr>
  <tr><td>AWS Delegated MS-NPRC Non-Compliant Devices</td><td>Members of this security group will be provided an exclusion from requiring secure channel communications with domain controllers. This group is for computer accounts.</td></tr>
  <tr><td>AWS Delegated Remote Access Service Administrators</td><td>Members of this security group can add and remove RAS servers from the RAS and IAS Servers group.</td></tr>
  <tr><td>AWS Delegated Replicate Directory Changes Administrators</td><td>Members of this security group can synchronize profile information in Active Directory with SharePoint Server.</td></tr>
  <tr><td>AWS Delegated Server Administrators</td><td>Members of this security group are included in the local administrators group on all domain joined computers.</td></tr>
  <tr><td>AWS Delegated Sites and Services Administrators</td><td>Members of this security group can rename the Default-First-Site-Name object in Active Directory Sites and Services.</td></tr>
  <tr><td>AWS Delegated System Management Administrators</td><td>Members of this security group can create and manage objects in the System Management container.</td></tr>
  <tr><td>AWS Delegated Terminal Server Licensing Administrators</td><td>Members of this security group can add and remove Terminal Server License Servers from the Terminal Server License Servers group.</td></tr>
  <tr><td>AWS Delegated User Principal Name Suffix Administrators</td><td>Members of this security group can add and remove user principal name suffixes.</td></tr>
</tbody>
</table>

**Note**  
You can add to these AWS Delegated Groups.
+ Creates and applies the following Group Policy Objects (GPOs):
**Note**  
You do not have permissions to delete, modify, or unlink these GPOs. This is by design as they are reserved for AWS use. You may link them to OUs that you control if needed. 



<table>
<thead>
  <tr><th>Group policy name</th><th>Applies to</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Default Domain Policy</td><td>Domain</td><td>Includes domain password and Kerberos policies.</td></tr>
  <tr><td>ServerAdmins</td><td>All non domain controller computer accounts</td><td>Adds the 'AWS Delegated Server Administrators' as a member of the BUILTIN\Administrators Group.</td></tr>
  <tr><td>AWS Reserved Policy:User</td><td>AWS Reserved user accounts</td><td>Sets recommended security settings on all user accounts in the AWS Reserved OU.</td></tr>
  <tr><td>AWS Managed Active Directory Policy</td><td>All domain controllers</td><td>Sets recommended security settings on all domain controllers.</td></tr>
  <tr><td>TimePolicyNT5DS</td><td>All non PDCe domain controllers</td><td>Sets all non PDCe domain controllers time policy to use Windows Time (NT5DS).</td></tr>
  <tr><td>TimePolicyPDC</td><td>The PDCe domain controller</td><td>Sets the PDCe domain controller's time policy to use Network Time Protocol (NTP).</td></tr>
  <tr><td>Default Domain Controllers Policy</td><td>Not used</td><td>Provisioned during domain creation, AWS Managed Active Directory Policy is used in its place. </td></tr>
</tbody>
</table>


  If you would like to see the settings of each GPO, you can view them from a domain joined Windows instance with the [Group policy management console (GPMC)](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753298(v=ws.10)) enabled.
+ Creates the following default local accounts for AWS Managed Microsoft AD management:
**Important**  
Be sure to save the admin password. Directory Service does not store this password, and it cannot be retrieved. However, you [can reset a password from the Directory Service console](ms_ad_manage_users_groups_reset_password.md) or by using the [ResetUserPassword](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html) API.  
**Admin**  
The Admin is the directory administrator account created when the AWS Managed Microsoft AD is first created. You provide a password for this account when you create an AWS Managed Microsoft AD. This account is located under the Users OU (For example, Corp > Users). You use this account to manage your Active Directory in the AWS. For more information, see [AWS Managed Microsoft AD Administrator account and group permissions](ms_ad_getting_started_admin_account.md).  
**AWS*\_{{11111111111}}***  
Any account name starting with AWS followed by an underscore and located in AWS Reserved OU is a service-managed account. This service-managed account is used by AWS to interact with the Active Directory. These accounts are created when AWS Directory Service Data is enabled and with each new AWS application authorized on Active Directory. These accounts are only accessible by AWS services.  
**krbtgt account**  
The krbtgt account plays an important role in the Kerberos ticket exchanges used by your AWS Managed Microsoft AD. The krbtgt account is a special account used for Kerberos ticket-granting ticket (TGT) encryption, and it plays a crucial role in the security of the Kerberos authentication protocol. For more information, see [Microsoft documentation](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn745899(v=ws.11)#krbtgt-account).   
AWS automatically rotates the krbtgt account password for your AWS Managed Microsoft AD twice every 90 days. There is a 24 hour waiting period between the two consecutive rotations every 90 days.

For more information about the admin account and other accounts created by Active Directory, see [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts).