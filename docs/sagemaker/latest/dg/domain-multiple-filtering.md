# How domain resource display filtering

works

Amazon SageMaker AI automatically filters the resources displayed in Studio or Studio Classic based
on the Amazon SageMaker AI domain. This filtering is done by using the `sagemaker:domain-arn`
tag attached to SageMaker AI resources. Resources created in other domains are automatically
hidden.

###### Note

This only applies to the Studio or Studio Classic UI. SageMaker AI does not support resource
filtering using the AWS CLI by default.

In Amazon SageMaker Studio or Amazon SageMaker Studio Classic, you'll only see resources that:

- Were created within the current domain.
- Don't have the `sagemaker:domain-arn` tag associated with them. These
  untagged resources are either created outside the context of a domain or were created
  before 11/30/2022.
  To improve resource filtering, you can add the `sagemaker:domain-arn` tag to
  untagged resources by following the steps in [Backfill domain tags](domain-multiple-backfill.md "domain-multiple-backfill.md").

Additionally, all resources created in shared spaces are automatically filtered to that
particular shared space.
