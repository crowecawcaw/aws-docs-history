

# Actions, resources, and condition keys for AWS Marketplace Seller Reporting

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

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDataSubscription](https://docs.aws.amazon.com/marketplace/latest/userguide/data-subscriptions.html)  **
  - **Description:** Grants permission to create a data subscription that delivers a seller dataset to an S3 bucket in the caller's AWS account on a schedule
  - **Resource types (\*required):** [DataSubscription\*](#list_marketplace-seller-reporting-resource-DataSubscription)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-seller-reporting-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-seller-reporting-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-seller-reporting-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDataSubscription](https://docs.aws.amazon.com/marketplace/latest/userguide/data-subscriptions.html)  **
  - **Description:** Grants permission to delete a data subscription owned by the calling account, stopping future deliveries
  - **Resource types (\*required):** [DataSubscription\*](#list_marketplace-seller-reporting-resource-DataSubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-seller-reporting-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDataSubscription](https://docs.aws.amazon.com/marketplace/latest/userguide/data-subscriptions.html)  **
  - **Description:** Grants permission to retrieve the details and delivery progress of a data subscription owned by the calling account
  - **Resource types (\*required):** [DataSubscription\*](#list_marketplace-seller-reporting-resource-DataSubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-seller-reporting-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSellerDashboard](https://docs.aws.amazon.com/marketplace/latest/userguide/dashboards.html#reports-accessing)  **
  - **Description:** Grants permission to view a seller dashboard
  - **Resource types (\*required):** [SellerDashboard\*](#list_marketplace-seller-reporting-resource-SellerDashboard)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSellerReportingData](https://docs.aws.amazon.com/marketplace/latest/userguide/reports-and-data-feed.html)  **
  - **Description:** Grants permission to query a seller reporting dataset
  - **Resource types (\*required):** [SellerDataset\*](#list_marketplace-seller-reporting-resource-SellerDataset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDataSubscriptions](https://docs.aws.amazon.com/marketplace/latest/userguide/data-subscriptions.html)  **
  - **Description:** Grants permission to list the data subscriptions owned by the calling account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/marketplace/latest/userguide/data-subscriptions.html)  **
  - **Description:** Grants permission to list the tags on a data subscription owned by the calling account
  - **Resource types (\*required):** [DataSubscription\*](#list_marketplace-seller-reporting-resource-DataSubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-seller-reporting-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/marketplace/latest/userguide/data-subscriptions.html)  **
  - **Description:** Grants permission to add or overwrite tags on a data subscription owned by the calling account
  - **Resource types (\*required):** [DataSubscription\*](#list_marketplace-seller-reporting-resource-DataSubscription)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-seller-reporting-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-seller-reporting-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-seller-reporting-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/marketplace/latest/userguide/data-subscriptions.html)  **
  - **Description:** Grants permission to remove tags from a data subscription owned by the calling account
  - **Resource types (\*required):** [DataSubscription\*](#list_marketplace-seller-reporting-resource-DataSubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-seller-reporting-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-seller-reporting-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Marketplace Seller Reporting
<a name="list_marketplace-seller-reporting-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [DataSubscription](https://docs.aws.amazon.com/marketplace/latest/userguide/data-subscriptions.html)  | arn:${Partition}:aws-marketplace::${Account}:${Catalog}/ReportingData/${FactTable}/DataSubscription/${DataSubscriptionId} | [aws:ResourceTag/${TagKey}](#list_marketplace-seller-reporting-aws_ResourceTag___TagKey_) | 
|  [SellerDashboard](https://docs.aws.amazon.com/marketplace/latest/userguide/dashboards.html#reports-accessing)  | arn:${Partition}:aws-marketplace::${Account}:${Catalog}/ReportingData/${FactTable}/Dashboard/${DashboardName} |   | 
|  [SellerDataset](https://docs.aws.amazon.com/marketplace/latest/userguide/reports-and-data-feed.html)  | arn:${Partition}:aws-marketplace::${Account}:${Catalog}/ReportingData/${FactTable}/Dataset/${DatasetName} |   | 

## Condition keys for AWS Marketplace Seller Reporting
<a name="list_marketplace-seller-reporting-policy-keys"></a>

AWS Marketplace Seller Reporting defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 