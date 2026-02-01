# Troubleshoot user-based

subscriptions in License Manager

The following are troubleshooting tips to help solve issues that can occur with
user-based subscriptions in AWS License Manager.

###### Contents

- [Troubleshoot
  instance compliance](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-compliance "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-compliance")
- [Troubleshoot user subscription product configuration
  failures](user-based-subscriptions-troubleshoot.md#product_configuration_failing "user-based-subscriptions-troubleshoot.md#product_configuration_failing")
- [Troubleshoot user subscription instances launch failures](user-based-subscriptions-troubleshoot.md#instance_launch_failures "user-based-subscriptions-troubleshoot.md#instance_launch_failures")
- [Troubleshoot license
  compliance](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-license-compliance "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-license-compliance")
- [Troubleshoot
  instance connectivity](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-connectivity "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-connectivity")
- [Troubleshoot failures to
  join the domain](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-domain-join "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-domain-join")
- [Troubleshoot Systems Manager connectivity](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-connectivity "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-connectivity")
- [Troubleshoot
  Systems Manager Run Command](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-commands "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-commands")
- [Troubleshoot Microsoft RDS Licensing failures](user-based-subscriptions-troubleshoot.md#usubs-troubleshoot-rds-licensing "user-based-subscriptions-troubleshoot.md#usubs-troubleshoot-rds-licensing")
- [Troubleshoot Microsoft Office activation failures](user-based-subscriptions-troubleshoot.md#usubs-troubleshoot-office-activation "user-based-subscriptions-troubleshoot.md#usubs-troubleshoot-office-activation")
- [Troubleshoot the inability to delete Active Directory](user-based-subscriptions-troubleshoot.md#delete_active_directory "user-based-subscriptions-troubleshoot.md#delete_active_directory")
- [Troubleshoot inability to delete
  AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService Service Linked Role (SLR)](user-based-subscriptions-troubleshoot.md#delete_service_linked_role "user-based-subscriptions-troubleshoot.md#delete_service_linked_role")
- [Troubleshoot subscription is not
  present error for RDS SAL product](user-based-subscriptions-troubleshoot.md#rds_sal_subscription_error "user-based-subscriptions-troubleshoot.md#rds_sal_subscription_error")
- [Troubleshoot license counts not showing up correctly](user-based-subscriptions-troubleshoot.md#license_counts_not_showing "user-based-subscriptions-troubleshoot.md#license_counts_not_showing")
- [Troubleshoot RDS License Diagnoser issues](user-based-subscriptions-troubleshoot.md#rds_licensing_mode_error "user-based-subscriptions-troubleshoot.md#rds_licensing_mode_error")
- [Troubleshoot trusts](user-based-subscriptions-troubleshoot.md#troubleshoot_trusts "user-based-subscriptions-troubleshoot.md#troubleshoot_trusts")
- [Troubleshoot billing issues for user subscriptions](user-based-subscriptions-troubleshoot.md#billing_user_subscriptions "user-based-subscriptions-troubleshoot.md#billing_user_subscriptions")
- [Troubleshoot inactive marketplace subscription status](user-based-subscriptions-troubleshoot.md#inactive_marketplace_status "user-based-subscriptions-troubleshoot.md#inactive_marketplace_status")
- [Troubleshoot user limits per instance](user-based-subscriptions-troubleshoot.md#user_limits_per_instance "user-based-subscriptions-troubleshoot.md#user_limits_per_instance")
- [Troubleshoot CAL token not vended after migration to RDS SAL](user-based-subscriptions-troubleshoot.md#cal_token "user-based-subscriptions-troubleshoot.md#cal_token")
- [Seamless domain join not working for EC2 instances with user
  subscription products](user-based-subscriptions-troubleshoot.md#seamless_domain_join "user-based-subscriptions-troubleshoot.md#seamless_domain_join")
- [VPC endpoint was created in my account](user-based-subscriptions-troubleshoot.md#vpc_endpoint_created "user-based-subscriptions-troubleshoot.md#vpc_endpoint_created")
- [Remove all VPC endpoint resources created by License Manager](user-based-subscriptions-troubleshoot.md#remove_vpc_endpoint "user-based-subscriptions-troubleshoot.md#remove_vpc_endpoint")
- [Change a username on Managed Active Directory](user-based-subscriptions-troubleshoot.md#change_username "user-based-subscriptions-troubleshoot.md#change_username")
- [Dissociate users from a terminated instance](user-based-subscriptions-troubleshoot.md#dissociate_terminated_instance "user-based-subscriptions-troubleshoot.md#dissociate_terminated_instance")
- [Install additional software on user subscription instances](user-based-subscriptions-troubleshoot.md#additional_software "user-based-subscriptions-troubleshoot.md#additional_software")
- [Japanese Language Packs on user subscription
  instances](user-based-subscriptions-troubleshoot.md#japanese_language_packs "user-based-subscriptions-troubleshoot.md#japanese_language_packs")
- [Local Administrator user on user subscription
  instances](user-based-subscriptions-troubleshoot.md#local_admin_user "user-based-subscriptions-troubleshoot.md#local_admin_user")
- [Number of users that can RDP to a user subscriptions
  instance](user-based-subscriptions-troubleshoot.md#rdp_user_limit "user-based-subscriptions-troubleshoot.md#rdp_user_limit")
- [Users in my self-managed AD for Office and Visual Studio products](user-based-subscriptions-troubleshoot.md#self_managed_ad "user-based-subscriptions-troubleshoot.md#self_managed_ad")
- [Supported Windows operating systems](user-based-subscriptions-troubleshoot.md#supported_os "user-based-subscriptions-troubleshoot.md#supported_os")
- [Supported versions of Office and Visual Studio](user-based-subscriptions-troubleshoot.md#supported_software "user-based-subscriptions-troubleshoot.md#supported_software")
- [Using user subscription with older Windows Server
  versions](user-based-subscriptions-troubleshoot.md#older_windows_versions "user-based-subscriptions-troubleshoot.md#older_windows_versions")
- [Using License Manager user subscriptions across accounts or
  regions](user-based-subscriptions-troubleshoot.md#unsupported_scenarios "user-based-subscriptions-troubleshoot.md#unsupported_scenarios")
- [Tips for contacting AWS Support](user-based-subscriptions-troubleshoot.md#aws_support_tips "user-based-subscriptions-troubleshoot.md#aws_support_tips")

## Troubleshoot

instance compliance

Instances providing user-based subscriptions must remain in a healthy status to be in
compliance. Instances that are marked as unhealthy no longer meet the required
prerequisites. License Manager will attempt to return the instance to a healthy status, but
instances that are not able to return to a healthy status are terminated.

Instances which are launched to provide user-based subscriptions and are unable to
complete the initial configuration will be terminated. You must correct the
configuration issue and launch new instances to provide user-based subscriptions in this
scenario. For more information, see the [Prerequisites to create
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites").

## Troubleshoot user subscription product configuration

failures

Your product configuration may be failing due to issues with outbound network access. To address this, ensure that the default security group permits outbound traffic to the IP addresses of each domain controller's network interface as well as SSM.

- Verify that default security group settings facilitate outbound traffic to the IP addresses of domain controller network interfaces.
  - License Manager creates two network interfaces which use the default security group of the VPC where your AWS Managed Microsoft AD is provisioned.
    These interfaces are used for required service functionality with your directory. Ensure that your default security group allows outbound traffic to each
    domain controller's network interface IP address, or the security group used by the domain controllers.
    For more information, see [Prerequisites to create user-based subscriptions](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites") and [What gets created](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.md") in the Directory Service Administration Guide.

- Configure outbound internet access from instances providing user-based subscriptions or VPC endpoints.
  - Outbound internet access from the instances providing user-based subscriptions, or VPC endpoints, must be configured for your instances to communicate with SSM.
    For more information, see [Setting up Systems Manager for EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the AWS Systems Manager User Guide.

Once the provisioning process is complete, you can associate a different security group to the interfaces created by License Manager. The security group you select must also allow the required traffic to each domain controller's network interface IPv4 address or security group. For more information, see [Work with security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the Amazon Virtual Private Cloud User Guide.

## Troubleshoot user subscription instances launch failures

Your instance launches can be failing due to multiple reasons. Here are some of the common issues for which an instance launch may fail:

- Ensure your instance is discoverable by SSM, see [Troubleshoot
  instance connectivity](#user-based-subscriptions-troubleshoot-instance-connectivity "#user-based-subscriptions-troubleshoot-instance-connectivity").
- Ensure your instance is able to join your domain, see [Troubleshoot failures to
  join the domain](#user-based-subscriptions-troubleshoot-domain-join "#user-based-subscriptions-troubleshoot-domain-join").
- Ensure that the Route53 outbound resolver endpoint rule is set. For more information, see the blog post [Integrating your Directory Service's DNS resolution with Amazon Route 53 Resolvers](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/ "https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/").
- If launching instances from custom AMIs created on top of User subscription AMIs, please make sure to perform Sysprep and ensure unique computer names when creating and launching instances from custom AMIs.

## Troubleshoot license

compliance

If you configured your Active Directory to provide user-based subscriptions with Microsoft Office, you
must ensure your resources can connect to the VPC endpoints License Manager creates. The endpoints
require inbound traffic on TCP port 1688 from the instances providing user-based
subscriptions.

You can use [Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") to
help confirm that the networking configuration from your instances providing user-based
subscriptions and the VPC endpoints are configured properly. You can specify an instance
ID launched in a subnet providing user-based subscriptions as the source, and a VPC
endpoint provisioned for Microsoft Office products as the destination. Specify TCP as the protocol
and 1688 for the destination port for the path to analyze. For more information, see
[How can
I troubleshoot connectivity issues over my gateway and interface VPC
endpoints?](https://aws.amazon.com/premiumsupport/knowledge-center/vpc-fix-gateway-or-interface-endpoint/ "https://aws.amazon.com/premiumsupport/knowledge-center/vpc-fix-gateway-or-interface-endpoint/").

## Troubleshoot

instance connectivity

Users must be able to use RDP to connect to the instances providing user-based
subscriptions in order to use the products within. For more information on
troubleshooting instance connectivity, see [Troubleshoot connecting to your Windows instance](../../../AWSEC2/latest/UserGuide/troubleshoot-connect-windows-instance.md "../../../AWSEC2/latest/UserGuide/troubleshoot-connect-windows-instance.md") in the
_Amazon EC2 User Guide_.

## Troubleshoot failures to

join the domain

Users must be able to connect to the instances providing the user-based subscription
products with their user identities from the Active Directory configured in the License Manager settings.
Instances that fail to join the domain will be terminated.

To troubleshoot, you may need to launch an instance and [manually join
the domain](../../../directoryservice/latest/admin-guide/join_windows_instance.md "../../../directoryservice/latest/admin-guide/join_windows_instance.md") so that the resource is not terminated before you can investigate.
The instance must receive and execute the Systems Manager Run Command successfully, and the
instance must also be able to complete the domain join within the operating system. For
more information, see [Understanding command
statuses](../../../systems-manager/latest/userguide/monitor-commands.md "../../../systems-manager/latest/userguide/monitor-commands.md") in the _AWS Systems Manager User Guide_ and [How to troubleshoot errors that occur when you join Windows-based computers to a
domain](https://docs.microsoft.com/en-US/troubleshoot/windows-server/identity/troubleshoot-errors-join-computer-to-domain "https://docs.microsoft.com/en-US/troubleshoot/windows-server/identity/troubleshoot-errors-join-computer-to-domain") on the Microsoft website.

If you launch instances from a custom AMI that uses a user-based subscription product AMI
as its base image, you must perform Sysprep steps on the custom AMI to ensure a unique
computer name at launch. Before you run Sysprep with /generalize, ensure that the machine
is removed from the domain.

## Troubleshoot Systems Manager connectivity

Instances that provide user-based subscriptions must be managed by AWS Systems Manager or they
will be terminated. For more information, see [Troubleshooting
SSM Agent](../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md "../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md") and [Troubleshooting managed node availability](../../../systems-manager/latest/userguide/troubleshooting-managed-instances.md "../../../systems-manager/latest/userguide/troubleshooting-managed-instances.md") in the _AWS Systems Manager User
Guide_.

## Troubleshoot

Systems Manager Run Command

Run Command, a capability of Systems Manager, is used with instances providing user-based
subscriptions to join the domain, harden the operating system, and perform access audits
for the included product. For more information, see [Understanding command
statuses](../../../systems-manager/latest/userguide/monitor-commands.md "../../../systems-manager/latest/userguide/monitor-commands.md") in the _AWS Systems Manager User Guide_.

## Troubleshoot Microsoft RDS Licensing failures

If you experience issues with CAL (Client Access License) issuance, check whether there
are additional Microsoft RDS licensing servers present in your server farm or Terminal Servers
group. We do not recommend having additional licensing servers in these locations, as that can
interfere with CAL issuance and lead to licensing complications.

To resolve this issue, ensure that only the intended Microsoft RDS servers remain in your
server farm and Terminal Servers group.

When troubleshooting licensing issues, be aware that connections using the /admin flag bypass
standard licensing checks, as this flag is intended for administrative purposes, and doesn't
consume a CAL. This can mask underlying licensing problems. To diagnose licensing issues, verify
that standard user connections (without the /admin flag) are functioning correctly for license
management.

## Troubleshoot Microsoft Office activation failures

If Microsoft Office activation fails, verify that your instance has access to the VPC that's
defined for License Manager. Either of the following options satisfies this requirement:

- Your instance is running in the VPC that's onboarded with License Manager (through VPC
  endpoint)
- Your instance is running in a VPC that's peered with the License Manager onboarded VPC.

To resolve this issue, ensure that your instance is moved to the correct VPC, or establish VPC
peering with the License Manager onboarded VPC.

## Troubleshoot the inability to delete Active Directory

License Manager is registered as an authorized application with Directory Service during configuration, thereby safeguarding active directories from deletion once configured. As part of the standard procedure, customers need to first remove all instances, instance associations, and user subscriptions. Following this, they can proceed with removing the active directory from the License Manager and subsequently delete the directory itself.

## Troubleshoot inability to delete

AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService Service Linked Role (SLR)

License Manager requires the "AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService" service-linked role for managing AWS resources that will provide user-based subscriptions. A service-linked role makes setting up License Manager easier because you don't have to manually add the necessary permissions. License Manager defines the permissions of its service-linked roles, and unless defined otherwise, only License Manager can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

For more information, see [Prerequisites to create
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites") and [License Manager – User-based subscription role](user-based-subscription-role.md "user-based-subscription-role.md") and [Service-linked roles](../../../singlesignon/latest/userguide/slrconcept.md "../../../singlesignon/latest/userguide/slrconcept.md").

## Troubleshoot \*subscription is not

present\* error for RDS SAL product

Your account must have a subscription to Windows Server Remote Desktop Services Subscriber Access License (RDS SAL). All users associated with instances providing user-based subscription products must have a single active subscription to this license in addition to any other products they would like to use. Your user will be subscribed to RDS SAL on their behalf when they subscribe to a user-based subscription product.

But if this has been unsubscribed or removed due to other compliance reasons, you might have to resubscribe. If you are already subscribed, you can try unsubscribing and resubscribing, which will not affect your License Manager user subscriptions.

## Troubleshoot license counts not showing up correctly

After initial setup or configuration changes, it can take up to 24 hours for the license server to display accurate license counts for all license types in the License Diagnoser.

What to do:

- Wait up to 24 hours after setup before expecting accurate license count reporting

This delay is normal and allows the license server sufficient time to properly synchronize and update all license information across different license types. If you run into an error please refer [Troubleshoot RDS License Diagnoser issues](#rds_licensing_mode_error "#rds_licensing_mode_error").

## Troubleshoot RDS License Diagnoser issues

These errors are typically caused by credential or permission issues. To resolve:

1. **Verify user credentials:** Ensure you are using the same user account that was provided to License Manager during onboarding
2. **Check session credentials:** If you see **"Credentials not available"** against the server in the summary section:
   1. Click on the license server in the summary section that shows **"Credentials not available"**
   2. In the right-hand side menu that opens, add the credentials of the user that was onboarded to License Manager
   3. Click **"Refresh"**

If the issue persists, follow the additional troubleshooting steps outlined in Microsoft's documentation: [Cannot connect to RDS - No license server](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/cannot-connect-rds-no-license-server "https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/cannot-connect-rds-no-license-server")

This should resolve most credential and permission-related issues with the License Diagnoser.

## Troubleshoot trusts

Based on our experience working with many customers, the vast majority of trust
configuration issues are either DNS resolution or networking connectivity errors. These are some
troubleshooting steps to help you resolve common issues:

- Check whether you allowed outbound networking traffic on the AWS Managed Microsoft AD.
- If the DNS server or the network for your on-premises domain uses a public (non-RFC 1918) IP address space, follow these steps:
  - In the Directory Service console, go to the IP routing section for your directory, choose **Actions**, and then choose **Add route**.
  - Enter the IP address block of your DNS server or on-premises network using CIDR format, for example 203.0.113.0/24.
  - This step isn't necessary if both your DNS server and your on-premises network are using RFC 1918 private IP address spaces.

- After you verify the security group and check whether any applicable routes are required,
  launch a Windows Server instance and join it to the AWS Managed Microsoft AD directory. Once the instance
  is launched:
  - Run this PowerShell command to test DNS connectivity:

  ```
  Resolve-DnsName -Name 'example.local' -DnsOnly
  ```

You should also look through the message explanations in the [Trust creation status reasons guide](../../../directoryservice/latest/admin-guide/ms_ad_troubleshooting_trust_creation.md "../../../directoryservice/latest/admin-guide/ms_ad_troubleshooting_trust_creation.md") in the Directory Service documentation.

## Troubleshoot billing issues for user subscriptions

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

## Troubleshoot inactive marketplace subscription status

After you configure your directory with the required products, you would need to subscribe to the required products. Products with a Marketplace Subscription Status of Inactive require you to subscribe before you can associate users to an instance and utilize them.

## Troubleshoot user limits per instance

There is a limit of 25 instances per user. In case you need adjustment, please reach out to AWS Support. Users are charged for their subscription once, regardless of their usage of multiple instances.

## Troubleshoot CAL token not vended after migration to RDS SAL

If you use your own Microsoft RDS license servers, any Client Access License (CAL) tokens
already issued remain valid until they expire. During this period users with valid CAL tokens are
not automatically subscribed to the RDS SAL product. New user sessions are not automatically
subscribed to RDS SAL even though License Manager is configured. License Manager does not
override existing CAL tokens issued by your own license servers. The service-managed license
server begins issuing tokens and handling new requests only after the existing CAL tokens expire.
Once the currently issued CAL tokens reach their expiration date, new token requests are handled
by the service-managed license server, and users are auto-subscribed to the RDS SAL product as
needed.

## Seamless domain join not working for EC2 instances with user

subscription products

License Manager needs to perform domain join on these instances using SSM to allow authorized access to only users subscribed to the product. As a result, the seamless domain join feature is deactivated.

## VPC endpoint was created in my account

License Manager creates VPC endpoints required for your resources to connect to activation servers and remain in compliance when you configure your VPC.

## Remove all VPC endpoint resources created by License Manager

In order to delete the VPC endpoint resources, you must perform the following actions:

- Disassociate all users from their user-based subscriptions. For more information, see [Disassociate users from an instance that
  provides License Manager user-based subscriptions](usubs-disassociate-users.md "usubs-disassociate-users.md").
- Remove any directory that is configured from the License Manager settings. For more information, see [Deregister an Active Directory from License Manager settings](usubs-deregister-ad.md "usubs-deregister-ad.md").
- Terminate all instances providing user-based subscription products. For more information, see [Launch an instance from a license included AMI](usubs-launch-instance.md "usubs-launch-instance.md").

## Change a username on Managed Active Directory

Changing a username has no effect on their ability to RDP into associated instances. The
associated users should be able to use their updated login details to RDP into user subscription
instances.

## Dissociate users from a terminated instance

Whenever a user subscriptions instance is terminated, all the users that are associated to
the instance are disassociated. You do not have to manually disassociate the user.

###### Note

Users are not dissociated if the instance is stopped.

## Install additional software on user subscription instances

You can install additional software on your instances that aren't available as user-based subscriptions. Additional software installations aren't tracked by License Manager. These installations must be performed using the Admin account which is created by default in your AWS Managed Microsoft AD directory.
For more information, see [Admin account](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_admin_account.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_admin_account.md") in the Directory Service Administration Guide.

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

## Number of users that can RDP to a user subscriptions

instance

Instances that provide user-based subscriptions support up to two active user sessions at a
time as stated in [Use License Manager user-based subscriptions for supported software products](user-based-subscriptions.md "user-based-subscriptions.md"). By
default, Windows allows up to 2 Remote Desktop connections including an Admin connection at any
given time, in all editions of Windows server. For using more than 2 concurrent users, customers
need to setup an RDS Licensing server.

## Users in my self-managed AD for Office and Visual Studio products

To associate users in your self-managed directory, you must establish a two-way forest trust between your self-managed directory and your AWS Managed Microsoft AD directory.
For more information, see [Tutorial:
Create a trust relationship between your AWS Managed Microsoft AD and your self-managed Active Directory domain](../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust.md "../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust.md") in the Directory Service Administration Guide.

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
3. To streamline subscription results, you can search for all or part of the subscription name. For example, Office LTSC Professional Plus or Visual Studio Enterprise.
4. Select **Launch new instance** from the subscription panel. This opens a launch configuration page.
5. To launch an instance from an AMI that's based on an earlier version of the Windows OS platform, select the full AWS Marketplace website link, located under the Software version. This takes you to a configuration page where you can select from a list of versions.
6. The list shows the latest AMI versions for the supported Windows OS platforms. Select the Windows OS version that you want to launch from.

## Using License Manager user subscriptions across accounts or

regions

These scenarios are supported:

- Using License Manager user subscriptions across accounts

- Using License Manager user subscriptions with shared Active Directory

These scenarios are not supported:

- Using License Manager user subscriptions across regions

## Tips for contacting AWS Support

- When contacting AWS support, please create an instance with the same settings as a terminated instance and enable instance termination protection for a quick response.
- For any RDP related issues we would require RDP related logs to help debug these issues. Please utilize the 'AWSSupport-RunEC2RescueForWindowsTool' for environments with internet access. For more information, see [EC2Rescue for Windows Server](../../../AWSEC2/latest/WindowsGuide/ec2rw-ssm.md "../../../AWSEC2/latest/WindowsGuide/ec2rw-ssm.md").
- By using an Office instance as a working instance and mounting a volume restored from a snapshot of the original instance's volume, it is possible to collect data even in an environment without internet access.
- Troubleshooting Instance Launches from Backup AMIs: If you launch an instance from a backup AMI, you must terminate the original instance.
