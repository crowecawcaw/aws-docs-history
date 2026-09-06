

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# (Optional) Configure OpsCenter to manage OpsItems across accounts by using Quick Setup
<a name="OpsCenter-quick-setup-cross-account"></a>

Quick Setup simplifies setup and configuration tasks for Systems Manager tools. Quick Setup for OpsCenter helps you complete the following tasks for managing OpsItems across accounts:
+ Specifying the delegated administrator account
+ Creating required AWS Identity and Access Management (IAM) policies and roles
+ Specifying an AWS Organizations organization, or a subset of member accounts, where a delegated administrator can manage OpsItems across accounts

When you configure OpsCenter to manage OpsItems across accounts by using Quick Setup, Quick Setup creates the following resources in the specified accounts. These resources give the specified accounts permission to work with OpsItems and use Automation runbooks to fix issues with AWS resources generating OpsItems.



| Resources | Accounts | 
| --- | --- | 
| `AWSServiceRoleForAmazonSSM_AccountDiscovery` AWS Identity and Access Management (IAM) service-linked role<br />For more information about this role, see [Using roles to collect AWS account information for OpsCenter and Explorer](using-service-linked-roles-service-action-2.md). | AWS Organizations management account and delegated administrator account | 
| `OpsItem-CrossAccountManagementRole` IAM role<br /> `AWS-SystemsManager-AutomationAdministrationRole` IAM role | Delegated administrator account | 
| `OpsItem-CrossAccountExecutionRole` IAM role<br /> `AWS-SystemsManager-AutomationExecutionRole` IAM role<br /> `AWS::SSM::ResourcePolicy` Systems Manager resource policy for the default OpsItem group (`OpsItemGroup`) | All AWS Organizations member accounts | 

**Note**  
If you previously configured OpsCenter to manage OpsItems across accounts using the [manual method](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-getting-started-multiple-accounts.html), you must delete the AWS CloudFormation stacks or stack sets created during Steps 4 and 5 of that process. If those resources exist in your account when you complete the following procedure, Quick Setup fails to configure cross-account OpsItem management properly.

**To configure OpsCenter to manage OpsItems across accounts by using Quick Setup**

1. Sign in to the AWS Management Console using the AWS Organizations management account.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Quick Setup**.

1. Choose the **Library** tab.

1. Scroll to the bottom and locate the **OpsCenter** configuration tile. Choose **Create**.

1. On the Quick Setup OpsCenter page, in the **Delegated administrator** section, enter an account ID. If you are unable to edit this field, then a delegated administrator account has already been specified for Systems Manager.

1. In the **Targets** section, choose an option. If you choose **Custom**, then select the organizational units (OU) where you want to manage OpsItems across accounts.

1. Choose **Create**.

Quick Setup creates the OpsCenter configuration and deploys the required AWS resources to the designated OUs. 

**Note**  
If you don't want to manage OpsItems across multiple accounts, you can delete the configuration from Quick Setup. When you delete the configuration, Quick Setup deletes the following IAM policies and roles created when the configuration was originally deployed:  
`OpsItem-CrossAccountManagementRole` from the delegated administrator account
`OpsItem-CrossAccountExecutionRole` and `SSM::ResourcePolicy` from all Organizations member accounts
Quick Setup removes the configuration from all organizational units and AWS Regions where the configuration was originally deployed.

## Troubleshooting issues with a Quick Setup configuration for OpsCenter
<a name="OpsCenter-quick-setup-cross-account-troubleshooting"></a>

This section includes information to help you troubleshoot issues when configuring cross-account OpsItem management using Quick Setup.

**Topics**
+ [Deployment to these StackSets failed: delegatedAdmin](#OpsCenter-quick-setup-cross-account-troubleshooting-stack-set-failed)
+ [Quick Setup configuration status shows Failed](#OpsCenter-quick-setup-cross-account-troubleshooting-configuration-failed)

### Deployment to these StackSets failed: delegatedAdmin
<a name="OpsCenter-quick-setup-cross-account-troubleshooting-stack-set-failed"></a>

When creating an OpsCenter configuration, Quick Setup deploys two AWS CloudFormation stack sets in the Organizations management account. The stack sets use the following prefix: `AWS-QuickSetup-SSMOpsCenter`. If Quick Setup displays the following error: `Deployment to these StackSets failed: delegatedAdmin` use the following procedure to fix this issue.

**To troubleshoot a StackSets failed:delegatedAdmin error**

1. If you received the `Deployment to these StackSets failed: delegatedAdmin` error in a red banner in the Quick Setup console, sign in to the delegated administrator account and the AWS Region designated as the Quick Setup home Region.

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Choose the stack created by your Quick Setup configuration. The stack name includes the following: **AWS-QuickSetup-SSMOpsCenter**.
**Note**  
Sometimes CloudFormation deletes failed stack deployments. If the stack isn't available in the **Stacks** table, choose **Deleted** from the filter list.

1. View the **Status** and **Status reason**. For more information about stack statuses, see [Stack status codes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html#cfn-console-view-stack-data-resources-status-codes) in the *AWS CloudFormation User Guide*. 

1. To understand the exact step that failed, view the **Events** tab and review each event's **Status**. For more information, see [Troubleshooting](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html) in the *AWS CloudFormation User Guide*.

**Note**  
If you are unable to resolve the deployment failure using the CloudFormation troubleshooting steps, delete the configuration and try again.

### Quick Setup configuration status shows Failed
<a name="OpsCenter-quick-setup-cross-account-troubleshooting-configuration-failed"></a>

If the **Configuration details** table on the **Configuration details** page shows a configuration status of `Failed`, sign in to the AWS account and Region where it failed.

**To troubleshoot a Quick Setup failure to create an OpsCenter configuration**

1. Sign in to the AWS account and the AWS Region where the failure occurred.

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Choose the stack created by your Quick Setup configuration. The stack name includes the following: **AWS-QuickSetup-SSMOpsCenter**.
**Note**  
Sometimes CloudFormation deletes failed stack deployments. If the stack isn't available in the **Stacks** table, choose **Deleted** from the filter list.

1. View the **Status** and **Status reason**. For more information about stack statuses, see [Stack status codes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html#cfn-console-view-stack-data-resources-status-codes) in the *AWS CloudFormation User Guide*. 

1. To understand the exact step that failed, view the **Events** tab and review each event's **Status**. For more information, see [Troubleshooting](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html) in the *AWS CloudFormation User Guide*.

#### Member account configuration shows ResourcePolicyLimitExceededException
<a name="OpsCenter-quick-setup-cross-account-troubleshooting-policy-limit-exception"></a>

If a stack status shows `ResourcePolicyLimitExceededException`, the account has previously onboarded to OpsCenter cross-account management by using the [manual method](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-getting-started-multiple-accounts.html). To resolve this issue, you must delete the AWS CloudFormation stacks or stack sets created during Steps 4 and 5 of the manual onboarding process. For more information, see [Delete a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-delete.html) and [Deleting a stack on the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) in the *AWS CloudFormation User Guide*.