# Configuring VPC access for EMR Serverless applications to connect to data

You can configure EMR Serverless applications to connect to your data stores within your
VPC, such as Amazon Redshift clusters, Amazon RDS databases or Amazon S3 buckets with VPC endpoints. Your EMR Serverless application has outbound connectivity to the data stores within your VPC.
By default, EMR Serverless blocks both inbound access to your applications and outbound internet access to enhance security.

###### Note

You must configure VPC access if you want to use an external Hive metastore database for
your application. For information about how to configure an external Hive metastore, refer to
[Metastore configuration](metastore-config.md "metastore-config.md").

## Create application

On the **Create application** page, choose custom settings and
specify the VPC, subnets and security groups that EMR Serverless applications can
use.

### VPCs

Choose the name of the virtual private cloud (VPC) that contains your data stores. The
**Create application** page lists all VPCs for your chosen
AWS Region.

### Subnets

Choose the subnets within the VPC that contains your data store. The **Create
application** page lists all subnets for the data stores in your VPC. Both public and private subnets are
supported. You can pass either private or public subnets to your applications. The choice of whether to have a public or
private subnet has a few associated considerations to be aware of.

For private subnets:

- The associated route tables must not have internet gateways.
- For outbound connectivity to the internet, if needed, configure outbound routes using
  a NAT Gateway. To configure a NAT Gateway, refer to [NAT
  gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-working-with "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-working-with").
