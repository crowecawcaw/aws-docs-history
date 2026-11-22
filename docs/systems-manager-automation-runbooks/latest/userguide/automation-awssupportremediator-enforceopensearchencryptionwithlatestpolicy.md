

# `AWSSupportRemediator-EnforceOpenSearchEncryptionWithLatestPolicy`

**Description**

Enforces HTTPS and enables the latest TLS security policy (`Policy-Min-TLS-1-2-PFS-2023-10`) on the endpoint of the specified Amazon OpenSearch Service domain.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Connections to OpenSearch domains should be encrypted using the latest TLS security policy](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-8).

If the OpenSearch Service domain does not exist, or already has HTTPS enforcement and the latest TLS security policy enabled, the automation completes successfully without making changes.

Enforcing HTTPS blocks unencrypted HTTP connections. The TLS security policy (`Policy-Min-TLS-1-2-PFS-2023-10`) requires TLS 1.2 or later with perfect forward secrecy cipher suites. Clients using TLS 1.0, TLS 1.1, or unsupported cipher suites lose connectivity. Encrypting data in transit also has processing overhead that might affect cluster performance. Test your applications with this setting to validate compatibility and performance before applying the change.

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

1. **validateDomain** - Validates whether the OpenSearch Service domain exists and whether its endpoint already has HTTPS enforcement and the latest TLS security policy enabled. Returns the initial endpoint configuration for rollback reference.

1. **branchOnChangeRequired** - Branches on whether the OpenSearch Service domain endpoint requires a configuration change. Ends the automation when the domain endpoint is already compliant.

1. **enableDomainEndpointEncryptionTLS** - Enables HTTPS enforcement and sets the latest TLS security policy (`Policy-Min-TLS-1-2-PFS-2023-10`) on the OpenSearch Service domain endpoint.

**Outputs**
+ validateDomain.ChangeRequired: Whether the OpenSearch Service domain endpoint requires a configuration change.
+ validateDomain.InitialDomainEndpointEncryption: The TLS security policy on the domain endpoint before the automation runs.
+ validateDomain.InitialEnforceHTTPSStatus: The EnforceHTTPS setting on the domain endpoint before the automation runs.
+ validateDomain.ValidationMessage: A message describing the validation result.