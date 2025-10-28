# Required VPC endpoints and DNS

configuration

AWS Management Console Private Access requires the following two VPC endpoints per Region. Replace
`region` with your own Region information.

1. com.amazonaws.`region`.console for AWS Management Console
2. com.amazonaws.`region`.signin for AWS Sign-In

###### Note

Always provision infrastructure and networking connectivity to the US East (N. Virginia)
(us-east-1) Region, regardless of other Regions you use with the AWS Management Console. You can use
AWS Transit Gateway to set up connectivity between the US East (N. Virginia) and every other Region.
For more information, see [Getting started with transit
gateways](../../../vpc/latest/tgw/tgw-getting-started.md "../../../vpc/latest/tgw/tgw-getting-started.md") in the _Amazon VPC Transit Gateways guide_. You can also use Amazon VPC
peering. For more information, see [What is VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") in the
_Amazon VPC Peering Guide_. To compare these options, see [Amazon VPC-to-Amazon VPC connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md") in the _Amazon Virtual
Private Cloud Connectivity Options whitepaper_.

###### Topics

- [DNS configuration for
  AWS Management Console and AWS Sign-In](dns-configuration-console-signin.md "dns-configuration-console-signin.md")
- [VPC endpoints and DNS
  configuration for AWS services in the AWS Management Console](vpc-dns-configuration-aws-services.md "vpc-dns-configuration-aws-services.md")
