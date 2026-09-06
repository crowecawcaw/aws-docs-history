

# Amazon Inspector finding types
<a name="findings-types"></a>

 This section describes the different finding types in Amazon Inspector. 

**Topics**
+ [Package vulnerability](#findings-types-package)
+ [Code vulnerability](#findings-types-code)
+ [Network reachability](#findings-types-network)

## Package vulnerability
<a name="findings-types-package"></a>

Package vulnerability findings identify software packages in your AWS environment that are exposed to Common Vulnerabilities and Exposures (CVEs). Attackers can exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems. The CVE system is a reference method for publicly known information security vulnerabilities and exposures. For more information, see [https://www.cve.org/](https://www.cve.org/). 

Amazon Inspector can generate package vulnerability findings for EC2 instances, ECR container images, and Lambda functions. Package vulnerability findings include details that are unique to this type of finding. These details are the [Inspector score and vulnerability intelligence](findings-understanding-score.md).

For Windows EC2 instances, package vulnerability findings can be identified by Microsoft Knowledge Base (KB) IDs instead of individual CVEs. If a KB update addresses one or more CVEs, Amazon Inspector reports a single KB finding, for example `KB5023697`, instead of a separate finding for each CVE. A KB finding specifies the highest CVSS score, EPSS score, and exploit availability across all constituent CVEs.

## Code vulnerability
<a name="findings-types-code"></a>

 Code vulnerability findings help identify lines of code that can be exploited. Code vulnerabilities include missing encryption, data leaks, injection flaws, and weak cryptography. Amazon Inspector generates code vulnerability findings through [Lambda function scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html) and its [Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) feature. 

 Amazon Inspector evaluates Lambda function application code using automated reasoning and machine learning to analyzes application code for overall security compliance. It identifies policy violations and vulnerabilities based on internal detectors developed in collaboration with Amazon Q. For a list of possible detections, see [Amazon Q Detector Library](https://docs.aws.amazon.com/amazonq/detector-library/). 

 Code scanning captures snippets of code to highlight detected vulnerabilities. For example, a code snippet might show hardcoded credentials or other sensitive materials in plaintext. Amazon Q stores code snippets associated with code vulnerabilities. By default, your code is encrypted with an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). However, you can create a customer managed key to encrypt your code if you want more control over this information. For more information, see [Encryption at rest for code in your findings](encryption-rest.md#encryption-code-snippets). 

**Note**  
 The delegated administrator for an organization cannot view code snippets that belong to member accounts. 

## Network reachability
<a name="findings-types-network"></a>

Network reachability findings indicate that there are open network paths to Amazon EC2 instances in your environment. These findings appear when your TCP and UDP ports are reachable from the VPC edges, such as an internet gateway (including instances behind Application Load Balancers or Classic Load Balancers), a VPC peering connection, or a VPN through a virtual gateway. These findings highlight network configurations that may be overly permissive, such as mismanaged security groups, Access Control Lists, or internet gateways, or that may allow for potentially malicious access. 

 Amazon Inspector only generates network reachability findings for Amazon EC2 instances. Amazon Inspector performs scans for network reachability findings every 12 hours once Amazon Inspector is enabled. 

Amazon Inspector evaluates the following configurations when scanning for network paths: 
+ [Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
+ [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
+ [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
+ [Elastic Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
+ [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)
+ [Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
+ [Network Access Control Lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
+ [Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
+ [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html)
+ [Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
+ [Virtual Private Clouds](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)
+ [Virtual Private Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-create-vpg)
+ [VPC endpoints](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html)
+ [VPC gateway endpoints](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html)
+ [VPC peering connections](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
+ [VPN connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html)