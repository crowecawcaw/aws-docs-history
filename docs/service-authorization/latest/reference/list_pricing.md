

# Actions, resources, and condition keys for AWS Price List
<a name="list_pricing"></a>

AWS Price List (service prefix: `pricing`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/using-pelong.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Price_List_Service.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/pricing/pricing.json) for this service.

**Topics**
+ [API operations defined by AWS Price List](#list_pricing-operations)
+ [Actions defined by AWS Price List](#list_pricing-actions-as-permissions)
+ [Resource types defined by AWS Price List](#list_pricing-resources-for-iam-policies)
+ [Condition keys for AWS Price List](#list_pricing-policy-keys)

## API operations defined by AWS Price List
<a name="list_pricing-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pricing-actions-as-permissions).




- **   DescribeServices  **
  - **IAM action:**  [pricing:DescribeServices](#list_pricing-action-DescribeServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAttributeValues  **
  - **IAM action:**  [pricing:GetAttributeValues](#list_pricing-action-GetAttributeValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPriceListFileUrl  **
  - **IAM action:**  [pricing:GetPriceListFileUrl](#list_pricing-action-GetPriceListFileUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProducts  **
  - **IAM action:**  [pricing:GetProducts](#list_pricing-action-GetProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPriceLists  **
  - **IAM action:**  [pricing:ListPriceLists](#list_pricing-action-ListPriceLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Price List
<a name="list_pricing-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DescribeServices](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_DescribeServices.html)  | Grants permission to retrieve service details for all (paginated) services (if serviceCode is not set) or service detail for a particular service (if given serviceCode) |  |   | Read | 
|   [GetAttributeValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html)  | Grants permission to retrieve all (paginated) possible values for a given attribute |  |   | Read | 
|   [GetPriceListFileUrl](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.html)  | Grants permission to retrieve the price list file URL for the given parameters |  |   | Read | 
|   [GetProducts](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetProducts.html)  | Grants permission to retrieve all matching products with given search criteria |  |   | Read | 
|   [ListPriceLists](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html)  | Grants permission to list all (paginated) eligible price lists for the given parameters |  |   | Read | 

## Resource types defined by AWS Price List
<a name="list_pricing-resources-for-iam-policies"></a>

AWS Price List does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Price List
<a name="list_pricing-policy-keys"></a>

AWS Price List has no service-specific condition keys that can be used in the `Condition` element of policy statements.