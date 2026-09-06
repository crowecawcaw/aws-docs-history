

# Actions, resources, and condition keys for AWS Marketplace Reporting
<a name="list_marketplace-reporting"></a>

AWS Marketplace Reporting (service prefix: `aws-marketplace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace/latest/buyerguide/procurement-insights.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace/latest/APIReference/reporting-apis.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace/latest/APIReference/permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json) for this service.

**Topics**
+ [API operations defined by AWS Marketplace Reporting](#list_marketplace-reporting-operations)
+ [Actions defined by AWS Marketplace Reporting](#list_marketplace-reporting-actions-as-permissions)
+ [Resource types defined by AWS Marketplace Reporting](#list_marketplace-reporting-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace Reporting](#list_marketplace-reporting-policy-keys)

## API operations defined by AWS Marketplace Reporting
<a name="list_marketplace-reporting-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_marketplace-reporting-actions-as-permissions).




- **   GetBuyerDashboard  **
  - **IAM action:**  [aws-marketplace:GetBuyerDashboard](#list_marketplace-reporting-action-GetBuyerDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Marketplace Reporting
<a name="list_marketplace-reporting-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetBuyerDashboard](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.html)  **
  - **Description:** Grants permission to view a dashboard that shows a buyer's AWS Marketplace purchase data
  - **Resource types (\*required):** [Dashboard\*](#list_marketplace-reporting-resource-Dashboard)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by AWS Marketplace Reporting
<a name="list_marketplace-reporting-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Dashboard](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.html#API_marketplace-reporting_GetBuyerDashboard_RequestBody)  | arn:${Partition}:aws-marketplace::${Account}:${Catalog}/ReportingData/${FactTable}/Dashboard/${DashboardName} |   | 

## Condition keys for AWS Marketplace Reporting
<a name="list_marketplace-reporting-policy-keys"></a>

AWS Marketplace Reporting has no service-specific condition keys that can be used in the `Condition` element of policy statements.