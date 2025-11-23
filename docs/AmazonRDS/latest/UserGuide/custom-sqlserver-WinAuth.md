# Configure Self-Managed or On-premise AD

To join your on-premise or self-managed Microsoft AD to your RDS Custom for SQL Server DB instance, your Active Domain must be configured as follows:

- Define the subnets in the VPC associated with your RDS Custom for SQL Server DB instance in your self-managed
  or on-premises AD. Confirm there are no conflicts between the subnets in your VPC and the subnets in your AD sites.
- Your AD domain controller has a domain functional level of Windows Server 2008 R2 or higher.
- Your AD domain name can't be in Single Lable Domain (SLD) format. RDS Custom for SQL Server does not support SLD domains.
- The fully qualified domain name (FQDN) for your AD can't exceed 47 characters.

## Configure your network connectivity

Configure your self-managed or on-premise AD network connectivity in the following manner:

- Set up connectivity between Amazon VPC where your RDS Custom for SQL Server instance is running,
  and your AD. Use Direct Connect, Site-to-Site VPN, AWS Transit Gateway, and VPC Peering.
- Allow traffic on the ports your RDS Custom for SQL Server security groups and network ACLs to your self-managed
  or on-premise AD. For more information, see [Network configuration port rules](custom-sqlserver-WinAuth.md "custom-sqlserver-WinAuth.md").

![Microsoft SQL Server Windows Authentication directory](images/custom-sqs-SM-NC.png)

##

Configure DNS resolution

Set up the following requirements to configure DNS resolution with self-managed or on-premises AD's:

- Configure DNS resolution within your VPC to resolve your self-hosted Active Directory's
  fully qualified domain name (FQDN). An example of an FQDN is `corp.example.local`.
  To configure DNS resolution, configure the VPC DNS resolver to forward queries for certain domains
  with an Amazon Route 53 outbound endpoint and resolver rule. For more information, see
  [Configure a Route 53 Resolver outbound endpoint to resolve DNS records](https://repost.aws/knowledge-center/route53-resolve-with-outbound-endpoint "https://repost.aws/knowledge-center/route53-resolve-with-outbound-endpoint").
- For workloads that leverage both VPCs and on-premises resources, you must resolve DNS records hosted on-premises.
  On-premise resources might need to resolve names hosted on AWS.

To create a hybrid cloud setup, use resolver endpoints and conditional forwarding riles to resolve DNS queries
between your on-premise resources and custom VPC. For more information, see
[Resolving DNS queries between VPCs and your network](../../../Route53/latest/DeveloperGuide/resolver-overview-DSN-queries-to-vpc.md "../../../Route53/latest/DeveloperGuide/resolver-overview-DSN-queries-to-vpc.md") in the _Amazon Route 53 Developer Guide_.

###### Important

Modifying the DNS resolver settings of the network interface on the RDS Custom for SQL Server causes DNS-enabled VPC
endpoints to no longer work correctly. DNS-enabled VPC endpoints are required for instances
within private subnets without internet access.
