# Configure Microsoft Active

Directory using AWS Directory Service

AWS Managed Microsoft AD creates a fully managed Microsoft Active Directory in AWS that is powered
by Windows Server 2019 and operates at the 2012 R2 Forest and Domain functional levels. AWS Directory Service creates the domain controllers in different subnets in an
Amazon VPC, making your directory highly available even in the event of failure.

To create a directory with AWS Managed Microsoft AD, see [Getting started with AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md") in
the _AWS Directory Service Administration Guide_.

## Configure your network connectivity

### Enable cross-VPC traffic between the directory and the DB instance

To locate the directory and the DB instance in the same VPC, skip this step and
move on to next step in [Network configuration port rules](custom-sqlserver-WinAuth.md "custom-sqlserver-WinAuth.md").

To locate the directory and the DB instance in different VPCs, configure cross-VPC traffic using VPC peering or AWS Transit Gateway.
For more information about using VPC peering,
see [What is VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") in the
_Amazon VPC Peering Guide_ and [What is AWS Transit Gateway?](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md")
in the _Amazon VPC Transit Gateways_.

###### Enable cross-VPC traffic using VPC peering

1. Set up appropriate VPC routing rules to ensure that network traffic can flow both ways.
2. Allow the DB instance's security group to recieve inbound traffic from the directory's security group.
   For more information, see [Network configuration port rules](custom-sqlserver-WinAuth.md "custom-sqlserver-WinAuth.md").
3. Network access control list (ACL) must not block traffic.

If a different AWS account owns the directory, you must share the directory. To share the directory with
AWS account within which the RDS Custom for SQL Server instance is by following the
[Tutorial: Sharing your AWS Managed Microsoft AD for seamless EC2 domain-join](../../../directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.md "../../../directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.md") in the _AWS Directory Service Administration Guide_.

###### Sharing a directory betweens AWS accounts

1. Sign in to the AWS Directory Service console using the account for the DB instance and check if the domain has the `SHARED`
   status before proceeding.
2. After signing in to the AWS Directory Service console using the account for the DB instance,
   note the **Directory ID** value. You use this ID to join the DB instance to the domain.

## Configure DNS resolution

When you create a directory with AWS Managed Microsoft AD, AWS Directory Service creates two domain controllers and adds
the DNS service on your behalf.

If you have an existing AWS Managed Microsoft AD or plan on launching one in a VPC other than your RDS Custom for SQL Server DB instance,
configure the VPC DNS resolver to forward queries for certain domains with a Route 53 outbound and resolver rule,
see [Configure a Route 53 Resolver outbound endpoint to resolve DNS records](https://repost.aws/knowledge-center/route53-resolve-with-outbound-endpoint "https://repost.aws/knowledge-center/route53-resolve-with-outbound-endpoint").
