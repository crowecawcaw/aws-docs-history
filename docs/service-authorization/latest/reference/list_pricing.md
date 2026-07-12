# Actions, resources, and condition keys for AWS Price List

AWS Price List (service prefix: `pricing`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awsaccountbilling/latest/aboutv2/using-pelong.md "../../../awsaccountbilling/latest/aboutv2/using-pelong.md").
- View a list of the [API operations available for
  this service](../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Price_List_Service.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Price_List_Service.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/pricing/pricing.json "https://servicereference.us-east-1.amazonaws.com/v1/pricing/pricing.json") for this service.

###### Topics

- [API operations defined by AWS Price List](#list_pricing-operations "#list_pricing-operations")
- [Actions defined by AWS Price List](#list_pricing-actions-as-permissions "#list_pricing-actions-as-permissions")
- [Resource types defined by AWS Price List](#list_pricing-resources-for-iam-policies "#list_pricing-resources-for-iam-policies")
- [Condition keys for AWS Price List](#list_pricing-policy-keys "#list_pricing-policy-keys")

## API operations defined by AWS Price List

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pricing-actions-as-permissions "#list_pricing-actions-as-permissions").

| Operation           | IAM action                                                                                                         | Condition key | Possible value(s) | Access level |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| DescribeServices    | [pricing:DescribeServices](#list_pricing-action-DescribeServices "#list_pricing-action-DescribeServices")          |               |                   | Read         |
| GetAttributeValues  | [pricing:GetAttributeValues](#list_pricing-action-GetAttributeValues "#list_pricing-action-GetAttributeValues")    |               |                   | Read         |
| GetPriceListFileUrl | [pricing:GetPriceListFileUrl](#list_pricing-action-GetPriceListFileUrl "#list_pricing-action-GetPriceListFileUrl") |               |                   | Read         |
| GetProducts         | [pricing:GetProducts](#list_pricing-action-GetProducts "#list_pricing-action-GetProducts")                         |               |                   | Read         |
| ListPriceLists      | [pricing:ListPriceLists](#list_pricing-action-ListPriceLists "#list_pricing-action-ListPriceLists")                |               |                   | Read         |

## Actions defined by AWS Price List

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                          | Description                                                                                                                                                              | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | -------------- | ------------ |
| [DescribeServices](../../../aws-cost-management/latest/APIReference/API_pricing_DescribeServices.md "../../../aws-cost-management/latest/APIReference/API_pricing_DescribeServices.md")          | Grants permission to retrieve service details for all (paginated) services (if serviceCode is not set) or service detail for a particular service (if given serviceCode) |                             |                | Read         |
| [GetAttributeValues](../../../aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.md "../../../aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.md")    | Grants permission to retrieve all (paginated) possible values for a given attribute                                                                                      |                             |                | Read         |
| [GetPriceListFileUrl](../../../aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.md "../../../aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.md") | Grants permission to retrieve the price list file URL for the given parameters                                                                                           |                             |                | Read         |
| [GetProducts](../../../aws-cost-management/latest/APIReference/API_pricing_GetProducts.md "../../../aws-cost-management/latest/APIReference/API_pricing_GetProducts.md")                         | Grants permission to retrieve all matching products with given search criteria                                                                                           |                             |                | Read         |
| [ListPriceLists](../../../aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.md "../../../aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.md")                | Grants permission to list all (paginated) eligible price lists for the given parameters                                                                                  |                             |                | Read         |

## Resource types defined by AWS Price List

AWS Price List does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Price List

AWS Price List has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
