# Actions, resources, and condition keys for AWS Marketplace Procurement Systems Integration

AWS Marketplace Procurement Systems Integration (service prefix: `aws-marketplace`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../marketplace/latest/buyerguide.md "../../../marketplace/latest/buyerguide.md").
- View a list of the [API operations available for
  this service](../../../marketplace/latest/buyerguide.md "../../../marketplace/latest/buyerguide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../marketplace/latest/buyerguide/procurement-systems-integration.md "../../../marketplace/latest/buyerguide/procurement-systems-integration.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json "https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json") for this service.

###### Topics

- [Actions defined by AWS Marketplace Procurement Systems Integration](#list_marketplace-procurement-integration-actions-as-permissions "#list_marketplace-procurement-integration-actions-as-permissions")
- [Permission-only actions for AWS Marketplace Procurement Systems Integration](#list_marketplace-procurement-integration-permission-only-actions "#list_marketplace-procurement-integration-permission-only-actions")
- [Resource types defined by AWS Marketplace Procurement Systems Integration](#list_marketplace-procurement-integration-resources-for-iam-policies "#list_marketplace-procurement-integration-resources-for-iam-policies")
- [Condition keys for AWS Marketplace Procurement Systems Integration](#list_marketplace-procurement-integration-policy-keys "#list_marketplace-procurement-integration-policy-keys")

## Actions defined by AWS Marketplace Procurement Systems Integration

AWS Marketplace Procurement Systems Integration has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Marketplace Procurement Systems Integration

The following actions are defined by AWS Marketplace Procurement Systems Integration but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                            | Resource types (\*required) | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [DescribeProcurementSystemConfiguration](../../../marketplace/latest/buyerguide/procurement-systems-integration.md "../../../marketplace/latest/buyerguide/procurement-systems-integration.md") | Grants permission to describe the Procurement System integration configuration (e.g. Coupa) for the individual account, or for the entire AWS Organization if one exists. This action can only be performed by the master account if using an AWS Organization         |                             |                | Read         |
| [PutProcurementSystemConfiguration](../../../marketplace/latest/buyerguide/procurement-systems-integration.md "../../../marketplace/latest/buyerguide/procurement-systems-integration.md")      | Grants permission to create or update the Procurement System integration configuration (e.g. Coupa) for the individual account, or for the entire AWS Organization if one exists. This action can only be performed by the master account if using an AWS Organization |                             |                | Write        |

## Resource types defined by AWS Marketplace Procurement Systems Integration

AWS Marketplace Procurement Systems Integration does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace Procurement Systems Integration

AWS Marketplace Procurement Systems Integration has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
