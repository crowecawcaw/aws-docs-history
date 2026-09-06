

# Using roles for AWS Backup Audit Manager
<a name="using-service-linked-roles-AWSServiceRoleForBackupReports"></a>

AWS Backup uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts). A service-linked role is a unique type of IAM role that is linked directly to AWS Backup. Service-linked roles are predefined by AWS Backup and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up AWS Backup easier because you don’t have to manually add the necessary permissions. AWS Backup defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Backup can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your AWS Backup resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for AWS Backup
<a name="service-linked-role-permissions-AWSServiceRoleForBackupReports"></a>

AWS Backup uses the service-linked role named **AWSServiceRoleForBackupReports** – Provides AWS Backup with permission to create controls, frameworks, and reports.

The AWSServiceRoleForBackupReports service-linked role trusts the following services to assume the role:
+ `reports.backup.amazonaws.com`

To view the permissions for this policy, see [AWSServiceRolePolicyForBackupReports](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSServiceRolePolicyForBackupReports.html) in the *AWS Managed Policy Reference*.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS Backup
<a name="create-service-linked-role-AWSServiceRoleForBackupReports"></a>

You don't need to manually create a service-linked role. When you create a framework or a report plan in the AWS Management Console, the AWS CLI, or the AWS API, AWS Backup creates the service-linked role for you. 

**Important**  
 This service-linked role can appear in your account if you completed an action in another service that uses the features supported by this role. To learn more, see [A New Role Appeared in My IAM Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create a framework or a report plan, AWS Backup creates the service-linked role for you again. 

## Editing a service-linked role for AWS Backup
<a name="edit-service-linked-role-AWSServiceRoleForBackupReports"></a>

AWS Backup does not allow you to edit the AWSServiceRoleForBackupReports service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Edite a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console) in the *IAM User Guide*.

## Deleting a service-linked role for AWS Backup
<a name="delete-service-linked-role-AWSServiceRoleForBackupReports"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up a service-linked role
<a name="service-linked-role-review-before-delete-AWSServiceRoleForBackupReports"></a>

Before you can use IAM to delete a service-linked role, you must first delete any resources used by the role. You must delete all frameworks and report plans.

**Note**  
If the AWS Backup service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes, then try the operation again.

**To delete AWS Backup resources used by the AWSServiceRoleForBackupReports (console)**

1. To delete all frameworks, see [Deleting frameworks](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-frameworks.html).

1. To delete all report plans, see [Deleting report plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/delete-report-plan.html).

**To delete AWS Backup resources used by the AWSServiceRoleForBackupReports (AWS CLI)**

1. To delete all frameworks, use [delete-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-framework.html).

1. To delete all report plans, use [delete-report-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-report-plan.html).

**To delete AWS Backup resources used by the AWSServiceRoleForBackupReports (API)**

1. To delete all frameworks, use [DeleteFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteFramework.html).

1. To delete all report plans, use [DeleteReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteReportPlan.html).

### Manually delete the service-linked role
<a name="slr-manual-delete-AWSServiceRoleForBackupReports"></a>

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForBackupReports service-linked role. For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.

## Supported Regions for AWS Backup service-linked roles
<a name="slr-regions-AWSServiceRoleForBackupReports"></a>

AWS Backup supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS Backup supported features and Regions](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-region).