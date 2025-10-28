Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Amazon CodeGuru Reviewer permissions

reference

You can use AWS condition keys in your CodeGuru Reviewer policies to express conditions.
For a list, see [IAM JSON policy
elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

You specify the actions in the policy's `Action` field. To specify an
action, use the `codeguru-reviewer:` prefix followed by the API operation name (for
example, `codeguru-reviewer:AssociateRepository` and
`codeguru-reviewer:DisassociateRepository`). To specify multiple actions in a
single statement, separate them with commas (for example, `"Action": [
 "codeguru-reviewer:AssociateRepository", "codeguru-reviewer:DisassociateRepository" ]`).

**Using wildcard characters**

You specify an Amazon Resource Name (ARN), with or without a wildcard character (\*),
as the resource value in the policy's `Resource` field. You can use a
wildcard to specify multiple actions or resources. For example,
`codeguru-reviewer:*` specifies all CodeGuru Reviewer actions and
`codeguru-reviewer:List*` specifies all CodeGuru Reviewer actions that begin with the word
`List`. The following example refers to all repository associations with
a universally unique identifier (UUID) that begins with `PullRequest-GITHUB`.

```
arn:aws:codeguru-reviewer:us-east-2:123456789012:association:PullRequest-GITHUB*
```

You can use the following table as a reference when you are setting up [Authenticating with identities](auth-and-access-control.md#security_iam_authentication "auth-and-access-control.md#security_iam_authentication")
and writing permissions policies that you can attach to an IAM identity
(identity-based policies).

CodeGuru Reviewer API operations and required
permissions for actions| CodeGuru Reviewer API operations | Required permissions (API actions) | Resources |
| --- | --- | --- |
| `AssociateRepository` | `codeguru-reviewer:AssociateRepository` Required to associate a repository with CodeGuru Reviewer. | `*` |
| `CreateCodeReview` | `codeguru-reviewer:CreateCodeReview` Required to create a code review to analyze all code under a specified branch in an associated repository. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `DescribeCodeReview` | `codeguru-reviewer:DescribeCodeReview` Required to view information about a code review, including its status. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `DescribeRecommendationFeedback` | `codeguru-reviewer:DescribeRecommendationFeedback` Required to view customer feedback about a recommendation. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `DescribeRepositoryAssociation` | `codeguru-reviewer:DescribeRepositoryAssociation` Required to view information about a repository association and its status details. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `DisassociateRepository` | `codeguru-reviewer:DisassociateRepository` Required to remove the association between CodeGuru Reviewer and a repository. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `ListCodeReviews` | `codeguru-reviewer:ListCodeReviews` Required to view the names of all code reviews in the current AWS account that were created in the past 90 days. | `*` |
| `ListRecommendationFeedback` | `codeguru-reviewer:ListRecommendationFeedback` Required to list all users' customer feedback for a code review recommendation.  | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `ListRecommendations` | `codeguru-reviewer:ListRecommendations` Required to view a list of all the recommendations for one completed code review. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `ListRepositoryAssociations` | `codeguru-reviewer:ListRepositoryAssociations` Required to list summary information about repository associations.  | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `ListTagsForResource` | `codeguru-reviewer:ListTagsForResource` Required to list tags associated with an associated repository ARN. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `PutRecommendationFeedback` | `codeguru-reviewer:PutRecommendationFeedback` Required to store feedback for a code review recommendation. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `TagResource` | `codeguru-reviewer:TagResource` Required for adding one or more tags to an associated repository. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| `UnTagResource` | `codeguru-reviewer:UnTagResource` Required for removing a tag from an associated repository. | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
