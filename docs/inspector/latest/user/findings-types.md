# Amazon Inspector finding types

This section describes the different finding types in Amazon Inspector.

###### Topics

- [Package vulnerability](#findings-types-package "#findings-types-package")
- [Code vulnerability](#findings-types-code "#findings-types-code")
- [Network reachability](#findings-types-network "#findings-types-network")

## Package vulnerability

Package vulnerability findings identify software packages in your AWS environment
that are exposed to Common Vulnerabilities and Exposures (CVEs). Attackers can exploit
these unpatched vulnerabilities to compromise the confidentiality, integrity, or
availability of data, or to access other systems. The CVE system is a reference method
for publicly known information security vulnerabilities and exposures. For more
information, see [https://www.cve.org/](https://www.cve.org/ "https://www.cve.org/").

Amazon Inspector can generate package vulnerability findings for EC2 instances, ECR container images, and
Lambda functions. Package vulnerability findings have additional details unique to this finding type, these are the [Inspector score and vulnerability intelligence](findings-understanding-score.md "findings-understanding-score.md").

## Code vulnerability

Code vulnerability findings help identify lines of code that can be exploited.
Code vulnerabilities include missing encryption, data leaks, injection flaws, and weak cryptography.
Amazon Inspector generates code vulnerability findings through [Lambda function scanning](scanning-lambda.md "scanning-lambda.md") and its [Code Security](code-security-assessments.md "code-security-assessments.md") feature.

Amazon Inspector evaluates Lambda function application code using automated reasoning and machine learning to analyzes application code for overall security compliance.
It identifies policy violations and vulnerabilities based on internal detectors developed in collaboration with Amazon Q.
For a list of possible detections, see [Amazon Q Detector Library](../../../amazonq/detector-library.md "../../../amazonq/detector-library.md").

Code scanning captures snippets of code to highlight detected vulnerabilities.
For example, a code snippet might show hardcoded credentials or other sensitive materials in plaintext.
Amazon Q stores code snippets associated with code vulnerabilities.
By default, your code is encrypted with an [AWS owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk").
However, you can create a customer managed key to encrypt your code if you want more control over this information.
For more information, see [Encryption at rest for code in your findings](encryption-rest.md#encryption-code-snippets "encryption-rest.md#encryption-code-snippets").

###### Note

The delegated administrator for an organization cannot view code snippets that belong to member accounts.

## Network reachability

Network reachability findings indicate that there are open network paths to Amazon EC2
instances in your environment. These findings appear when your TCP and UDP ports are
reachable from the VPC edges, such as an internet gateway (including instances behind
Application Load Balancers or Classic Load Balancers), a VPC peering connection, or a VPN through a virtual gateway. These
findings highlight network configurations that may be overly permissive, such as
mismanaged security groups, Access Control Lists, or internet gateways, or that may
allow for potentially malicious access.

Amazon Inspector only generates network reachability findings for Amazon EC2 instances.
Amazon Inspector performs scans for network reachability findings every 12 hours once Amazon Inspector is enabled.

Amazon Inspector evaluates the following configurations when scanning for network paths:

- [Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md")
- [Application Load Balancers](../../../elasticloadbalancing/latest/application/introduction.md "../../../elasticloadbalancing/latest/application/introduction.md")
- [Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")
- [Elastic Load Balancers](../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md "../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md")
- [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md")
- [Internet Gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md")
- [Network Access Control Lists](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md")
- [Route Tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md")
- [Security Groups](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md")
- [Subnets](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md")
- [Virtual Private Clouds](../../../vpc/latest/userguide/how-it-works.md "../../../vpc/latest/userguide/how-it-works.md")
- [Virtual Private Gateways](../../../vpc/latest/userguide/SetUpVPNConnections.md#vpn-create-vpg "../../../vpc/latest/userguide/SetUpVPNConnections.md#vpn-create-vpg")
- [VPC endpoints](../../../whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.md "../../../whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.md")
- [VPC gateway endpoints](../../../whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.md "../../../whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.md")
- [VPC peering connections](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md")
- [VPN connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md")
