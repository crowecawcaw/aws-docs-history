

# `AWSSupportRemediator-EnableOpenSearchNodeToNodeEncryption`

**Description**

Enables node-to-node encryption for the specified Amazon OpenSearch Service domain.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [OpenSearch domains should encrypt data sent between nodes](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-3).

If the OpenSearch Service domain does not exist or node-to-node encryption is already enabled, the automation completes successfully without making changes.

Enabling node-to-node encryption triggers a blue/green deployment of the OpenSearch Service domain. The domain remains available during this process, but the deployment might temporarily affect cluster performance. OpenSearch Service provisions a new set of instances in a green environment while the update runs. The update might take several hours to complete. If the blue/green deployment encounters issues, you can recover your data using [snapshot restore procedures](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-snapshot-restore.html).

You cannot reverse node-to-node encryption through the OpenSearch Service API. To disable this setting, take a manual snapshot of the encrypted domain. Create a new domain without node-to-node encryption. Migrate your data to the new domain, then delete the original domain.

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
+ DomainName

  Type: String

  Description: (Required) The name of the OpenSearch Service domain.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `es:DescribeDomains`
+ `es:UpdateDomainConfig`

**Document Steps**

1. **validateDomain** - Validates whether the OpenSearch Service domain exists and whether node-to-node encryption is already enabled.

1. **branchOnChangeRequired** - Branches on whether to enable node-to-node encryption on the OpenSearch Service domain.

1. **enableOpenSearchNodeToNodeEncryption** - Enables node-to-node encryption for the specified OpenSearch Service domain by updating the domain configuration.

**Outputs**
+ validateDomain.ChangeRequired: Whether a change is required for the request.
+ validateDomain.InitialNodeToNodeEncryption: Initial value of node-to-node encryption for the OpenSearch Service domain before the runbook runs.
+ validateDomain.ValidationMessage: The reason no change is needed.