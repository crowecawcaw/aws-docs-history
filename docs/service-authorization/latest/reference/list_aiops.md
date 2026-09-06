

# Actions, resources, and condition keys for Amazon AI Operations
<a name="list_aiops"></a>

Amazon AI Operations (service prefix: `aiops`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aiops/aiops.json) for this service.

**Topics**
+ [API operations defined by Amazon AI Operations](#list_aiops-operations)
+ [Actions defined by Amazon AI Operations](#list_aiops-actions-as-permissions)
+ [Resource types defined by Amazon AI Operations](#list_aiops-resources-for-iam-policies)
+ [Condition keys for Amazon AI Operations](#list_aiops-policy-keys)

## API operations defined by Amazon AI Operations
<a name="list_aiops-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_aiops-actions-as-permissions).




- **   CreateInvestigationGroup  **
  - **IAM action:**  [aiops:CreateInvestigationGroup](#list_aiops-action-CreateInvestigationGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aiops:TagResource](#list_aiops-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** aiops.amazonaws.com / **Access level:** Write

- **   DeleteInvestigationGroup  **
  - **IAM action:**  [aiops:DeleteInvestigationGroup](#list_aiops-action-DeleteInvestigationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInvestigationGroupPolicy  **
  - **IAM action:**  [aiops:DeleteInvestigationGroupPolicy](#list_aiops-action-DeleteInvestigationGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetInvestigationGroup  **
  - **IAM action:**  [aiops:GetInvestigationGroup](#list_aiops-action-GetInvestigationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInvestigationGroupPolicy  **
  - **IAM action:**  [aiops:GetInvestigationGroupPolicy](#list_aiops-action-GetInvestigationGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInvestigationGroups  **
  - **IAM action:**  [aiops:ListInvestigationGroups](#list_aiops-action-ListInvestigationGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [aiops:ListTagsForResource](#list_aiops-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutInvestigationGroupPolicy  **
  - **IAM action:**  [aiops:PutInvestigationGroupPolicy](#list_aiops-action-PutInvestigationGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [aiops:TagResource](#list_aiops-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [aiops:UntagResource](#list_aiops-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateInvestigationGroup  **
  - **IAM action:**  [aiops:UpdateInvestigationGroup](#list_aiops-action-UpdateInvestigationGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** aiops.amazonaws.com / **Access level:** Write



## Actions defined by Amazon AI Operations
<a name="list_aiops-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateInvestigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_CreateInvestigation.html)  **
  - **Description:** Grants permission to create a new investigation in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInvestigationEvent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_CreateInvestigationEvent.html)  **
  - **Description:** Grants permission to create a new investigation event in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInvestigationGroup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_CreateInvestigationGroup.html)  **
  - **Description:** Grants permission to create a new investigation group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_aiops-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_aiops-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInvestigationResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_CreateInvestigationResource.html)  **
  - **Description:** Grants permission to create an investigation resource in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_CreateReport.html)  **
  - **Description:** Grants permission to create a new report in the specified investigation
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvestigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_DeleteInvestigation.html)  **
  - **Description:** Grants permission to delete an investigation in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvestigationGroup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_DeleteInvestigationGroup.html)  **
  - **Description:** Grants permission to delete the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvestigationGroupPolicy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_DeleteInvestigationGroupPolicy.html)  **
  - **Description:** Grants permission to delete the investigation group policy attached to an investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GenerateReport.html)  **
  - **Description:** Grants permission to generate a report in the specified investigation report
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEphemeralInvestigationResults](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetEphemeralInvestigationResults.html)  **
  - **Description:** Grants permission to run and retrieve ephemeral investigation results
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetFact](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetFact.html)  **
  - **Description:** Grants permission to retrieve a fact in the specified investigation report
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFactVersions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetFactVersions.html)  **
  - **Description:** Grants permission to retrieve all versions of a fact token in the specified investigation report
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvestigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetInvestigation.html)  **
  - **Description:** Grants permission to retrieve an investigation in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvestigationEvent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetInvestigationEvent.html)  **
  - **Description:** Grants permission to retrieve an investigation event in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvestigationGroup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetInvestigationGroup.html)  **
  - **Description:** Grants permission to retrieve the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvestigationGroupPolicy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetInvestigationGroupPolicy.html)  **
  - **Description:** Grants permission to retrieve the investigation group policy attached to an investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvestigationResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetInvestigationResource.html)  **
  - **Description:** Grants permission to retrieve an investigation resource in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_GetReport.html)  **
  - **Description:** Grants permission to retrieve a report in the specified investigation
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFacts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_ListFacts.html)  **
  - **Description:** Grants permission to list all facts in the specified investigation report
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInvestigationEvents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_ListInvestigationEvents.html)  **
  - **Description:** Grants permission to list all investigation events in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInvestigationGroups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_ListInvestigationGroups.html)  **
  - **Description:** Grants permission to list all investigation groups in the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInvestigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_ListInvestigations.html)  **
  - **Description:** Grants permission to list all investigations that are in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReports](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_ListReports.html)  **
  - **Description:** Grants permission to list all reports in the specified investigation
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for the specified resource
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutFact](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_PutFact.html)  **
  - **Description:** Grants permission to create or update a new fact in the specified investigation report
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutInvestigationGroupPolicy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_PutInvestigationGroupPolicy.html)  **
  - **Description:** Grants permission to create/update the investigation group policy attached to an investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_TagResource.html)  **
  - **Description:** Grants permission to add or update the specified tags for the specified resource
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_aiops-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_aiops-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from the specified resource
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_aiops-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateInvestigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_UpdateInvestigation.html)  **
  - **Description:** Grants permission to update an investigation in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInvestigationEvent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_UpdateInvestigationEvent.html)  **
  - **Description:** Grants permission to update an investigation event in the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInvestigationGroup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_UpdateInvestigationGroup.html)  **
  - **Description:** Grants permission to update the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_UpdateReport.html)  **
  - **Description:** Grants permission to update a report in the specified investigation
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateInvestigationGroup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_ValidateInvestigationGroup.html)  **
  - **Description:** Grants permission to validate the specified investigation group
  - **Resource types (\*required):** [investigation-group\*](#list_aiops-resource-investigation-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon AI Operations
<a name="list_aiops-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [investigation-group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_InvestigationGroup.html)  | arn:${Partition}:aiops:${Region}:${Account}:investigation-group/${InvestigationGroupId} | [aws:ResourceTag/${TagKey}](#list_aiops-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon AI Operations
<a name="list_aiops-policy-keys"></a>

Amazon AI Operations defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 