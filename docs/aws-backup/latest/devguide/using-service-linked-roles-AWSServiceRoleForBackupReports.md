# Using roles for AWS Backup Audit Manager

AWS Backup uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Backup. Service-linked roles are predefined by AWS Backup and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Backup easier because you don’t have to
manually add the necessary permissions. AWS Backup defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS Backup can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
protects your AWS Backup resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role

permissions for AWS Backup

AWS Backup uses the service-linked role named **AWSServiceRoleForBackupReports**
– Provides AWS Backup with permission to create controls, frameworks, and reports.

The AWSServiceRoleForBackupReports service-linked role trusts the following services to assume the
role:

- `reports.backup.amazonaws.com`

To view the permissions for this policy, see [AWSServiceRolePolicyForBackupReports](../../../aws-managed-policy/latest/reference/AWSServiceRolePolicyForBackupReports.md "../../../aws-managed-policy/latest/reference/AWSServiceRolePolicyForBackupReports.md") in the _AWS Managed Policy Reference_.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for

AWS Backup

You don't need to manually create a service-linked role. When you
create a framework or a report plan in the AWS Management Console, the AWS CLI, or the AWS API, AWS Backup
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in another
service that uses the features supported by this role.
To
learn more, see [A New Role Appeared in My IAM Account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create a framework or a report plan, AWS Backup creates the service-linked role for you again.

## Editing a service-linked role for

AWS Backup

AWS Backup does not allow you to edit the AWSServiceRoleForBackupReports service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Edite a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the
_IAM User Guide_.

## Deleting a service-linked role for

AWS Backup

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up your service-linked role before
you can manually delete it.

### Cleaning up a

service-linked role

Before you can use IAM to delete a service-linked role, you must first delete any
resources used by the role. You must delete all frameworks and report plans.

###### Note

If the AWS Backup service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes, then try the
operation again.

###### To delete AWS Backup resources used by the AWSServiceRoleForBackupReports (console)

1. To delete all frameworks, see [Deleting
   frameworks](deleting-frameworks.md "deleting-frameworks.md").
2. To delete all report plans, see [Deleting report
   plans](delete-report-plan.md "delete-report-plan.md").

###### To delete AWS Backup resources used by the AWSServiceRoleForBackupReports (AWS CLI)

1. To delete all frameworks, use [delete-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-framework.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-framework.html").
2. To delete all report plans, use [delete-report-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-report-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-report-plan.html").

###### To delete AWS Backup resources used by the AWSServiceRoleForBackupReports (API)

1. To delete all frameworks, use [DeleteFramework](API_DeleteFramework.md "API_DeleteFramework.md").
2. To delete all report plans, use [DeleteReportPlan](API_DeleteReportPlan.md "API_DeleteReportPlan.md").

### Manually delete the service-linked

role

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForBackupReports
service-linked role. For more information, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the
_IAM User Guide_.

## Supported Regions for AWS Backup

service-linked roles

AWS Backup supports using service-linked roles in all of the Regions where the
service is available. For more information, see [AWS Backup supported features and Regions](whatisbackup.md#features-by-region "whatisbackup.md#features-by-region").
