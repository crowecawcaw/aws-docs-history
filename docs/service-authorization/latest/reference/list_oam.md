

# Actions, resources, and condition keys for Amazon CloudWatch Observability Access Manager
<a name="list_oam"></a>

Amazon CloudWatch Observability Access Manager (service prefix: `oam`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/OAM/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/oam/oam.json) for this service.

**Topics**
+ [Actions defined by Amazon CloudWatch Observability Access Manager](#list_oam-actions-as-permissions)
+ [Resource types defined by Amazon CloudWatch Observability Access Manager](#list_oam-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Observability Access Manager](#list_oam-policy-keys)

## Actions defined by Amazon CloudWatch Observability Access Manager
<a name="list_oam-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateLink.html)  **
  - **Description:** Grants permission to create a link between a monitoring account and a source account for cross-account monitoring
  - **Resource types (\*required):** [Sink\*](#list_oam-resource-Sink)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_oam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_oam-aws_TagKeys)<br />[oam:ResourceTypes](#list_oam-oam_ResourceTypes)
  - **Access level:** Write

- **   [CreateSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html)  **
  - **Description:** Grants permission to create a sink in an account so that it can be used as a monitoring account for cross-account monitoring
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_oam-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_oam-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteLink.html)  **
  - **Description:** Grants permission to delete a link between a monitoring account and a source account for cross-account monitoring
  - **Resource types (\*required):** [Link\*](#list_oam-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteSink.html)  **
  - **Description:** Grants permission to delete a cross-account monitoring sink in a monitoring account
  - **Resource types (\*required):** [Sink\*](#list_oam-resource-Sink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetLink.html)  **
  - **Description:** Grants permission to retrieve complete information about one cross-account monitoring link
  - **Resource types (\*required):** [Link\*](#list_oam-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSink.html)  **
  - **Description:** Grants permission to retrieve complete information about one cross-account monitoring sink
  - **Resource types (\*required):** [Sink\*](#list_oam-resource-Sink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSinkPolicy.html)  **
  - **Description:** Grants permission to retrieve information for the IAM policy for a cross-account monitoring sink
  - **Resource types (\*required):** [Sink\*](#list_oam-resource-Sink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAttachedLinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinks.html)  **
  - **Description:** Grants permission to retrieve a list of links that are linked for a cross-account monitoring sink
  - **Resource types (\*required):** [Sink\*](#list_oam-resource-Sink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListLinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html)  **
  - **Description:** Grants permission to retrieve the ARNs of cross-account monitoring links in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html)  **
  - **Description:** Grants permission to retrieve the ARNs of cross-account monitoring sinks in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [Link](#list_oam-resource-Link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Sink](#list_oam-resource-Sink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html)  **
  - **Description:** Grants permission to create or update the IAM policy for a cross-account monitoring sink
  - **Resource types (\*required):** [Sink\*](#list_oam-resource-Sink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [Link](#list_oam-resource-Link) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_oam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_oam-aws_TagKeys)
  - **Resource types (\*required):** [Sink](#list_oam-resource-Sink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_oam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_oam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [Link](#list_oam-resource-Link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_oam-aws_TagKeys)
  - **Resource types (\*required):** [Sink](#list_oam-resource-Sink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_oam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_UpdateLink.html)  **
  - **Description:** Grants permission to update an existing link between a monitoring account and a source account
  - **Resource types (\*required):** [Link\*](#list_oam-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_)<br />[oam:ResourceTypes](#list_oam-oam_ResourceTypes)
  - **Access level:** Write



## Resource types defined by Amazon CloudWatch Observability Access Manager
<a name="list_oam-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)  | arn:${Partition}:oam:${Region}:${Account}:link/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_) | 
|  [Sink](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)  | arn:${Partition}:oam:${Region}:${Account}:sink/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_oam-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Observability Access Manager
<a name="list_oam-policy-keys"></a>

Amazon CloudWatch Observability Access Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [oam:ResourceTypes](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatchobservabilityaccessmanager.html)  | Filters access by the presence of resource types in the request | ArrayOfString | 