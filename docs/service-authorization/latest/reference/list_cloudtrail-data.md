

# Actions, resources, and condition keys for AWS CloudTrail Data
<a name="list_cloudtrail-data"></a>

AWS CloudTrail Data (service prefix: `cloudtrail-data`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudtrail-data/cloudtrail-data.json) for this service.

**Topics**
+ [API operations defined by AWS CloudTrail Data](#list_cloudtrail-data-operations)
+ [Actions defined by AWS CloudTrail Data](#list_cloudtrail-data-actions-as-permissions)
+ [Resource types defined by AWS CloudTrail Data](#list_cloudtrail-data-resources-for-iam-policies)
+ [Condition keys for AWS CloudTrail Data](#list_cloudtrail-data-policy-keys)

## API operations defined by AWS CloudTrail Data
<a name="list_cloudtrail-data-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudtrail-data-actions-as-permissions).




- **   PutAuditEvents  **
  - **IAM action:**  [cloudtrail-data:PutAuditEvents](#list_cloudtrail-data-action-PutAuditEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS CloudTrail Data
<a name="list_cloudtrail-data-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [PutAuditEvents](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html)  **
  - **Description:** Grants permission to ingest your application events into CloudTrail Lake
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-data-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-data-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS CloudTrail Data
<a name="list_cloudtrail-data-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-channels)  | arn:${Partition}:cloudtrail:${Region}:${Account}:channel/${ChannelId} | [aws:ResourceTag/${TagKey}](#list_cloudtrail-data-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CloudTrail Data
<a name="list_cloudtrail-data-policy-keys"></a>

AWS CloudTrail Data defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 