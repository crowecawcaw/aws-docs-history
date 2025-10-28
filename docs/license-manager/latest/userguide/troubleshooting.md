# Troubleshooting License Manager

The following information can help you troubleshoot issues when using AWS License Manager.
Before you start, confirm that your License Manager setup meets the requirements stated in
[Settings in License Manager](settings.md "settings.md").

## Cross-account discovery error

While setting up cross-account discovery, you may encounter the following error message on
the **Inventory search** page:

_Athena Exception: Athena Query failed because - Insufficient
permissions to execute the query. Please migrate your Catalog to enable access to this
database._

This can occur if your Athena service uses the Athena-managed data catalog rather than the
AWS Glue Data Catalog. For upgrade instructions, see [Upgrading
to the AWS Glue Data Catalog Step-by-Step](../../../athena/latest/ug/glue-upgrade.md "../../../athena/latest/ug/glue-upgrade.md").

## Management account cannot disassociate resources from a self-managed license

If a member account of an Organization deletes the
`AWSServiceRoleForAWSLicenseManagerMemberAccountRole` Service Linked Role (SLR) in
its account, and there are member-owned resources associated with a self-managed license, the
management account is prevented from disassociating licenses from those member-account resources.
This means that the member account resources will continue to consume licenses from the
management account pool. To allow the management account to disassociate resources, restore the
SLR.

This behavior accounts for cases when a customer prefers not to allow the management account
to perform some actions affecting member-account resources.

## Systems Manager Inventory is out of date

Systems Manager stores data in its Inventory data for 30 days. During this period, License Manager counts a
managed instance as active even if it is not pingable. After inventory data has been purged from
Systems Manager, License Manager marks the instance as inactive and updates local inventory data. To keep managed
instance counts accurate, we recommend manually deregistering instances in Systems Manager so that License Manager
can run cleanup operations.

## Apparent persistence of a de-registered AMI

License Manager purges stale associations between resources and self-managed licenses once every few
hours. If an AMI associated with a self-managed license is deregistered through Amazon EC2, The AMI
may briefly continue to appear in the License Manager resource inventory before being purged.

## New child account instances are slow to appear in resource

inventory

When cross-account support is enabled, License Manager updates customer accounts at 1 PM daily by
default. Instances added later in the day show up in the management account resource inventory on
the following day. You can change the frequency at which the update script runs by editing the
`LicenseManagerResourceSynDataProcessJobTrigger` in the AWS Glue console for the management
account.

## After enabling cross-account mode, child account instances are

slow to appear

When you enable cross-account mode in License Manager, instances in child accounts may take anywhere
from a few minutes to a few hours to appear in the resource inventory. The time depends on the
number of child accounts and the number of instances in each child account.

## Cross-account discovery cannot be disabled

After an account is configured for cross-account discovery, it is impossible to revert to
single-account discovery.

## Child account user cannot associate shared

self-managed license with an instance

When this occurs and cross-account discovery has been enabled, check for the
following:

- The child account has been removed from the organization.
- The child account has been removed from the resource share created in the management
  account.
- The self-managed license has been removed from the resource share.

## Linking AWS Organizations accounts fails

If the **Settings** page reports this error, it means that an account is
not a member of an organization for the following reasons:

- A child account was removed from the organization.
- A customer turned off access to License Manager from organization console of the management
  account.

## User subscription product configuration

failing

Your product configuration may be failing due to issues with outbound network access. To address this, ensure that the default security group permits outbound traffic to the IPv4 addresses of each domain controller's network interface as well as SSM.

- Verify that default security group settings facilitate outbound traffic to the IPv4 addresses of domain controller network interfaces.
  - License Manager creates two network interfaces which use the default security group of the VPC where your AWS Managed Microsoft AD is provisioned.
    These interfaces are used for required service functionality with your directory. Ensure that your default security group allows outbound traffic to each
    domain controller's network interface IPv4 address, or the security group used by the domain controllers.
    For more information, see [Prerequisites to create user-based subscriptions](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites") and [What gets created](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.md") in the AWS Directory Service Administration Guide.

