

# `AWSSupportRemediator-EnableOpenSearchLogging`

**Description**

Enables audit or error logging for an Amazon OpenSearch Service domain by publishing the logs to an Amazon CloudWatch Logs log group.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM controls [OpenSearch domains should have audit logging enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-5) and [OpenSearch domain error logging to CloudWatch Logs should be enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-4).

If the OpenSearch Service domain does not exist, or if the requested logging type is already enabled, the automation completes successfully without making changes.

The CloudWatch Logs log group must be in the same AWS account and AWS Region as the OpenSearch Service domain. Before running this runbook, attach a CloudWatch Logs resource policy that allows OpenSearch Service to publish log events to the target log group.

Enabling logging might incur additional CloudWatch Logs ingestion and storage costs. For more information about pricing, see [Amazon CloudWatch Logs pricing](https://aws.amazon.com/cloudwatch/pricing/).

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
+ CloudWatchLogGroupName

  Type: String

  Description: (Required) The name of the CloudWatch Logs log group that receives the OpenSearch Service logs. The log group must exist in the same AWS account and AWS Region as the domain.
+ DomainName

  Type: String

  Description: (Required) The name of the OpenSearch Service domain to enable logging for.
+ LogType

  Type: String

  Description: (Optional) The type of logging to enable on the OpenSearch Service domain. Valid values are `Error` and `Audit`.

  Default: Error

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `es:DescribeDomains`
+ `es:UpdateDomainConfig`

**Document Steps**

1. **validateDomain** - Validates that the OpenSearch Service domain exists and checks whether the requested logging type is already enabled.

1. **branchOnChangeRequired** - Branches on whether enabling logging is required.

1. **enableOpenSearchLogging** - Enables the requested logging type on the OpenSearch Service domain by updating the domain configuration.

**Outputs**
+ validateDomain.ChangeRequired: Whether enabling logging is required.
+ validateDomain.InitialLoggingStatus: The initial status of the requested logging type before the automation runs.
+ validateDomain.ValidationMessage: A message describing the validation result.