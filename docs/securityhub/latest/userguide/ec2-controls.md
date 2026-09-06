

# Security Hub CSPM controls for Amazon EC2
<a name="ec2-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon Elastic Compute Cloud (Amazon EC2) service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [EC2.1] Amazon EBS snapshots should not be configured to be publicly restorable
<a name="ec2-1"></a>

**Related requirements:** PCI DSS v3.2.1/1.2.1,PCI DSS v3.2.1/1.3.1,PCI DSS v3.2.1/1.3.4,PCI DSS v3.2.1/7.2.1, NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration

**Severity:** Critical 

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`ebs-snapshot-public-restorable-check`](https://docs.aws.amazon.com/config/latest/developerguide/ebs-snapshot-public-restorable-check.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon Elastic Block Store snapshots are configured to be publicly restorable. The control fails if Amazon EBS snapshots are configured to be restorable by all.

EBS snapshots are used to back up the data on your EBS volumes to Amazon S3 at a specific point in time. You can use the snapshots to restore previous states of EBS volumes. It is rarely acceptable to share a snapshot with the public. Typically the decision to share a snapshot publicly was made in error or without a complete understanding of the implications. This check helps ensure that all such sharing was fully planned and intentional.

### Remediation
<a name="ec2-1-remediation"></a>

To make a public EBS snapshot private, see [Share a snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html#share-unencrypted-snapshot) in the *Amazon EC2 User Guide*. For **Actions, Modify permissions**, choose **Private**.

## [EC2.2] VPC default security groups should not allow inbound or outbound traffic
<a name="ec2-2"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/5.5, PCI DSS v3.2.1/1.2.1,PCI DSS v3.2.1/1.3.4,PCI DSS v3.2.1/2.1, CIS AWS Foundations Benchmark v1.2.0/4.3, CIS AWS Foundations Benchmark v1.4.0/5.3, CIS AWS Foundations Benchmark v3.0.0/5.4, NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(5)

**Category:** Protect > Secure network configuration

**Severity:** High 

**Resource type:** `AWS::EC2::SecurityGroup`

**AWS Config rule:** [`vpc-default-security-group-closed`](https://docs.aws.amazon.com/config/latest/developerguide/vpc-default-security-group-closed.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the default security group of a VPC allows inbound or outbound traffic. The control fails if the security group allows inbound or outbound traffic.

The rules for the [default security group](https://docs.aws.amazon.com/vpc/latest/userguide/default-security-group.html) allow all outbound and inbound traffic from network interfaces (and their associated instances) that are assigned to the same security group. We recommend that you don't use the default security group. Because the default security group cannot be deleted, you should change the default security group rules setting to restrict inbound and outbound traffic. This prevents unintended traffic if the default security group is accidentally configured for resources such as EC2 instances.

### Remediation
<a name="ec2-2-remediation"></a>

To remediate this issue, start by creating new least-privilege security groups. For instructions, see [Create a security group](https://docs.aws.amazon.com/vpc/latest/userguide/security-groups.html#creating-security-groups) in the *Amazon VPC User Guide*. Then, assign the new security groups to your EC2 instances. For instructions, see [Change an instance's security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#changing-security-group) in the *Amazon EC2 User Guide*.

After you assign the new security groups to your resources, remove all inbound and outbound rules from the default security groups. For instructions, see [Configure security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html) in the *Amazon VPC User Guide*.

## [EC2.3] Attached Amazon EBS volumes should be encrypted at-rest
<a name="ec2-3"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::EC2::Volume`

**AWS Config rule:** [`encrypted-volumes`](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the EBS volumes that are in an attached state are encrypted. To pass this check, EBS volumes must be in use and encrypted. If the EBS volume is not attached, then it is not subject to this check.

For an added layer of security of your sensitive data in EBS volumes, you should enable EBS encryption at rest. Amazon EBS encryption offers a straightforward encryption solution for your EBS resources that doesn't require you to build, maintain, and secure your own key management infrastructure. It uses KMS keys when creating encrypted volumes and snapshots.

To learn more about Amazon EBS encryption, see [Amazon EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) in the *Amazon EC2 User Guide*.

### Remediation
<a name="ec2-3-remediation"></a>

There's no direct way to encrypt an existing unencrypted volume or snapshot. You can only encrypt a new volume or snapshot when you create it.

If you enabled encryption by default, Amazon EBS encrypts the resulting new volume or snapshot using your default key for Amazon EBS encryption. Even if you have not enabled encryption by default, you can enable encryption when you create an individual volume or snapshot. In both cases, you can override the default key for Amazon EBS encryption and choose a symmetric customer managed key.

For more information, see [Creating an Amazon EBS volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html) and [Copying an Amazon EBS snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html) in the *Amazon EC2 User Guide*.

## [EC2.4] Stopped EC2 instances should be removed after a specified time period
<a name="ec2-4"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Identify > Inventory

**Severity:** Medium

**Resource type:** `AWS::EC2::Instance`

**AWS Config rule:** `ec2-stopped-instance-days-check` (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `AllowedDays` | Number of days the EC2 instance is allowed to be in a stopped state before generating a failed finding. | Integer | `1` to `365` | `30` | 

This control checks whether an Amazon EC2 instance has been stopped for longer than the allowed number of days. The control fails if an EC2 instance is stopped for longer than the maximum allowed time period. Unless you provide a custom parameter value for the maximum allowed time period, Security Hub CSPM uses a default value of 30 days.

When an EC2 instance has not run for a significant period of time, it creates a security risk because the instance is not being actively maintained (analyzed, patched, updated). If it is later launched, the lack of proper maintenance could result in unexpected issues in your AWS environment. To safely maintain an EC2 instance over time in an inactive state, start it periodically for maintenance and then stop it after maintenance. Ideally, this should be an automated process.

**Note**  
This control evaluates the number of days that an EC2 instance has been stopped using the timestamp from `StateTransitionReason` for the instance. When the `StateTransitionReason` does not include a timestamp (such as when an instance is stopped due to an internal error), the control uses the instance's launch time instead. In this case, if the launch time is older than the maximum allowed time period, the control generates a FAILED finding. 

### Remediation
<a name="ec2-4-remediation"></a>

To terminate an inactive EC2 instance, see [Terminate an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#terminating-instances-console) in the *Amazon EC2 User Guide*.

## [EC2.6] VPC flow logging should be enabled in all VPCs
<a name="ec2-6"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/3.7, CIS AWS Foundations Benchmark v1.2.0/2.9, CIS AWS Foundations Benchmark v1.4.0/3.9, CIS AWS Foundations Benchmark v3.0.0/3.7, NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-7(8), NIST.800-171.r2 3.1.20, NIST.800-171.r2 3.3.1, NIST.800-171.r2 3.13.1, PCI DSS v3.2.1/10.3.3, PCI DSS v3.2.1/10.3.4, PCI DSS v3.2.1/10.3.5, PCI DSS v3.2.1/10.3.6

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::EC2::VPC`

**AWS Config rule:** [`vpc-flow-logs-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/vpc-flow-logs-enabled.html)

**Schedule type:** Periodic

**Parameters:**
+ `trafficType`: `REJECT` (not customizable)

This control checks whether Amazon VPC Flow Logs are found and enabled for VPCs. The traffic type is set to `Reject`. The control fails if VPC Flow Logs aren't enabled for VPCs in your account.

**Note**  
This control doesn't check whether Amazon VPC Flow Logs are enabled through Amazon Security Lake for the AWS account.

With the VPC Flow Logs feature, you can capture information about the IP address traffic going to and from network interfaces in your VPC. After you create a flow log, you can view and retrieve its data in CloudWatch Logs. To reduce cost, you can also send your flow logs to Amazon S3. 

Security Hub CSPM recommends that you enable flow logging for packet rejects for VPCs. Flow logs provide visibility into network traffic that traverses the VPC and can detect anomalous traffic or provide insight during security workflows.

By default, the record includes values for the different components of the IP address flow, including the source, destination, and protocol. For more information and descriptions of the log fields, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

### Remediation
<a name="ec2-6-remediation"></a>

To create a VPC Flow Log, see [Create a Flow Log](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-flow-logs.html#create-flow-log) in the *Amazon VPC User Guide*. After you open the Amazon VPC console, choose **Your VPCs**. For **Filter**, choose **Reject** or **All**.

## [EC2.7] EBS default encryption should be enabled
<a name="ec2-7"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/5.1.1, CIS AWS Foundations Benchmark v1.4.0/2.2.1, CIS AWS Foundations Benchmark v3.0.0/2.2.1, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`ec2-ebs-encryption-by-default`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-ebs-encryption-by-default.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether account-level encryption is enabled by default for Amazon Elastic Block Store (Amazon EBS) volumes. The control fails if the account level encryption isn't enabled for EBS volumes. 

When encryption is enabled for your account, Amazon EBS volumes and snapshot copies are encrypted at rest. This adds an additional layer of protection for your data. For more information, see [Encryption by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) in the *Amazon EC2 User Guide*.

### Remediation
<a name="ec2-7-remediation"></a>

To configure default encryption for Amazon EBS volumes, see [Encryption by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) in the *Amazon EC2 User Guide*.

## [EC2.8] EC2 instances should use Instance Metadata Service Version 2 (IMDSv2)
<a name="ec2-8"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/5.7, CIS AWS Foundations Benchmark v3.0.0/5.6, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6, PCI DSS v4.0.1/2.2.6

**Category:** Protect > Network Security

**Severity:** High

**Resource type:** `AWS::EC2::Instance`

**AWS Config rule:** [`ec2-imdsv2-check`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-imdsv2-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether your EC2 instance metadata version is configured with Instance Metadata Service Version 2 (IMDSv2). The control passes if `HttpTokens` is set to required for IMDSv2. The control fails if `HttpTokens` is set to `optional`.

You use instance metadata to configure or manage the running instance. The IMDS provides access to temporary, frequently rotated credentials. These credentials remove the need to hard code or distribute sensitive credentials to instances manually or programmatically. The IMDS is attached locally to every EC2 instance. It runs on a special "link local" IP address of 169.254.169.254. This IP address is only accessible by software that runs on the instance.

Version 2 of the IMDS adds new protections for the following types of vulnerabilities. These vulnerabilities could be used to try to access the IMDS.
+ Open website application firewalls
+ Open reverse proxies
+ Server-side request forgery (SSRF) vulnerabilities
+ Open Layer 3 firewalls and network address translation (NAT)

Security Hub CSPM recommends that you configure your EC2 instances with IMDSv2.

### Remediation
<a name="ec2-8-remediation"></a>

To configure EC2 instances with IMDSv2, see [Recommended path to requiring IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.html#recommended-path-for-requiring-imdsv2) in the *Amazon EC2 User Guide*.

## [EC2.9] Amazon EC2 instances should not have a public IPv4 address
<a name="ec2-9"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:** `AWS::EC2::Instance`

**AWS Config rule:** [`ec2-instance-no-public-ip`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-no-public-ip.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether EC2 instances have a public IP address. The control fails if the `publicIp` field is present in the EC2 instance configuration item. This control applies to IPv4 addresses only. 

A public IPv4 address is an IP address that is reachable from the internet. If you launch your instance with a public IP address, then your EC2 instance is reachable from the internet. A private IPv4 address is an IP address that is not reachable from the internet. You can use private IPv4 addresses for communication between EC2 instances in the same VPC or in your connected private network.

IPv6 addresses are globally unique, and therefore are reachable from the internet. However, by default all subnets have the IPv6 addressing attribute set to false. For more information about IPv6, see [IP addressing in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html) in the *Amazon VPC User Guide*.

If you have a legitimate use case to maintain EC2 instances with public IP addresses, then you can suppress the findings from this control. For more information about front-end architecture options, see the [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/) or the [This Is My Architecture series](https://aws.amazon.com/this-is-my-architecture/?tma.sort-by=item.additionalFields.airDate&tma.sort-order=desc&awsf.category=categories%23mobile) AWS video series.

### Remediation
<a name="ec2-9-remediation"></a>

Use a non-default VPC so that your instance isn't assigned a public IP address by default.

When you launch an EC2 instance into a default VPC, it is assigned a public IP address. When you launch an EC2 instance into a non-default VPC, the subnet configuration determines whether it receives a public IP address. The subnet has an attribute to determine if new EC2 instances in the subnet receive a public IP address from the public IPv4 address pool.

You can disassociate an automatically-assigned public IP address from your EC2 instance. For more information, see [Public IPv4 addresses and external DNS hostnames](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses) in the *Amazon EC2 User Guide*.

## [EC2.10] Amazon EC2 should be configured to use VPC endpoints that are created for the Amazon EC2 service
<a name="ec2-10"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-171.r2 3.1.3, NIST.800-171.r2 3.13.1

**Category:** Protect > Secure network configuration > API private access

**Severity:** Medium

**Resource type:** `AWS::EC2::VPC`

**AWS Config rule:** [vpc-endpoint-enabled](https://docs.aws.amazon.com/config/latest/developerguide/vpc-endpoint-enabled.html)

**Schedule type:** Periodic

**Parameters:** 
+ `serviceNames`: `ec2` (not customizable)

This control checks whether a service endpoint for Amazon EC2 is created for each VPC. The control fails if a VPC does not have a VPC endpoint created for the Amazon EC2 service. 

This control evaluates resources in single account. It cannot describe resources that are outside of the account. Because AWS Config and Security Hub CSPM do not conduct cross-account checks, you will see `FAILED` findings for VPCs that are shared across accounts. Security Hub CSPM recommends that you suppress these `FAILED` findings.

To improve the security posture of your VPC, you can configure Amazon EC2 to use an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink, a technology that enables you to access Amazon EC2 API operations privately. It restricts all network traffic between your VPC and Amazon EC2 to the Amazon network. Because endpoints are supported within the same Region only, you cannot create an endpoint between a VPC and a service in a different Region. This prevents unintended Amazon EC2 API calls to other Regions. 

To learn more about creating VPC endpoints for Amazon EC2, see [Amazon EC2 and interface VPC endpoints ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html)in the *Amazon EC2 User Guide*.

### Remediation
<a name="ec2-10-remediation"></a>

To create an interface endpoint to Amazon EC2 from the Amazon VPC console, see [Create a VPC endpoint ](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws)in the *AWS PrivateLink Guide*. For **Service name**, choose **com.amazonaws.{{region}}.ec2**.

You can also create and attach an endpoint policy to your VPC endpoint to control access to the Amazon EC2 API. For instructions on creating a VPC endpoint policy, see [Create an endpoint policy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html#endpoint-policy) in the *Amazon EC2 User Guide*.

## [EC2.12] Unused Amazon EC2 EIPs should be removed
<a name="ec2-12"></a>

**Related requirements:** PCI DSS v3.2.1/2.4, NIST.800-53.r5 CM-8(1)

**Category:** Protect > Secure network configuration

**Severity:** Low

**Resource type:** `AWS::EC2::EIP`

**AWS Config rule:** [`eip-attached`](https://docs.aws.amazon.com/config/latest/developerguide/eip-attached.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Elastic IP (EIP) addresses that are allocated to a VPC are attached to EC2 instances or in-use elastic network interfaces (ENIs).

A failed finding indicates you may have unused EC2 EIPs.

This will help you maintain an accurate asset inventory of EIPs in your cardholder data environment (CDE).

### Remediation
<a name="ec2-12-remediation"></a>

To release an unused EIP, see [Release an Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-releasing) in the *Amazon EC2 User Guide*.

## [EC2.13] Security groups should not allow ingress from 0.0.0.0/0 or ::/0 to port 22
<a name="ec2-13"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/4.1, NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 CM-7, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(5), NIST.800-171.r2 3.1.3, NIST.800-171.r2 3.13.1, PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/2.2.2, PCI DSS v4.0.1/1.3.1

**Category:** Protect > Secure network configuration

**Severity:** High

**Resource type:** `AWS::EC2::SecurityGroup`

**AWS Config rule:** [`restricted-ssh`](https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html)

**Schedule type:** Change triggered and periodic

**Parameters:** None

This control checks whether an Amazon EC2 security group allows ingress from 0.0.0.0/0 or ::/0 to port 22. The control fails if the security group allows ingress from 0.0.0.0/0 or ::/0 to port 22.

Security groups provide stateful filtering of ingress and egress network traffic to AWS resources. We recommend that no security group allow unrestricted ingress access to port 22. Removing unfettered connectivity to remote console services, such as SSH, reduces a server's exposure to risk.

### Remediation
<a name="ec2-13-remediation"></a>

To prohibit ingress to port 22, remove the rule that allows such access for each security group associated with a VPC. For instructions, see [Update security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#updating-security-group-rules) in the *Amazon EC2 User Guide*. After selecting a security group in the Amazon EC2 console, choose **Actions, Edit inbound rules**. Remove the rule that allows access to port 22.

## [EC2.14] Security groups should not allow ingress from 0.0.0.0/0 or ::/0 to port 3389
<a name="ec2-14"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/4.2, PCI DSS v4.0.1/1.3.1

**Category:** Protect > Secure network configuration

**Severity:** High

**Resource type:** `AWS::EC2::SecurityGroup`

**AWS Config rule:** [`restricted-common-ports`](https://docs.aws.amazon.com/config/latest/developerguide/restricted-common-ports.html) (created rule is `restricted-rdp`)

**Schedule type:** Change triggered and periodic

**Parameters:** None

This control checks whether an Amazon EC2 security group allows ingress from 0.0.0.0/0 or ::/0 to port 3389. The control fails if the security group allows ingress from 0.0.0.0/0 or ::/0 to port 3389.

Security groups provide stateful filtering of ingress and egress network traffic to AWS resources. We recommend that no security group allow unrestricted ingress access to port 3389. Removing unfettered connectivity to remote console services, such as RDP, reduces a server's exposure to risk.

### Remediation
<a name="ec2-14-remediation"></a>

To prohibit ingress to port 3389, remove the rule that allows such access for each security group associated with a VPC. For instructions, see [Update security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html#updating-security-group-rules) in the *Amazon VPC User Guide*. After selecting a security group in the Amazon VPC Console, choose **Actions, Edit inbound rules**. Remove the rule that allows access to port 3389.

## [EC2.15] Amazon EC2 subnets should not automatically assign public IP addresses
<a name="ec2-15"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v4.0.1/1.4.4

**Category:** Protect > Network Security

**Severity:** Medium

**Resource type:** `AWS::EC2::Subnet`

**AWS Config rule:** [`subnet-auto-assign-public-ip-disabled`](https://docs.aws.amazon.com/config/latest/developerguide/subnet-auto-assign-public-ip-disabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Virtual Private Cloud (Amazon VPC) subnet is configured to automatically assign public IP addresses. The control fails if the subnet is configured to automatically assign public IPv4 or IPv6 addresses.

Subnets have attributes that determine whether network interfaces automatically receive public IPv4 and IPv6 addresses. For IPv4, this attribute is set to `TRUE` for default subnets and `FALSE` for nondefault subnets (with an exception for nondefault subnets created through the EC2 launch instance wizard, where it's set to `TRUE`). For IPv6, this attribute is set to `FALSE` for all subnets by default. When these attributes are enabled, instances launched in the subnet automatically receive the corresponding IP addresses (IPv4 or IPv6) on their primary network interface.

### Remediation
<a name="ec2-15-remediation"></a>

To configure a subnet to not assign public IP addresses, see [Modify the IP addressing attributes of your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-public-ip.html) in the *Amazon VPC User Guide*.

## [EC2.16] Unused Network Access Control Lists should be removed
<a name="ec2-16"></a>

**Related requirements:** NIST.800-53.r5 CM-8(1), NIST.800-171.r2 3.4.7, PCI DSS v4.0.1/1.2.7

**Category:** Protect > Network Security

**Severity:** Low

**Resource type:** `AWS::EC2::NetworkAcl`

**AWS Config rule:** [`vpc-network-acl-unused-check`](https://docs.aws.amazon.com/config/latest/developerguide/vpc-network-acl-unused-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether there are any unused network access control lists (network ACLs) in your virtual private cloud (VPC). The control fails if the network ACL isn't associated with a subnet. The control doesn't generate findings for an unused default network ACL.

The control checks the item configuration of the resource `AWS::EC2::NetworkAcl` and determines the relationships of the network ACL.

If the only relationship is the VPC of the network ACL, the control fails.

If other relationships are listed, then the control passes.

### Remediation
<a name="ec2-16-remediation"></a>

For instructions on deleting an unused network ACL, see [Deleting a network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#DeleteNetworkACL) in the *Amazon VPC User Guide*. You can't delete the default network ACL or an ACL that is associated with subnets.

## [EC2.17] Amazon EC2 instances should not use multiple ENIs
<a name="ec2-17"></a>

**Related requirements:** NIST.800-53.r5 AC-4(21)

**Category:** Protect > Network Security

**Severity:** Low

**Resource type:** `AWS::EC2::Instance`

**AWS Config rule:** [`ec2-instance-multiple-eni-check`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-multiple-eni-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an EC2 instance uses multiple Elastic Network Interfaces (ENIs) or Elastic Fabric Adapters (EFAs). This control passes if a single network adapter is used. The control includes an optional parameter list to identify the allowed ENIs. This control also fails if an EC2 instance that belongs to an Amazon EKS cluster uses more than one ENI. If your EC2 instances need to have multiple ENIs as part of an Amazon EKS cluster, you can suppress those control findings.

Multiple ENIs can cause dual-homed instances, meaning instances that have multiple subnets. This can add network security complexity and introduce unintended network paths and access.

### Remediation
<a name="ec2-17-remediation"></a>

To detach a network interface from an EC2 instance, see [Detach a network interface from an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#detach_eni) in the *Amazon EC2 User Guide*.

## [EC2.18] Security groups should only allow unrestricted incoming traffic for authorized ports
<a name="ec2-18"></a>

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(5), NIST.800-171.r2 3.1.3, NIST.800-171.r2 3.1.20, NIST.800-171.r2 3.13.1

**Category:** Protect > Secure network configuration > Security group configuration

**Severity:** High

**Resource type:** `AWS::EC2::SecurityGroup`

**AWS Config rule:** [`vpc-sg-open-only-to-authorized-ports`](https://docs.aws.amazon.com/config/latest/developerguide/vpc-sg-open-only-to-authorized-ports.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `authorizedTcpPorts` | List of authorized TCP ports | IntegerList (minimum of 1 item and maximum of 32 items) | `1` to `65535` | `[80,443]` | 
| `authorizedUdpPorts` | List of authorized UDP ports | IntegerList (minimum of 1 item and maximum of 32 items) | `1` to `65535` | No default value | 

This control checks whether an Amazon EC2 security group permits unrestricted incoming traffic from unauthorized ports. The control status is determined as follows:
+ If you use the default value for `authorizedTcpPorts`, the control fails if the security group permits unrestricted incoming traffic from any port other than ports 80 and 443.
+ If you provide custom values for `authorizedTcpPorts` or `authorizedUdpPorts`, the control fails if the security group permits unrestricted incoming traffic from any unlisted port.

Security groups provide stateful filtering of ingress and egress network traffic to AWS. Security group rules should follow the principal of least privileged access. Unrestricted access (IP address with a /0 suffix) increases the opportunity for malicious activity such as hacking, denial-of-service attacks, and loss of data. Unless a port is specifically allowed, the port should deny unrestricted access.

### Remediation
<a name="ec2-18-remediation"></a>

To modify a security group, see [Work with security groups](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-groups.html) in the *Amazon VPC User Guide*.

## [EC2.19] Security groups should not allow unrestricted access to ports with high risk
<a name="ec2-19"></a>

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5 CM-7, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(5), NIST.800-171.r2 3.1.3, NIST.800-171.r2 3.1.20, NIST.800-171.r2 3.13.1

**Category:** Protect > Restricted network access

**Severity:** Critical

**Resource type:** `AWS::EC2::SecurityGroup`

**AWS Config rule:** [`restricted-common-ports`](https://docs.aws.amazon.com/config/latest/developerguide/restricted-common-ports.html) (created rule is `vpc-sg-restricted-common-ports`)

**Schedule type:** Change triggered and periodic

**Parameters:** `"blockedPorts": "20,21,22,23,25,110,135,143,445,1433,1434,3000,3306,3389,4333,5000,5432,5500,5601,8080,8088,8888,9200,9300"` (not customizable)

This control checks whether unrestricted incoming traffic for an Amazon EC2 security group is accessible to the specified ports that are considered to be high risk. This control fails if any of the rules in a security group allow ingress traffic from '0.0.0.0/0' or '::/0' to those ports.

Security groups provide stateful filtering of ingress and egress network traffic to AWS resources. Unrestricted access (0.0.0.0/0) increases opportunities for malicious activity, such as hacking, denial-of-service attacks, and loss of data. No security group should allow unrestricted ingress access to the following ports:
+ 20, 21 (FTP)
+ 22 (SSH)
+ 23 (Telnet)
+ 25 (SMTP)
+ 110 (POP3)
+ 135 (RPC)
+ 143 (IMAP)
+ 445 (CIFS)
+ 1433, 1434 (MSSQL)
+ 3000 (Go, Node.js, and Ruby web development frameworks)
+ 3306 (mySQL)
+ 3389 (RDP)
+ 4333 (ahsp)
+ 5000 (Python web development frameworks)
+ 5432 (postgresql)
+ 5500 (fcp-addr-srvr1) 
+ 5601 (OpenSearch Dashboards)
+ 8080 (proxy)
+ 8088 (legacy HTTP port)
+ 8888 (alternative HTTP port)
+ 9200 or 9300 (OpenSearch)

### Remediation
<a name="ec2-19-remediation"></a>

To delete rules from a security group, see [Delete rules from a security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#deleting-security-group-rule) in the *Amazon EC2 User Guide*.

## [EC2.20] Both VPN tunnels for an AWS Site-to-Site VPN connection should be up
<a name="ec2-20"></a>

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5), NIST.800-171.r2 3.1.13, NIST.800-171.r2 3.1.20

**Category:** Recover > Resilience > High availability

**Severity:** Medium 

**Resource type:**`AWS::EC2::VPNConnection`

**AWS Config rule:** [`vpc-vpn-2-tunnels-up`](https://docs.aws.amazon.com/config/latest/developerguide/vpc-vpn-2-tunnels-up.html)

**Schedule type:** Change triggered

**Parameters:** None

A VPN tunnel is an encrypted link where data can pass from the customer network to or from AWS within an AWS Site-to-Site VPN connection. Each VPN connection includes two VPN tunnels which you can simultaneously use for high availability. Ensuring that both VPN tunnels are up for a VPN connection is important for confirming a secure and highly available connection between an AWS VPC and your remote network.

This control checks that both VPN tunnels provided by AWS Site-to-Site VPN are in UP status. The control fails if one or both tunnels are in DOWN status.

### Remediation
<a name="ec2-20-remediation"></a>

To modify VPN tunnel options, see [Modifying Site-to-Site VPN tunnel options](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-tunnel-options.html) in the AWS Site-to-Site VPN User Guide.

## [EC2.21] Network ACLs should not allow ingress from 0.0.0.0/0 to port 22 or port 3389
<a name="ec2-21"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/5.2, CIS AWS Foundations Benchmark v1.4.0/5.1, CIS AWS Foundations Benchmark v3.0.0/5.1, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5 CM-7, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(5), NIST.800-171.r2 3.1.3, NIST.800-171.r2 3.1.20, NIST.800-171.r2 3.13.1, PCI DSS v4.0.1/1.3.1

**Category:** Protect > Secure Network Configuration

**Severity:** Medium 

**Resource type:**`AWS::EC2::NetworkAcl`

**AWS Config rule:** [`nacl-no-unrestricted-ssh-rdp`](https://docs.aws.amazon.com/config/latest/developerguide/nacl-no-unrestricted-ssh-rdp.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a network access control list (network ACL) allows unrestricted access to the default TCP ports for SSH/RDP ingress traffic. The control fails if the network ACL inbound entry allows a source CIDR block of '0.0.0.0/0' or '::/0' for TCP ports 22 or 3389. The control doesn't generate findings for a default network ACL.

Access to remote server administration ports, such as port 22 (SSH) and port 3389 (RDP), should not be publicly accessible, as this may allow unintended access to resources within your VPC.

### Remediation
<a name="ec2-21-remediation"></a>

To edit network ACL traffic rules, see [Work with network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-tasks) in the *Amazon VPC User Guide*.

## [EC2.22] Unused Amazon EC2 security groups should be removed
<a name="ec2-22"></a>

**Category:** Identify > Inventory

**Severity:** Medium 

**Resource type:** `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`

**AWS Config rule:** [`ec2-security-group-attached-to-eni-periodic`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-security-group-attached-to-eni-periodic.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether security groups are attached to Amazon Elastic Compute Cloud (Amazon EC2) instances or to an elastic network interface. The control fails if the security group is not associated with an Amazon EC2 instance or an elastic network interface.

**Important**  
On September 20, 2023, Security Hub CSPM removed this control from the AWS Foundational Security Best Practices and NIST SP 800-53 Revision 5 standards. This control continues to be part of the AWS Control Tower service-managed standard. This control produces a passed finding if security groups are attached to EC2 instances or an elastic network interface. However, for certain use cases, unattached security groups don't pose a security risk. You can use other EC2 controls—such as EC2.2, EC2.13, EC2.14, EC2.18, and EC2.19—to monitor your security groups.

### Remediation
<a name="ec2-22-remediation"></a>

To create, assign and delete security groups, see [Security groups for your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the *Amazon EC2 User Guide*.

## [EC2.23] Amazon EC2 Transit Gateways should not automatically accept VPC attachment requests
<a name="ec2-23"></a>

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** High 

**Resource type:**`AWS::EC2::TransitGateway`

**AWS Config rule:** [`ec2-transit-gateway-auto-vpc-attach-disabled`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-transit-gateway-auto-vpc-attach-disabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if EC2 transit gateways are automatically accepting shared VPC attachments. This control fails for a transit gateway that automatically accepts shared VPC attachment requests.

Turning on `AutoAcceptSharedAttachments` configures a transit gateway to automatically accept any cross-account VPC attachment requests without verifying the request or the account the attachment is originating from. To follow the best practices of authorization and authentication, we recommended turning off this feature to ensure that only authorized VPC attachment requests are accepted.

### Remediation
<a name="ec2-23-remediation"></a>

To modify a transit gateway, see [Modify a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying) in the Amazon VPC Developer Guide.

## [EC2.24] Amazon EC2 paravirtual instance types should not be used
<a name="ec2-24"></a>

**Related requirements:** NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** Medium 

**Resource type:**`AWS::EC2::Instance`

**AWS Config rule:** [`ec2-paravirtual-instance-check`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-paravirtual-instance-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the virtualization type of an EC2 instance is paravirtual. The control fails if the `virtualizationType` of the EC2 instance is set to `paravirtual`.

Linux Amazon Machine Images (AMIs) use one of two types of virtualization: paravirtual (PV) or hardware virtual machine (HVM). The main differences between PV and HVM AMIs are the way in which they boot and whether they can take advantage of special hardware extensions (CPU, network, and storage) for better performance.

Historically, PV guests had better performance than HVM guests in many cases, but because of enhancements in HVM virtualization and the availability of PV drivers for HVM AMIs, this is no longer true. For more information, see [Linux AMI virtualization types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html) in the Amazon EC2 User Guide.

### Remediation
<a name="ec2-24-remediation"></a>

To update an EC2 instance to a new instance type, see [Change the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) in the *Amazon EC2 User Guide*.

## [EC2.25] Amazon EC2 launch templates should not assign public IPs to network interfaces
<a name="ec2-25"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High 

**Resource type:**`AWS::EC2::LaunchTemplate`

**AWS Config rule:** [`ec2-launch-template-public-ip-disabled`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-launch-template-public-ip-disabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon EC2 launch templates are configured to assign public IP addresses to network interfaces upon launch. The control fails if an EC2 launch template is configured to assign a public IP address to network interfaces or if there is at least one network interface that has a public IP address.

A public IP address is one that is reachable from the internet. If you configure your network interfaces with a public IP address, then the resources associated with those network interfaces may be reachable from the internet. EC2 resources shouldn't be publicly accessible because this may permit unintended access to your workloads.

### Remediation
<a name="ec2-25-remediation"></a>

To update an EC2 launch template, see [Change the default network interface settings](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface) in the *Amazon EC2 Auto Scaling User Guide*.

## [EC2.28] EBS volumes should be covered by a backup plan
<a name="ec2-28"></a>

**Category:** Recover > Resilience > Backups enabled

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6, NIST.800-53.r5 CP-6(1), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-12, NIST.800-53.r5 SI-13(5)

**Severity:** Low

**Resource type:** `AWS::EC2::Volume`

**AWS Config rule:** [`ebs-resources-protected-by-backup-plan`](https://docs.aws.amazon.com/config/latest/developerguide/ebs-resources-protected-by-backup-plan.html) ``

**Schedule type:** Periodic

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `backupVaultLockCheck` | The control produces a `PASSED` finding if the parameter is set to `true` and the resource uses AWS Backup Vault Lock. | Boolean | `true` or `false` | No default value | 

This control evaluates if an Amazon EBS volume in `in-use` state is covered by a backup plan. The control fails if an EBS volume isn't covered by a backup plan. If you set the `backupVaultLockCheck` parameter equal to `true`, the control passes only if the EBS volume is backed up in an AWS Backup locked vault.

Backups help you recover more quickly from a security incident. They also strengthen the resilience of your systems. Including Amazon EBS volumes in a backup plan helps you protect your data from unintended loss or deletion.

### Remediation
<a name="ec2-28-remediation"></a>

To add an Amazon EBS volume to an AWS Backup backup plan, see [Assigning resources to a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html) in the *AWS Backup Developer Guide*.

## [EC2.33] EC2 transit gateway attachments should be tagged
<a name="ec2-33"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::TransitGatewayAttachment`

**AWS Config rule:** `tagged-ec2-transitgatewayattachment` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 transit gateway attachment has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the transit gateway attachment doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the transit gateway attachment isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-33-remediation"></a>

To add tags to an EC2 transit gateway attachment, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.34] EC2 transit gateway route tables should be tagged
<a name="ec2-34"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::TransitGatewayRouteTable`

**AWS Config rule:** `tagged-ec2-transitgatewayroutetable` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 transit gateway route table has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the transit gateway route table doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the transit gateway route table isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-34-remediation"></a>

To add tags to an EC2 transit gateway route table, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.35] EC2 network interfaces should be tagged
<a name="ec2-35"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::NetworkInterface`

**AWS Config rule:** `tagged-ec2-networkinterface` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 network interface has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the network interface doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the network interface isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-35-remediation"></a>

To add tags to an EC2 network interface, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.36] EC2 customer gateways should be tagged
<a name="ec2-36"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::CustomerGateway`

**AWS Config rule:** `tagged-ec2-customergateway` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 customer gateway has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the customer gateway doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the customer gateway isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-36-remediation"></a>

To add tags to an EC2 customer gateway, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.37] EC2 Elastic IP addresses should be tagged
<a name="ec2-37"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::EIP`

**AWS Config rule:** `tagged-ec2-eip` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 Elastic IP address has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the Elastic IP address doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the Elastic IP address isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-37-remediation"></a>

To add tags to an EC2 Elastic IP address, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.38] EC2 instances should be tagged
<a name="ec2-38"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::Instance`

**AWS Config rule:** `tagged-ec2-instance` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 instance has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the instance doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the instance isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-38-remediation"></a>

To add tags to an EC2 instance, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.39] EC2 internet gateways should be tagged
<a name="ec2-39"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::InternetGateway`

**AWS Config rule:** `tagged-ec2-internetgateway` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 internet gateway has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the internet gateway doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the internet gateway isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-39-remediation"></a>

To add tags to an EC2 internet gateway, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.40] EC2 NAT gateways should be tagged
<a name="ec2-40"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::NatGateway`

**AWS Config rule:** `tagged-ec2-natgateway` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 network address translation (NAT) gateway has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the NAT gateway doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the NAT gateway isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-40-remediation"></a>

To add tags to an EC2 NAT gateway, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.41] EC2 network ACLs should be tagged
<a name="ec2-41"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::NetworkAcl`

**AWS Config rule:** `tagged-ec2-networkacl` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 network access control list (network ACL) has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the network ACL doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the network ACL isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-41-remediation"></a>

To add tags to an EC2 network ACL, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.42] EC2 route tables should be tagged
<a name="ec2-42"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::RouteTable`

**AWS Config rule:** `tagged-ec2-routetable` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 route table has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the route table doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the route table isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-42-remediation"></a>

To add tags to an EC2 route table, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.43] EC2 security groups should be tagged
<a name="ec2-43"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::SecurityGroup`

**AWS Config rule:** `tagged-ec2-securitygroup` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 security group has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the security group doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the security group isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-43-remediation"></a>

To add tags to an EC2 security group, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.44] EC2 subnets should be tagged
<a name="ec2-44"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::Subnet`

**AWS Config rule:** `tagged-ec2-subnet` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 subnet has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the subnet doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the subnet isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-44-remediation"></a>

To add tags to an EC2 subnet, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.45] EC2 volumes should be tagged
<a name="ec2-45"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::Volume`

