# Actions, resources, and condition keys for AWS Sustainability

AWS Sustainability (service prefix: `sustainability`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../sustainability/latest/userguide/what-is-sustainability.md "../../../sustainability/latest/userguide/what-is-sustainability.md").
- View a list of the [API operations available for
  this service](../../../sustainability/latest/APIReference/Welcome.md "../../../sustainability/latest/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../sustainability/latest/userguide/security-iam.md "../../../sustainability/latest/userguide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/sustainability/sustainability.json "https://servicereference.us-east-1.amazonaws.com/v1/sustainability/sustainability.json") for this service.

###### Topics

- [API operations defined by AWS Sustainability](#list_sustainability-operations "#list_sustainability-operations")
- [Actions defined by AWS Sustainability](#list_sustainability-actions-as-permissions "#list_sustainability-actions-as-permissions")
- [Resource types defined by AWS Sustainability](#list_sustainability-resources-for-iam-policies "#list_sustainability-resources-for-iam-policies")
- [Condition keys for AWS Sustainability](#list_sustainability-policy-keys "#list_sustainability-policy-keys")

## API operations defined by AWS Sustainability

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sustainability-actions-as-permissions "#list_sustainability-actions-as-permissions").

| Operation                                  | IAM action                                                                                                                                                                                                   | Condition key | Possible value(s) | Access level |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| GetEstimatedCarbonEmissions                | [sustainability:GetEstimatedCarbonEmissions](#list_sustainability-action-GetEstimatedCarbonEmissions "#list_sustainability-action-GetEstimatedCarbonEmissions")                                              |               |                   | Read         |
| GetEstimatedCarbonEmissionsDimensionValues | [sustainability:GetEstimatedCarbonEmissionsDimensionValues](#list_sustainability-action-GetEstimatedCarbonEmissionsDimensionValues "#list_sustainability-action-GetEstimatedCarbonEmissionsDimensionValues") |               |                   | Read         |

## Actions defined by AWS Sustainability

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                                                     | Description                                                                                                    | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetCarbonFootprintSummary](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                                                    | Grants permission to view the carbon footprint tool                                                            |                             |                | Read         |
| [GetEstimatedCarbonEmissions](../../../sustainability/latest/APIReference/API_GetEstimatedCarbonEmissions.md "../../../sustainability/latest/APIReference/API_GetEstimatedCarbonEmissions.md")                                              | Grants permission to view estimated carbon emission values based on customer grouping and filtering parameters |                             |                | Read         |
| [GetEstimatedCarbonEmissionsDimensionValues](../../../sustainability/latest/APIReference/API_GetEstimatedCarbonEmissionsDimensionValues.md "../../../sustainability/latest/APIReference/API_GetEstimatedCarbonEmissionsDimensionValues.md") | Grants permission to view the possible dimension values available for the estimated carbon emission values     |                             |                | Read         |

## Resource types defined by AWS Sustainability

AWS Sustainability does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Sustainability

AWS Sustainability has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
