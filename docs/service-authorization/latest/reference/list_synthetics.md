

# Actions, resources, and condition keys for Amazon CloudWatch Synthetics
<a name="list_synthetics"></a>

Amazon CloudWatch Synthetics (service prefix: `synthetics`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/synthetics/synthetics.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudWatch Synthetics](#list_synthetics-operations)
+ [Actions defined by Amazon CloudWatch Synthetics](#list_synthetics-actions-as-permissions)
+ [Resource types defined by Amazon CloudWatch Synthetics](#list_synthetics-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Synthetics](#list_synthetics-policy-keys)

## API operations defined by Amazon CloudWatch Synthetics
<a name="list_synthetics-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_synthetics-actions-as-permissions).




- **   AssociateResource  **
  - **IAM action:**  [synthetics:AssociateResource](#list_synthetics-action-AssociateResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCanary  **
  - **IAM action:**  [synthetics:CreateCanary](#list_synthetics-action-CreateCanary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [synthetics:TagResource](#list_synthetics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** synthetics.amazonaws.com / **Access level:** Write

- **   CreateGroup  **
  - **IAM action:**  [synthetics:CreateGroup](#list_synthetics-action-CreateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [synthetics:TagResource](#list_synthetics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCanary  **
  - **IAM action:**  [synthetics:DeleteCanary](#list_synthetics-action-DeleteCanary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGroup  **
  - **IAM action:**  [synthetics:DeleteGroup](#list_synthetics-action-DeleteGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCanaries  **
  - **IAM action:**  [synthetics:DescribeCanaries](#list_synthetics-action-DescribeCanaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCanariesLastRun  **
  - **IAM action:**  [synthetics:DescribeCanariesLastRun](#list_synthetics-action-DescribeCanariesLastRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRuntimeVersions  **
  - **IAM action:**  [synthetics:DescribeRuntimeVersions](#list_synthetics-action-DescribeRuntimeVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateResource  **
  - **IAM action:**  [synthetics:DisassociateResource](#list_synthetics-action-DisassociateResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCanary  **
  - **IAM action:**  [synthetics:GetCanary](#list_synthetics-action-GetCanary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCanaryRuns  **
  - **IAM action:**  [synthetics:GetCanaryRuns](#list_synthetics-action-GetCanaryRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroup  **
  - **IAM action:**  [synthetics:GetGroup](#list_synthetics-action-GetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssociatedGroups  **
  - **IAM action:**  [synthetics:ListAssociatedGroups](#list_synthetics-action-ListAssociatedGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupResources  **
  - **IAM action:**  [synthetics:ListGroupResources](#list_synthetics-action-ListGroupResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroups  **
  - **IAM action:**  [synthetics:ListGroups](#list_synthetics-action-ListGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [synthetics:ListTagsForResource](#list_synthetics-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartCanary  **
  - **IAM action:**  [synthetics:StartCanary](#list_synthetics-action-StartCanary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCanaryDryRun  **
  - **IAM action:**  [synthetics:StartCanaryDryRun](#list_synthetics-action-StartCanaryDryRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** synthetics.amazonaws.com / **Access level:** Write

- **   StopCanary  **
  - **IAM action:**  [synthetics:StopCanary](#list_synthetics-action-StopCanary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [synthetics:TagResource](#list_synthetics-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [synthetics:UntagResource](#list_synthetics-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCanary  **
  - **IAM action:**  [synthetics:UpdateCanary](#list_synthetics-action-UpdateCanary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** synthetics.amazonaws.com / **Access level:** Write



## Actions defined by Amazon CloudWatch Synthetics
<a name="list_synthetics-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_AssociateResource.html)  **
  - **Description:** Grants permission to associate a resource with a group
  - **Resource types (\*required):** [group\*](#list_synthetics-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html)  **
  - **Description:** Grants permission to create a canary
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_synthetics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateGroup.html)  **
  - **Description:** Grants permission to create a group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_synthetics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html)  **
  - **Description:** Grants permission to delete a canary. Amazon Synthetics deletes all the resources except for the Lambda function and the CloudWatch Alarms if you created one
  - **Resource types (\*required):** [canary\*](#list_synthetics-resource-canary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteGroup.html)  **
  - **Description:** Grants permission to delete a group
  - **Resource types (\*required):** [group\*](#list_synthetics-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html)  **
  - **Description:** Grants permission to list information of all canaries
  - **Resource types (\*required):** 
  - **Condition keys:** [synthetics:Names](#list_synthetics-synthetics_Names)
  - **Access level:** Read

- **   [DescribeCanariesLastRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanariesLastRun.html)  **
  - **Description:** Grants permission to list information about the last test run associated with all canaries
  - **Resource types (\*required):** 
  - **Condition keys:** [synthetics:Names](#list_synthetics-synthetics_Names)
  - **Access level:** Read

- **   [DescribeRuntimeVersions](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeRuntimeVersions.html)  **
  - **Description:** Grants permission to list information about Synthetics canary runtime versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DisassociateResource.html)  **
  - **Description:** Grants permission to disassociate a resource from a group
  - **Resource types (\*required):** [group\*](#list_synthetics-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [GetCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html)  **
  - **Description:** Grants permission to view the details of a canary
  - **Resource types (\*required):** [canary\*](#list_synthetics-resource-canary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Read

- **   [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html)  **
  - **Description:** Grants permission to list information about all the test runs associated with a canary
  - **Resource types (\*required):** [canary\*](#list_synthetics-resource-canary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Read

- **   [GetGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetGroup.html)  **
  - **Description:** Grants permission to view the details of a group
  - **Resource types (\*required):** [group\*](#list_synthetics-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Read

- **   [ListAssociatedGroups](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListAssociatedGroups.html)  **
  - **Description:** Grants permission to list information about the associated groups of a canary
  - **Resource types (\*required):** [canary\*](#list_synthetics-resource-canary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** List

- **   [ListGroupResources](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroupResources.html)  **
  - **Description:** Grants permission to list information about canaries in a group
  - **Resource types (\*required):** [group\*](#list_synthetics-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroups.html)  **
  - **Description:** Grants permission to list information of all groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags and values associated with a resource
  - **Resource types (\*required):** [canary](#list_synthetics-resource-canary) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [group](#list_synthetics-resource-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanary.html)  **
  - **Description:** Grants permission to start a canary, so that Amazon CloudWatch Synthetics starts monitoring a website
  - **Resource types (\*required):** [canary\*](#list_synthetics-resource-canary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [StartCanaryDryRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.html)  **
  - **Description:** Grants permission to start a canary dry run, so that Amazon CloudWatch Synthetics can execute a test execution of a canary with provided parameters
  - **Resource types (\*required):** [canary\*](#list_synthetics-resource-canary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [StopCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StopCanary.html)  **
  - **Description:** Grants permission to stop a canary
  - **Resource types (\*required):** [canary\*](#list_synthetics-resource-canary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a resource
  - **Resource types (\*required):** [canary](#list_synthetics-resource-canary) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_synthetics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Resource types (\*required):** [group](#list_synthetics-resource-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_synthetics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a resource
  - **Resource types (\*required):** [canary](#list_synthetics-resource-canary) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Resource types (\*required):** [group](#list_synthetics-resource-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html)  **
  - **Description:** Grants permission to update a canary
  - **Resource types (\*required):** [canary\*](#list_synthetics-resource-canary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_synthetics-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by Amazon CloudWatch Synthetics
<a name="list_synthetics-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)  | arn:${Partition}:synthetics:${Region}:${Account}:canary:${CanaryName} | [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_) | 
|  [group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Groups.html)  | arn:${Partition}:synthetics:${Region}:${Account}:group:${GroupId} | [aws:ResourceTag/${TagKey}](#list_synthetics-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Synthetics
<a name="list_synthetics-policy-keys"></a>

Amazon CloudWatch Synthetics defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 
|   [synthetics:Names](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html)  | Filters access based on the name of the canary | ArrayOfString | 