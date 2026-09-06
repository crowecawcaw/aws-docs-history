

# Service-linked role for AWS DMS
<a name="slr-services-sl"></a>

AWS DMS uses the service-linked role named **AWSServiceRoleForDMSServerless**. AWS DMS uses this service-linked role to create and manage AWS DMS resources on your behalf. AWS DMS uses this role for automatic instance management so that you only have to manage replications. DMS Schema Conversion also uses this role to access designated Amazon S3 resources on your behalf.

The [AWSServiceRoleForDMSServerless](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy) service-linked role trusts the following services to assume the role:
+ `dms.amazonaws.com`

You must configure permissions to allow an IAM entity, such as a user, group, or role, to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS DMS
<a name="create-slr-sl"></a>

AWS DMS programmatically creates a AWS DMS service-linked role when you start a replication task, start a premigration assessment, or create a migration project with a virtual data provider within DMS Schema Conversion. You can view this role in the IAM console. You can also choose to create this role manually. To create the role manually, use the IAM console to create a service-linked role with the **DMS** use case. In the AWS CLI or the AWS API, create a service-linked role using `dms.amazonaws.com` for the service name. For more information, see [ Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

**Note**  
If you delete a role while you have replications in your account, the replication results in a failure.

## Editing a service-linked role for AWS DMS
<a name="edit-slr-sl"></a>

AWS DMS does not allow you to edit the AWSServiceRoleForDMSServerless service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS DMS
<a name="delete-slr-sl"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. Thus, you don’t have an unused entity that isn't actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

**Note**  
If the AWS DMS service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete AWS DMS resources used by the AWSServiceRoleForDMSServerless**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2](https://console.aws.amazon.com/dms/v2/).

1. In the navigation pane, choose **Serverless replications** under ****Migrate data****. The **Serverless** page opens.

1. Choose your serverless replication and choose **Delete**.

1. To confirm deletion, enter the serverless replication name in the text input field. Next, choose **Delete**.

After you delete all serverless replications, you can delete the service-linked role.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForDMSServerless service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported regions for AWS DMS service-linked roles
<a name="slr-regions-sl"></a>

AWS DMS supports using service-linked roles in all of the regions where the service is available. 