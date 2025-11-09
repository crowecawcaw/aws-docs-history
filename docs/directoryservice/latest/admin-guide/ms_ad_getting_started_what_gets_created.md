# What gets created with your

AWS Managed Microsoft AD

When you create an Active Directory with AWS Managed Microsoft AD, AWS Directory Service performs the following tasks on your
behalf:

- Automatically creates and associates an elastic network interface (ENI) with each of your domain controllers.
  Each of these ENIs are essential for connectivity between your VPC and AWS Directory Service domain controllers and should never be deleted.
  You can identify all network interfaces reserved for use with AWS Directory Service by the description: "AWS created network interface for
  directory _directory-id_". For more information,
  see [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the _Amazon EC2 User Guide_.
  The default DNS Server of the AWS Managed Microsoft AD Active Directory is the VPC DNS server at Classless Inter-Domain Routing (CIDR)+2.
  For more information, see [Amazon DNS server](../../../vpc/latest/userguide/vpc-dns.md#AmazonDNS "../../../vpc/latest/userguide/vpc-dns.md#AmazonDNS")
  in _Amazon VPC User Guide_.

###### Note

Domain controllers are deployed across two Availability Zones in a region by default
and connected to your Amazon VPC (VPC). Backups are automatically taken once per day, and the
Amazon EBS (EBS) volumes are encrypted to ensure that data is secured at rest. Domain
controllers that fail are automatically replaced in the same Availability Zone using the
same IP address, and a full disaster recovery can be performed using the latest
backup.

- Provisions Active Directory within your VPC using two domain controllers for fault tolerance and
  high availability. More domain controllers can be provisioned for higher resiliency and
  performance after the directory has been successfully created and is [Active](ms_ad_directory_status.md "ms_ad_directory_status.md"). For more information, see [Deploying additional domain controllers for your
  AWS Managed Microsoft AD](ms_ad_deploy_additional_dcs.md "ms_ad_deploy_additional_dcs.md").

###### Note

AWS does not allow the installation of monitoring agents on AWS Managed Microsoft AD domain
controllers.

- Creates an [AWS
  Security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")
  `sg-1234567890abcdef0` that establishes network rules for traffic
  in and out of your domain controllers. The default outbound rule permits all traffic to all
  IPv4 addresses. The default inbound rules allows only traffic through ports that are
  required by Active Directory from the primary IPv4 CIDR block associated with the VPC hosting for your
  AWS Managed Microsoft AD. For additional security, the ENIs that are created do not have Elastic IPs
  attached to them and you do not have permission to attach an Elastic IP to those ENIs.
  Therefore by default, the only inbound traffic that can communicate with your AWS Managed Microsoft AD
  is local VPC. You can change the security group rules to allow additional traffic sources,
  for example from other peered VPCs or CIDRs reachable via VPN. Use extreme caution if you
  attempt to change these rules as you may break your ability to communicate with your domain
  controllers. For more information, see [AWS Managed Microsoft AD best practices](ms_ad_best_practices.md "ms_ad_best_practices.md") and [Enhancing your AWS Managed Microsoft AD network security
  configuration](ms_ad_network_security.md "ms_ad_network_security.md").

You can use prefix lists to manage your CIDR blocks within the security
group rules. Prefix lists make it easier to manage and configure security groups and route
tables. You can consolidate multiple CIDR blocks with the same port and protocols to scale
your network traffic.

    + In a Windows environment, clients often communicate via [Server Message Block (SMB)](https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview "https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview") or port 445. This protocol facilitates various
     actions like file and printer sharing and general network communication. You will see
     clients traffic on port 445 to management interfaces of your AWS Managed Microsoft AD domain
     controllers.


    This traffic occurs as SMB clients rely on DNS (port 53) and NetBIOS (port 138) name
     resolution to locate your AWS Managed Microsoft AD domain resources. These clients are directed to
     any available interface on the domain controllers when locating domain resources. This
     behavior is expected and often occurs in environments with multiple network adapters and
     where [SMB Multichannel](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn610980(v=ws.11) "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn610980(v=ws.11)") allows clients to establish connections across different
     interfaces for enhanced performance and redundancy.

The following AWS Security group rules are created by default:

**Inbound Rules**

| Protocol  | Port range      | Source                                                                        | Type of traffic                | Active Directory usage                                                            |
| --------- | --------------- | ----------------------------------------------------------------------------- | ------------------------------ | --------------------------------------------------------------------------------- |
| ICMP      | N/A             | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | Ping                           | LDAP Keep Alive, DFS                                                              |
| TCP & UDP | 53              | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | DNS                            | User and computer authentication, name resolution, trusts                         |
| TCP & UDP | 88              | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | Kerberos                       | User and computer authentication, forest level trusts                             |
| TCP & UDP | 389             | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | LDAP                           | Directory, replication, user and computer authentication group policy,<br>trusts  |
| TCP & UDP | 445             | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | SMB / CIFS                     | Replication, user and computer authentication, group policy, trusts               |
| TCP & UDP | 464             | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | Kerberos change / set password | Replication, user and computer authentication, trusts                             |
| TCP       | 135             | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | Replication                    | RPC, EPM                                                                          |
| TCP       | 636             | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | LDAP SSL                       | Directory, replication, user and computer authentication, group policy,<br>trusts |
| TCP       | 1024<br>• 65535 | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | RPC                            | Replication, user and computer authentication, group policy, trusts               |
| TCP       | 3268<br>• 3269  | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | LDAP GC & LDAP GC SSL          | Directory, replication, user and computer authentication, group policy,<br>trusts |
| UDP       | 123             | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | Windows Time                   | Windows Time, trusts                                                              |
| UDP       | 138             | AWS Managed Microsoft AD VPC IPv4 CIDR                                        | DFSN & NetLogon                | DFS, group policy                                                                 |
| All       | All             | AWS created security group for domain controllers<br>(`sg-1234567890abcdef0`) | All Traffic                    |                                                                                   |

**Outbound Rules**

| Protocol | Port range | Destination | Type of traffic | Active Directory usage |
| -------- | ---------- | ----------- | --------------- | ---------------------- |
| All      | All        | 0.0.0.0/0   | All Traffic     |                        |

- For more information about the ports and protocols used by Active Directory, see [Service overview and network port requirements for Windows](https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements#system-services-ports "https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements#system-services-ports") in Microsoft
  documentation.
- Creates a directory administrator account with the user name Admin and the specified
  password. This account is located under the Users OU (For example, Corp >
  Users). You use this account to manage your directory in the AWS Cloud. For more
  information, see [AWS Managed Microsoft AD Administrator account and
  group permissions](ms_ad_getting_started_admin_account.md "ms_ad_getting_started_admin_account.md").

###### Important

Be sure to save this password. AWS Directory Service does not store this password, and it cannot be
retrieved. However, you can reset a password from the AWS Directory Service console or by using the [ResetUserPassword](../devguide/API_ResetUserPassword.md "../devguide/API_ResetUserPassword.md") API.

- Creates the following three organizational units (OUs) under the domain root:

| OU name              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Delegated Groups | Stores all of the groups that you can use to delegate AWS specific<br>permissions to your users.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AWS Reserved         | Stores all AWS management specific accounts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <_yourdomainname_>   | The name of this OU is based off of the NetBIOS name you typed when you created<br>your directory. If you did not specify a NetBIOS name, it will default to the first<br>part of your Directory DNS name (for example, in the case of corp.example.com, the<br>NetBIOS name would be _corp_). This OU is owned by AWS and<br>contains all of your AWS-related directory objects, which you are granted Full<br>Control over. Two child OUs exist under this OU by default; Computers and Users. For example:<br>+ Corp<br>• Computers<br>• Users |

- Creates the following groups in the AWS Delegated Groups OU:

| Group name                                                          | Description                                                                                                                                                                                                          |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Delegated Account Operators                                     | Members of this security group have limited account management capability such<br>as password resets                                                                                                                 |
| AWS Delegated Active Directory Based Activation<br>Administrators   | Members of this security group can create Active Directory volume licensing<br>activation objects, which enables enterprises to activate computers through a<br>connection to their domain.                          |
| AWS Delegated Add Workstations To Domain Users                      | Members of this security group can join 10 computers to a domain.                                                                                                                                                    |
| AWS Delegated Administrators                                        | Members of this security group can manage AWS Managed Microsoft AD, have full control of<br>all the objects in your OU and can manage groups contained in the AWS<br>Delegated Groups OU.                            |
| AWS Delegated Allowed to Authenticate Objects                       | Members of this security group are provided the ability to authenticate to<br>computer resources in the AWS Reserved OU (Only needed for<br>on-premises objects with Selective Authentication enabled Trusts).       |
| AWS Delegated Allowed to Authenticate to Domain<br>Controllers      | Members of this security group are provided the ability to authenticate to<br>computer resources in the Domain Controllers OU (Only needed for<br>on-premises objects with Selective Authentication enabled Trusts). |
| AWS Delegated Deleted Object Lifetime Administrators                | Members of this security group can modify the<br>msDS-DeletedObjectLifetime object, which defines how long a<br>deleted object will be available to recover from the AD Recycle Bin.                                 |
| AWS Delegated Distributed File System Administrators                | Members of this security group can add and remove FRS, DFS-R, and DFS name<br>spaces.                                                                                                                                |
| AWS Delegated Domain Name System Administrators                     | Members of this security group can manage Active Directory integrated<br>DNS.                                                                                                                                        |
| AWS Delegated Dynamic Host Configuration Protocol<br>Administrators | Members of this security group can authorize Windows DHCP servers in the<br>enterprise.                                                                                                                              |
| AWS Delegated Enterprise Certificate Authority<br>Administrators    | Members of this security group can deploy and manage Microsoft Enterprise<br>Certificate Authority infrastructure.                                                                                                   |
| AWS Delegated Fine Grained Password Policy<br>Administrators        | Members of this security group can modify precreated fine-grained password<br>policies.                                                                                                                              |
| AWS Delegated FSx Administrators                                    | Members of this security group are provided the ability to manage Amazon FSx<br>resources.                                                                                                                           |
| AWS Delegated Group Policy Administrators                           | Members of this security group can perform group policy management tasks<br>(create, edit, delete, link).                                                                                                            |
| AWS Delegated Kerberos Delegation Administrators                    | Members of this security group can enable delegation on computer and user<br>account objects.                                                                                                                        |
| AWS Delegated Managed Service Account Administrators                | Members of this security group can create and delete Managed Service<br>Accounts.                                                                                                                                    |
| AWS Delegated MS-NPRC Non-Compliant Devices                         | Members of this security group will be provided an exclusion from requiring<br>secure channel communications with domain controllers. This group is for computer<br>accounts.                                        |
| AWS Delegated Remote Access Service Administrators                  | Members of this security group can add and remove RAS servers from the RAS and<br>IAS Servers group.                                                                                                                 |
| AWS Delegated Replicate Directory Changes<br>Administrators         | Members of this security group can synchronize profile information in Active<br>Directory with SharePoint Server.                                                                                                    |
| AWS Delegated Server Administrators                                 | Members of this security group are included in the local administrators group<br>on all domain joined computers.                                                                                                     |
| AWS Delegated Sites and Services Administrators                     | Members of this security group can rename the Default-First-Site-Name object in<br>Active Directory Sites and Services.                                                                                              |
| AWS Delegated System Management Administrators                      | Members of this security group can create and manage objects in the System<br>Management container.                                                                                                                  |
| AWS Delegated Terminal Server Licensing Administrators              | Members of this security group can add and remove Terminal Server License<br>Servers from the Terminal Server License Servers group.                                                                                 |
| AWS Delegated User Principal Name Suffix<br>Administrators          | Members of this security group can add and remove user principal name<br>suffixes.                                                                                                                                   |

###### Note

You can add to these AWS Delegated Groups.

- Creates and applies the following Group Policy Objects (GPOs):

###### Note

You do not have permissions to delete, modify, or unlink these GPOs. This is by design
as they are reserved for AWS use. You may link them to OUs that you control if needed.

| Group policy name                   | Applies to                                  | Description                                                                                        |
| ----------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Default Domain Policy               | Domain                                      | Includes domain password and Kerberos policies.                                                    |
| ServerAdmins                        | All non domain controller computer accounts | Adds the 'AWS Delegated Server Administrators' as a member of<br>the BUILTIN\Administrators Group. |
| AWS Reserved Policy:User            | AWS Reserved user accounts                  | Sets recommended security settings on all user accounts in the AWS<br>Reserved OU.                 |
| AWS Managed Active Directory Policy | All domain controllers                      | Sets recommended security settings on all domain controllers.                                      |
| TimePolicyNT5DS                     | All non PDCe domain controllers             | Sets all non PDCe domain controllers time policy to use Windows Time<br>(NT5DS).                   |
| TimePolicyPDC                       | The PDCe domain controller                  | Sets the PDCe domain controller's time policy to use Network Time Protocol<br>(NTP).               |
| Default Domain Controllers Policy   | Not used                                    | Provisioned during domain creation, AWS Managed Active Directory Policy is<br>used in its place.   |

If you would like to see the settings of each GPO, you can view them from a domain
joined Windows instance with the [Group policy management console (GPMC)](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753298(v=ws.10)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753298(v=ws.10)") enabled.

- Creates the following default local accounts for AWS Managed Microsoft AD
  management:

###### Important

Be sure to save the admin password. AWS Directory Service does not store this password, and it cannot
be retrieved. However, you [can
reset a password from the AWS Directory Service console](ms_ad_manage_users_groups_reset_password.md "ms_ad_manage_users_groups_reset_password.md") or by using the [ResetUserPassword](../devguide/API_ResetUserPassword.md "../devguide/API_ResetUserPassword.md") API.

**Admin**

The Admin is the directory administrator account
created when the AWS Managed Microsoft AD is first created. You provide a password for this
account when you create an AWS Managed Microsoft AD. This account is located under the
Users OU (For example, Corp > Users). You use this account to manage
your Active Directory in the AWS. For more information, see [AWS Managed Microsoft AD Administrator account and
group permissions](ms_ad_getting_started_admin_account.md "ms_ad_getting_started_admin_account.md").

**AWS_11111111111**

Any account name starting with AWS followed by an underscore and located in
AWS Reserved OU is a service-managed account. This service-managed
account is used by AWS to interact with the Active Directory. These accounts are created when
AWS Directory Service Data is enabled and with each new AWS application authorized on Active Directory. These
accounts are only accessible by AWS services.

**krbtgt account**

The krbtgt account plays an important role in the Kerberos ticket
exchanges used by your AWS Managed Microsoft AD. The krbtgt account is a special
account used for Kerberos ticket-granting ticket (TGT) encryption, and it plays a
crucial role in the security of the Kerberos authentication protocol. For more
information, see [Microsoft documentation](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn745899(v=ws.11)#krbtgt-account> "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn745899(v=ws.11)#krbtgt-account").

AWS automatically rotates the krbtgt account password for your
AWS Managed Microsoft AD twice every 90 days. There is a 24 hour waiting period between the two
consecutive rotations every 90 days.
For more information about the admin account and other accounts created by Active Directory, see [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts").
