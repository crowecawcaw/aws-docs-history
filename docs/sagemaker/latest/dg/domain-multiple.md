# Multiple domains overview

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

Having multiple Amazon SageMaker AI domain simplifies managing machine learning workflows for
administrators of enterprises with diverse business units, teams, or projects. Each domain
acts as a logically separate environment with its own configurations, settings, and user access
controls. This compartmentalization enables organizations to enforce clear boundaries between
different groups, teams, or use cases, enhancing the ability to securely allocate AWS
resources and permissions on a broad and granular level.

The following provides information about creating multiple domains.

- Amazon SageMaker AI supports the creation of multiple Amazon SageMaker AI domains in a single AWS Region for
  each account.
- Additional domains in an AWS Region have the same features and capabilities as the
  first domain in a Region.
- Each domain can have distinct domain settings.
- The same user profile cannot be added to multiple domains in a single Region within
  the same account.
  For information about domain limits, see [Amazon SageMaker AI endpoints and quotas](../../../general/latest/gr/sagemaker.md "../../../general/latest/gr/sagemaker.md").

The following topics provides information on how to use tags for your domain.

###### Topics

- [Automatic tag propagation](domain-multiple-tag.md "domain-multiple-tag.md")
- [How domain resource display filtering
  works](domain-multiple-filtering.md "domain-multiple-filtering.md")
- [Backfill domain tags](domain-multiple-backfill.md "domain-multiple-backfill.md")