- Configure outbound internet access from instances providing user-based subscriptions or VPC endpoints.
  - Outbound internet access from the instances providing user-based subscriptions, or VPC endpoints, must be configured for your instances to communicate with SSM.
    For more information, see [Setting up Systems Manager for EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the AWS Systems Manager User Guide.

Once the provisioning process is complete, you can associate a different security group to the interfaces created by License Manager. The security group you select must also allow the required traffic to each domain controller's network interface IPv4 address or security group. For more information, see [Work with security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the Amazon Virtual Private Cloud User Guide.

## User subscription instances failing to launch

Your instance launches can be failing due to multiple reasons. Here are some of the common issues for which an instance launch may fail:

- Ensure your instance is discoverable by SSM, see [Troubleshoot
  instance connectivity](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-connectivity "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-connectivity").
- Ensure your instance is able to join your domain, see [Troubleshoot failures to
  join the domain](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-domain-join "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-domain-join").
- Ensure that the Route53 outbound resolver endpoint rule is set. For more information, see the blog post [Integrating your Directory Service's DNS resolution with Amazon Route 53 Resolvers](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/ "https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/").
- If launching instances from custom AMIs created on top of User subscription AMIs, please make sure to perform Sysprep and ensure unique computer names when creating and launching instances from custom AMIs.

## Seamless domain join for EC2 instances with user

subscription products doesn't work

License Manager needs to perform domain join on these instances using SSM to allow authorized access to only users subscribed to the product. As a result, the seamless domain join feature is deactivated.

## Unable to delete active directory

License Manager is registered as an authorized application with Directory Service during configuration, thereby safeguarding active directories from deletion once configured. As part of the standard procedure, customers need to first remove all instances, instance associations, and user subscriptions. Following this, they can proceed with removing the active directory from the License Manager and subsequently delete the directory itself.

## VPC endpoint was created in my account

License Manager creates VPC endpoints required for your resources to connect to activation servers and remain in compliance when you configure your VPC.

## Remove all VPC endpoint resources created by License Manager

In order to delete the VPC endpoint resources, you must perform the following actions:

- Disassociate all users from their user-based subscriptions. For more information, see [Disassociate users from an instance that
  provides License Manager user-based subscriptions](usubs-disassociate-users.md "usubs-disassociate-users.md").
- Remove any directory that is configured from the License Manager settings. For more information, see [Deregister an Active Directory from License Manager settings](usubs-deregister-ad.md "usubs-deregister-ad.md").
- Terminate all instances providing user-based subscription products. For more information, see [Launch an instance from a license included AMI](usubs-launch-instance.md "usubs-launch-instance.md").

## Unable to delete

AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService Service Linked Role (SLR)

License Manager requires the "AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService" service-linked role for managing AWS resources that will provide user-based subscriptions. A service-linked role makes setting up License Manager easier because you don't have to manually add the necessary permissions. License Manager defines the permissions of its service-linked roles, and unless defined otherwise, only License Manager can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

For more information, see [Prerequisites to create
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites") and [License Manager – User-based subscription role](user-based-subscription-role.md "user-based-subscription-role.md") and [Service-linked roles](../../../singlesignon/latest/userguide/slrconcept.md "../../../singlesignon/latest/userguide/slrconcept.md").

## \*Subscription is not

present\* error for RDS SAL product

Your account must have a subscription to Windows Server Remote Desktop Services Subscriber Access License (RDS SAL). All users associated with instances providing user-based subscription products must have a single active subscription to this license in addition to any other products they would like to use. Your user will be subscribed to RDS SAL on their behalf when they subscribe to a user-based subscription product.

But if this has been unsubscribed or removed due to other compliance reasons, you might have to resubscribe. If you are already subscribed, you can try unsubscribing and resubscribing, which will not affect your License Manager user subscriptions.

## Troubleshooting trusts

Based on our experience working with many customers, the vast majority of trust
configuration issues are either DNS resolution or networking connectivity errors. These are some
troubleshooting steps to help you resolve common issues:

- Check whether you allowed outbound networking traffic on the AWS Managed Microsoft AD.
- If the DNS server or the network for your on-premises domain uses a public (non-RFC 1918) IP address space, follow these steps:
  - In the AWS Directory Service console, go to the IP routing section for your directory, choose **Actions**, and then choose **Add route**.
  - Enter the IP address block of your DNS server or on-premises network using CIDR format, for example 203.0.113.0/24.
  - This step isn't necessary if both your DNS server and your on-premises network are using RFC 1918 private IP address spaces.

- After you verify the security group and check whether any applicable routes are required,
  launch a Windows Server instance and join it to the AWS Managed Microsoft AD directory. Once the instance
  is launched:
  - Run this PowerShell command to test DNS connectivity:

  ```
  Resolve-DnsName -Name 'example.local' -DnsOnly
  ```

You should also look through the message explanations in the [Trust creation status reasons guide](../../../directoryservice/latest/admin-guide/ms_ad_troubleshooting_trust_creation.md "../../../directoryservice/latest/admin-guide/ms_ad_troubleshooting_trust_creation.md") in the AWS Directory Service documentation.

## Billing issues for user subscriptions

AWS will bill you through a monthly subscription, based on the number of users associated with the license included Microsoft Office or Visual Studio instances. These per-user charges are billed per calendar month, and the billing starts from the time you subscribe to the product. If you remove access to a user during the existing month, you will be billed for the user for the remainder of the month. You will stop incurring charges for the user the following month.

Furthermore:

- Billing is based on a per-user basis within User subscriptions. Only users who are subscribed to the product will incur charges, not all users in the active directory.
- Billing operates on a monthly cycle, starting from the first day of each calendar month. Charges are levied for the entire month, regardless of the specific date of subscription activation.
- You need an RDS SAL for each user who needs to access your Office/VS instances.
- To stop incurring charges for user-based subscriptions, you must disassociate the user
  from all instances they are associated with. Deleting a user from Active Directory does not
  disassociate the user from instances. For more information, see [Disassociate users from an instance that
  provides License Manager user-based subscriptions](usubs-disassociate-users.md "usubs-disassociate-users.md").
- A user is only counted once. You get charged per user for Microsoft Office and Visual
  Studio, irrespective of the number of EC2 instances the user connects to. Users are charged for
  their subscription once, regardless of their usage of multiple instances.

## User subscription products show Marketplace

subscription status of Inactive

After you configure your directory with the required products, you would need to subscribe to the required products. Products with a Marketplace Subscription Status of Inactive require you to subscribe before you can associate users to an instance and utilize them.

## Change a username on Managed Active Directory

Changing a username has no effect on their ability to RDP into associated instances. The
associated users should be able to use their updated login details to RDP into user subscription
instances.

## Dissociate users from a terminated

instance

Whenever a user subscriptions instance is terminated, all the users that are associated to
the instance are disassociated. You do not have to manually disassociate the user.

###### Note

Users are not dissociated if the instance is stopped.

## User limits per instance

There is a limit of 25 instances per user. In case you need adjustment, please reach out to AWS Support. Users are charged for their subscription once, regardless of their usage of multiple instances.

## Installing additional software on user subscription

instances

You can install additional software on your instances that aren't available as user-based subscriptions. Additional software installations aren't tracked by License Manager. These installations must be performed using the Admin account which is created by default in your AWS Managed Microsoft AD directory.
For more information, see [Admin account](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_admin_account.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_admin_account.md") in the AWS Directory Service Administration Guide.

To install additional software with the Admin account, you must:

- Subscribe the Admin account to the product provided by the instance.
- Associate the Admin account to the instance.
- Connect to the instance using the Admin account to perform the installation.

For more information, see [Get started with user-based
subscriptions in License Manager](user-based-subscriptions-getting-started.md "user-based-subscriptions-getting-started.md").

## Japanese Language Packs on user subscription

instances

Japanese language pack installation is supported with User subscription instances.

## Local Administrator user on user subscription

instances

We only allow users under the users managed active directory domain to be associated with
user subscription instances to prevent unauthorized access to these Microsoft products. When you
create local users with administrator privileges on instances that provide user-based
subscriptions, the instance's health status changes to unhealthy.

## Unhealthy instances

Instances providing user-based subscriptions must remain in a healthy status to be in
compliance. Instances that are marked as unhealthy no longer meet the required prerequisites.
License Manager attempts to return the instance to a healthy status, but instances that are not able to
return to a healthy status are terminated.

## Number of users that can RDP to a user subscriptions

instance

Instances that provide user-based subscriptions support up to two active user sessions at a
time as stated in [Use License Manager user-based subscriptions for supported software products](user-based-subscriptions.md "user-based-subscriptions.md"). By
default, Windows allows up to 2 Remote Desktop connections including an Admin connection at any
given time, in all editions of Windows server. For using more than 2 concurrent users, customers
need to setup an RDS Licensing server.

## Supported Windows operating systems

For information about supported Windows operating system platforms, see [Supported software products for
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-software "user-based-subscriptions.md#usubs-software").

## Supported versions of Office and Visual Studio

For information about supported software for user-based subscriptions, see [Supported
software for user-based subscriptions](user-based-subscriptions.md#usubs-software-supported "user-based-subscriptions.md#usubs-software-supported").

## Using user subscription with older Windows Server

versions

When you launch an instance from an AMI that supports Office LTSC Professional Plus or Microsoft Visual Studio, the launch defaults to the latest Windows OS platform version of the AMI (for example Windows Server 2022). To launch with an earlier OS platform version, follow these steps:

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. Choose **Manage subscriptions** from the navigation pane.
3. To streamline subscription results, you can search for all or part of the subscription name. For example, Office LTSC Professional Plus 2021 or Visual Studio Enterprise.
4. Select **Launch new instance** from the subscription panel. This opens a launch configuration page.
5. To launch an instance from an AMI that's based on an earlier version of the Windows OS platform, select the full AWS Marketplace website link, located under the Software version. This takes you to a configuration page where you can select from a list of versions.
6. The list shows the latest AMI versions for the supported Windows OS platforms. Select the Windows OS version that you want to launch from.

## Using License Manager user subscriptions across accounts or

regions

These scenarios are not supported:

- Using License Manager user subscriptions across accounts
- Using License Manager user subscriptions across regions
- Using License Manager user subscriptions with shared Active Directory

## CAL token handling during migration to RDS SAL

If you use your own Microsoft RDS license servers, any Client Access License (CAL) tokens
already issued remain valid until they expire. During this period users with valid CAL tokens are
not automatically subscribed to the RDS SAL product. New user sessions are not automatically
subscribed to RDS SAL even though License Manager is configured. License Manager does not
override existing CAL tokens issued by your own license servers. The service-managed license
server begins issuing tokens and handling new requests only after the existing CAL tokens expire.
Once the currently issued CAL tokens reach their expiration date, new token requests are handled
by the service-managed license server, and users are auto-subscribed to the RDS SAL product as
needed.

## Users in my self-managed AD with User subscription

products

To associate users in your self-managed directory, you must establish a two-way forest trust between your self-managed directory and your AWS Managed Microsoft AD directory.
For more information, see [Tutorial:
Create a trust relationship between your AWS Managed Microsoft AD and your self-managed Active Directory domain](../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust.md "../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust.md") in the AWS Directory Service Administration Guide.

## Tips for contacting AWS Support

- When contacting AWS support, please create an instance with the same settings as a terminated instance and enable instance termination protection for a quick response.
- For any RDP related issues we would require RDP related logs to help debug these issues. Please utilize the 'AWSSupport-RunEC2RescueForWindowsTool' for environments with internet access. For more information, see [EC2Rescue for Windows Server](../../../AWSEC2/latest/WindowsGuide/ec2rw-ssm.md "../../../AWSEC2/latest/WindowsGuide/ec2rw-ssm.md").
- By using an Office instance as a working instance and mounting a volume restored from a snapshot of the original instance's volume, it is possible to collect data even in an environment without internet access.
- Troubleshooting Instance Launches from Backup AMIs: If you launch an instance from a backup AMI, you must terminate the original instance.
