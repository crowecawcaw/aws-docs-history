# Actions, resources, and condition keys for AWS Marketplace Private Marketplace

AWS Marketplace Private Marketplace (service prefix: `aws-marketplace`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../marketplace/latest/buyerguide.md "../../../marketplace/latest/buyerguide.md").
- View a list of the [API operations available for
  this service](../../../marketplace/latest/buyerguide.md "../../../marketplace/latest/buyerguide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../marketplace/latest/buyerguide/private-marketplace.md "../../../marketplace/latest/buyerguide/private-marketplace.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json "https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json") for this service.

###### Topics

- [Actions defined by AWS Marketplace Private Marketplace](#list_private-marketplace-actions-as-permissions "#list_private-marketplace-actions-as-permissions")
- [Permission-only actions for AWS Marketplace Private Marketplace](#list_private-marketplace-permission-only-actions "#list_private-marketplace-permission-only-actions")
- [Resource types defined by AWS Marketplace Private Marketplace](#list_private-marketplace-resources-for-iam-policies "#list_private-marketplace-resources-for-iam-policies")
- [Condition keys for AWS Marketplace Private Marketplace](#list_private-marketplace-policy-keys "#list_private-marketplace-policy-keys")

## Actions defined by AWS Marketplace Private Marketplace

AWS Marketplace Private Marketplace has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Marketplace Private Marketplace

The following actions are defined by AWS Marketplace Private Marketplace but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                       | Resource types (\*required) | Condition keys | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [AssociateProductsWithPrivateMarketplace](../../../marketplace/latest/buyerguide/private-marketplace.md "../../../marketplace/latest/buyerguide/private-marketplace.md")    | Grants permission to approve a request for a product to be associated with the Private Marketplace. This action can be performed by any account in an AWS Organization, provided the user has permissions to do so, and the Organization's Service Control Policies allow it                      |                             |                | Write        |
| [CreatePrivateMarketplaceRequests](../../../marketplace/latest/buyerguide/private-marketplace.md "../../../marketplace/latest/buyerguide/private-marketplace.md")           | Grants permission to create a new request for a product or products to be associated with the Private Marketplace. This action can be performed by any account in an in an AWS Organization, provided the user has permissions to do so, and the Organization's Service Control Policies allow it |                             |                | Write        |
| [DescribePrivateMarketplaceRequests](../../../marketplace/latest/buyerguide/private-marketplace.md "../../../marketplace/latest/buyerguide/private-marketplace.md")         | Grants permission to describe requests and associated products in the Private Marketplace. This action can be performed by any account in an AWS Organization, provided the user has permissions to do so, and the Organization's Service Control Policies allow it                               |                             |                | List         |
| [DisassociateProductsFromPrivateMarketplace](../../../marketplace/latest/buyerguide/private-marketplace.md "../../../marketplace/latest/buyerguide/private-marketplace.md") | Grants permission to decline a request for a product to be associated with the Private Marketplace. This action can be performed by any account in an AWS Organization, provided the user has permissions to do so, and the Organization's Service Control Policies allow it                      |                             |                | Write        |
| [ListPrivateMarketplaceRequests](../../../marketplace/latest/buyerguide/private-marketplace.md "../../../marketplace/latest/buyerguide/private-marketplace.md")             | Grants permission to get a queryable list for requests and associated products in the Private Marketplace. This action can be performed by any account in an AWS Organization, provided the user has permissions to do so, and the Organization's Service Control Policies allow it               |                             |                | List         |

## Resource types defined by AWS Marketplace Private Marketplace

AWS Marketplace Private Marketplace does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace Private Marketplace

AWS Marketplace Private Marketplace has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
