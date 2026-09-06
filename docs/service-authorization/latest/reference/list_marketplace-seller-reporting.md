

# Actions, resources, and condition keys for AWS Marketplace Seller Reporting
<a name="list_marketplace-seller-reporting"></a>

AWS Marketplace Seller Reporting (service prefix: `aws-marketplace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace/latest/userguide/reports-and-data-feed.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace/latest/userguide/reports-and-data-feed.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace/latest/userguide/reports-and-data-feed.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json) for this service.

**Topics**
+ [Actions defined by AWS Marketplace Seller Reporting](#list_marketplace-seller-reporting-actions-as-permissions)
+ [Resource types defined by AWS Marketplace Seller Reporting](#list_marketplace-seller-reporting-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace Seller Reporting](#list_marketplace-seller-reporting-policy-keys)

## Actions defined by AWS Marketplace Seller Reporting
<a name="list_marketplace-seller-reporting-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetSellerDashboard](https://docs.aws.amazon.com/marketplace/latest/userguide/dashboards.html#reports-accessing)  **
  - **Description:** Grants permission to view a seller dashboard
  - **Resource types (\*required):** [SellerDashboard\*](#list_marketplace-seller-reporting-resource-SellerDashboard)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by AWS Marketplace Seller Reporting
<a name="list_marketplace-seller-reporting-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [SellerDashboard](https://docs.aws.amazon.com/marketplace/latest/userguide/dashboards.html#reports-accessing)  | arn:${Partition}:aws-marketplace::${Account}:${Catalog}/ReportingData/${FactTable}/Dashboard/${DashboardName} |   | 

## Condition keys for AWS Marketplace Seller Reporting
<a name="list_marketplace-seller-reporting-policy-keys"></a>

AWS Marketplace Seller Reporting has no service-specific condition keys that can be used in the `Condition` element of policy statements.