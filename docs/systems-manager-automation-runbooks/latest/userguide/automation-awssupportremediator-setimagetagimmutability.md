

# `AWSSupportRemediator-SetImageTagImmutability`

**Description**

Sets the image tag mutability setting of an Amazon Elastic Container Registry (Amazon ECR) repository to `IMMUTABLE`.

Setting image tag mutability to `IMMUTABLE` prevents any request from overwriting an existing image tag.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon ECR private repositories should have tag immutability configured](https://docs.aws.amazon.com/securityhub/latest/userguide/ecr-controls.html#ecr-2).

If the Amazon ECR repository does not exist or the image tag mutability is already set to `IMMUTABLE`, the automation completes successfully without making changes.

Setting the image tag mutability to `IMMUTABLE` applies only to tags pushed after this change. To revert to `MUTABLE`, update the repository configuration in the Amazon ECR console or by calling `ecr:PutImageTagMutability` directly.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ RepositoryName

  Type: String

  Description: (Required) The name of the Amazon ECR repository to update.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ecr:DescribeRepositories`
+ `ecr:PutImageTagMutability`

**Document Steps**

1. **validateRepository** - Validates that the Amazon ECR repository exists and checks whether its image tag mutability is already set to `IMMUTABLE`.

1. **branchOnChangeRequired** - Branches on whether the Amazon ECR repository image tag mutability needs to be updated.

1. **putImageTagMutability** - Sets the image tag mutability of the Amazon ECR repository to `IMMUTABLE`.

**Outputs**
+ validateRepository.ChangeRequired: Whether modification is required.
+ validateRepository.ValidationMessage: A message describing the validation result.