# MemoryDB security

Security for MemoryDB is managed at three levels:

- To control who can perform management actions on MemoryDB clusters and nodes, you use AWS Identity and Access Management (IAM).
  When you connect to AWS using IAM credentials, your AWS account must have IAM policies that grant the permissions required to perform operations. For more information, see [Identity and access management in MemoryDB](iam.md "iam.md")
- To control access levels to clusters, you create users with specified permissions and assign them to the Access Control Lists (ACL). The ACL, in turn,
  is then associated with one or more clusters. For more information, see [Authenticating users with Access Control Lists (ACLs)](clusters.md "clusters.md").
- MemoryDB clusters must be created in a virtual private cloud (VPC) based on the Amazon VPC service. To control which devices and Amazon EC2 instances
  can open connections to the endpoint and port of the node for MemoryDB clusters in a VPC, you use a VPC security group.
  You can make these endpoint and port connections using Transport Layer Security (TLS)/Secure Sockets Layer (SSL). In addition, firewall rules at your company can control
  whether devices running at your company can open connections to a MemoryDB cluster. For more information on VPCs, see [MemoryDB and Amazon VPC](vpcs.md "vpcs.md").
  For information about configuring security, see [Security in MemoryDB](security.md "security.md").