**AWS Config rule:** `tagged-ec2-volume` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 volume has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the volume doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the volume isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-45-remediation"></a>

To add tags to an EC2 volume, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.46] Amazon VPCs should be tagged
<a name="ec2-46"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::VPC`

**AWS Config rule:** `tagged-ec2-vpc` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon Virtual Private Cloud (Amazon VPC) has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the Amazon VPC doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the Amazon VPC isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-46-remediation"></a>

To add tags to a VPC, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.47] Amazon VPC endpoint services should be tagged
<a name="ec2-47"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::VPCEndpointService`

**AWS Config rule:** `tagged-ec2-vpcendpointservice` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon VPC endpoint service has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the endpoint service doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the endpoint service isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-47-remediation"></a>

To add tags to an Amazon VPC endpoint service, see [Manage Tags](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#add-remove-endpoint-service-tags) in the [Configure an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html) section of the *AWS PrivateLink Guide*.

## [EC2.48] Amazon VPC flow logs should be tagged
<a name="ec2-48"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::FlowLog`

**AWS Config rule:** `tagged-ec2-flowlog` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon VPC flow log has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the flow log doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the flow log isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-48-remediation"></a>

To add tags to an Amazon VPC flow log, see [Tag a flow log](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-flow-logs.html#modify-tags-flow-logs) in the *Amazon VPC User Guide*.

## [EC2.49] Amazon VPC peering connections should be tagged
<a name="ec2-49"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::VPCPeeringConnection`

**AWS Config rule:** `tagged-ec2-vpcpeeringconnection` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon VPC peering connection has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the peering connection doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the peering connection isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-49-remediation"></a>

To add tags to an Amazon VPC peering connection, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## [EC2.50] EC2 VPN gateways should be tagged
<a name="ec2-50"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::VPNGateway`

**AWS Config rule:** `tagged-ec2-vpngateway` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon EC2 VPN gateway has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the VPN gateway doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the VPN gateway isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-50-remediation"></a>

To add tags to an EC2 VPN gateway, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## [EC2.51] EC2 Client VPN endpoints should have client connection logging enabled
<a name="ec2-51"></a>

**Related requirements:** NIST.800-53.r5 AC-2(12), NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 AU-9(7), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4, NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), NIST.800-171.r2 3.1.12, NIST.800-171.r2 3.1.20, PCI DSS v4.0.1/10.2.1

**Category:** Identify > Logging

**Severity:** Low

**Resource type:** `AWS::EC2::ClientVpnEndpoint`

**AWS Config rule:** [`ec2-client-vpn-connection-log-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html) ``

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS Client VPN endpoint has client connection logging enabled. The control fails if the endpoint doesn't have client connection logging enabled.

