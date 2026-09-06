

# Service-linked roles for Data Exports
<a name="data-exports-SLR"></a>

Data Exports uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Data Exports. Service-linked roles are predefined by Data Exports and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Data Exports easier because you don’t have to manually add the necessary permissions. Data Exports defines the permissions of its service-linked role, and unless defined otherwise, only Data Exports can assume that role. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for Data Exports
<a name="data-exports-SLR-permissions"></a>

Data Exports uses the service-linked role named `AWSServiceRoleForBCMDataExports`, which enables access to AWS service data for exporting the data to a target location, such as Amazon S3, on behalf of the customer. This service-linked role is used for read-only actions to collect the least amount of AWS service data necessary. The service-linked role is used over time to ensure security and to continue refreshing the export data in the target location.

The `AWSServiceRoleForBCMDataExports` service-linked role trusts the `bcm-data-exports.amazonaws.com` service to assume the role.

The role permissions policy, `AWSBCMDataExportsServiceRolePolicy`, allows Data Exports to complete the following actions on the specified resources:
+ cost-optimization-hub:ListEnrollmentStatuses
+ cost-optimization-hub:ListRecommendation

For more information, see [Allows Data Exports to access other AWS services](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#data-exports-managedIAM).

To view the full permissions details of the service-linked role `AWSBCMDataExportsServiceRolePolicy`, see [AWSBCMDataExportsServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CostOptimizationHubServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

 You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the IAM User Guide.

## Creating the Data Exports service-linked role
<a name="data-exports-create-SLR"></a>

You don't need to manually create the Data Exports service-linked role. On the Data Exports console page, when you attempt to create an export of a table that requires the service-linked role, the service automatically creates the role for you.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account.

## Editing the Data Exports service-linked role
<a name="data-exports-edit-SLR"></a>

You can't edit the name or permissions of the `AWSServiceRoleForBCMDataExports` service-linked role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the IAM User Guide.

**To allow an IAM entity to edit the description of the `AWSServiceRoleForBCMDataExports` service-linked role**

Add the following statement to the permissions policy for the IAM entity that needs to edit the description of a service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:UpdateRoleDescription"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/bcm-data-exports.amazonaws.com/AWSServiceRoleForBCMDataExports",
    "Condition": {"StringLike": {"iam:AWSServiceName": "bcm-data-exports.amazonaws.com"}}
}
```

## Deleting the Data Exports service-linked role
<a name="data-exports-delete-SLR"></a>

If you no longer need to use Data Exports, we recommend that you delete the `AWSServiceRoleForBCMDataExports` service-linked role. That way, you don't have an unused entity that isn't actively monitored or maintained. However, before you can manually delete the service-linked role, you must first delete any Data Exports that require the service-linked role.

**To delete an export**

For information about deleting an export, see [Editing and deleting exports](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-edit-delete.html).

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS Command Line Interface (AWS CLI), or the AWS API to delete the `AWSServiceRoleForBCMDataExports` service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for Data Exports service-linked roles
<a name="data-exports-SLR-regions"></a>

Data Exports supports using service-linked roles in all of the AWS Regions where Data Exports is available. For more information, see AWS service endpoints.