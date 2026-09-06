

# What gets created with your hybrid directory
<a name="hybrid_directory_what_gets_created"></a>

When you create an Active Directory with AWS Managed Microsoft AD (Hybrid Edition), Directory Service performs several tasks automatically on your behalf. This topic provides a comprehensive reference of every resource, account, organizational unit, delegated group, and group policy object that AWS creates during directory provisioning.

The following resources are created automatically upon directory creation:
+ Elastic Network Interfaces (ENIs) for each domain controller
+ Active Directory domain controllers across two Availability Zones
+ Two Organizational Units (OUs) under the domain root
+ AWS Delegated Groups for delegated permissions management
+ Group Policy Objects (GPOs) for domain security configuration
+ Default local accounts for AWS management purposes

## Elastic Network Interfaces and Domain Controllers
<a name="hybrid_what_gets_created_enis"></a>

When provisioning a Hybrid directory, Directory Service automatically creates and associates an elastic network interface (ENI) with each of your domain controllers. These ENIs are essential for connectivity between your Amazon VPC and the Directory Service domain controllers.

**Important**  
You should never delete these ENIs. You can identify all network interfaces reserved for use with Directory Service by their description: "AWS created network interface for directory {{directory-id}}".

### Domain Controller architecture
<a name="hybrid_what_gets_created_dc_architecture"></a>

Directory Service provisions Active Directory within your VPC using two domain controllers by default, providing fault tolerance and high availability:
+ Domain controllers are deployed across two Availability Zones in a Region by default
+ Both domain controllers are connected to your Amazon VPC
+ Backups are automatically taken once per day
+ Amazon EBS volumes are encrypted to ensure data is secured at rest
+ Domain controllers that fail are automatically replaced in the same Availability Zone using the same IP address
+ Additional domain controllers can be provisioned for higher resiliency and performance after the directory is Active

### DNS server configuration
<a name="hybrid_what_gets_created_dns"></a>

The default DNS server of a Hybrid directory is the VPC DNS server at Classless Inter-Domain Routing (CIDR)\+2. For more information, refer to the Amazon DNS server documentation in the *Amazon VPC User Guide*.

**Note**  
AWS does not allow the installation of monitoring agents on AWS Managed Microsoft AD (Hybrid Edition) domain controllers.

## Organizational Units (OUs)
<a name="hybrid_what_gets_created_ous"></a>

Directory Service creates two Organizational Units (OUs) directly under your existing self-managed directory domain root. These OUs form the structural foundation for organizing directory objects, accounts, and delegated permissions within your AWS Managed Microsoft AD (Hybrid Edition).


| OU Name | Description | 
| --- | --- | 
| AWS Delegated Groups | Stores all of the groups that you can use to delegate AWS-specific permissions to your users. | 
| AWS Reserved | Stores all AWS management-specific accounts, including service-managed accounts used by AWS services. | 

**Domain OU Structure Example**

The following illustrates the default OU hierarchy for a domain named `corp.example.com` (NetBIOS: Corp):

```
corp.example.com (domain root)
    Corp
    AWS Delegated Groups
    AWS Reserved
```

## AWS Delegated Groups
<a name="hybrid_what_gets_created_delegated_groups"></a>

Directory Service creates a comprehensive set of security groups in the AWS Delegated Groups OU. Each group is designed to delegate a specific set of AWS and Active Directory permissions to your users, without requiring full domain administrator rights.

**Note**  
You can add members to these AWS Delegated Groups. Members of AWS Delegated Administrators can manage all groups in the AWS Delegated Groups OU.


| Group Name | Description | 
| --- | --- | 
| AWS Delegated Account Operators | Members have limited account management capability such as password resets. | 
| AWS Delegated Active Directory Based Activation Administrators | Members can create Active Directory volume licensing activation objects, enabling enterprises to activate computers through a connection to their domain. | 
| AWS Delegated Add Workstations To Domain Users | Members can join 10 computers to a domain. | 
| AWS Delegated Administrators | Members can manage AWS Managed Microsoft AD, have full control of all objects in your OU, and can manage groups in the AWS Delegated Groups OU. | 
| AWS Delegated Allowed to Authenticate Objects | Members are provided the ability to authenticate to computer resources in the AWS Reserved OU. Only needed for on-premises objects with Selective Authentication enabled Trusts. | 
| AWS Delegated Allowed to Authenticate to Domain Controllers | Members are provided the ability to authenticate to computer resources in the Domain Controllers OU. Only needed for on-premises objects with Selective Authentication enabled Trusts. | 
| AWS Delegated Deleted Object Lifetime Administrators | Members can modify the msDS-DeletedObjectLifetime object, which defines how long a deleted object will be available to recover from the AD Recycle Bin. | 
| AWS Delegated Distributed File System Administrators | Members can add and remove FRS, DFS-R, and DFS name spaces. | 
| AWS Delegated Domain Name System Administrators | Members can manage Active Directory integrated DNS. | 
| AWS Delegated Dynamic Host Configuration Protocol Administrators | Members can authorize Windows DHCP servers in the enterprise. | 
| AWS Delegated Enterprise Certificate Authority Administrators | Members can deploy and manage Microsoft Enterprise Certificate Authority infrastructure. | 
| AWS Delegated Fine Grained Password Policy Administrators | Members can modify precreated fine-grained password policies. | 
| AWS Delegated FSx Administrators | Members are provided the ability to manage Amazon FSx resources. | 
| AWS Delegated Group Policy Administrators | Members can perform group policy management tasks (create, edit, delete, link). | 
| AWS Delegated Kerberos Delegation Administrators | Members can enable delegation on computer and user account objects. | 
| AWS Delegated Managed Service Account Administrators | Members can create and delete Managed Service Accounts. | 
| AWS Delegated MS-NPRC Non-Compliant Devices | Members will be provided an exclusion from requiring secure channel communications with domain controllers. This group is for computer accounts. | 
| AWS Delegated Remote Access Service Administrators | Members can add and remove RAS servers from the RAS and IAS Servers group. | 
| AWS Delegated Replicate Directory Changes Administrators | Members can synchronize profile information in Active Directory with SharePoint Server. | 
| AWS Delegated Server Administrators | Members are included in the local administrators group on all domain-joined computers. | 
| AWS Delegated Sites and Services Administrators | Members can rename the Default-First-Site-Name object in Active Directory Sites and Services. | 
| AWS Delegated System Management Administrators | Members can create and manage objects in the System Management container. | 
| AWS Delegated Terminal Server Licensing Administrators | Members can add and remove Terminal Server License Servers from the Terminal Server License Servers group. | 
| AWS Delegated User Principal Name Suffix Administrators | Members can add and remove user principal name suffixes. | 

