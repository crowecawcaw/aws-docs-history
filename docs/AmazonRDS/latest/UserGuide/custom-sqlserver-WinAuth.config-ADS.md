

# Configure Microsoft Active Directory using Directory Service
<a name="custom-sqlserver-WinAuth.config-ADS"></a>

AWS Managed Microsoft AD creates a fully managed Microsoft Active Directory in AWS that is powered by Windows Server 2019 and operates at the 2016 Forest and Domain functional levels. Directory Service creates the domain controllers in different subnets in an Amazon VPC, making your directory highly available even in the event of failure.

To create a directory with AWS Managed Microsoft AD, see [Getting started with AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started.html) in the *AWS Directory Service Administration Guide*.

## Configure your network connectivity
<a name="custom-sqlserver-WinAuth.config-ADS.network"></a>

### Enable cross-VPC traffic between the directory and the DB instance
<a name="custom-sqlserver-WinAuth.config-ADS.network.x-vpc"></a>

To locate the directory and the DB instance in the same VPC, skip this step and move on to next step in [Network configuration port rules](custom-sqlserver-WinAuth.NWConfigPorts.md).

To locate the directory and the DB instance in different VPCs, configure cross-VPC traffic using VPC peering or AWS Transit Gateway. For more information about using VPC peering, see [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) in the *Amazon VPC Peering Guide* and [What is AWS Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) in the *Amazon VPC Transit Gateways*.

**Enable cross-VPC traffic using VPC peering**

1. Set up appropriate VPC routing rules to ensure that network traffic can flow both ways.

1. Allow the DB instance's security group to recieve inbound traffic from the directory's security group. For more information, see [Network configuration port rules](custom-sqlserver-WinAuth.NWConfigPorts.md).

1. Network access control list (ACL) must not block traffic.

If a different AWS account owns the directory, you must share the directory. To share the directory with AWS account within which the RDS Custom for SQL Server instance is by following the [ Tutorial: Sharing your AWS Managed Microsoft AD for seamless EC2 domain-join](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.html) in the *AWS Directory Service Administration Guide*.

**Sharing a directory betweens AWS accounts**

1. Sign in to the Directory Service console using the account for the DB instance and check if the domain has the `SHARED` status before proceeding.

1. After signing in to the Directory Service console using the account for the DB instance, note the **Directory ID** value. You use this ID to join the DB instance to the domain.

## Configure DNS resolution
<a name="custom-sqlserver-WinAuth.config-ADS.DNS"></a>

When you create a directory with AWS Managed Microsoft AD, Directory Service creates two domain controllers and adds the DNS service on your behalf.

If you have an existing AWS Managed Microsoft AD or plan on launching one in a VPC other than your RDS Custom for SQL Server DB instance, configure the VPC DNS resolver to forward queries for certain domains with a Route 53 outbound and resolver rule, see [ Configure a Route 53 Resolver outbound endpoint to resolve DNS records](https://repost.aws/knowledge-center/route53-resolve-with-outbound-endpoint).