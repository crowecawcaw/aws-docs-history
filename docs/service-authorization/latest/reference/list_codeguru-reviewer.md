

# Actions, resources, and condition keys for Amazon CodeGuru Reviewer
<a name="list_codeguru-reviewer"></a>

Amazon CodeGuru Reviewer (service prefix: `codeguru-reviewer`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codeguru-reviewer/codeguru-reviewer.json) for this service.

**Topics**
+ [API operations defined by Amazon CodeGuru Reviewer](#list_codeguru-reviewer-operations)
+ [Actions defined by Amazon CodeGuru Reviewer](#list_codeguru-reviewer-actions-as-permissions)
+ [Permission-only actions for Amazon CodeGuru Reviewer](#list_codeguru-reviewer-permission-only-actions)
+ [Resource types defined by Amazon CodeGuru Reviewer](#list_codeguru-reviewer-resources-for-iam-policies)
+ [Condition keys for Amazon CodeGuru Reviewer](#list_codeguru-reviewer-policy-keys)

## API operations defined by Amazon CodeGuru Reviewer
<a name="list_codeguru-reviewer-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codeguru-reviewer-actions-as-permissions).




- **   AssociateRepository  **
  - **IAM action:**  [codeguru-reviewer:AssociateRepository](#list_codeguru-reviewer-action-AssociateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeguru-reviewer:TagResource](#list_codeguru-reviewer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCodeReview  **
  - **IAM action:**  [codeguru-reviewer:CreateCodeReview](#list_codeguru-reviewer-action-CreateCodeReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCodeReview  **
  - **IAM action:**  [codeguru-reviewer:DescribeCodeReview](#list_codeguru-reviewer-action-DescribeCodeReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecommendationFeedback  **
  - **IAM action:**  [codeguru-reviewer:DescribeRecommendationFeedback](#list_codeguru-reviewer-action-DescribeRecommendationFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRepositoryAssociation  **
  - **IAM action:**  [codeguru-reviewer:DescribeRepositoryAssociation](#list_codeguru-reviewer-action-DescribeRepositoryAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateRepository  **
  - **IAM action:**  [codeguru-reviewer:DisassociateRepository](#list_codeguru-reviewer-action-DisassociateRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListCodeReviews  **
  - **IAM action:**  [codeguru-reviewer:ListCodeReviews](#list_codeguru-reviewer-action-ListCodeReviews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendationFeedback  **
  - **IAM action:**  [codeguru-reviewer:ListRecommendationFeedback](#list_codeguru-reviewer-action-ListRecommendationFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendations  **
  - **IAM action:**  [codeguru-reviewer:ListRecommendations](#list_codeguru-reviewer-action-ListRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRepositoryAssociations  **
  - **IAM action:**  [codeguru-reviewer:ListRepositoryAssociations](#list_codeguru-reviewer-action-ListRepositoryAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [codeguru-reviewer:ListTagsForResource](#list_codeguru-reviewer-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutRecommendationFeedback  **
  - **IAM action:**  [codeguru-reviewer:PutRecommendationFeedback](#list_codeguru-reviewer-action-PutRecommendationFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [codeguru-reviewer:TagResource](#list_codeguru-reviewer-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [codeguru-reviewer:UnTagResource](#list_codeguru-reviewer-action-UnTagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by Amazon CodeGuru Reviewer
<a name="list_codeguru-reviewer-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_AssociateRepository.html)  **
  - **Description:** Grants permission to associates a repository with Amazon CodeGuru Reviewer
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeguru-reviewer-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codeguru-reviewer-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview.html)  **
  - **Description:** Grants permission to create a code review
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeCodeReview.html)  **
  - **Description:** Grants permission to describe a code review
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRecommendationFeedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeRecommendationFeedback.html)  **
  - **Description:** Grants permission to describe a recommendation feedback on a code review
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeRepositoryAssociation.html)  **
  - **Description:** Grants permission to describe a repository association
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DisassociateRepository.html)  **
  - **Description:** Grants permission to disassociate a repository with Amazon CodeGuru Reviewer
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListCodeReviews](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListCodeReviews.html)  **
  - **Description:** Grants permission to list summary of code reviews
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommendationFeedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRecommendationFeedback.html)  **
  - **Description:** Grants permission to list summary of recommendation feedback on a code review
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecommendations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRecommendations.html)  **
  - **Description:** Grants permission to list summary of recommendations on a code review
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html)  **
  - **Description:** Grants permission to list summary of repository associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the resource attached to a associated repository ARN
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutRecommendationFeedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_PutRecommendationFeedback.html)  **
  - **Description:** Grants permission to put feedback for a recommendation on a code review
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_TagResource.html)  **
  - **Description:** Grants permission to attach resource tags to an associated repository ARN
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeguru-reviewer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeguru-reviewer-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UnTagResource](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate resource tags from an associated repository ARN
  - **Resource types (\*required):** [association\*](#list_codeguru-reviewer-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeguru-reviewer-aws_TagKeys)
  - **Access level:** Tagging, Write



## Permission-only actions for Amazon CodeGuru Reviewer
<a name="list_codeguru-reviewer-permission-only-actions"></a>

The following actions are defined by Amazon CodeGuru Reviewer but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateConnectionToken](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/Welcome.html)  | Grants permission to perform webbased oauth handshake for 3rd party providers |  |   | Read | 
|   [GetMetricsData](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/Welcome.html)  | Grants permission to view pull request metrics in console |  |   | Read | 
|   [ListThirdPartyRepositories](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/Welcome.html)  | Grants permission to list 3rd party providers repositories in console |  |   | Read | 

## Resource types defined by Amazon CodeGuru Reviewer
<a name="list_codeguru-reviewer-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [association](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-repositories.html)  | arn:${Partition}:codeguru-reviewer:${Region}:${Account}:association:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_codeguru-reviewer-aws_ResourceTag___TagKey_) | 
|  [codereview](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/code-reviews.html)  | arn:${Partition}:codeguru-reviewer:${Region}:${Account}:association:${ResourceId}:codereview:${CodeReviewId} |   | 

## Condition keys for Amazon CodeGuru Reviewer
<a name="list_codeguru-reviewer-policy-keys"></a>

Amazon CodeGuru Reviewer defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the presence of tag keys in the request | ArrayOfString | 