## Group Policy Objects (GPOs)
<a name="hybrid_what_gets_created_gpos"></a>

Directory Service creates and applies a set of Group Policy Objects (GPOs) to enforce security settings and administrative configurations across your AWS Managed Microsoft AD (Hybrid Edition) domain controllers. These GPOs are pre-configured and maintained by AWS.

**Important**  
You do not have permissions to delete, modify, or unlink these GPOs. This is by design, as they are reserved for AWS use. You may link them to OUs that you control if needed. To view the settings of each GPO, use the Group Policy Management Console (GPMC) from a domain-joined Windows instance.


| GPO Name | Applies to | Description | 
| --- | --- | --- | 
| AWS Reserved Policy:User | AWS Reserved user accounts | Sets recommended security settings on all user accounts in the AWS Reserved OU. | 
| AWS Hybrid Managed Active Directory Policy | All hybrid AD domain controllers | Sets recommended security settings on all domain controllers. | 
| AWS Managed AppLocker Policy | All hybrid AD domain controllers | Enforces code signing requirements for monitoring agents and other executables on Hybrid AD domain controllers. | 
| TimePolicyNT5DS | All non-PDCe hybrid AD domain controllers | Sets all non-PDCe domain controllers time policy to use Windows Time (NT5DS). | 
| TimePolicyPDC | The PDCe hybrid AD domain controller | Sets the PDCe domain controller's time policy to use Network Time Protocol (NTP). | 

**Fine-Grained Password Policy**

A Fine-Grained Password Policy is applied to enforce password requirements for accounts in the AWS Reserved OU.

## Default local accounts
<a name="hybrid_what_gets_created_accounts"></a>

Directory Service creates several default accounts in your AWS Managed Microsoft AD (Hybrid Edition) during provisioning. These accounts serve different operational roles and are managed in distinct ways.

### Admin account
<a name="hybrid_what_gets_created_admin_account"></a>

The Admin account is the directory administrator account created when the hybrid directory is first provisioned. This account is used by Directory Service to manage your hybrid AD domain controllers.
+ **Username:** Random
+ **Location:** AWS Reserved OU
+ **Purpose:** Manage your Active Directory in the AWS Cloud
+ **Access:** This account is only accessible by Directory Service and cannot be used by end-users

### `AWS_11111111111` (Service-Managed Accounts)
<a name="hybrid_what_gets_created_service_accounts"></a>

Any account name beginning with `AWS_` followed by an underscore and located in the AWS Reserved OU is a service-managed account. These accounts are used by AWS services to interact with the Active Directory.
+ **Account format:** `AWS_` followed by an account identifier (e.g., `AWS_11111111111`)
+ **Location:** AWS Reserved OU
+ **Created when:** Directory Service Data is enabled, or when a new AWS application is authorized on Active Directory
+ **Access:** These accounts are only accessible by AWS services and cannot be used by end-users

### krbtgt account
<a name="hybrid_what_gets_created_krbtgt"></a>

The krbtgt account plays a critical role in the Kerberos authentication infrastructure of your AWS Managed Microsoft AD (Hybrid Edition). This special account is used for Kerberos ticket-granting ticket (TGT) encryption and is integral to the security of all Kerberos-based authentication within the domain.

### Group Managed Service Accounts (gMSA)
<a name="hybrid_what_gets_created_gmsa"></a>

Directory Service creates a Group Managed Service Account (gMSA) in the AWS Reserved OU to support internal service authentication.

## Hybrid Administration Groups
<a name="hybrid_what_gets_created_admin_groups"></a>

Directory Service creates a set of security groups in the AWS Reserved OU. Each group is designed to perform administrative tasks for your hybrid directory domain controllers.


| Group Name | Description | 
| --- | --- | 
| AWS Administrators | Members have full control of all sub-objects in the customer OU and group management rights in AWS Delegated Groups OU. | 
| AWS Service Administrators | Hybrid directory specific complete unrestricted access to the computer/domain including the AWS Reserved OU. | 
| AWS Object Management Service Accounts | Highly privileged group for managing AWS hybrid directory full control over users and groups in customer OU. | 
| AWS Private CA Connector for AD Delegated Group | Used by AWS Private CA Connector for AD READ access to customer OU, READ/WRITE for CA objects. | 
| AWS Application and Service Delegated Group | Used for AWS Application/Service delegation manages SPNs on computer objects and creates GPOs. | 