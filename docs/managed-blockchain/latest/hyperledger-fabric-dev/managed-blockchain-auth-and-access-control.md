# Authentication and Access Control for AMB Access Hyperledger Fabric

AWS Identity and Access Management (IAM) permissions policies, VPC endpoint services powered by AWS
PrivateLink, and Amazon EC2 security groups provide the primary means for you to control
access to Amazon Managed Blockchain (AMB). In addition to these AWS services, open-source frameworks that
run on AMB Access have authentication and access control features that you can
configure.

IAM permissions policies are associated with AWS users in your account and
determine who has access to what. Permissions policies specify the actions that each
user can perform using AMB Access and other AWS services. VPC endpoint services allow each
AMB Access network member to connect privately to AMB Access resources. Amazon EC2 security groups act
as virtual firewalls and determine the inbound and outbound network traffic that is
allowed between AMB Access resources and other Amazon EC2 resources. In AMB Access, these security
groups are associated with the VPC endpoint in your account and with any framework
clients that run on AWS, such as a Hyperledger Fabric client running on an Amazon EC2
instance.

Before you configure authentication and access control using AWS services and
open-source features, we recommend that you review the following resources:

- For more information about IAM and IAM permissions policies, see [Identity and Access Management for Amazon Managed Blockchain (AMB) Hyperledger Fabric](security-iam.md "security-iam.md"). We also recommend
  [What is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and
  [IAM JSON Policy
  Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.
- For more information about VPC endpoints, see [Create an Interface VPC Endpoint for Amazon Managed Blockchain (AMB) Hyperledger Fabric](managed-blockchain-endpoints.md "managed-blockchain-endpoints.md") and [VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon VPC User Guide_.
- For more information about Amazon EC2 security groups, see [Configuring Security Groups for Amazon Managed Blockchain (AMB) Hyperledger Fabric](managed-blockchain-security-sgs.md "managed-blockchain-security-sgs.md") and [Amazon EC2 Security Groups for Linux Instances](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md") in the _Amazon EC2 User Guide_.
- For more information about the Hyperledger Fabric Certificate Authority (CA), see [Certificate Authority (CA) Setup](https://hyperledger-fabric-ca.readthedocs.io/en/latest/ "https://hyperledger-fabric-ca.readthedocs.io/en/latest/") in the Hyperledger Fabric documentation.
- For more information about the supported Hyperledger Fabric 2.2 application access control lists, see [Application Access Control Lists](https://hyperledger-fabric.readthedocs.io/en/release-2.2/access_control.html "https://hyperledger-fabric.readthedocs.io/en/release-2.2/access_control.html") in the Hyperledger Fabric documentation.
