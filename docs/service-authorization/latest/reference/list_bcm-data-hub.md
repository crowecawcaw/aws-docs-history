

# Actions, resources, and condition keys for AWS Billing and Cost Management Data Hub

AWS Billing and Cost Management Data Hub (service prefix: `bcm-data-hub`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-hub.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/bcm-data-hub/bcm-data-hub.json) for this service.

**Topics**
+ [Actions defined by AWS Billing and Cost Management Data Hub](#list_bcm-data-hub-actions-as-permissions)
+ [Resource types defined by AWS Billing and Cost Management Data Hub](#list_bcm-data-hub-resources-for-iam-policies)
+ [Condition keys for AWS Billing and Cost Management Data Hub](#list_bcm-data-hub-policy-keys)

## Actions defined by AWS Billing and Cost Management Data Hub
<a name="list_bcm-data-hub-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelQueryExecution](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to cancel a query execution
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataset](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to create a dataset
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bcm-data-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-data-hub-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDataset](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to get a dataset
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDatasetSchema](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to get a dataset schema
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQueryExecution](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to get a query execution
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryExecutionResults](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to get query execution results
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDatasets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to list datasets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListQueryExecutions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to list query executions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartQueryExecution](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to start a query execution
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bcm-data-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-data-hub-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-data-hub-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDataset](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html#sec-policies)  **
  - **Description:** Grants permission to update a dataset
  - **Resource types (\*required):** [dataset\*](#list_bcm-data-hub-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Billing and Cost Management Data Hub
<a name="list_bcm-data-hub-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [dataset](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/what-is-concepts.html)  | arn:${Partition}:bcm-data-hub:${Region}:${Account}:dataset/${Identifier} | [aws:ResourceTag/${TagKey}](#list_bcm-data-hub-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Billing and Cost Management Data Hub
<a name="list_bcm-data-hub-policy-keys"></a>

AWS Billing and Cost Management Data Hub defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 