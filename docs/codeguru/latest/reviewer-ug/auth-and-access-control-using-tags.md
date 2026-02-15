As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Using tags to control access to

Amazon CodeGuru Reviewer associated repositories

Conditions in IAM policy statements are part of the syntax that you can use to
specify permissions to CodeGuru Reviewer associated repository-based actions. You can create a
policy that allows or denies actions on associated repositories based on the tags
associated with those associated repositories, and then apply those policies to the
IAM groups you configure for managing users. For information about applying tags
to an associated repository using the console or AWS CLI, see [Add a tag to a CodeGuru Reviewer
associated repository](how-to-tag-associated-repositories-add.md "how-to-tag-associated-repositories-add.md"). For information about applying
tags using the CodeGuru Reviewer SDK, see [AssociateRepository](../reviewer-api/API_AssociateRepository.md#API_AssociateRepository_RequestSyntax "../reviewer-api/API_AssociateRepository.md#API_AssociateRepository_RequestSyntax") in the _Amazon CodeGuru Reviewer API Reference_. For
information about using tags to control access to AWS resources, see [Controlling Access
to AWS Resources Using Resource Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
_IAM User Guide_.

You can directly use tags on an associated repository to affect permissions on the
following CodeGuru Reviewer API operations:

- `AssociateRepository`
- `DescribeRepositoryAssociation`
- `DisassociateRepositoryAssociation`
  You can use tags on an associated repository to indirectly affect permissions on a
  code review that belongs to the associated repository. Use tags on an associated
  repository to affect permissions on the following CodeGuru Reviewer API operations that are related
  to code reviews:

- `CreateCodeReview`
- `ListRecommendations`
- `DescribeCodeReview`

###### Example 1: Limit CodeGuru Reviewer associated repository actions based on request tags

The following policy denies users permission to the
`DisassociateRepositoryAssociation` action if the request contains a
tag with the key `ViewAssocatedRepositoryDetails` and the key value
`DenyViewRepository`. In addition, the policy prevents these
unauthorized users from disassociating repositories by using the
`aws:TagKeys` condition key to not allow
`DisassociationAllowed` if the request contains a tag with the key
`DenyDisassociate`. An administrator must attach this IAM policy in
addition to the managed user policy to users who are not authorized to perform these
actions. The `aws:RequestTag` condition key is used to control which tags
can be passed in an IAM request

###### Example 2: Deny or allow actions on code reviews based on their associated repository's resource tags

You can create a policy that allows or denies actions on CodeGuru Reviewer code reviews by
using the CodeGuru Reviewer tags that are added to their associated repositories. An associated
repository contains code reviews, and you can use tags on the associated repository
to affect permissions on its code reviews. For example, you can create a policy that
denies users the ability to view recommendations created by code reviews in an
associated repository. The following policy denies a user with AWS account ID
123456789012 in the AWS Region us-west-2 from viewing recommendations
created by code reviews in all associated repositories that have a
`Recommendation` tag with a value of `Secret`.

###### Example 3: Limit all possible CodeGuru Reviewer actions to associated repositories based on resource tags

You can create policies that selectively allow CodeGuru Reviewer actions on all associated
repositories that are not tagged with specific tags. For example, the following
policy allows you to associate, disassociate, and view the details of associated
repositories that are not tagged with the specified tags:
