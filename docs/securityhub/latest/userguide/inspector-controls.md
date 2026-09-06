

# Security Hub CSPM controls for Amazon Inspector
<a name="inspector-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon Inspector service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [Inspector.1] Amazon Inspector EC2 scanning should be enabled
<a name="inspector-1"></a>

**Related requirements:** PCI DSS v4.0.1/11.3.1

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`inspector-ec2-scan-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/inspector-ec2-scan-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon Inspector EC2 scanning is enabled. For a standalone account, the control fails if Amazon Inspector EC2 scanning is disabled in the account. In a multi-account environment, the control fails if the delegated Amazon Inspector administrator account and all member accounts don't have EC2 scanning enabled.

In a multi-account environment, the control generates findings in only the delegated Amazon Inspector administrator account. Only the delegated administrator can enable or disable the EC2 scanning feature for the member accounts in the organization. Amazon Inspector member accounts can't modify this configuration from their accounts. This control generates `FAILED` findings if the delegated administrator has a suspended member account that doesn't have Amazon Inspector EC2 scanning enabled. To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in Amazon Inspector.

Amazon Inspector EC2 scanning extracts metadata from your Amazon Elastic Compute Cloud (Amazon EC2) instance, and then compares this metadata against rules collected from security advisories to produce findings. Amazon Inspector scans instances for package vulnerabilities and network reachability issues. For information about supported operating systems, including which operating system can be scanned without an SSM agent, see [Supported operating systems: Amazon EC2 scanning](https://docs.aws.amazon.com/inspector/latest/user/supported.html#supported-os-ec2).

### Remediation
<a name="inspector-1-remediation"></a>

To enable Amazon Inspector EC2 scanning, see [Activating scans](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html#activate-scans-proc) in the *Amazon Inspector User Guide*.

## [Inspector.2] Amazon Inspector ECR scanning should be enabled
<a name="inspector-2"></a>

**Related requirements:** PCI DSS v4.0.1/11.3.1

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`inspector-ecr-scan-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/inspector-ecr-scan-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon Inspector ECR scanning is enabled. For a standalone account, the control fails if Amazon Inspector ECR scanning is disabled in the account. In a multi-account environment, the control fails if the delegated Amazon Inspector administrator account and all member accounts don't have ECR scanning enabled.

In a multi-account environment, the control generates findings in only the delegated Amazon Inspector administrator account. Only the delegated administrator can enable or disable the ECR scanning feature for the member accounts in the organization. Amazon Inspector member accounts can't modify this configuration from their accounts. This control generates `FAILED` findings if the delegated administrator has a suspended member account that doesn't have Amazon Inspector ECR scanning enabled. To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in Amazon Inspector.

Amazon Inspector scans container images stored in Amazon Elastic Container Registry (Amazon ECR) for software vulnerabilities to generate package vulnerability findings. When you activate Amazon Inspector scans for Amazon ECR, you set Amazon Inspector as your preferred scanning service for your private registry. This replaces basic scanning, which is provided at no charge by Amazon ECR, with enhanced scanning, which is provided and billed through Amazon Inspector. Enhanced scanning gives you the benefit of vulnerability scanning for both operating system and programming language packages at the registry level. You can review findings discovered using enhanced scanning at the image level, for each layer of the image, on the Amazon ECR console. Additionally, you can review and work with these findings in other services not available for basic scanning findings, including AWS Security Hub CSPM and Amazon EventBridge.

### Remediation
<a name="inspector-2-remediation"></a>

To enable Amazon Inspector ECR scanning, see [Activating scans](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html#activate-scans-proc) in the *Amazon Inspector User Guide*.

## [Inspector.3] Amazon Inspector Lambda code scanning should be enabled
<a name="inspector-3"></a>

**Related requirements:** PCI DSS v4.0.1/6.2.4, PCI DSS v4.0.1/6.3.1

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`inspector-lambda-code-scan-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/inspector-lambda-code-scan-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon Inspector Lambda code scanning is enabled. For a standalone account, the control fails if Amazon Inspector Lambda code scanning is disabled in the account. In a multi-account environment, the control fails if the delegated Amazon Inspector administrator account and all member accounts don't have Lambda code scanning enabled.

In a multi-account environment, the control generates findings in only the delegated Amazon Inspector administrator account. Only the delegated administrator can enable or disable the Lambda code scanning feature for the member accounts in the organization. Amazon Inspector member accounts can't modify this configuration from their accounts. This control generates `FAILED` findings if the delegated administrator has a suspended member account that doesn't have Amazon Inspector Lambda code scanning enabled. To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in Amazon Inspector.

Amazon Inspector Lambda code scanning scans the custom application code within an AWS Lambda function for code vulnerabilities based on AWS security best practices. Lambda code scanning can detect injection flaws, data leaks, weak cryptography, or missing encryption in your code. This feature is available in [specific AWS Regions only](https://docs.aws.amazon.com/inspector/latest/user/inspector_regions.html#ins-regional-feature-availability). You can activate Lambda code scanning together with Lambda standard scanning (see [[Inspector.4] Amazon Inspector Lambda standard scanning should be enabled](#inspector-4)).

### Remediation
<a name="inspector-3-remediation"></a>

To enable Amazon Inspector Lambda code scanning, see [Activating scans](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html#activate-scans-proc) in the *Amazon Inspector User Guide*.

## [Inspector.4] Amazon Inspector Lambda standard scanning should be enabled
<a name="inspector-4"></a>

**Related requirements:** PCI DSS v4.0.1/6.2.4, PCI DSS v4.0.1/6.3.1

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`inspector-lambda-standard-scan-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/inspector-lambda-standard-scan-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon Inspector Lambda standard scanning is enabled. For a standalone account, the control fails if Amazon Inspector Lambda standard scanning is disabled in the account. In a multi-account environment, the control fails if the delegated Amazon Inspector administrator account and all member accounts don't have Lambda standard scanning enabled.

In a multi-account environment, the control generates findings in only the delegated Amazon Inspector administrator account. Only the delegated administrator can enable or disable the Lambda standard scanning feature for the member accounts in the organization. Amazon Inspector member accounts can't modify this configuration from their accounts. This control generates `FAILED` findings if the delegated administrator has a suspended member account that doesn't have Amazon Inspector Lambda standard scanning enabled. To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in Amazon Inspector.

Amazon Inspector Lambda standard scanning identifies software vulnerabilities in the application package dependencies you add to your AWS Lambda function code and layers. If Amazon Inspector detects a vulnerability in your Lambda function application package dependencies, Amazon Inspector produces a detailed `Package Vulnerability` type finding. You can activate Lambda code scanning together with Lambda standard scanning (see [[Inspector.3] Amazon Inspector Lambda code scanning should be enabled](#inspector-3)). 

### Remediation
<a name="inspector-4-remediation"></a>

To enable Amazon Inspector Lambda standard scanning, see [Activating scans](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html#activate-scans-proc) in the *Amazon Inspector User Guide*.