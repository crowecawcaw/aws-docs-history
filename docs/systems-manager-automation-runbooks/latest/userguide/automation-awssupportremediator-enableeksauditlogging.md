

# `AWSSupportRemediator-EnableEksAuditLogging`

**Description**

Enables audit logging to Amazon CloudWatch Logs for an Amazon Elastic Kubernetes Service (Amazon EKS) cluster.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [EKS clusters should have audit logging enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/eks-controls.html#eks-8).

If the Amazon EKS cluster does not exist or audit logging is already enabled, the automation completes successfully without making changes.

When the runbook enables audit logging, Amazon EKS delivers audit log entries to the Amazon CloudWatch Logs log group `/aws/eks/<cluster-name>/cluster`. Amazon EKS creates this log group automatically if it does not exist.

Enabling audit logging incurs additional Amazon CloudWatch Logs ingestion and storage costs. For more information about pricing, see [Amazon CloudWatch Logs pricing](https://aws.amazon.com/cloudwatch/pricing/).

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
+ EksClusterName

  Type: String

  Description: (Required) The name of the Amazon EKS cluster on which to enable audit logging.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `eks:DescribeCluster`
+ `eks:UpdateClusterConfig`

**Document Steps**

1. **validateEksCluster** - Validates that the Amazon EKS cluster exists and checks whether audit logging is already enabled.

1. **branchOnChangeRequired** - Branches on whether audit logging needs to be enabled.

1. **enableEKSAuditLog** - Enables audit logging on the Amazon EKS cluster.

**Outputs**
+ validateEksCluster.ChangeRequired: Whether audit logging needs to be enabled.
+ validateEksCluster.ValidationMessage: The reason for the validation result.
+ validateEksCluster.InitialEnabledLoggingTypes: The logging types enabled on the cluster before the runbook runs.