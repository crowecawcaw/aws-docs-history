# AWS Managed Microsoft AD best practices

Here are some suggestions and guidelines you should consider to avoid problems and get the
most out of AWS Managed Microsoft AD.

###### Topics

- [Best practices for setting up an
  AWS Managed Microsoft AD](#ms_ad_best_practices_set_up "#ms_ad_best_practices_set_up")
- [Best practices when using an AWS Managed Microsoft AD directory](#ms_ad_bp_using_directory "#ms_ad_bp_using_directory")
- [Best practices when programming your applications for an AWS Managed Microsoft AD](#program_apps "#program_apps")

## Best practices for setting up an

AWS Managed Microsoft AD

Here are some suggestions and guidelines for when you're setting up your
AWS Managed Microsoft AD:

###### Topics

- [Prerequisites](#ms_ad_best_practices_prereq "#ms_ad_best_practices_prereq")
- [Creating your AWS Managed Microsoft AD](#ms_ad_best_practices_create "#ms_ad_best_practices_create")

### Prerequisites

Consider these guidelines before creating your directory.

#### Verify you have the right directory type

AWS Directory Service provides multiple ways to use Microsoft Active Directory with other AWS
services. You can choose the directory service with the features you need at a cost
that fits your budget:

- **AWS Directory Service for Microsoft Active Directory** is a feature-rich managed
  Microsoft Active Directory hosted on the AWS cloud. AWS Managed Microsoft AD is your best choice
  if you have more than 5,000 users and need a trust relationship set up between an AWS
  hosted directory and your on-premises directories.
- **AD Connector** simply connects your
  existing on-premises Active Directory to AWS. AD Connector is your best
  choice when you want to use your existing on-premises directory with AWS
  services.
- **Simple AD** is a low-scale, low-cost directory
  with basic Active Directory compatibility. It supports 5,000 or fewer users, Samba
  4–compatible applications, and LDAP compatibility for LDAP-aware applications.

For a more detailed comparison of AWS Directory Service options, see [Which to choose](what_is.md#choosing_an_option "what_is.md#choosing_an_option").

#### Ensure your VPCs and instances are configured

correctly

In order to connect to, manage, and use your directories, you must properly
configure the VPCs that the directories are associated with. See either [Prerequisites for creating a
AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_prereqs "ms_ad_getting_started.md#ms_ad_getting_started_prereqs"), [AD Connector prerequisites](ad_connector_getting_started.md#prereq_connector "ad_connector_getting_started.md#prereq_connector"), or [Simple AD prerequisites](simple_ad_getting_started.md#prereq_simple "simple_ad_getting_started.md#prereq_simple") for information about the
VPC security and networking requirements.

If you are adding an instance to your domain, ensure that you have connectivity
and remote access to your instance as described in [Ways to join an Amazon EC2 instance to your
AWS Managed Microsoft AD](ms_ad_join_instance.md "ms_ad_join_instance.md").

#### Be aware of your limits

Learn about the various limits for your specific directory type. The available storage and the aggregate size of your objects are the only limitations on the number of objects you may store in your directory. See either [AWS Managed Microsoft AD quotas](ms_ad_limits.md "ms_ad_limits.md"), [AD Connector quotas](ad_connector_limits.md "ad_connector_limits.md"), or [Simple AD quotas](simple_ad_limits.md "simple_ad_limits.md") for details about your chosen directory.

#### Understand your directory's AWS security group

configuration and use

AWS creates a [security group](../../../AWSEC2/latest/UserGuide/using-network-security.md#adding-security-group-rule "../../../AWSEC2/latest/UserGuide/using-network-security.md#adding-security-group-rule") and attaches it to your directory's domain controller [elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md"). This security group blocks unnecessary traffic to the domain
controller and allows traffic that is necessary for Active Directory communications. AWS configures
the security group to open only the ports that are required for Active Directory communications. In
the default configuration, the security group accepts traffic to these ports from
AWS Managed Microsoft AD VPC IPv4 CIDR address. AWS attaches the security group to your domain
controller interfaces that are accessible from within your peered or resized [VPCs](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/"). These interfaces are inaccessible from the
internet even if you modify routing tables, change the network connections to your VPC,
and configure the [NAT Gateway
service](../../../AmazonVPC/latest/UserGuide/vpc-nat-gateway.md "../../../AmazonVPC/latest/UserGuide/vpc-nat-gateway.md"). As such, only instances and computers that have a network path into the
VPC can access the directory. This simplifies setup by eliminating the requirement for you
to configure specific address ranges. Instead, you configure routes and security groups
into the VPC that permit traffic only from trusted instances and computers.

##### Modifying the directory security group

If you want to increase the security of your directory security groups, you can
modify them to accept traffic from a more restrictive list of IP addresses. For example,
you could change the accepted addresses from your VPC IPv4 CIDR range to a CIDR range
that is specific to a single subnet or computer. Similarly, you might choose to restrict
the destination addresses to which your domain controllers can communicate. Make such
changes only if you fully understand how security group filtering works. For more
information, see [Amazon EC2
security groups for Linux instances](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md") in the _Amazon EC2 User
Guide_. Improper changes can result in loss of communications to intended
computers and instances. AWS recommends that you do not attempt to open additional
ports to the domain controller as this decreases the security of your directory. Please
carefully review the [AWS Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

###### Warning

It is technically possible for you to associate the security groups, which your
directory uses, with other EC2 instances that you create. However, AWS recommends
against this practice. AWS may have reasons to modify the security group without
notice to address functional or security needs of the managed directory. Such changes
affect any instances with which you associate the directory security group.
Furthermore, associating the directory security group with your EC2 instances creates
a potential security risk for your EC2 instances. The directory security group accepts
traffic on required Active Directory ports from AWS Managed Microsoft AD VPC IPv4 CIDR address. If you
associate this Security Group with an EC2 instance that has a public IP address
attached to the internet, then any computer on the internet can communicate with your
EC2 instance on the opened ports.

### Creating your AWS Managed Microsoft AD

Here are some suggestions to consider as you create your AWS Managed Microsoft AD.

###### Topics

- [Remember your administrator ID and password](#ms_ad_remember_pw "#ms_ad_remember_pw")
- [Create a DHCP options set](#bp_create_dhcp_options_set "#bp_create_dhcp_options_set")
- [Enable Conditional Forwarder
  Setting](#bp_conditional_forwarder_settings "#bp_conditional_forwarder_settings")
- [Deploy additional domain controllers](#bp_create_additional_dcs "#bp_create_additional_dcs")
- [Understand username restrictions for AWS
  applications](#usernamerestrictions "#usernamerestrictions")

#### Remember your administrator ID and password

When you set up your directory, you provide a password for the administrator account.
That account ID is _Admin_ for AWS Managed Microsoft AD. Remember the password that
you create for this account; otherwise you will not be able to add objects to your
directory.

#### Create a DHCP options set

We recommend that you create a DHCP options set for your AWS Directory Service directory and assign
the DHCP options set to the VPC that your directory is in. That way any instances in that
VPC can point to the specified domain, and DNS servers can resolve their domain
names.

For more information about DHCP options sets, see [Creating or changing a DHCP options set for
AWS Managed Microsoft AD](dhcp_options_set.md "dhcp_options_set.md").

#### Enable Conditional Forwarder

Setting

The following conditional forward settings _Store this conditional forwarder
in Active Directory, replicate as follows:_ should be enabled. Enabling these
settings will ensure the conditional forwarder setting is persistent when a node is
replaced due to infrastructure failure or overload failure.

Conditional forwarders should be created on one Domain Controller with the previous
setting enabled. This will allow replication to other Domain Controllers.

#### Deploy additional domain controllers

By default, AWS creates two domain controllers that exist in separate Availability
Zones. This provides fault resiliency during software patching and other events that may
make one domain controller unreachable or unavailable. We recommend that you [deploy additional domain
controllers](ms_ad_deploy_additional_dcs.md "ms_ad_deploy_additional_dcs.md") to further increase resiliency and ensure scale-out performance in
the event of a longer term event that affects access to a domain controller or an
Availability Zone.

For more information, see [Use the Windows DC locator service](#program_dc_locator "#program_dc_locator").

#### Understand username restrictions for AWS

applications

AWS Directory Service provides support for most character formats that can be used in the construction
of usernames. However, there are character restrictions that are enforced on usernames
that will be used for signing in to AWS applications, such as WorkSpaces, WorkDocs, Amazon WorkMail, or
Quick Suite. These restrictions require that the following characters not be used:

- Spaces
- Multibyte characters
- !"#$%&'()\*+,/:;<=>?@[\]^`{|}~

###### Note

The @ symbol is allowed as long as it precedes a UPN suffix.

## Best practices when using an AWS Managed Microsoft AD directory

Here are some suggestions to keep in mind when using your AWS Managed Microsoft AD.

###### Topics

- [Do not alter predefined users, groups and organizational
  units](#predefined_groups "#predefined_groups")
- [Automatically join domains](#auto_join_domains "#auto_join_domains")
- [Set up trusts correctly](#setup_trust_correctly "#setup_trust_correctly")
- [Track your domain controller performance](#bp_scale_dcs "#bp_scale_dcs")
- [Carefully plan for schema extensions](#manage_schema_extensions "#manage_schema_extensions")
- [About load balancers](#manage_load_balancer "#manage_load_balancer")
- [Make a backup of your instance](#make_backups "#make_backups")
- [Set up SNS messaging](#use_sns "#use_sns")
- [Apply directory service settings](#ds-settings "#ds-settings")
- [Remove Amazon Enterprise applications before deleting a
  directory](#remove_rds "#remove_rds")
- [Use SMB 2.x clients when accessing the SYSVOL and NETLOGON
  shares](#use_smbv2 "#use_smbv2")

### Do not alter predefined users, groups and organizational

units

When you use AWS Directory Service to launch a directory, AWS creates an organizational unit (OU) that
contains all your directory's objects. This OU, which has the NetBIOS name that you typed
when you created your directory, is located in the domain root. The domain root is owned and
managed by AWS. Several groups and an administrative user are also created.

Do not move, delete or in any other way alter these predefined objects. Doing so can
make your directory inaccessible by both yourself and AWS. For more information, see [What gets created with your
AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md").

### Automatically join domains

When launching a Windows instance that is to be part of an AWS Directory Service domain, it is often
easiest to join the domain as part of the instance creation process rather than manually
adding the instance later. To automatically join a domain, simply select the correct
directory for **Domain join directory** when launching a new instance. You
can find details in [Joining an Amazon EC2 Windows instance to your AWS Managed Microsoft AD
Active Directory](launching_instance.md "launching_instance.md").

### Set up trusts correctly

When setting up trust relationship between your AWS Managed Microsoft AD directory and another
directory, keep in mind these guidelines:

- The trust type must match on both sides (Forest or External)
- Ensure the trust direction is setup correctly if using a one-way trust (Outgoing on
  trusting domain, Incoming on trusted domain)
- Both fully qualified domain names (FQDNs) and NetBIOS names must be unique between
  forests / domains

For more details and specific instructions on setting up a trust relationship, see [Creating a trust relationship between your AWS Managed Microsoft AD and self-managed AD](ms_ad_setup_trust.md "ms_ad_setup_trust.md").

### Track your domain controller performance

To help optimize scaling decisions and improve directory resilience and performance, we
recommend that you use CloudWatch metrics. For more information, see [Using CloudWatch to monitor the performance of your AWS Managed Microsoft AD domain controllers](ms_ad_monitor_dc_performance.md "ms_ad_monitor_dc_performance.md").

For instructions on how to set up domain controller metrics using the CloudWatch console, see
[How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/ "https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/") in the AWS
Security Blog.

### Carefully plan for schema extensions

Thoughtfully apply schema extensions to index your directory for important and frequent
queries. Use care to not over-index the directory as indexes consume directory space and
rapidly changing indexed values can result in performance problems. To add indexes, you must
create a Lightweight Directory Access Protocol (LDAP) Directory Interchange Format (LDIF)
file and extend your schema change. For more information, see [Extend your AWS Managed Microsoft AD schema](ms_ad_schema_extensions.md "ms_ad_schema_extensions.md").

### About load balancers

Do not use a load balancer in front of the AWS Managed Microsoft AD end-points. Microsoft designed Active Directory
(AD) for use with a domain controller (DC) discovery algorithm that finds the most
responsive operational DC without external load balancing. External network load balancers
inaccurately detect active DCs and can result in your application being sent to a DC that is
coming up but not ready for use. For more information, see [Load balancers and Active Directory](https://social.technet.microsoft.com/wiki/contents/articles/33547.load-balancers-and-active-directory.aspx "https://social.technet.microsoft.com/wiki/contents/articles/33547.load-balancers-and-active-directory.aspx") on Microsoft TechNet which recommends fixing
applications to use Active Directory correctly rather than implementing external load
balancers.

### Make a backup of your instance

If you decide to manually add an instance to an existing AWS Directory Service domain, make a backup or
take a snapshot of that instance first. This is particularly important when joining a Linux
instance. Some of the procedures used to add an instance, if not performed correctly, can
render your instance unreachable or unusable. For more information, see [Restoring your AWS Managed Microsoft AD with snapshots](ms_ad_snapshots.md "ms_ad_snapshots.md").

### Set up SNS messaging

With Amazon Simple Notification Service (Amazon SNS), you can receive email or text (SMS) messages when the status of
your directory changes. You will be notified if your directory goes from an
**Active** status to an **Impaired** or
**Inoperable** status. You also receive a notification when the directory
returns to an Active status.

Also remember that if you have an SNS topic that receives messages from AWS Directory Service, before
deleting that topic from the Amazon SNS console, you should associate your directory with a
different SNS topic. Otherwise you risk missing important directory status messages. For
information about how to set up Amazon SNS, see [Enabling AWS Managed Microsoft AD directory status
notifications with Amazon Simple Notification Service](ms_ad_enable_notifications.md "ms_ad_enable_notifications.md").

### Apply directory service settings

AWS Managed Microsoft AD allows you to tailor your security configuration to meet your compliance
and security requirements. AWS Managed Microsoft AD deploys and maintains the configuration to all
domain controllers in your directory, including when adding new regions or additional domain
controllers. You can configure and apply these security settings for all your new and
existing directories. You can do this in the console by following the steps in [Edit directory security settings](ms_ad_directory_settings.md#edit-ds-settings "ms_ad_directory_settings.md#edit-ds-settings") or through the [UpdateSettings
API](../devguide/API_UpdateSettings.md "../devguide/API_UpdateSettings.md").

For more information, see [Editing AWS Managed Microsoft AD directory security settings](ms_ad_directory_settings.md "ms_ad_directory_settings.md").

### Remove Amazon Enterprise applications before deleting a

directory

Before deleting a directory that is associated with one or more Amazon Enterprise
Applications such as, WorkSpaces, Amazon WorkSpaces Application Manager, WorkDocs, Amazon WorkMail, AWS Management Console, or Amazon Relational Database Service (Amazon RDS), you
must first remove each application. For more information how to remove these applications,
see [Deleting your AWS Managed Microsoft AD](ms_ad_delete.md "ms_ad_delete.md").

### Use SMB 2.x clients when accessing the SYSVOL and NETLOGON

shares

Client computers use Server Message Block (SMB) to access the SYSVOL and NETLOGON shares
on AWS Managed Microsoft AD domain controllers for Group Policy, login scripts and other files.
AWS Managed Microsoft AD only supports SMB version 2.0 (SMBv2) and newer.

The SMBv2 and newer version protocols add a number of features that improve client
performance and increase the security of your domain controllers and clients. This change
follows recommendations by the [United States Computer Emergency Readiness Team](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices "https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices") and [Microsoft](https://blogs.technet.microsoft.com/filecab/2016/09/16/stop-using-smb1/ "https://blogs.technet.microsoft.com/filecab/2016/09/16/stop-using-smb1/") to disable SMBv1.

###### Important

If you currently use SMBv1 clients to access the SYSVOL and NETLOGON shares of your
domain controller, you must update those clients to use SMBv2 or newer. Your directory
will work correctly but your SMBv1 clients will fail to connect to the SYSVOL and NETLOGON
shares of your AWS Managed Microsoft AD domain controllers, and will also be unable to process Group
Policy.

SMBv1 clients will work with any other SMBv1 compatible file servers that you have.
However, AWS recommends that you update all of your SMB servers and clients to SMBv2 or
newer. To learn more about disabling SMBv1 and updating it to newer SMB versions on your
systems, see these postings on [Microsoft
TechNet](https://blogs.technet.microsoft.com/filecab/2016/09/16/stop-using-smb1/ "https://blogs.technet.microsoft.com/filecab/2016/09/16/stop-using-smb1/") and [Microsoft Documentation](https://learn.microsoft.com/en-US/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3?tabs=server "https://learn.microsoft.com/en-US/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3?tabs=server").

**Tracking SMBv1 Remote Connections**

You can review the **Microsoft-Windows-SMBServer/Audit**
Windows Event log remotely connecting to the AWS Managed Microsoft AD domain controller, any events in
this log indicate SMBv1 connections. Below is an example of the information you might see in
one of these logs:

_SMB1 access_

_Client Address: ###.###.###.###_

_Guidance:_

_This event indicates that a client attempted to access the server using SMB1.
To stop auditing SMB1 access, use the PowerShell cmdlet
Set-SmbServerConfiguration._

## Best practices when programming your applications for an AWS Managed Microsoft AD

Before you program your applications to work with AWS Managed Microsoft AD, consider the
following:

###### Topics

- [Use the Windows DC locator service](#program_dc_locator "#program_dc_locator")
- [Load test before rolling out to production](#program_load_test "#program_load_test")
- [Use efficient LDAP queries](#program_ldap_query "#program_ldap_query")

### Use the Windows DC locator service

When developing applications, use the Windows DC locator service or use the Dynamic
DNS (DDNS) service of your AWS Managed Microsoft AD to locate domain controllers (DCs). Do not hard code
applications with the address of a DC. The DC locator service helps ensure directory load is
distributed and enables you to take advantage of horizontal scaling by adding domain
controllers to your deployment. If you bind your application to a fixed DC and the DC
undergoes patching or recovery, your application will lose access to the DC instead of using
one of the remaining DCs. Furthermore, hard coding of the DC can result in hot spotting on a
single DC. In severe cases, hot spotting may cause your DC to become unresponsive. Such
cases may also cause AWS directory automation to flag the directory as impaired and may
trigger recovery processes that replace the unresponsive DC.

### Load test before rolling out to production

Be sure to do lab testing with objects and requests that are representative of your
production workload to confirm that the directory scales to the load of your application.
Should you require additional capacity, test with additional DCs while distributing requests
between the DCs. For more information, see [Deploying additional domain controllers for your
AWS Managed Microsoft AD](ms_ad_deploy_additional_dcs.md "ms_ad_deploy_additional_dcs.md").

### Use efficient LDAP queries

Broad LDAP queries to a domain controller across tens of thousands of objects can
consume significant CPU cycles in a single DC, resulting in hot spotting. This may affect
applications that share the same DC during the query.
