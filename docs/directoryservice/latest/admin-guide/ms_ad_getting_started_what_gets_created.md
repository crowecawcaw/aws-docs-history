

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html)

  **Outbound Rules**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html)
+ For more information about the ports and protocols used by Active Directory, see [Service overview and network port requirements for Windows](https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements#system-services-ports) in Microsoft documentation.
+ Creates a directory administrator account with the user name Admin and the specified password. This account is located under the Users OU (For example, Corp > Users). You use this account to manage your directory in the AWS Cloud. For more information, see [AWS Managed Microsoft AD Administrator account and group permissions](ms_ad_getting_started_admin_account.md).
**Important**  
Be sure to save this password. Directory Service does not store this password, and it cannot be retrieved. However, you can reset a password from the Directory Service console or by using the [ResetUserPassword](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html) API.
+ Creates the following three organizational units (OUs) under the domain root:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html)
+ Creates the following groups in the AWS Delegated Groups OU:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html)
**Note**  
You can add to these AWS Delegated Groups.
+ Creates and applies the following Group Policy Objects (GPOs):
**Note**  
You do not have permissions to delete, modify, or unlink these GPOs. This is by design as they are reserved for AWS use. You may link them to OUs that you control if needed.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html)

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