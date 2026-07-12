# Actions, resources, and condition keys for AWS Billing And Cost Management Recommended Actions

AWS Billing And Cost Management Recommended Actions (service prefix: `bcm-recommended-actions`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../cost-management/latest/userguide/view-billing-dashboard.md#recommended-actions-widget "../../../cost-management/latest/userguide/view-billing-dashboard.md#recommended-actions-widget").
- View a list of the [API operations available for
  this service](../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Billing_and_Cost_Management_Recommended_Actions.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Billing_and_Cost_Management_Recommended_Actions.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../cost-management/latest/userguide/billing-permissions-ref.md#allows-recommended-actions-access "../../../cost-management/latest/userguide/billing-permissions-ref.md#allows-recommended-actions-access") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/bcm-recommended-actions/bcm-recommended-actions.json "https://servicereference.us-east-1.amazonaws.com/v1/bcm-recommended-actions/bcm-recommended-actions.json") for this service.

###### Topics

- [API operations defined by AWS Billing And Cost Management Recommended Actions](#list_bcm-recommended-actions-operations "#list_bcm-recommended-actions-operations")
- [Actions defined by AWS Billing And Cost Management Recommended Actions](#list_bcm-recommended-actions-actions-as-permissions "#list_bcm-recommended-actions-actions-as-permissions")
- [Resource types defined by AWS Billing And Cost Management Recommended Actions](#list_bcm-recommended-actions-resources-for-iam-policies "#list_bcm-recommended-actions-resources-for-iam-policies")
- [Condition keys for AWS Billing And Cost Management Recommended Actions](#list_bcm-recommended-actions-policy-keys "#list_bcm-recommended-actions-policy-keys")

## API operations defined by AWS Billing And Cost Management Recommended Actions

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_bcm-recommended-actions-actions-as-permissions "#list_bcm-recommended-actions-actions-as-permissions").

| Operation              | IAM action                                                                                                                                                                  | Condition key | Possible value(s) | Access level |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| ListRecommendedActions | [bcm-recommended-actions:ListRecommendedActions](#list_bcm-recommended-actions-action-ListRecommendedActions "#list_bcm-recommended-actions-action-ListRecommendedActions") |               |                   | List         |

## Actions defined by AWS Billing And Cost Management Recommended Actions

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                                                                                         | Description                                       | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [ListRecommendedActions](../../../aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_ListRecommendedActions.md "../../../aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_ListRecommendedActions.md") | Grants permission to list all recommended actions |                             |                | List         |

## Resource types defined by AWS Billing And Cost Management Recommended Actions

AWS Billing And Cost Management Recommended Actions does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Billing And Cost Management Recommended Actions

AWS Billing And Cost Management Recommended Actions has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
