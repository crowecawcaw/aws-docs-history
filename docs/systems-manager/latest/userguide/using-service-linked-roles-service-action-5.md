

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Using roles to maintain Quick Setup-provisioned resource health and consistency
<a name="using-service-linked-roles-service-action-5"></a>

Systems Manager uses the service-linked role named **`AWSServiceRoleForSSMQuickSetup`**. 

## `AWSServiceRoleForSSMQuickSetup` service-linked role permissions for Systems Manager
<a name="service-linked-role-permissions-service-action-5"></a>

The `AWSServiceRoleForSSMQuickSetup` service-linked role trusts the following services to assume the role:
+ `ssm-quicksetup.amazonaws.com`

AWS Systems Manager uses this IAM service role to check configuration health, ensure consistent use of parameters and provisioned resources, and remediate resources when drift is detected.

The role permissions policy allows Systems Manager to complete the following actions on the specified resources:
+ `ssm` (Systems Manager) – Reads information about the state that configured resources are intended to be in, including in delegated administrator accounts. 
+ `iam` (AWS Identity and Access Management) – This is required for resource data syncs to be accessible across entire organizations in AWS Organizations.
+ `organizations` (AWS Organizations) – Reads information about the member accounts that belong to an organization as configured in Organizations. 
+ `cloudformation` (CloudFormation) – Reads information about CloudFormation stacks used to manage the state of resources and CloudFormation stackset operations.

The managed policy that is used to provide permissions for the `AWSServiceRoleForSSMQuickSetup` role is `SSMQuickSetupRolePolicy`. For details about the permissions it grants, see [AWS managed policy: SSMQuickSetupRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-SSMQuickSetupRolePolicy).

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating the `AWSServiceRoleForSSMQuickSetup` service-linked role for Systems Manager
<a name="create-service-linked-role-service-action-5"></a>

You don't need to manually create the AWSServiceRoleForSSMQuickSetup service-linked role. When you create a Quick Setup configuration in the AWS Management Console, Systems Manager creates the service-linked role for you. 

## Editing the `AWSServiceRoleForSSMQuickSetup` service-linked role for Systems Manager
<a name="edit-service-linked-role-service-action-5"></a>

Systems Manager does not allow you to edit the `AWSServiceRoleForSSMQuickSetup` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting the `AWSServiceRoleForSSMQuickSetup` service-linked role for Systems Manager
<a name="delete-service-linked-role-service-action-5"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up the `AWSServiceRoleForSSMQuickSetup` service-linked role
<a name="service-linked-role-review-before-delete-service-action-5"></a>

Before you can use IAM to delete the `AWSServiceRoleForSSMQuickSetup` service-linked role, you must first delete the Quick Setup configurations that are using the role. For more information, see [Editing and deleting your configuration](quick-setup-using.md#quick-setup-edit-delete).

### Manually delete the `AWSServiceRoleForSSMQuickSetup` service-linked role
<a name="slr-manual-delete-service-action-5"></a>

Use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForSSMQuickSetup` service-linked role. For more information, see the following topics:
+ [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*
+ [delete-configuration-manager](https://docs.aws.amazon.com/cli/latest/reference/ssm-quicksetup/delete-configuration-manager.html) in the Quick Setup section of the *AWS CLI Reference*
+ [DeleteConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_DeleteConfigurationManager.html) in the *Quick Setup API Reference*

## Supported Regions for the Systems Manager  `AWSServiceRoleForSSMQuickSetup` service-linked role
<a name="slr-regions-service-action-5"></a>

Systems Manager does not support using service-linked roles in every Region where the service is available. You can use the AWSServiceRoleForSSMQuickSetup role in the following Regions.
+ US East (Ohio)
+ US East (N. Virginia)
+ US West (N. California)
+ US West (Oregon)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (Stockholm)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ South America (São Paulo)