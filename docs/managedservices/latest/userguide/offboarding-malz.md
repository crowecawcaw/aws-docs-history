# Offboard from AMS multi-account landing zone accounts

There are two types of AWS accounts that you can offboard from AMS Advanced multi-account landing zone:

- Application accounts
- Core accounts
  To offboard all accounts from your AMS Multi-account landing zone, you must offboard all Application accounts before you offboard Core accounts.

To take over and continue operating workloads in offboarded Application or Core accounts, make sure that you review this documentation with your AMS account team. This documentation outlines the changes that AMS performs during the offboard process.

## Tasks to complete for continued operation of offboarded accounts

The following tasks are required for continued operation of accounts that you offboarded from AMS multi-account landing zone:

- **Turn on Developer mode:** To gain more permission to your accounts, turn on Developer mode before you offboard Application accounts from AMS. When you turn on Developer mode, you can more easily make the necessary changes to prepare for offboarding. Don’t try to remove or
  modify AMS infrastructure resources. If you delete AMS
  infrastructure resources, then AMS might not be able to
  successfully offboard your account. For information about how to
  enable Developer mode, see
  [Getting started with AMS Advanced Developer mode](developer-mode-implement.md "developer-mode-implement.md").

If you can’t complete the necessary changes to prepare for
offboarding after you turn on Developer mode, then contact your
AMS account team to discuss your requirements.

