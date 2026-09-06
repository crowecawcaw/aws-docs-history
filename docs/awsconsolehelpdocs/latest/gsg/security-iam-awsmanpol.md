

# AWS managed policies for the AWS Management Console
<a name="security-iam-awsmanpol"></a>



An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

 





## AWS managed policy: AWSManagementConsoleBasicUserAccess
<a name="security-iam-awsmanpol-AWSManagementConsoleBasicUserAccess"></a>





You can attach `AWSManagementConsoleBasicUserAccess` to your users, groups, and roles.



This policy grants the permissions necessary for non-administrative users of the AWS Management Console. This includes features such as resource discovery, notifications, browser-based shell access, and customized navigation.



**Permissions details**

This `AWSManagementConsoleBasicUserAccess` is grouped into the following sets of permissions:




+ `cloudshell` – Allows principals full access to AWS CloudShell capabilities, including environment creation, session management, and command execution.
+ `ec2` – Allows principals to describe Regions enabled for the account in [Unified Navigation](unified-navigation.md).
+ `notifications` – Allows principals to obtain events from AWS User Notifications.
+ `q` – Allows principals to chat with Amazon Q Developer.
+ `resource-explorer-2` – Allows principals to search and discover AWS resources using [Unified Search](using-search.md).
+ `uxc` – Allows principals to read AWS User Experience Customization settings.
+ `action-recommendations` – Allows principals to receive contextual action recommendations.
+ `account` – Allows principals to retrieve information about the specified account including its account name, account ID, and account creation date and time.



To view the permissions for this policy, see [AWSManagementConsoleBasicUserAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSManagementConsoleBasicUserAccess.html) in the *AWS Managed Policy Reference.*

## AWS managed policy: AWSManagementConsoleAdministratorAccess
<a name="security-iam-awsmanpol-AWSManagementConsoleAdministratorAccess"></a>





You can attach `AWSManagementConsoleAdministratorAccess` to your users, groups, and roles.



This policy grants full access to configure and customize the AWS Management Console. It allows administrators to set account colors, enable user notifications, and configure resource discovery. It also includes permissions from the `AWSManagementConsoleBasicUserAccess` managed policy, which are essential for non-administrative users of the AWS Management Console.



**Permissions details**

This `AWSManagementConsoleAdministratorAccess` is grouped into the following sets of permissions:




+ `cloudshell` – Allows principals full access to AWS CloudShell capabilities, including environment creation, session management, and command execution.
+ `ec2` – Allows principals to describe Regions enabled for the account in [Unified Navigation](unified-navigation.md).
+ `notifications` – Allows principals to access and update notification configurations, events, and feature opt-in status.
+ `q` – Allows principals to chat with Amazon Q Developer for AI-assisted support.
+ `resource-explorer-2` – Allows principals to search and discover AWS resources using [Unified Search](using-search.md).
+ `uxc` – Allows principals full access to AWS User Experience Customization settings.
+ `action-recommendations` – Allows principals to receive contextual action recommendations.
+ `account` – Allows principals to retrieve information about the specified account including its account name, account ID, and account creation date and time.



To view the permissions for this policy, see [AWSManagementConsoleAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSManagementConsoleAdministratorAccess.html) in the *AWS Managed Policy Reference.*

## AWS Management Console updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for the AWS Management Console since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Management Console Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AWSManagementConsoleBasicUserAccess](#security-iam-awsmanpol-AWSManagementConsoleBasicUserAccess) – Updated policy | Added `uxc:GetAccountCustomizations` and `uxc:ListServices` permissions. | March 26, 2026 | 
| [AWSManagementConsoleAdministratorAccess](#security-iam-awsmanpol-AWSManagementConsoleAdministratorAccess) – Updated policy | Added `uxc:GetAccountCustomizations`, `uxc:UpdateAccountCustomizations`, and `uxc:ListServices` permissions. | March 26, 2026 | 
| [AWSManagementConsoleBasicUserAccess](#security-iam-awsmanpol-AWSManagementConsoleBasicUserAccess) – Updated policy | Updated policy to add permissions to allow users to see account information and receive action recommendations while navigating the AWS Management Console. | December 9, 2025 | 
| [AWSManagementConsoleAdministratorAccess](#security-iam-awsmanpol-AWSManagementConsoleAdministratorAccess) – Updated policy | Updated policy to add permissions to allow users to see account information and receive action recommendations while navigating the AWS Management Console. | December 9, 2025 | 
| [AWSManagementConsoleBasicUserAccess](#security-iam-awsmanpol-AWSManagementConsoleBasicUserAccess) – New policy | Added a new AWS managed policy that grants permissions necessary for basic AWS Management Console navigation, account color viewing, and resource discovery. | August 14, 2025 | 
| [AWSManagementConsoleAdministratorAccess](#security-iam-awsmanpol-AWSManagementConsoleAdministratorAccess) – New policy | Added a new AWS managed policy that provides full access to configure and customize the AWS Management Console. | August 14, 2025 | 
| AWS Management Console started tracking changes | AWS Management Console started tracking changes for its AWS managed policies. | August 14, 2025 | 