# Configure a virtual private cloud

Amazon Virtual Private Cloud (VPC) is a fundamental building block, allowing you to provision a logically isolated virtual network within the AWS cloud. By creating your own VPC, you gain full control over the networking environment, including the ability to define IP address ranges, subnets, routing tables, and connectivity options.

Your AWS account contains a default VPC for each AWS Region. This default VPC comes pre-configured with settings that make it a convenient option for quickly launching resources. However, the default VPC may not always align with your long-term networking needs. This is where creating additional VPCs can be advantageous.

Creating additional VPCs offers several advantages over relying on the default VPC that comes provisioned with every new AWS account. With a self-managed VPC, you can architect the network topology to align precisely with your specific requirements, whether that's implementing a multi-tier application, connecting to on-premises resources, or segregating workloads by department or business unit.

In addition, creating multiple VPCs can enable greater security and isolation between your different applications or business units. Each VPC acts as a separate, virtual network, allowing you to apply distinct security policies, access controls, and routing configurations tailored to each environment.

Ultimately, the decision to use the default VPC or create one (or more) custom VPCs should be based on your specific application requirements, security needs, and long-term scalability goals. Investing the time to thoughtfully design your VPC infrastructure can pay dividends in the form of a robust, secure, and adaptable cloud networking foundation.

###### Contents

- [VPC basics](vpc-subnet-basics.md "vpc-subnet-basics.md")
- [VPC configuration options](create-vpc-options.md "create-vpc-options.md")
- [Default VPCs](default-vpc.md "default-vpc.md")
- [Create a VPC](create-vpc.md "create-vpc.md")
- [Visualize the resources in your VPC](view-vpc-resource-map.md "view-vpc-resource-map.md")
- [Add or remove CIDR block](add-ipv4-cidr.md "add-ipv4-cidr.md")
- [DHCP option sets](VPC_DHCP_Options.md "VPC_DHCP_Options.md")
- [DNS attributes](vpc-dns.md "vpc-dns.md")
- [Network Address Usage](network-address-usage.md "network-address-usage.md")
- [Share a VPC subnet](vpc-sharing.md "vpc-sharing.md")
- [Extend a VPC to other Zones](Extend_VPCs.md "Extend_VPCs.md")
- [Delete your VPC](delete-vpc.md "delete-vpc.md")
- [Generate IaC from console actions](vpcs-automate-c2c.md "vpcs-automate-c2c.md")
