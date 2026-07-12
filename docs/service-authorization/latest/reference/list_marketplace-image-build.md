# Actions, resources, and condition keys for AWS Marketplace Image Building Service

AWS Marketplace Image Building Service (service prefix: `aws-marketplace`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../marketplace/latest/buyerguide/buyer-private-image-build.md "../../../marketplace/latest/buyerguide/buyer-private-image-build.md").
- View a list of the [API operations available for
  this service](../../../marketplace/latest/buyerguide/buyer-private-image-build.md "../../../marketplace/latest/buyerguide/buyer-private-image-build.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../marketplace/latest/buyerguide/completing-prerequisite-steps.md "../../../marketplace/latest/buyerguide/completing-prerequisite-steps.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json "https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json") for this service.

###### Topics

- [Actions defined by AWS Marketplace Image Building Service](#list_marketplace-image-build-actions-as-permissions "#list_marketplace-image-build-actions-as-permissions")
- [Permission-only actions for AWS Marketplace Image Building Service](#list_marketplace-image-build-permission-only-actions "#list_marketplace-image-build-permission-only-actions")
- [Resource types defined by AWS Marketplace Image Building Service](#list_marketplace-image-build-resources-for-iam-policies "#list_marketplace-image-build-resources-for-iam-policies")
- [Condition keys for AWS Marketplace Image Building Service](#list_marketplace-image-build-policy-keys "#list_marketplace-image-build-policy-keys")

## Actions defined by AWS Marketplace Image Building Service

AWS Marketplace Image Building Service has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Marketplace Image Building Service

The following actions are defined by AWS Marketplace Image Building Service but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                             | Description                                     | Resource types (\*required) | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | --------------------------- | -------------- | ------------ |
| [DescribeBuilds](../../../marketplace/latest/buyerguide/api-reference.md "../../../marketplace/latest/buyerguide/api-reference.md") | Describes Image Builds identified by a build Id |                             |                | Read         |
| [ListBuilds](../../../marketplace/latest/buyerguide/api-reference.md "../../../marketplace/latest/buyerguide/api-reference.md")     | Lists Image Builds.                             |                             |                | Read         |
| [StartBuild](../../../marketplace/latest/buyerguide/api-reference.md "../../../marketplace/latest/buyerguide/api-reference.md")     | Starts an Image Build                           |                             |                | Write        |

## Resource types defined by AWS Marketplace Image Building Service

AWS Marketplace Image Building Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace Image Building Service

AWS Marketplace Image Building Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
