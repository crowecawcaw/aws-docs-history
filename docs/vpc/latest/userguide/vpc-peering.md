# Connect VPCs using VPC peering

A VPC peering connection is a networking feature that enables secure and direct communication between two virtual private clouds (VPCs) within the AWS infrastructure. This private connection allows resources in the peered VPCs to interact with each other as if they were part of the same network, eliminating the need to traverse the public internet.

![A VPC peering connection](images/peering-intro-diagram.png)
The process of creating a VPC peering connection leverages the existing VPC infrastructure
to establish this connection, without the requirement of a gateway, AWS Site-to-Site VPN, or any additional
physical hardware. This design ensures that there is no single point of failure or bandwidth
bottleneck.

One of the key advantages of a VPC peering connection is the ability to connect VPCs across
different AWS accounts or even different AWS Regions. This flexibility allows organizations
to seamlessly integrate their cloud resources, whether they are within the same account or
spread across multiple accounts and geographic locations. The private nature of the connection
also ensures that all data traffic between the peered VPCs remains within the AWS network,
without ever traversing the public internet.

The use cases for VPC peering connections are wide-ranging. Organizations can leverage this
feature to enable secure communication between different tiers of an application (such as web
servers and database servers), facilitate the sharing of resources between multiple teams or
business units, or even enable hybrid cloud architectures by connecting on-premises networks to
their AWS VPCs.

A VPC peering connection is a networking connection between two VPCs that enables you to
route traffic between them privately. Resources in peered VPCs can communicate with each other
as if they are within the same network. You can create a VPC peering connection between your own
VPCs, with a VPC in another AWS account, or with a VPC in a different AWS Region. Traffic
between peered VPCs never traverses the public internet.

For more information, see the [Amazon VPC Peering Guide](../peering.md "../peering.md").
