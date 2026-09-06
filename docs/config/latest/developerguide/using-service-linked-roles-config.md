

# Using Service-Linked Roles for AWS Config
<a name="using-service-linked-roles-config"></a>

## Service-Linked Role Permissions for AWS Config
<a name="slr-permissions"></a>

AWS Config uses the service-linked role named **AwsServiceRoleForConfig** – AWS Config uses this service-linked role to call other AWS services on your behalf. To view the latest updates, see [AWS Config updates to AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates).

The AwsServiceRoleForConfig service-linked role trusts the following services to assume the role:
+ `config.amazonaws.com`

The role permissions policy named AWSConfigServiceRolePolicy allows AWS Config to complete the following actions on the specified resources:
+ Read-only and write-only permissions for AWS Config resources
+ Read-only permissions for resources in other services that AWS Config supports

To view the managed policy for **AwsServiceRoleForConfig**, see [AWS managed policies for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSConfigServiceRolePolicy).

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

To use a service-linked role with AWS Config, you must configure permissions on your Amazon S3 bucket and Amazon SNS topic. For more information, see [Required Permissions for the Amazon S3 Bucket When Using Service-Linked Roles](s3-bucket-policy.md#required-permissions-using-servicelinkedrole), [Required Permissions for the AWS KMS Key When Using Service-Linked Roles (S3 Bucket Delivery)](s3-kms-key-policy.md#required-permissions-s3-kms-key-using-servicelinkedrole), and [Required Permissions for the Amazon SNS Topic When Using Service-Linked Roles](sns-topic-policy.md#required-permissions-snstopic-using-servicelinkedrole).

## Creating a Service-Linked Role for AWS Config
<a name="create-slr"></a>

In the IAM CLI or the IAM API, create a service-linked role with the `config.amazonaws.com` service name. For more information, see [Creating a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

## Editing a Service-Linked Role for AWS Config
<a name="edit-slr"></a>

AWS Config does not allow you to edit the **AwsServiceRoleForConfig** service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html) in the *IAM User Guide*.

## Deleting a Service-Linked Role for AWS Config
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

**Note**  
If the AWS Config service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete AWS Config resources used by the AwsServiceRoleForConfig**

Ensure that you do not have `ConfigurationRecorders` using the service-linked role. You can use the AWS Config console to stop the configuration recorder. To stop recording, under **Recording is on**, choose **Turn off**.

You can delete the `ConfigurationRecorder` using the AWS Config API:

```
$ aws configservice delete-configuration-recorder --configuration-recorder-name {{default}}
```

**To manually delete the service-linked role using IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the AwsServiceRoleForConfig service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the *IAM User Guide*.

## Supported Regions for AWS Config Service-Linked Roles
<a name="slr-regions"></a>

AWS Config supports using the AwsServiceRoleForConfig role in all of the Regions where the service is available. For more information, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).