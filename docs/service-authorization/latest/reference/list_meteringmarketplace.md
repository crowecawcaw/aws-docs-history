# Actions, resources, and condition keys for AWS Marketplace Metering Service

AWS Marketplace Metering Service (service prefix: `aws-marketplace`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../marketplace/latest/APIReference.md "../../../marketplace/latest/APIReference.md").
- View a list of the [API operations available for
  this service](../../../marketplace/latest/APIReference.md "../../../marketplace/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../marketplace/latest/userguide/iam-user-policy-for-aws-marketplace-actions.md "../../../marketplace/latest/userguide/iam-user-policy-for-aws-marketplace-actions.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json "https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json") for this service.

###### Topics

- [API operations defined by AWS Marketplace Metering Service](#list_meteringmarketplace-operations "#list_meteringmarketplace-operations")
- [Actions defined by AWS Marketplace Metering Service](#list_meteringmarketplace-actions-as-permissions "#list_meteringmarketplace-actions-as-permissions")
- [Resource types defined by AWS Marketplace Metering Service](#list_meteringmarketplace-resources-for-iam-policies "#list_meteringmarketplace-resources-for-iam-policies")
- [Condition keys for AWS Marketplace Metering Service](#list_meteringmarketplace-policy-keys "#list_meteringmarketplace-policy-keys")

## API operations defined by AWS Marketplace Metering Service

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_meteringmarketplace-actions-as-permissions "#list_meteringmarketplace-actions-as-permissions").

| Operation       | IAM action                                                                                                                             | Condition key | Possible value(s) | Access level |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| BatchMeterUsage | [aws-marketplace:BatchMeterUsage](#list_meteringmarketplace-action-BatchMeterUsage "#list_meteringmarketplace-action-BatchMeterUsage") |               |                   | Write        |
| MeterUsage      | [aws-marketplace:MeterUsage](#list_meteringmarketplace-action-MeterUsage "#list_meteringmarketplace-action-MeterUsage")                |               |                   | Write        |
| RegisterUsage   | [aws-marketplace:RegisterUsage](#list_meteringmarketplace-action-RegisterUsage "#list_meteringmarketplace-action-RegisterUsage")       |               |                   | Write        |
| ResolveCustomer | [aws-marketplace:ResolveCustomer](#list_meteringmarketplace-action-ResolveCustomer "#list_meteringmarketplace-action-ResolveCustomer") |               |                   | Write        |

## Actions defined by AWS Marketplace Metering Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                 | Resource types (\*required) | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [BatchMeterUsage](../../../marketplace/latest/APIReference/API_marketplace-metering_BatchMeterUsage.md "../../../marketplace/latest/APIReference/API_marketplace-metering_BatchMeterUsage.md") | Grants permission to post metering records for a set of customers for SaaS applications                                                                                                                                                                     |                             |                | Write        |
| [MeterUsage](../../../marketplace/latest/APIReference/API_marketplace-metering_MeterUsage.md "../../../marketplace/latest/APIReference/API_marketplace-metering_MeterUsage.md")                | Grants permission to emit metering records                                                                                                                                                                                                                  |                             |                | Write        |
| [RegisterUsage](../../../marketplace/latest/APIReference/API_marketplace-metering_RegisterUsage.md "../../../marketplace/latest/APIReference/API_marketplace-metering_RegisterUsage.md")       | Grants permission to to verify that the customer running your paid software is subscribed to your product on AWS Marketplace, enabling you to guard against unauthorized use. Meters software use per ECS task, per hour, with usage prorated to the second |                             |                | Write        |
| [ResolveCustomer](../../../marketplace/latest/APIReference/API_marketplace-metering_ResolveCustomer.md "../../../marketplace/latest/APIReference/API_marketplace-metering_ResolveCustomer.md") | Grants permission to resolve a registration token to obtain a CustomerIdentifier and product code                                                                                                                                                           |                             |                | Write        |

## Resource types defined by AWS Marketplace Metering Service

AWS Marketplace Metering Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace Metering Service

AWS Marketplace Metering Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
