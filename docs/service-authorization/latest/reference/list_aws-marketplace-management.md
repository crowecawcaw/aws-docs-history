# Actions, resources, and condition keys for AWS Marketplace Management Portal

AWS Marketplace Management Portal (service prefix: `aws-marketplace-management`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../marketplace/latest/userguide/marketplace-management-portal-user-access.md "../../../marketplace/latest/userguide/marketplace-management-portal-user-access.md").
- View a list of the [API operations available for
  this service](../../../marketplace/latest/userguide.md "../../../marketplace/latest/userguide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../marketplace/latest/userguide/marketplace-management-portal-user-access.md "../../../marketplace/latest/userguide/marketplace-management-portal-user-access.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace-management/aws-marketplace-management.json "https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace-management/aws-marketplace-management.json") for this service.

###### Topics

- [Actions defined by AWS Marketplace Management Portal](#list_aws-marketplace-management-actions-as-permissions "#list_aws-marketplace-management-actions-as-permissions")
- [Permission-only actions for AWS Marketplace Management Portal](#list_aws-marketplace-management-permission-only-actions "#list_aws-marketplace-management-permission-only-actions")
- [Resource types defined by AWS Marketplace Management Portal](#list_aws-marketplace-management-resources-for-iam-policies "#list_aws-marketplace-management-resources-for-iam-policies")
- [Condition keys for AWS Marketplace Management Portal](#list_aws-marketplace-management-policy-keys "#list_aws-marketplace-management-policy-keys")

## Actions defined by AWS Marketplace Management Portal

AWS Marketplace Management Portal has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Marketplace Management Portal

The following actions are defined by AWS Marketplace Management Portal but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                                                                                        | Description                                                                                         | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetAdditionalSellerNotificationRecipients](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions") | Grants permission to view additional seller notification recipients                                 |                             |                | Read         |
| [GetBankAccountVerificationDetails](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")         | Grants permission to view bank account verification status                                          |                             |                | Read         |
| [GetSecondaryUserVerificationDetails](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")       | Grants permission to view secondary user account verification status                                |                             |                | Read         |
| [GetSellerVerificationDetails](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")              | Grants permission to view account verification status                                               |                             |                | Read         |
| [PutAdditionalSellerNotificationRecipients](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions") | Grants permission to update additional seller notification recipients                               |                             |                | Write        |
| [PutBankAccountVerificationDetails](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")         | Grants permission to update bank account verification status                                        |                             |                | Write        |
| [PutSecondaryUserVerificationDetails](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")       | Grants permission to update secondary user account verification status                              |                             |                | Write        |
| [PutSellerVerificationDetails](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")              | Grants permission to update account verification status                                             |                             |                | Write        |
| [uploadFiles](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")                               | Allows access to the File Upload page inside the AWS Marketplace Management Portal                  |                             |                | Write        |
| [viewMarketing](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")                             | Allows access to the Marketing page inside the AWS Marketplace Management Portal                    |                             |                | List         |
| [viewReports](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")                               | Allows access to the Reports page inside the AWS Marketplace Management Portal                      |                             |                | List         |
| [viewSettings](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")                              | Allows access to the Settings page inside the AWS Marketplace Management Portal                     |                             |                | List         |
| [viewSupport](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions")                               | Allows access to the Customer Support Eligibility page inside the AWS Marketplace Management Portal |                             |                | List         |

## Resource types defined by AWS Marketplace Management Portal

AWS Marketplace Management Portal does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace Management Portal

AWS Marketplace Management Portal has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
