

# Managing service-linked roles for business plans
<a name="using-roles-for-partner-central-account"></a>

AWS Partner Central uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that links directly to AWS Partner Central. AWS Partner Central predefines its service-linked roles, and they include all the permissions that the service requires to update your business plans on your behalf.

A service-linked role makes setting up AWS Partner Central easier because you don't have to manually add the necessary permissions. AWS Partner Central defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Partner Central can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy can't be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html#all_svcs) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

To create or delete the business plan service-linked role, you need IAM permissions that an AWS account administrator usually has. If you aren't an administrator, ask your AWS account administrator to complete these tasks for you or to grant you the permissions.

**Topics**
+ [Service-linked role permissions for business plans](#slr-permissions)
+ [Creating a service-linked role](#create-slr)
+ [Editing a service-linked role](#edit-slr)
+ [Deleting a service-linked role](#delete-slr)
+ [Supported Regions](#slr-regions)

## Service-linked role permissions for business plans
<a name="slr-permissions"></a>

After you turn on AWS collaboration, your AWS partner development team can update your business plans through the service-linked role named `AWSServiceRoleForPartnerCentralAccount`.

The `AWSServiceRoleForPartnerCentralAccount` service-linked role trusts the following services to assume the role:
+ `partnercentral-account.amazonaws.com`

With the role permissions policy named `AWSPartnerCentralAccountManagementServiceRolePolicy`, your AWS partner development team can create, update, and cancel your business plans, and manage your plan items, submission tasks, and attachments. The policy covers only business plans in the AWS account that owns the role, and only while you have AWS collaboration turned on.

For details about the permissions in this policy, see [AWSPartnerCentralAccountManagementServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralAccountManagementServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

For information about policy updates, see [AWS Partner Central updates to AWS managed policies](managed-policies.md#security-iam-awsmanpol-updates).

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role
<a name="create-slr"></a>

To create the `AWSServiceRoleForPartnerCentralAccount` service-linked role, you need the following permissions:
+ `iam:CreateServiceLinkedRole`, to create the role
+ `iam:GetRole`, to view the role status
+ `partnercentral:GetBusinessPlanSettings` and `partnercentral:PutBusinessPlanSettings`, to view and turn on AWS collaboration<a name="create-slr-console"></a>

**To create a service-linked role (console)**

This procedure creates the service-linked role and turns on AWS collaboration, so that your AWS partner development team can work on your business plans.

1. Open the [AWS Partner Central settings page](https://us-east-1.console.aws.amazon.com/partnercentral/settings), signed in with the AWS account that owns your business plans.

1. On the settings page, choose **Service roles**.

1. In the **Business plan service-linked roles** section, review the status. If it shows **AWS collaboration connected**, the role already exists and AWS collaboration is on, so you can stop here.

1. In the same section, choose **Enable AWS collaboration**.

1. On the **Service-linked role for Business plans** page, under **Review service-linked role**, select the **AWS Partner Central Business plans service-linked role for this account** check box.

1. On the same page, choose **Create service-linked role**.

The **Service roles** tab opens again with the message "Service-linked role was successfully created". If the role already existed, the message is "AWS collaboration enabled". The **Business plan service-linked roles** section then shows the status **AWS collaboration connected**. The status change can take a few minutes.

If you have issues turning on AWS collaboration, use the following table to resolve the error message that appears on the **Service roles** tab.


| Error message | What to do | 
| --- | --- | 
| "You don't have permission to create a service-linked role." | Ask your AWS account administrator to grant you the iam:CreateServiceLinkedRole permission, or to complete these steps for you. For more information, see [Troubleshoot IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html) in the IAM User Guide. | 
| "Failed to create the service-linked role." | AWS Partner Central couldn't create the role. To create it again, complete the steps in [To create a service-linked role (console)](#create-slr-console). | 
| "AWS collaboration couldn't be enabled" | The service-linked role exists, but AWS Partner Central couldn't turn on AWS collaboration. To turn it on, complete the steps in [To create a service-linked role (console)](#create-slr-console). AWS Partner Central finds the existing role and turns on AWS collaboration only. | 

You see the **Enable AWS collaboration** button only if your account can use AWS collaboration and hasn't turned it on yet. If your account can't use it, you see the status **AWS collaboration isn't available for this account** instead.

You now have the `AWSServiceRoleForPartnerCentralAccount` service-linked role, and your AWS partner development team can update your business plans. If you delete the role, turn on AWS collaboration again to recreate it.

To create the role with the AWS CLI, first install the AWS CLI and configure it with credentials for the AWS account that owns your business plans, as described in [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS Command Line Interface User Guide*. You also need the `iam:CreateServiceLinkedRole` permission. If you create the role with the AWS CLI, you still need to turn on AWS collaboration by finishing the steps in the AWS Partner Central console.

**To create a service-linked role (AWS CLI)**

1. Run the following command, entering `partnercentral-account.amazonaws.com` for `--aws-service-name`.

   ```
   PROMPT> aws iam create-service-linked-role --aws-service-name partnercentral-account.amazonaws.com
   ```
**Note**  
To resolve an `AccessDenied` error from this command, ask your AWS account administrator to grant you the `iam:CreateServiceLinkedRole` permission, and then run the command again.

   The output shows the details of the new role, including its Amazon Resource Name (ARN).

1. On the **Service roles** tab of the [AWS Partner Central settings page](https://us-east-1.console.aws.amazon.com/partnercentral/settings), choose **Enable AWS collaboration**.

1. Select the **AWS Partner Central Business plans service-linked role for this account** check box.

1. Choose **Create service-linked role**. AWS Partner Central finds the role that you created and turns on AWS collaboration.

For more information, see [Create a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) in the *IAM User Guide*.

## Editing a service-linked role
<a name="edit-slr"></a>

You can't edit the `AWSServiceRoleForPartnerCentralAccount` service-linked role in AWS Partner Central. After you create it, you can't change its name. Other entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Update a role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-settings.html#id_roles_update-description) in the *IAM User Guide*.

## Deleting a service-linked role
<a name="delete-slr"></a>

Delete the service-linked role when you no longer need the feature that requires it. That way, you don't keep an unused role that no one actively monitors or maintains.

**Note**  
To complete this procedure, you need the `iam:DeleteServiceLinkedRole` permission. If you don't have it, ask your AWS account administrator to grant it or complete these steps for you. The procedure disconnects AWS collaboration before it deletes the role.

**Important**  
After you delete the role, your AWS partner development team can't update your business plans until you recreate the role. Your business plans stay the same, and they stay available to your organization.

**To delete a service-linked role**

1. Open the [AWS Partner Central settings page](https://us-east-1.console.aws.amazon.com/partnercentral/settings), signed in with the AWS account that owns your business plans.

1. On the settings page, choose **Service roles**.

1. In the **Business plan service-linked roles** section, choose **Disconnect**.

1. In the confirmation dialog, choose **Disconnect** to turn off AWS collaboration.

1. In the AWS Identity and Access Management (IAM) console, delete the `AWSServiceRoleForPartnerCentralAccount` service-linked role. You can also use the AWS CLI or the AWS API. For instructions on deleting a service-linked role, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.

   IAM can take some time to delete the role. To check the deletion status with the AWS CLI, run the `aws iam get-service-linked-role-deletion-status` command.

   If IAM can't delete the role, make sure that AWS collaboration is disconnected, and then delete the role again.

The role no longer appears in IAM. To work with your AWS partner development team again, turn on AWS collaboration, which recreates the role.

## Supported Regions
<a name="slr-regions"></a>

AWS Partner Central supports the `AWSServiceRoleForPartnerCentralAccount` service-linked role in the AWS Region where business plans are available.

**Note**  
Business plans are available only in the US East (N. Virginia) Region (`us-east-1`).