- **Choose an alternate method for EC2 stack access:** After you offboard Application accounts from AMS, you can’t use
  RFCs to access your stack resources. Review [Offboarding changes](#offboarding-malz-offboarding-changes "#offboarding-malz-offboarding-changes"), and then choose an alternate access method so that you
  retain access to your stacks. For more information, see [Access Alternatives](#offboarding-malz-access-alternatives "#offboarding-malz-access-alternatives").

## Offboard AMS Application accounts

To offboard Application accounts from your multi-account landing zone environment, complete the following steps for each account:

1. Verify that there are no open RFCs in the account. For more
   information, see [Create, clone, update, find, and cancel RFCs](ex-rfc-use-examples.md "ex-rfc-use-examples.md").
2. Verify that you can access the primary or root user email
   address for the account.
3. From the Application account, submit an RFC with the
   [Application Account | Confirm offboarding](../ctref/management-managed-application-account-confirm-offboarding.md "../ctref/management-managed-application-account-confirm-offboarding.md") (ct-2wlfo2jxj2rkj) change type. In the RFC, specify the Application account to offboard.
4. From the Management account, submit an RFC with the
   [Management account | Offboard Application Account](../ctref/management-managed-management-account-offboard-application-account.md "../ctref/management-managed-management-account-offboard-application-account.md") (ct-0vdiy51oyrhhm) change type. In the RFC, specify the
   Application account to offboard. Also, indicate if you want to
   delete or retain the transit gateway attachment to the landing
   zone.
5. To make sure that AMS billing is stopped, notify your CSDM
   that you offboarded the account.

The following occurs after the Application account is offboarded:

- All components are disassociated from AMS services, but your
  created resources remain in the account. You can choose to
  keep or close the AMS offboarded account.
- Core accounts and other remaining Application accounts
  function normally after an Application account is offboarded.
- AMS billing is stopped, but AWS billing isn’t stopped until
  you close the account. For more information, see [What
  you need to know before closing your account](../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations "../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations").
- If an account is closed, then the account is visible in your
  organization in the `suspended` state for 90 days.
  After 90 days, the closed account is permanently removed and
  no longer visible in your organization.
- After the account is closed, you can still sign in and file a support case or contact Support for 90 days.
- After 90 days, any content that remains in the account is
  permanently deleted and the remaining AWS services are
  terminated.

**Q: Can I use my federated IAM roles to
continue to access an Application account that I offboarded from
my AMS multi-account landing zone?**
Yes. AMS created [default
AWS Identity and Access Management (IAM) roles](defaults-user-role.md "defaults-user-role.md") remain
available in the account after AMS offboarding. However, these
roles and policies are designed for use with AMS access
management. To provide the necessary access for your users, you
might need to deploy your own IAM resources.

**Q: How do I gain full access to an
Application account that I offboarded from my AMS multi-account landing zone?**
Offboarded Application accounts are moved to the
**Deprecated** Organizational
Unit (OU) in the AWS Organizations account structure. This move
lifts SCP access restrictions that previously blocked root user
access. For information about how to reset root user
credentials, see [Resetting
a lost or forgotten root user password](../../../IAM/latest/UserGuide/reset-root-password.md "../../../IAM/latest/UserGuide/reset-root-password.md").

**Q: What changes are made during
Application account offboarding?**
For information about actions that AMS takes when the service
offboards accounts, see [Offboarding changes](#offboarding-malz-offboarding-changes "#offboarding-malz-offboarding-changes").

**Q: Can I offboard an Application account
without detaching it from the transit gateway?**
Yes. Use the [Management account | Offboard Application Account](../ctref/management-managed-management-account-offboard-application-account.md "../ctref/management-managed-management-account-offboard-application-account.md") (ct-0vdiy51oyrhhm) change type to submit the RFC, and specify the
`DeleteTransitGatewayAttachment` parameter as `False`.

**Q: How long does it take to offboard an
Application account?**
When you use the [Management account | Offboard Application Account](../ctref/management-managed-management-account-offboard-application-account.md "../ctref/management-managed-management-account-offboard-application-account.md") (ct-0vdiy51oyrhhm) change type, RFCs complete within 1 hour.

**Q: Is it mandatory that I close the
offboarded account?**
No. Account closure after AMS offboarding isn’t mandatory.
During the offboarding process, AMS removes its access and
management of your AWS account, but your account and your
resources within the account remain. It's important to note that
after AMS offboarding, you’re solely responsible for managing
and maintaining your AWS account and resources. AMS isn’t
responsible for any issues, incidents, or service disruptions
that might occur in your account after the offboarding process
is complete. For more information, see [How
do I close my AWS account?](http://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/ "http://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/").

**Q: If I submit an account closure
request, are all existing resources deleted
immediately?**
No. Account closure doesn’t terminate your resources. Resources
in the account automatically terminate 90 days after the closure
request. AMS billing stops, but AWS resource billing doesn’t
stop until you close the account. For more information, see [What
you need to know before closing your account](../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations "../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations").

**Q: Can I schedule the offboarding of an Application account?**
Yes. You can schedule the RFCs to run at a specific time. However, the [Application Account | Confirm offboarding](../ctref/management-managed-application-account-confirm-offboarding.md "../ctref/management-managed-application-account-confirm-offboarding.md") RFC must complete before you can schedule the [Management account | Offboard Application Account](../ctref/management-managed-management-account-offboard-application-account.md "../ctref/management-managed-management-account-offboard-application-account.md") RFC. For more information, see [RFC scheduling](ex-rfc-scheduling.md "ex-rfc-scheduling.md").

- **R**: Responsible party. The
  party responsible for completing the listed task.
- **A**: Accountable party.
  The party that approves the completed task.
- **C**: Consulted party. A
  party whose opinions are sought, typically as subject matter
  experts, and with whom there is bilateral communication.
- **I**: Informed party. A
  party that’s informed on progress, often only on completion
  of the task or deliverable.

| Activity                                                                                                                                               | Customer | AWS Managed Services (AMS) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | -------------------------- |
| **Prerequisites**                                                                                                                                      |          |                            |
| Verify access to the root email address for each AWS<br>account ID that will be offboarded                                                             | R        | C                          |
| Review AMS documentation on recommended customer actions<br>and prepare accounts for AMS offboarding                                                   | R        | C                          |
| If needed, submit an RFC to enable Developer mode to<br>prepare accounts for AMS offboarding                                                           | R        | I                          |
| If needed, choose an alternate method for EC2 stack access.                                                                                            | R        | I                          |
| **Offboarding**                                                                                                                                        |          |                            |
| Submit RFCs to confirm and request offboarding of<br>Application accounts                                                                              | R        | I                          |
| Offboard AMS components from Application accounts                                                                                                      | I        | R                          |
| Notify AMS CSDM of offboarded accounts to stop AMS<br>billing                                                                                          | R        | I                          |
| **Post-offboarding**                                                                                                                                   |          |                            |
| Reset root user account password and verify root access<br>in offboarded accounts                                                                      | R        | C                          |
| Close the account or follow AMS guidance on recommended<br>customer actions in the AMS offboarding documentation to<br>continue operating the accounts | R        | C                          |

## Offboard Core accounts

To offboard multi-account landing zone Core accounts, complete the
following steps:

1. Verify that all Application accounts in the landing zone were
   offboarded from AMS.
2. Verify that you have no open RFCs in the accounts. For more
   information, see [Create, clone, update, find, and cancel RFCs](ex-rfc-use-examples.md "ex-rfc-use-examples.md").
3. Verify that you can access the primary or root user email
   address for all Core accounts. For more information, see [Multi-Account Landing Zone accounts](malz-net-arch-accounts.md "malz-net-arch-accounts.md").
4. Verify that you can access the primary or root user phone
   number for the management account. Use the
   `AWSManagedServicesBillingRole` IAM role to update the phone
   number. For more information, see [How
   do I update my telephone number that's associated with my AWS
   account?](https://repost.aws/knowledge-center/update-phone-number "https://repost.aws/knowledge-center/update-phone-number").
5. Log in to your AMS landing zone management account and submit
   an AMS service request. In the service request, specify to
   offboard your entire landing zone.

The following occurs after the Core accounts are offboarded:

- All components are disassociated from AMS services, but some
  AWS resources remain in the account. You can choose to keep or
  close the AMS offboarded Core accounts.
- AMS billing is stopped, but AWS billing isn’t stopped until
  you close the account. For more information, see [What
  you need to know before closing your account](../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations "../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations").
- If an account is closed, then the account is visible in your
  organization in the `suspended` state for 90 days.
  After 90 days, the closed member account is permanently
  removed and is no longer visible in your organization.
- After the account is closed, you can still sign in and file a
  support case or contact Support for 90 days.
- After the account is closed for 90 days, any content that
  remains in the account is permanently deleted, and the
  remaining AWS services are terminated.

**Q: Can I use my federated IAM roles to
continue to access the offboarded Core accounts?**
Yes. AMS created [default
AWS Identity and Access Management (IAM) roles](defaults-user-role.md "defaults-user-role.md") remain
available in the offboarded account. However, these
roles and policies are designed for use with AMS access
management. To provide the necessary access for your users, you
might need to deploy your own IAM resources.

**Q: How do I gain full access to the
Management, Shared Services, Networking, or other
non-Application [MALZ
account](malz-net-arch-accounts.md "malz-net-arch-accounts.md") after offboarding from AMS multi-account landing
zone?**
After offboarding, follow the instructions in [Resetting
a lost or forgotten root user password](../../../IAM/latest/UserGuide/reset-root-password.md "../../../IAM/latest/UserGuide/reset-root-password.md") to use primary
(root) user credentials to access Core accounts other than the
management account. Unlike other account types, the management
account retains an inaccessible multi-factor authentication
(MFA) device that’s associated to the root user to prevent
usage. To regain root access you must follow the [lost
MFA device recovery process](https://aws.amazon.com/blogs/security/reset-your-aws-root-accounts-lost-mfa-device-faster-by-using-the-aws-management-console/ "https://aws.amazon.com/blogs/security/reset-your-aws-root-accounts-lost-mfa-device-faster-by-using-the-aws-management-console/").

**Q: What changes are made during Core
account offboarding?**
For information about actions that AMS takes when the service
offboards accounts, see [Offboarding changes](#offboarding-malz-offboarding-changes "#offboarding-malz-offboarding-changes").

**Q: How long does Core account
offboarding take to complete?**
The Core account offboarding process typically takes up to 30
days to complete. However, to make sure that all required steps
are correctly completed, you must initiate the offboarding
request at least 7 days before offboarding starts. To facilitate
an easy transition, plan ahead and submit your offboarding
request in advance.

**Q: How do I manage shared components
after AMS offboarding?**
AMS Managed Active Directory and other shared services
infrastructure components are designed for AMS operator access.
You might need to update Amazon Elastic Compute Cloud (Amazon EC2) security groups, AWS Organizations service control policy
(SCP), or make other changes to retain full access to these
components.

**Q: Can I close offboarded Core
accounts?**
By default, Application accounts have multiple dependencies on
MALZ Core accounts, such as AWS Organizations membership,
transit gateway network connectivity, and DNS resolution through
AMS Managed Active Directory. After you resolve these
dependences, you can decommission and close the offboarded Core
account. For more information, see [Multi-Account Landing Zone accounts](malz-net-arch-accounts.md "malz-net-arch-accounts.md").

- **R**: Responsible party. The
  party responsible for completing the listed task.
- **A**: Accountable party.
  The party that approves the completed task.
- **C**: Consulted party. A
  party whose opinions are sought, typically as subject matter
  experts, and with whom there is bilateral communication.
- **I**: Informed party. A
  party that’s informed on progress, often only on completion
  of the task or deliverable.

| Activity                                                                                                                                             | Customer | AWS Managed Services (AMS) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------------------- |
| **Prerequisites**                                                                                                                                    |          |                            |
| Verify access to the root email address for each AWS<br>account ID that will be offboarded                                                           | R        | C                          |
| Verify access to and update the root user phone number<br>for the management account                                                                 | R        | C                          |
| Review AMS documentation on recommended customer actions<br>and prepare accounts for AMS offboarding                                                 | R        | C                          |
| **Offboarding**                                                                                                                                      |          |                            |
| Submit service request to request offboarding of the landing zone                                                                                    | R        | I                          |
| Offboard AMS components from Core accounts                                                                                                           | I        | R                          |
| **Post-offboarding**                                                                                                                                 |          |                            |
| Reset root user account password and verify root access<br>in offboarded accounts                                                                    | R        | C                          |
| Close the accounts or follow AMS guidance on recommended<br>customer actions in AMS offboarding documentation to<br>continue to operate the accounts | R        | C                          |

## Offboarding changes

The following table describes the actions that AMS takes for
multi-account landing zone offboarding, potential impacts, and
recommended actions.

| Component                                            | Account type                  | Actions taken to offboard                                                                                                                                                                                                                                                                                                                                                                                                                                       | Potential impacts                                                                                                                                                                                                                                                                                                                                       | Recommended customer action                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access management                                    | Application accounts          | After offboarding, stack access RFCs for just-in-time,<br>time-bound access can no longer be submitted to access<br>EC2 stacks through AMS bastion hosts<br>AMS no longer manages access-related components on any<br>existing EC2 resource stacks (PBIS Open agent, domain<br>join scripts)                                                                                                                                                                    | Can’t use AMS bastions through RFS to access EC2<br>instances<br>EC2 instances launched from non AMS provided AMIs aren’t<br>joined to Managed Active Directory domain<br>If not removed, AMS launch scripts in existing resource<br>stacks might produce errors because of missing AMS<br>dependencies, and prevent rejoining to a different<br>domain | Use alternate methods to access EC2 instance (see<br>[Access Alternatives](#offboarding-malz-access-alternatives "#offboarding-malz-access-alternatives"))<br>Remove AMS launch scripts from existing EC2 resource<br>stacks (see [Disable AMS EC2 launch scripts](#offboarding-malz-disable-ec2-launch-scripts "#offboarding-malz-disable-ec2-launch-scripts")) |
| Access management (cont’d)                           | Core accounts                 | If you migrated from PBIS Open to PBIS Enterprise (AD<br>Bridge), then AMS no longer renews licensing after core<br>account offboarding                                                                                                                                                                                                                                                                                                                         | If PBIS Enterprise license is allowed to expire, Active Directory<br>credentials aren’t valid for existing Linux-based EC2<br>instance stacks                                                                                                                                                                                                           | If you migrated to PBIS Enterprise (AD Bridge), then<br>decide whether to maintain licensing or decommission (see [PBIS Open/Enterprise (AD Bridge)](#offboarding-malz-pbis-open-enterprise "#offboarding-malz-pbis-open-enterprise"))                                                                                                                           |
| Logging, Monitoring, Incident/Event Management       | Application and Core accounts | AMS components to deploy<br>[Alerts from baseline monitoring in AMS](monitoring-default-metrics.md "monitoring-default-metrics.md") are removed<br>Existing deployed Amazon CloudWatch alarms remain but no<br>longer create AMS incidents<br>AWS Config aggregation authorizations from AMS and the<br>MALZ Core security account are removed<br>AWS Config rules remain deployed and Amazon GuardDuty<br>remains enabled, but no longer creates AMS incidents | Newly created resources don’t have AMS baseline<br>monitoring and alarms applied<br>Infrastructure metric alarms and security events no<br>longer generate AMS incidents<br>AWS Config is no longer aggregated in a central account                                                                                                                     | Define, capture, and analyze operations metrics to view<br>workload events and take appropriate action.<br>Implement any required alert workflow to continue to<br>apply required operational monitoring and alarms on new<br>resources and to for receive security alerts from AWS Config and Amazon GuardDuty.                                                 |
| Continuity management (Backup and Restore)           | Application accounts          | AMS no longer monitors backup jobs or performs backup<br>and restore requests<br>AMS default backup vaults, backup encryption key, and<br>backup role remain                                                                                                                                                                                                                                                                                                    | Backup operation failures might not be noticed                                                                                                                                                                                                                                                                                                          | Monitor and review backup plan configurations                                                                                                                                                                                                                                                                                                                    |
| Patch management                                     | Application and Core accounts | AMS no longer monitors patching operations for<br>successful execution or performs manual patching<br>AMS no longer updates AMS infrastructure components<br>AMS provided patch baselines are retained<br>AMS provided AWS Systems Manager patch automation<br>runbooks are unshared and no longer available for use                                                                                                                                            | Patching operation failures might not be noticed<br>Existing patch configurations that depend on AMS<br>provided Systems Manager Automation runbooks must be<br>reconfigured to continue uninterrupted                                                                                                                                                  | Review and reconfigure patching configurations as needed                                                                                                                                                                                                                                                                                                         |
| Network management                                   | Application accounts          | If specified, the transit gateway attachment in the<br>offboarded Application account is removed                                                                                                                                                                                                                                                                                                                                                                | Offboarded Application account can no longer use a transit<br>gateway to access shared services, such as Managed Active<br>Directory or other Application accounts                                                                                                                                                                                      | Specify `DeleteTransitGatewayAttachment` as `False` to retain<br>the transit gateway connectivity                                                                                                                                                                                                                                                                |
| Security management                                  | Application accounts          | Account is detached from central Trend Micro DSM<br>console. Also, endpoint agents no longer forward alerts<br>through the AMS incident process<br>Trend Micro agents remain installed but are no longer<br>managed or updated by AMS<br>AMS provided AMI customizations that deploy Trend Micro<br>agent are no longer maintained or updated by AMS                                                                                                            | EC2 instance endpoint malware detections might not be<br>noticed<br>The Trend micro agent isn’t deployed on EC2 instances<br>that are launched from non AMS provided AMIs                                                                                                                                                                               | Consider options for continuing or discontinuing Trend<br>Micro (see<br>[Trend Micro Deep Security](#offboarding-malz-trend-micro-deep-sec "#offboarding-malz-trend-micro-deep-sec"))                                                                                                                                                                            |
| Security management (cont’d)                         | Core accounts                 | Trend Micro DSM infrastructure is left in place within<br>Shared Services accounts but no longer maintained or<br>updated by AMS<br>Trend Micro DSM no longer forwards alerts through the AMS<br>incident process                                                                                                                                                                                                                                               | EC2 instance endpoint malware detections might go<br>unnoticed<br>EC2 instance endpoint protection might be impacted if<br>infrastructure isn’t maintained (definition updates,<br>licensing, and so on)                                                                                                                                                | Decide whether to continue or discontinue Trend Micro (see<br>(see [Trend Micro Deep Security](#offboarding-malz-trend-micro-deep-sec "#offboarding-malz-trend-micro-deep-sec"))                                                                                                                                                                                 |
| Change management                                    | Application and Core accounts | AMS RFC console and API is removed<br>AMS custom service control policies (SCPs) that contain<br>account-level access restrictions are detached during<br>Application account offboarding, and deleted during Core<br>account offboarding                                                                                                                                                                                                                       | You must use a native AWS API to create new resources, change existing resources, or update existing<br>AWS CloudFormation stacks<br>Access restrictions are no longer imposed at the<br>account-level through AMS provided SCPs                                                                                                                        | Make sure that user roles provide sufficient access to<br>use AWS services<br>Create SCPs to provide account-level permission<br>restrictions                                                                                                                                                                                                                    |
| AMS OS images and automations for service management | Application and Core accounts | AMS no longer provides support on customizations and<br>launch scripts included in AMS provided EC2 AMIs<br>AMS provided EC2 AMIs remain available in your<br>offboarded accounts<br>AMS provided Systems Manager Automation runbooks are<br>unshared and no longer available for use                                                                                                                                                                           | After offboarding, AMS provided AMIs launched with AWS CloudFormation send cfn-signal `FAILURE` because of<br>missing dependencies on AMS components<br>Operational processes that depend on AMS provided<br>Systems Manager Automation runbooks might fail                                                                                             | Review and update any build or operational processes that<br>are dependent on AMS provided AMIs or Systems Manager<br>Automation runbooks                                                                                                                                                                                                                        |
| Shared services infrastructure                       | Core accounts                 | AMS access is removed and AMS no longer manages shared<br>components, including AMS Managed Active Directory, AWS Transit Gateway, and AWS Organizations                                                                                                                                                                                                                                                                                                        | Loss of management over shared infrastructure                                                                                                                                                                                                                                                                                                           | Reset admin access to AMS Managed Active Directory and<br>assume management of shared services components                                                                                                                                                                                                                                                        |
| Reporting                                            | Application and Core accounts | AMS no longer collects account or resource-level details<br>for aggregate reporting                                                                                                                                                                                                                                                                                                                                                                             | Loss of insight into operational and business metrics<br>(backup and patching coverage, change management, and<br>incident activity)                                                                                                                                                                                                                    | Replace any needed aggregate data reporting across<br>accounts with their own solution                                                                                                                                                                                                                                                                           |
| AMS account team and service desk                    | Application and Core accounts | AMS account team (CSDM, CA) and AMS operations service<br>desk no longer support the offboarded accounts                                                                                                                                                                                                                                                                                                                                                        | Loss of operational support with expertise in the AMS<br>designed multi-account landing zone architecture and related components                                                                                                                                                                                                                        | Make sure that there’s sufficient personnel and<br>familiarity with account structure and resources to<br>support operations in the environment                                                                                                                                                                                                                  |

## Access Alternatives

The following are alternatives methods for retaining access to your EC2 stack after you offboard AMS accounts:

- **Use Session Manager** to
  access EC2 instances with elevated permissions without
  requiring bastions or inbound network access. For more
  information, see [AWS Systems Manager Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md").
- **Rejoin EC2 instances to a different
  Active Directory domain** with new domain
  credentials. If you use AWS Directory Service, then see [Join
  an EC2 instance to your AWS Managed Microsoft AD directory](../../../directoryservice/latest/admin-guide/ms_ad_join_instance.md "../../../directoryservice/latest/admin-guide/ms_ad_join_instance.md").
- **Use local user accounts** that you created through one of the other access methods or
  through [AWS Systems Manager Run Command](../../../systems-manager/latest/userguide/run-command.md "../../../systems-manager/latest/userguide/run-command.md").

## Disable AMS EC2 launch scripts

### Linux operating systems

Use your distribution’s package manager to uninstall the
`ams-modules` package. For example, for Amazon Linux 2 use `yum remove ams-modules`.

### Windows operating systems

To disable EC2 launch scripts in Windows, complete the following steps:

1. Windows Server 2008/2012/2012r2/2016/2019:

Disable or remove the Managed Services Startup scheduled task from Task Scheduler. To list scheduled tasks, run the `Get-ScheduledTask -TaskName '*Ec2*'` command.

Windows Server 2022:

Remove the [EC2Launch v2 task](../../../AWSEC2/latest/WindowsGuide/ec2launch-v2-settings.md#ec2launch-v2-schema-agent-config "../../../AWSEC2/latest/WindowsGuide/ec2launch-v2-settings.md#ec2launch-v2-schema-agent-config"). This task runs `Initialize-AMSBoot` in `postReady` stage in C:\ProgramData\Amazon\EC2Launch\config\agent-config.yml on the instance. The following is a snippet from an example `agent-config.yml`:

```
{
	"task": "executeScript",
	"inputs": [
		{
			"frequency": "always",
			"type": "powershell",
			"runAs": "localSystem"
		}
	]
}

```

2. (Optional) Remove the following file contents:

```
C:\Program Files\WindowsPowerShell\Modules\AWSManagedServices.*
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\AWSManagedServices.Build.Utilities\*

```

## PBIS Open/Enterprise (AD Bridge)

To determine if you use PBIS Open or PBIS Enterprise (AD Bridge) edition, run the following command in a Linux EC2 managed instance:

```
yum info | grep pbis
```

The following is example output that shows PBIS Enterprise (AD Bridge):

```
Name        : pbis-enterprise
From repo   : pbise
Name        : pbis-enterprise-devel
Repo        : pbise
Description : The pbis-enterprise-devel package includes the development

```

### PBIS Open

PBIS Open is a deprecated product that BeyondTrust no longer supports. For more information, see the [BeyondTrust pbis-open documentation](https://github.com/BeyondTrust/pbis-open/wiki/Documentation "https://github.com/BeyondTrust/pbis-open/wiki/Documentation").

### AD Bridge (PBIS Enterprise)

You can do one of the following:

- **Renew licensing and continue operating AD Bridge.** Contact BeyondTrust to discuss licensing and support.
- **Discontinue use of AD Bridge.** Run the following Shell command to remove PBIS-Enterprise package from Linux managed instances. For more information, see the BeyondTrust documentation [Leave a Domain and Uninstall the AD Bridge Agent](https://www.beyondtrust.com/docs/ad-bridge/getting-started/installation/leaving-domain.htm "https://www.beyondtrust.com/docs/ad-bridge/getting-started/installation/leaving-domain.htm").

```
$ sudo /opt/pbis/bin/uninstall.sh purge
```

### Leave the AMS managed Active Directory domain without removing PBIS agent

You have the option to leave the AMS managed Active Directory without removing the PBIS agent. Use one of the following solutions, depending on your operating system:

Linux operating systemsUse PBIS from the AMS managed AD to run the following shell command to unjoin a Linux EC2 instance. For more information, see the [BeyondTrust pbis-open](https://github.com/BeyondTrust/pbis-open/wiki/Documentation "https://github.com/BeyondTrust/pbis-open/wiki/Documentation") or [BeyondTrust AD Bridge](https://www.beyondtrust.com/docs/ad-bridge "https://www.beyondtrust.com/docs/ad-bridge") documentation, depending on which version you use.

```
$ sudo /opt/pbis/bin/domainjoin-cli leave
```

You might see an error message similar to the following:

```
Error: LW_ERROR_KRB5_REALM_CANT_RESOLVE [code 0x0000a3e1]
Cannot resolve network address for KDC in requested realm

```

If this error occurs, then run the following commands to delete AD provider registry and restart `lwsm` services:

```
$ /opt/pbis/bin/regshell dir '[HKEY_THIS_MACHINE\Services\lsass\Parameters\Providers\ActiveDirectory\DomainJoin]'
```

Use the directory ID output that you received from the previous command (for example, `A123EXAMPLE.AMAZONAWS.COM`) to run the following commands:

```
$ /opt/pbis/bin/regshell delete_tree \
'[HKEY_THIS_MACHINE\Services\lsass\Parameters\Providers\ActiveDirectory\DomainJoin\`DIRECTORYID`]'

$ /etc/pbis/redhat/lwsmd restart

$ /opt/pbis/bin/lwsm restart lwreg

```

Windows operating systems

```
# Collect hostname and domain name using:

Test-ComputerSecureChannel -verbose

# Disjoin computer from the domain:

netdom remove `hostname` /domain:`domain name` /force

```

###### Note

Make sure to disable or remove Managed Services Startup scheduled task as mentioned in [Disable AMS EC2 launch scripts](#offboarding-malz-disable-ec2-launch-scripts "#offboarding-malz-disable-ec2-launch-scripts").

## Trend Micro Deep Security

Use one of the following options to continue or discontinue the use of Trend Micro Deep Security:

###### Continue usage

- **(If offboarding the entire MALZ) After Core account offboarding, reconnect offboarded Application accounts to the existing Trend Micro Deep Security Manager (DSM) and maintain licensing in shared Services account.** For more information, see [Add AWS cloud accounts](https://help.deepsecurity.trendmicro.com/12_0/aws/Add-Computers/add-aws.html?Highlight=account%20sync "https://help.deepsecurity.trendmicro.com/12_0/aws/Add-Computers/add-aws.html?Highlight=account%20sync") and [Check your license information](https://help.deepsecurity.trendmicro.com/12_0/aws/Manage-Components/ui-admin-licenses.html "https://help.deepsecurity.trendmicro.com/12_0/aws/Manage-Components/ui-admin-licenses.html").
  1.  Log in to the shared services account and navigate to the Secrets Manager console.
  2.  Retrieve DSM console admin credentials that are stored in the `/ams/eps/` path.
  3.  Log in to the DSM console at [https://dsm.sentinel.int](https://dsm.sentinel.int/ "https://dsm.sentinel.int/").
  4.  Choose **Use Cross Account Role**, and then enter `arn:aws:iam::ACCOUNTID:role/mc_eps_cross_account_role`. Replace **ACCOUNTID** with the offboarded Application account ID.
  5.  Choose **Next**.
  6.  Wait several minutes for DSM to process the account discovery and show that sync was successful.

- **Reconnect offboarded Application accounts to a new Trend Micro DSM installation.** For more information, see [Activate and protect agents](https://help.deepsecurity.trendmicro.com/12_0/aws/agent-initiated-activation-communication.html?Highlight=activation "https://help.deepsecurity.trendmicro.com/12_0/aws/agent-initiated-activation-communication.html?Highlight=activation") and [Activate the agent](https://help.deepsecurity.trendmicro.com/12_0/aws/Get-Started/Install/activate-agent.html?Highlight=activate%20agent "https://help.deepsecurity.trendmicro.com/12_0/aws/Get-Started/Install/activate-agent.html?Highlight=activate%20agent").
- **Reconnect offboarded Application accounts to Trend Micro Cloud One.** For more information, see [Migrate from Deep Security to Workload Security](https://help.deepsecurity.trendmicro.com/20_0/on-premise/migration.html "https://help.deepsecurity.trendmicro.com/20_0/on-premise/migration.html") and [Migrate from an on-premises DSM](https://cloudone.trendmicro.com/docs/workload-security/migration/ "https://cloudone.trendmicro.com/docs/workload-security/migration/").

###### Discontinue usage

- **Uninstall Trend Micro Deep Security Agents from offboarded Application accounts.** For more information, see [Uninstall Deep Security](https://help.deepsecurity.trendmicro.com/12_0/aws/Get-Started/Install/ig-uninstall-basic.html?Highlight=uninstall%20agent "https://help.deepsecurity.trendmicro.com/12_0/aws/Get-Started/Install/ig-uninstall-basic.html?Highlight=uninstall%20agent").