Client VPN endpoints allow remote clients to securely connect to resources in a Virtual Private Cloud (VPC) in AWS. Connection logs allow you to track user activity on the VPN endpoint and provides visibility. When you enable connection logging, you can specify the name of a log stream in the log group. If you don't specify a log stream, the Client VPN service creates one for you.

### Remediation
<a name="ec2-51-remediation"></a>

To enable connection logging, see [Enable connection logging for an existing Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-with-connection-logs.html#create-connection-log-existing) in the *AWS Client VPN Administrator Guide*.

## [EC2.52] EC2 transit gateways should be tagged
<a name="ec2-52"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::TransitGateway`

**AWS Config rule:** `tagged-ec2-transitgateway` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an Amazon EC2 transit gateway has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the transit gateway doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the transit gateway isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ec2-52-remediation"></a>

To add tags to an EC2 transit gateway, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*.

## [EC2.53] EC2 security groups should not allow ingress from 0.0.0.0/0 to remote server administration ports
<a name="ec2-53"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/5.3, CIS AWS Foundations Benchmark v3.0.0/5.2, PCI DSS v4.0.1/1.3.1

**Category:** Protect > Secure network configuration > Security group configuration

**Severity:** High

**Resource type:** `AWS::EC2::SecurityGroup`

**AWS Config rule:** [`vpc-sg-port-restriction-check`](https://docs.aws.amazon.com/config/latest/developerguide/vpc-sg-port-restriction-check.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `ipType` | The IP version | String | Not customizable | `IPv4` | 
| `restrictPorts` | List of ports that should reject ingress traffic | IntegerList | Not customizable | `22,3389` | 

This control checks whether an Amazon EC2 security group allows ingress from 0.0.0.0/0 to remote server administration ports (ports 22 and 3389). The control fails if the security group allows ingress from 0.0.0.0/0 to port 22 or 3389.

Security groups provide stateful filtering of ingress and egress network traffic to AWS resources. We recommend that no security group allow unrestricted ingress access to remote server administration ports, such as SSH to port 22 and RDP to port 3389, using either the TDP (6), UDP (17), or ALL (-1) protocols. Permitting public access to these ports increases resource attack surface and the risk of resource compromise.

### Remediation
<a name="ec2-53-remediation"></a>

To update an EC2 security group rule to prohibit ingress traffic to the specified ports, see [Update security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#updating-security-group-rules) in the *Amazon EC2 User Guide*. After selecting a security group in the Amazon EC2 console, choose **Actions, Edit inbound rules**. Remove the rule that allows access to port 22 or port 3389.

## [EC2.54] EC2 security groups should not allow ingress from ::/0 to remote server administration ports
<a name="ec2-54"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/5.4, CIS AWS Foundations Benchmark v3.0.0/5.3, PCI DSS v4.0.1/1.3.1

**Category:** Protect > Secure network configuration > Security group configuration

**Severity:** High

**Resource type:** `AWS::EC2::SecurityGroup`

**AWS Config rule:** [`vpc-sg-port-restriction-check`](https://docs.aws.amazon.com/config/latest/developerguide/vpc-sg-port-restriction-check.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `ipType` | The IP version | String | Not customizable | `IPv6` | 
| `restrictPorts` | List of ports that should reject ingress traffic | IntegerList | Not customizable | `22,3389` | 

This control checks whether an Amazon EC2 security group allows ingress from ::/0 to remote server administration ports (ports 22 and 3389). The control fails if the security group allows ingress from ::/0 to port 22 or 3389.

Security groups provide stateful filtering of ingress and egress network traffic to AWS resources. We recommend that no security group allow unrestricted ingress access to remote server administration ports, such as SSH to port 22 and RDP to port 3389, using either the TDP (6), UDP (17), or ALL (-1) protocols. Permitting public access to these ports increases resource attack surface and the risk of resource compromise.

### Remediation
<a name="ec2-54-remediation"></a>

To update an EC2 security group rule to prohibit ingress traffic to the specified ports, see [Update security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#updating-security-group-rules) in the *Amazon EC2 User Guide*. After selecting a security group in the Amazon EC2 console, choose **Actions, Edit inbound rules**. Remove the rule that allows access to port 22 or port 3389.

## [EC2.55] VPCs should be configured with an interface endpoint for ECR API
<a name="ec2-55"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4)

**Category:** Protect > Secure access management > Access control

**Severity:** Medium

**Resource type:** `AWS::EC2::VPC`, `AWS::EC2::VPCEndpoint`

**AWS Config rule:** [vpc-endpoint-enabled](https://docs.aws.amazon.com/config/latest/developerguide/vpc-endpoint-enabled.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Required | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | --- | 
| serviceNames  | Required  | The name of the service that the control evaluates  | String  | Not customizable  | ecr.api | 
| vpcIds  | Optional  | Comma-separated list of Amazon VPC IDs for VPC endpoints. If provided, the control fails if the services specified in the serviceName parameter don't have one of these VPC endpoints.  | StringList  | Customize with one or more VPC IDs  | No default value  | 

This control checks whether a virtual private cloud (VPC) that you manage has an interface VPC endpoint for Amazon ECR API. The control fails if the VPC doesn't have an interface VPC endpoint for ECR API. This control evaluates resources in a single account.

AWS PrivateLink enables customers to access services hosted on AWS in a highly available and scalable manner, while keeping all the network traffic within the AWS network. Service users can privately access services powered by PrivateLink from their VPC or their on-premises, without using public IPs, and without requiring traffic to traverse across the internet.

### Remediation
<a name="ec2-55-remediation"></a>

To configure a VPC endpoint, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

## [EC2.56] VPCs should be configured with an interface endpoint for Docker Registry
<a name="ec2-56"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4)

**Category:** Protect > Secure access management > Access control

**Severity:** Medium

**Resource type:** `AWS::EC2::VPC`, `AWS::EC2::VPCEndpoint`

**AWS Config rule:** [vpc-endpoint-enabled](https://docs.aws.amazon.com/config/latest/developerguide/vpc-endpoint-enabled.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Required | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | --- | 
| serviceNames  | Required  | The name of the service that the control evaluates  | String  | Not customizable  | ecr.dkr | 
| vpcIds  | Optional  | Comma-separated list of Amazon VPC IDs for VPC endpoints. If provided, the control fails if the services specified in the serviceName parameter don't have one of these VPC endpoints.  | StringList  | Customize with one or more VPC IDs  | No default value  | 

This control checks whether a virtual private cloud (VPC) that you manage has an interface VPC endpoint for Docker Registry. The control fails if the VPC doesn't have an interface VPC endpoint for Docker Registry. This control evaluates resources in a single account.

AWS PrivateLink enables customers to access services hosted on AWS in a highly available and scalable manner, while keeping all the network traffic within the AWS network. Service users can privately access services powered by PrivateLink from their VPC or their on-premises, without using public IPs, and without requiring traffic to traverse across the internet.

### Remediation
<a name="ec2-56-remediation"></a>

To configure a VPC endpoint, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

## [EC2.57] VPCs should be configured with an interface endpoint for Systems Manager
<a name="ec2-57"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4)

**Category:** Protect > Secure access management > Access control

**Severity:** Medium

**Resource type:** `AWS::EC2::VPC`, `AWS::EC2::VPCEndpoint`

**AWS Config rule:** [vpc-endpoint-enabled](https://docs.aws.amazon.com/config/latest/developerguide/vpc-endpoint-enabled.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Required | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | --- | 
| serviceNames  | Required  | The name of the service that the control evaluates  | String  | Not customizable  | ssm | 
| vpcIds  | Optional  | Comma-separated list of Amazon VPC IDs for VPC endpoints. If provided, the control fails if the services specified in the serviceName parameter don't have one of these VPC endpoints.  | StringList  | Customize with one or more VPC IDs  | No default value  | 

This control checks whether a virtual private cloud (VPC) that you manage has an interface VPC endpoint for AWS Systems Manager. The control fails if the VPC doesn't have an interface VPC endpoint for Systems Manager. This control evaluates resources in a single account.

AWS PrivateLink enables customers to access services hosted on AWS in a highly available and scalable manner, while keeping all the network traffic within the AWS network. Service users can privately access services powered by PrivateLink from their VPC or their on-premises, without using public IPs, and without requiring traffic to traverse across the internet.

### Remediation
<a name="ec2-57-remediation"></a>

To configure a VPC endpoint, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

## [EC2.58] VPCs should be configured with an interface endpoint for Systems Manager Incident Manager Contacts
<a name="ec2-58"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4)

**Category:** Protect > Secure access management > Access control

**Severity:** Medium

**Resource type:** `AWS::EC2::VPC`, `AWS::EC2::VPCEndpoint`

**AWS Config rule:** [vpc-endpoint-enabled](https://docs.aws.amazon.com/config/latest/developerguide/vpc-endpoint-enabled.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Required | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | --- | 
| serviceNames  | Required  | The name of the service that the control evaluates  | String  | Not customizable  | ssm-contacts | 
| vpcIds  | Optional  | Comma-separated list of Amazon VPC IDs for VPC endpoints. If provided, the control fails if the services specified in the serviceName parameter don't have one of these VPC endpoints.  | StringList  | Customize with one or more VPC IDs  | No default value  | 

This control checks whether a virtual private cloud (VPC) that you manage has an interface VPC endpoint for AWS Systems Manager Incident Manager Contacts. The control fails if the VPC doesn't have an interface VPC endpoint for Systems Manager Incident Manager Contacts. This control evaluates resources in a single account.

AWS PrivateLink enables customers to access services hosted on AWS in a highly available and scalable manner, while keeping all the network traffic within the AWS network. Service users can privately access services powered by PrivateLink from their VPC or their on-premises, without using public IPs, and without requiring traffic to traverse across the internet.

### Remediation
<a name="ec2-58-remediation"></a>

To configure a VPC endpoint, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

## [EC2.60] VPCs should be configured with an interface endpoint for Systems Manager Incident Manager
<a name="ec2-60"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4)

**Category:** Protect > Secure access management > Access control

**Severity:** Medium

**Resource type:** `AWS::EC2::VPC`, `AWS::EC2::VPCEndpoint`

**AWS Config rule:** [vpc-endpoint-enabled](https://docs.aws.amazon.com/config/latest/developerguide/vpc-endpoint-enabled.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Required | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | --- | 
| serviceNames  | Required  | The name of the service that the control evaluates  | String  | Not customizable  | ssm-incidents | 
| vpcIds  | Optional  | Comma-separated list of Amazon VPC IDs for VPC endpoints. If provided, the control fails if the services specified in the serviceName parameter don't have one of these VPC endpoints.  | StringList  | Customize with one or more VPC IDs  | No default value  | 

This control checks whether a virtual private cloud (VPC) that you manage has an interface VPC endpoint for AWS Systems Manager Incident Manager. The control fails if the VPC doesn't have an interface VPC endpoint for Systems Manager Incident Manager. This control evaluates resources in a single account.

AWS PrivateLink enables customers to access services hosted on AWS in a highly available and scalable manner, while keeping all the network traffic within the AWS network. Service users can privately access services powered by PrivateLink from their VPC or their on-premises, without using public IPs, and without requiring traffic to traverse across the internet.

### Remediation
<a name="ec2-60-remediation"></a>

To configure a VPC endpoint, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

## [EC2.170] EC2 launch templates should use Instance Metadata Service Version 2 (IMDSv2)
<a name="ec2-170"></a>

**Related requirements:** PCI DSS v4.0.1/2.2.6

**Category:** Protect > Network Security

**Severity:** Low

**Resource type:** `AWS::EC2::LaunchTemplate`

**AWS Config rule:** [ec2-launch-template-imdsv2-check](https://docs.aws.amazon.com/config/latest/developerguide/ec2-launch-template-imdsv2-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EC2 launch template is configured with Instance Metadata Service Version 2 (IMDSv2). The control fails if `HttpTokens` is set to `optional`.

Running resources on supported software versions ensures optimal performance, security, and access to the latest features. Regular updates safeguard against vulnerabilities, which help ensure a stable and efficient user experience.

### Remediation
<a name="ec2-170-remediation"></a>

To require IMDSv2 on an EC2 launch template, see [Configure the Instance Metadata Service options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the *Amazon EC2 User Guide*.

## [EC2.171] EC2 VPN connections should have logging enabled
<a name="ec2-171"></a>

**Related requirements:** CIS AWS Foundations Benchmark v3.0.0/5.3, PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::EC2::VPNConnection`

**AWS Config rule:** [ec2-vpn-connection-logging-enabled](https://docs.aws.amazon.com/config/latest/developerguide/ec2-vpn-connection-logging-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS Site-to-Site VPN connection has Amazon CloudWatch Logs enabled for both tunnels. The control fails if a Site-to-Site VPN connection doesn't have CloudWatch Logs enabled for both tunnels.

AWS Site-to-Site VPN logs provide you with deeper visibility into your Site-to-Site VPN deployments. With this feature, you have access to Site-to-Site VPN connection logs that provide details on IP Security (IPsec) tunnel establishment, Internet Key Exchange (IKE) negotiations, and dead peer detection (DPD) protocol messages. Site-to-Site VPN logs can be published to CloudWatch Logs. This feature provides customers with a single consistent way to access and analyze detailed logs for all of their Site-to-Site VPN connections.

### Remediation
<a name="ec2-171-remediation"></a>

To enable tunnel logging on an EC2 VPN connection, see [AWS Site-to-Site VPN logs](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-logs.html#enable-logs) in the *AWS Site-to-Site VPN User Guide*.

## [EC2.172] EC2 VPC Block Public Access settings should block internet gateway traffic
<a name="ec2-172"></a>

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** Medium

**Resource type:** `AWS::EC2::VPCBlockPublicAccessOptions`

**AWS Config rule:** `ec2-vpc-bpa-internet-gateway-blocked` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `vpcBpaInternetGatewayBlockMode` | String value of the VPC BPA options mode. | Enum | `block-bidirectional`, `block-ingress` | No default value | 

This control checks whether Amazon EC2 VPC Block Public Access (BPA) settings are configured to block internet gateway traffic for all Amazon VPCs in the AWS account. The control fails if VPC BPA settings aren't configured to block internet gateway traffic. For the control to pass, the VPC BPA `InternetGatewayBlockMode` must be set to `block-bidirectional` or `block-ingress`. If the parameter `vpcBpaInternetGatewayBlockMode` is provided, the control passes only if the VPC BPA value for `InternetGatewayBlockMode` matches the parameter.

Configuring the VPC BPA settings for your account in an AWS Region lets you block resources in VPCs and subnets that you own in that Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If you need specific VPCs and subnets to be able to reach or be reachable from the internet, you can exclude them by configuring VPC BPA exclusions. For instructions on creating and deleting exclusions, see [Create and delete exclusions](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa-basics.html#security-vpc-bpa-exclusions) in the *Amazon VPC User Guide*.

### Remediation
<a name="ec2-172-remediation"></a>

To enable bi-directional BPA at the account level, see [Enable BPA bidirectional mode for your account](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa-basics.html#security-vpc-bpa-enable-bidir) in the *Amazon VPC User Guide*. To enable ingress-only BPA, see [Change VPC BPA mode to ingress-only](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa-basics.html#security-vpc-bpa-ingress-only). To enable VPC BPA at the Organization level, see [Enable VPC BPA at the Organization level](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa-basics.html#security-vpc-bpa-exclusions-orgs).

## [EC2.173] EC2 Spot Fleet requests with launch parameters should enable encryption for attached EBS volumes
<a name="ec2-173"></a>

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::EC2::SpotFleet`

**AWS Config rule:** [ec2-spot-fleet-request-ct-encryption-at-rest](https://docs.aws.amazon.com/config/latest/developerguide/ec2-spot-fleet-request-ct-encryption-at-rest.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EC2 Spot Fleet request that specifies launch parameters is configured to enable encryption for all Amazon Elastic Block Store (Amazon EBS) volumes attached to EC2 instances. The control fails if the Spot Fleet request specifies launch parameters and doesn't enable encryption for one or more EBS volumes specified in the request.

For an additional layer of security, you should enable encryption for Amazon EBS volumes. Encryption operations then occur on the servers that host Amazon EC2 instances, which helps ensure the security of both data at rest and data in transit between an instance and its attached EBS storage. Amazon EBS encryption is a straightforward encryption solution for EBS resources associated with your EC2 instances. With EBS encryption, you aren't required to build, maintain, and secure your own key management infrastructure. EBS encryption uses AWS KMS keys when creating encrypted volumes.

**Notes**  
This control doesn't generate findings for Amazon EC2 Spot Fleet requests that use launch templates. It also doesn't generate findings for Spot Fleet requests that don't explicitly specify a value for the `encrypted` parameter.

### Remediation
<a name="ec2-173-remediation"></a>

There's no direct way to encrypt an existing, unencrypted Amazon EBS volume. You can encrypt a new volume only when you create it.

However, if you enable encryption by default, Amazon EBS encrypts new volumes by using your default key for EBS encryption. If you don't enable encryption by default, you can enable encryption when you create an individual volume. In both cases, you can override the default key for EBS encryption and choose a customer managed AWS KMS key. For more information about EBS encryption, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) in the *Amazon EBS User Guide*.

For information about creating an Amazon EC2 Spot Fleet request, see [Create a Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-spot-fleet.html) in the *Amazon Elastic Compute Cloud User Guide*.

## [EC2.174] EC2 DHCP option sets should be tagged
<a name="ec2-174"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::DHCPOptions`

**AWS Config rule:** [ec2-dhcp-options-tagged](https://docs.aws.amazon.com/config/latest/developerguide/ec2-dhcp-options-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an Amazon EC2 DHCP option set has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the option set doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the option set doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="ec2-174-remediation"></a>

For information about adding tags to an Amazon EC2 DHCP option set, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## [EC2.175] EC2 launch templates should be tagged
<a name="ec2-175"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::LaunchTemplate`

**AWS Config rule:** [ec2-launch-template-tagged](https://docs.aws.amazon.com/config/latest/developerguide/ec2-launch-template-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an Amazon EC2 launch template has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the launch template doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the launch template doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="ec2-175-remediation"></a>

For information about adding tags to an Amazon EC2 launch template, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## [EC2.176] EC2 prefix lists should be tagged
<a name="ec2-176"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::PrefixList`

**AWS Config rule:** [ec2-prefix-list-tagged](https://docs.aws.amazon.com/config/latest/developerguide/ec2-prefix-list-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an Amazon EC2 prefix list has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the prefix list doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the prefix list doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="ec2-176-remediation"></a>

For information about adding tags to an Amazon EC2 prefix list, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## [EC2.177] EC2 traffic mirror sessions should be tagged
<a name="ec2-177"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::TrafficMirrorSession`

**AWS Config rule:** [ec2-traffic-mirror-session-tagged](https://docs.aws.amazon.com/config/latest/developerguide/ec2-traffic-mirror-session-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an Amazon EC2 traffic mirror session has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the session doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the session doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="ec2-177-remediation"></a>

For information about adding tags to an Amazon EC2 traffic mirror session, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## [EC2.178] EC2 traffic mirror filters should be tagged
<a name="ec2-178"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::TrafficMirrorFilter`

**AWS Config rule:** [ec2-traffic-mirror-filter-tagged](https://docs.aws.amazon.com/config/latest/developerguide/ec2-traffic-mirror-filter-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an Amazon EC2 traffic mirror filter has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the filter doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the filter doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="ec2-178-remediation"></a>

For information about adding tags to an Amazon EC2 traffic mirror filter, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## [EC2.179] EC2 traffic mirror targets should be tagged
<a name="ec2-179"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::EC2::TrafficMirrorTarget`

**AWS Config rule:** [ec2-traffic-mirror-target-tagged](https://docs.aws.amazon.com/config/latest/developerguide/ec2-traffic-mirror-target-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an Amazon EC2 traffic mirror target has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the target doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the target doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="ec2-179-remediation"></a>

For information about adding tags to an Amazon EC2 traffic mirror target, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## [EC2.180] EC2 network interfaces should have source/destination checking enabled
<a name="ec2-180"></a>

**Category:** Protect > Network Security

**Severity:** Medium

**Resource type:** `AWS::EC2::NetworkInterface`

**AWS Config rule:** [ec2-enis-source-destination-check-enabled](https://docs.aws.amazon.com/config/latest/developerguide/ec2-enis-source-destination-check-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether source/destination checking is enabled for an Amazon EC2 elastic network interface (ENI) that's managed by users. The control fails if source/destination checking is disabled for the user-managed ENI. This control checks only the following types of ENIs: `aws_codestar_connections_managed`, `branch`, `efa`, `interface`, `lambda`, and `quicksight`.

Source/destination checking for Amazon EC2 instances and attached ENIs should be enabled and configured consistently across your EC2 instances. Each ENI has its own setting for source/destination checks. If source/destination checking is enabled, Amazon EC2 enforces source/destination address validation, which ensures that an instance is either the source or the destination of any traffic that it receives. This provides an additional layer of network security by preventing resources from handling unintended traffic and preventing IP address spoofing.

**Note**  
If you're using an EC2 instance as a NAT instance and you disabled source/destination checking for its ENI, you can use a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) instead.

### Remediation
<a name="ec2-180-remediation"></a>

For information about enabling source/destination checks for an Amazon EC2 ENI, see [Modify network interface attributes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-network-interface-attributes.html#modify-source-dest-check) in the *Amazon EC2 User Guide*.

## [EC2.181] EC2 launch templates should enable encryption for attached EBS volumes
<a name="ec2-181"></a>

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::EC2::LaunchTemplate`

**AWS Config rule:** [ec2-launch-templates-ebs-volume-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/ec2-launch-templates-ebs-volume-encrypted.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EC2 launch template enables encryption for all attached EBS volumes. The control fails if the encryption parameter is set to `False` for any EBS volumes specified by the EC2 launch template.

Amazon EBS encryption is a straightforward encryption solution for EBS resources that are associated with Amazon EC2 instances. With EBS encryption, you aren't required to build, maintain, and secure your own key management infrastructure. EBS encryption uses AWS KMS keys when creating encrypted volumes and snapshots. Encryption operations occur on the servers that host EC2 instances, which helps ensure the security of data at rest and data in transit between an EC2 instance and its attached EBS storage. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) in the *Amazon EBS User Guide*.

You can enable EBS encryption during manual launches of individual EC2 instances. However, there are several benefits to using EC2 launch templates and configuring encryption settings in those templates. You can enforce encryption as a standard and ensure the use of consistent encryption settings. You can also reduce the risk of error and security gaps that might occur with manual launches of instances.

**Note**  
When this control checks an EC2 launch template, it only evaluates EBS encryption settings that are explicitly specified by the template. The evaluation doesn’t include encryption settings that are inherited from account-level EBS encryption settings, AMI block device mappings, or source snapshot encryption statuses.

### Remediation
<a name="ec2-181-remediation"></a>

After you create an Amazon EC2 launch template, you can't modify it. However, you can create a new version of a launch template and change the encryption settings in that new version of the template. You can also specify the new version as the default version of the launch template. Then, if you launch an EC2 instance from a launch template and don't specify a template version, EC2 uses the settings of the default version when it launches the instance. For more information, see [Modify a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-launch-template-versions.html) in the *Amazon EC2 User Guide*.

## [EC2.182] Block public access settings should be enabled for Amazon EBS snapshots
<a name="ec2-182"></a>

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:** `AWS::EC2::SnapshotBlockPublicAccess`

**AWS Config rule:** [ebs-snapshot-block-public-access](https://docs.aws.amazon.com/config/latest/developerguide/ebs-snapshot-block-public-access.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether account level block public access is enabled to prevent sharing of Amazon EBS snapshots to all. The control fails if block public access is not enabled to block sharing of Amazon EBS snapshots to all.

To prevent public sharing of your Amazon EBS snapshots, you can enable block public access for snapshots. Once block public access for snapshots is enabled in a Region, any attempt to publicly share snapshots in that Region is automatically blocked. This helps improve the security of the snapshots and protect the snapshot data from unauthorized or unintended access. 

### Remediation
<a name="ec2-182-remediation"></a>

To enable block public access for snapshots, see [Configure block public access for Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-enable.html) in the *Amazon EBS User Guide*. For **Block public access**, choose **Block all public access**.

## [EC2.183] EC2 VPN connections should use IKEv2 protocol
<a name="ec2-183"></a>

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::EC2::VPNConnection`

**AWS Config rule:** [ec2-vpn-connection-ike-version-check](https://docs.aws.amazon.com/config/latest/developerguide/ec2-vpn-connection-ike-version-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS Site-to-Site VPN connection is configured to use IKEv2 protocol. The control fails if a Site-to-Site VPN connection allows IKEv1 protocol or does not explicitly restrict to IKEv2 on all VPN tunnels.

IKEv2 provides stronger cryptographic algorithms and improved security features compared to the legacy IKEv1 protocol, including built-in protection against denial-of-service attacks and enhanced authentication mechanisms. IKEv1 has known vulnerabilities and weaknesses in its key exchange process that can be exploited by attackers to compromise VPN tunnel security. By enforcing IKEv2-only connections, you reduce your attack surface and ensure VPN communications use modern, industry-standard encryption protocols that better protect data in transit.

### Remediation
<a name="ec2-183-remediation"></a>

To update the IKE version for a VPN tunnel on an EC2 VPN connection, see [Modify AWS Site-to-Site VPN tunnel options](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-tunnel-options.html) in the *AWS Site-to-Site VPN User Guide*.