# Service-linked role for AWS DMS

AWS DMS uses the service-linked role named **AWSServiceRoleForDMSServerless**.
AWS DMS uses this service-linked role to create and manage AWS DMS resources on your behalf. AWS DMS uses this role for automatic instance management so that you only have to manage replications.

The [AWSServiceRoleForDMSServerless](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy") service-linked role
trusts the following services to assume the role:

- `dms.amazonaws.com`
  You must configure permissions to allow an IAM entity, such as a user, group, or role, to
  create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for AWS DMS

When you start a replication task, or start a premigration assessment, AWS DMS programmatically creates a AWS DMS
service linked role. You can view this role in the IAM console. You can also
choose to create this role manually. To create the role manually, use the IAM console to
create a service-linked role with the **DMS** use case. In the AWS CLI or the
AWS API, create a service-linked role using `dms.amazonaws.com` for the service
name. For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_. If you delete this service-linked role, you can use
this same process to create the role again.

###### Note

If you delete a role while you have replications in your account, the replication
results in a failure.

## Editing a service-linked role for AWS DMS

AWS DMS does not allow you to edit the AWSServiceRoleForDMSServerless service-linked role. After you
create a service-linked role, you can't change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for AWS DMS

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. Thus, you don’t have an unused entity that isn't actively
monitored or maintained. However, you must clean up the resources for your service-linked role
before you can manually delete it.

###### Note

If the AWS DMS service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete AWS DMS resources used by the AWSServiceRoleForDMSServerless

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2](https://console.aws.amazon.com/https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/https://console.aws.amazon.com/dms/v2/").
2. In the navigation pane, choose **Serverless replications** under \***\*Migrate data\*\***. The
   **Serverless** page opens.
3. Choose your serverless replication and choose **Delete**.
4. To confirm deletion, enter the serverless replication name in the text input field.
   Next, choose **Delete**.

After you delete all serverless replications, you can delete the service-linked
role.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForDMSServerless service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for AWS DMS service-linked roles

AWS DMS supports using service-linked roles in all of the regions where
the service is available.