- For Amazon S3 connectivity, configure either a NAT Gateway or a VPC
  endpoint. To configure an S3 VPC endpoint, refer to [Create a
  gateway endpoint](../../../vpc/latest/privatelink/vpc-endpoints-s3.md#create-gateway-endpoint-s3 "../../../vpc/latest/privatelink/vpc-endpoints-s3.md#create-gateway-endpoint-s3").
- If you configure an S3 VPC endpoint and you attach an endpoint policy to control access, follow
  the instructions in [Logging for EMR Serverless with managed storage](logging.md#jobs-log-storage-managed-storage "logging.md#jobs-log-storage-managed-storage") to provide
  permissions for EMR Serverless to store and serve application logs.
- For connectivity to other AWS services outside the VPC, such as to Amazon DynamoDB,
  configure either VPC endpoints or a NAT gateway. To configure VPC endpoints for
  AWS services, refer to [Work with
  VPC endpoints](../../../vpc/latest/privatelink/what-is-privatelink.md#working-with-privatelink "../../../vpc/latest/privatelink/what-is-privatelink.md#working-with-privatelink").

###### Note

When you set up an Amazon EMR Serverless application in a private subnet, we suggest that you also set up VPC endpoints for Amazon S3. If your EMR Serverless application
is in a private subnet without VPC endpoints for Amazon S3, you incur additional NAT gateway charges that are associated with S3 traffic. This is because the traffic between your
EMR application and Amazon S3 will not stay within your VPC when VPC endpoints aren't configured.

For public subnets:

- These have a route to an Internet Gateway.
- You must ensure proper security group configurations to control
  outbound traffic.

Workers can connect to the data stores within your VPC through outbound traffic. By default, EMR Serverless blocks
inbound access to workers. This is to improve security.

When you use AWS Config, EMR Serverless creates an elastic network interface item record
for every worker. To avoid costs related to this resource, consider turning off
`AWS::EC2::NetworkInterface` in AWS Config.

###### Note

We suggest that you select multiple subnets across multiple Availability Zones.
This is because the subnets that you choose determine the Availability Zones
available for an EMR Serverless application to launch. Each worker consumes an IP
address on the subnet where it is launched. Please ensure that the specified subnets
have sufficient IP addresses for the number of workers you plan to launch. For more
information on subnet planning, refer to [Best practices for subnet
planning](#subnet-best-practices "#subnet-best-practices").

#### Considerations and limitations for subnets

- EMR Serverless with public subnets does not support AWS Lake Formation.
- Inbound traffic isn't supported for public subnets.

### Security groups

Choose one or more security groups that can communicate with your data stores. The
**Create application** page lists all security groups in your VPC.
EMR Serverless associates these security groups with elastic network interfaces that are
attached to your VPC subnets.

###### Note

We suggest that you create a separate security group for EMR Serverless
applications. EMR Serverless does not allow you to **Create**/**Update**/**Start application** if security groups have ports open to the public internet
on **0.0.0.0/0** or the **::/0** range. This provides enhanced security, isolation, and makes managing network rules more efficient. For
example, this blocks unexpected traffic to workers with public IP addresses. To communicate with Amazon Redshift clusters, for instance, define the traffic rules between
Redshift and EMR Serverless security groups, as demonstrated in the example
in the following section.

###### Example — Communication with Amazon Redshift clusters

1. Add a rule for inbound traffic to the Amazon Redshift security group from one of the
   EMR Serverless security groups.

| Type    | Protocol | Port range | Source                          |
| ------- | -------- | ---------- | ------------------------------- |
| All TCP | TCP      | 5439       | `emr-serverless-security-group` |

2. Add a rule for outbound traffic from one of the EMR Serverless security groups.
   Do this in one of two ways. First, open outbound traffic to all
   ports.

| Type        | Protocol | Port range | Destination |
| ----------- | -------- | ---------- | ----------- |
| All traffic | TCP      | ALL        | 0.0.0.0/0   |

Alternatively, you can restrict outbound traffic to Amazon Redshift clusters. This is
useful only when the application must communicate with Amazon Redshift clusters and nothing
else.

| Type    | Protocol | Port range | Source                    |
| ------- | -------- | ---------- | ------------------------- |
| All TCP | TCP      | 5439       | `redshift-security-group` |

## Configure application

You can change the network configuration for an existing EMR Serverless application
from the **Configure application** page.

### Access job run details

On the **Job run detail** page, access the subnet used by your
job for a specific run. Note that a job runs only in one subnet selected from the
specified subnets.

## Best practices for subnet

planning

AWS resources are created in a subnet which is a subset of available IP addresses in
an Amazon VPC. For example, a VPC with a /16 netmask has up to 65,536 available IP addresses
which can be broken into multiple smaller networks using subnet masks. As an example, you
can split this range into two subnets with each using /17 mask and 32,768 available IP
addresses. A subnet resides within an Availability Zone and cannot span across zones.

The subnets should be designed keeping in mind your EMR Serverless application scaling
limits. For example, if you have an application requesting 4 vCpu workers and can scale up
to 4,000 vCpu, then your application requires at most 1,000 workers for a total of 1,000
network interfaces. We suggest that you create subnets across multiple Availability Zones. This
allows EMR Serverless to retry your job or provision pre-initialized capacity in a
different Availability Zone in an unlikely event when an Availability Zone fails. Therefore, each subnet in
at least two Availability Zones should have more than 1,000 available IP addresses.

You need subnets with mask size lower than or equal to 22 to provision 1,000 network
interfaces. Any mask greater than 22 does not meet the requirement. For example, a subnet
mask of /23 provides 512 IP addresses, while a mask of /22 provides 1024 and a mask of /21
provides 2048 IP addresses. Below is an example of 4 subnets with /22 mask in a VPC of /16
netmask that can be allocated to different Availability Zones. There is a difference of five between
available and usable IP addresses because first four IP addresses and last IP address in
each subnet is reserved by AWS.

| Subnet ID | Subnet Address | Subnet Mask      | IP Address Range           | Available IP Addresses | Usable IP Addresses |
| --------- | -------------- | ---------------- | -------------------------- | ---------------------- | ------------------- |
| 1         | 10.0.0.0       | 255.255.252.0/22 | 10.0.0.0<br>• 10.0.3.255   | 1,024                  | 1,019               |
| 2         | 10.0.4.0       | 255.255.252.0/22 | 10.0.4.0<br>• 10.0.7.255   | 1,024                  | 1,019               |
| 3         | 10.0.8.0       | 255.255.252.0/22 | 10.0.8.0<br>• 10.0.11.255  | 1,024                  | 1,019               |
| 4         | 10.0.12.0      | 255.255.252.0/22 | 10.0.12.0<br>• 10.0.15.255 | 1,024                  | 1,019               |

You should evaluate if your workload is best suited for larger worker sizes. Using
larger worker sizes requires fewer network interfaces. For example, using 16vCpu workers
with an application scaling limit of 4,000 vCpu requires at most 250 workers for a total
of 250 available IP addresses to provision network interfaces. You need subnets in multiple
Availability Zones with mask size lower than or equal to 24 to provision 250 network interfaces. Any
mask size greater than 24 offers less than 250 IP addresses.

If you share subnets across multiple applications, each subnet should be designed
keeping in mind collective scaling limits of all your applications. For example, if you have
3 applications requesting 4 vCpu workers and each can scale up to 4000 vCpu with 12,000 vCpu
account-level service based quota, each subnet requires 3000 available IP addresses. If
the VPC that you want to use doesn't have a sufficient number of IP addresses, try to
increase the number of available IP addresses. You can do this by associating additional
Classless Inter-Domain Routing (CIDR) blocks with your VPC. For more information, refer to [Associate additional IPv4 CIDR blocks with your VPC](../../../vpc/latest/userguide/working-with-vpcs.md#add-ipv4-cidr "../../../vpc/latest/userguide/working-with-vpcs.md#add-ipv4-cidr") in the
_Amazon VPC User Guide_.

You can use one of the many tools available online to quickly generate subnet
definitions and review their available range of IP addresses.
