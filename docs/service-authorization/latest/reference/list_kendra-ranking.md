

# Actions, resources, and condition keys for Amazon Kendra Intelligent Ranking
<a name="list_kendra-ranking"></a>

Amazon Kendra Intelligent Ranking (service prefix: `kendra-ranking`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/kendra/latest/dg/intelligent-rerank.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/kendra/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/kendra/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kendra-ranking/kendra-ranking.json) for this service.

**Topics**
+ [API operations defined by Amazon Kendra Intelligent Ranking](#list_kendra-ranking-operations)
+ [Actions defined by Amazon Kendra Intelligent Ranking](#list_kendra-ranking-actions-as-permissions)
+ [Resource types defined by Amazon Kendra Intelligent Ranking](#list_kendra-ranking-resources-for-iam-policies)
+ [Condition keys for Amazon Kendra Intelligent Ranking](#list_kendra-ranking-policy-keys)

## API operations defined by Amazon Kendra Intelligent Ranking
<a name="list_kendra-ranking-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kendra-ranking-actions-as-permissions).




- **   CreateRescoreExecutionPlan  **
  - **IAM action:**  [kendra-ranking:CreateRescoreExecutionPlan](#list_kendra-ranking-action-CreateRescoreExecutionPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kendra-ranking:TagResource](#list_kendra-ranking-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteRescoreExecutionPlan  **
  - **IAM action:**  [kendra-ranking:DeleteRescoreExecutionPlan](#list_kendra-ranking-action-DeleteRescoreExecutionPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeRescoreExecutionPlan  **
  - **IAM action:**  [kendra-ranking:DescribeRescoreExecutionPlan](#list_kendra-ranking-action-DescribeRescoreExecutionPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRescoreExecutionPlans  **
  - **IAM action:**  [kendra-ranking:ListRescoreExecutionPlans](#list_kendra-ranking-action-ListRescoreExecutionPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [kendra-ranking:ListTagsForResource](#list_kendra-ranking-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   Rescore  **
  - **IAM action:**  [kendra-ranking:Rescore](#list_kendra-ranking-action-Rescore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [kendra-ranking:TagResource](#list_kendra-ranking-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [kendra-ranking:UntagResource](#list_kendra-ranking-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateRescoreExecutionPlan  **
  - **IAM action:**  [kendra-ranking:UpdateRescoreExecutionPlan](#list_kendra-ranking-action-UpdateRescoreExecutionPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Kendra Intelligent Ranking
<a name="list_kendra-ranking-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateRescoreExecutionPlan](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_CreateRescoreExecutionPlan.html)  **
  - **Description:** Grants permission to create a RescoreExecutionPlan
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-ranking-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_kendra-ranking-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteRescoreExecutionPlan](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_DeleteRescoreExecutionPlan.html)  **
  - **Description:** Grants permission to delete a RescoreExecutionPlan
  - **Resource types (\*required):** [rescore-execution-plan\*](#list_kendra-ranking-resource-rescore-execution-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-ranking-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeRescoreExecutionPlan](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_DescribeRescoreExecutionPlan.html)  **
  - **Description:** Grants permission to describe a RescoreExecutionPlan
  - **Resource types (\*required):** [rescore-execution-plan\*](#list_kendra-ranking-resource-rescore-execution-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-ranking-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListRescoreExecutionPlans](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_ListRescoreExecutionPlans.html)  **
  - **Description:** Grants permission to list all RescoreExecutionPlans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [rescore-execution-plan](#list_kendra-ranking-resource-rescore-execution-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-ranking-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [Rescore](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_Rescore.html)  **
  - **Description:** Grants permission to Rescore documents with Kendra Intelligent Ranking
  - **Resource types (\*required):** [rescore-execution-plan\*](#list_kendra-ranking-resource-rescore-execution-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-ranking-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with given key value pairs
  - **Resource types (\*required):** [rescore-execution-plan](#list_kendra-ranking-resource-rescore-execution-plan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-ranking-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-ranking-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-ranking-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_UntagResource.html)  **
  - **Description:** Grants permission to remove the tag with the given key from a resource
  - **Resource types (\*required):** [rescore-execution-plan](#list_kendra-ranking-resource-rescore-execution-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-ranking-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-ranking-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateRescoreExecutionPlan](https://docs.aws.amazon.com/kendra/latest/dg/API_Ranking_UpdateRescoreExecutionPlan.html)  **
  - **Description:** Grants permission to update a RescoreExecutionPlan
  - **Resource types (\*required):** [rescore-execution-plan\*](#list_kendra-ranking-resource-rescore-execution-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-ranking-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Kendra Intelligent Ranking
<a name="list_kendra-ranking-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [rescore-execution-plan](https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html)  | arn:${Partition}:kendra-ranking:${Region}:${Account}:rescore-execution-plan/${RescoreExecutionPlanId} | [aws:ResourceTag/${TagKey}](#list_kendra-ranking-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Kendra Intelligent Ranking
<a name="list_kendra-ranking-policy-keys"></a>

Amazon Kendra Intelligent Ranking defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 