# Actions, resources, and condition keys for AWS Marketplace Reporting

AWS Marketplace Reporting (service prefix: `aws-marketplace`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../marketplace/latest/buyerguide/procurement-insights.md "../../../marketplace/latest/buyerguide/procurement-insights.md").
- View a list of the [API operations available for
  this service](../../../marketplace/latest/APIReference/reporting-apis.md "../../../marketplace/latest/APIReference/reporting-apis.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../marketplace/latest/APIReference/permissions.md "../../../marketplace/latest/APIReference/permissions.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json "https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json") for this service.

###### Topics

- [API operations defined by AWS Marketplace Reporting](#list_marketplace-reporting-operations "#list_marketplace-reporting-operations")
- [Actions defined by AWS Marketplace Reporting](#list_marketplace-reporting-actions-as-permissions "#list_marketplace-reporting-actions-as-permissions")
- [Resource types defined by AWS Marketplace Reporting](#list_marketplace-reporting-resources-for-iam-policies "#list_marketplace-reporting-resources-for-iam-policies")
- [Condition keys for AWS Marketplace Reporting](#list_marketplace-reporting-policy-keys "#list_marketplace-reporting-policy-keys")

## API operations defined by AWS Marketplace Reporting

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_marketplace-reporting-actions-as-permissions "#list_marketplace-reporting-actions-as-permissions").

| Operation         | IAM action                                                                                                                                       | Condition key | Possible value(s) | Access level |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| GetBuyerDashboard | [aws-marketplace:GetBuyerDashboard](#list_marketplace-reporting-action-GetBuyerDashboard "#list_marketplace-reporting-action-GetBuyerDashboard") |               |                   | Read         |

## Actions defined by AWS Marketplace Reporting

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                | Description                                                                              | Resource types (\*required)                                                                                    | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| [GetBuyerDashboard](../../../marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.md "../../../marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.md") | Grants permission to view a dashboard that shows a buyer's AWS Marketplace purchase data | [Dashboard\*](#list_marketplace-reporting-resource-Dashboard "#list_marketplace-reporting-resource-Dashboard") |                | Read         |

## Resource types defined by AWS Marketplace Reporting

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                                                                                                                                                                 | ARN                                                                                                           | Condition keys |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------- |
| [Dashboard](../../../marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.md#API_marketplace-reporting_GetBuyerDashboard_RequestBody "../../../marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.md#API_marketplace-reporting_GetBuyerDashboard_RequestBody") | arn:${Partition}:aws-marketplace::${Account}:${Catalog}/ReportingData/${FactTable}/Dashboard/${DashboardName} |                |

## Condition keys for AWS Marketplace Reporting

AWS Marketplace Reporting has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
