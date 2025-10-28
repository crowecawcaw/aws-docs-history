# Configure network access between Studio and data sources (for administrators)

This section provides information about how administrators can configure a network to enable
communication between Amazon SageMaker Studio and [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/") or [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"), either
within a private Amazon VPC or over the internet. The networking instructions vary based on whether the Studio domain and the data
store are deployed within a private [Amazon Virtual Private Cloud](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") (VPC) or
communicate over the internet.

By default, Studio runs in an AWS managed VPC with [internet access](studio-notebooks-and-internet-access.md#studio-notebooks-and-internet-access-default "studio-notebooks-and-internet-access.md#studio-notebooks-and-internet-access-default"). When using an internet connection, Studio accesses AWS resources, such as Amazon S3 buckets, over the internet. However, if you have security
requirements to control access to your data and job containers, we recommend that you configure
Studio and your data store (Amazon Redshift or Athena) so that your data and containers aren’t
accessible over the internet. To control access to your resources or run Studio without
public internet access, you can specify the `VPC only` network access type
when you onboard to [Amazon SageMaker AI domain](gs-studio-onboard.md "gs-studio-onboard.md"). In this scenario, Studio establishes connections with other
AWS services via private [VPC endpoints](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md"). For
information about configuring Studio in `VPC only` mode, see [Connect Studio to external resources in a VPC](studio-notebooks-and-internet-access.md#studio-notebooks-and-internet-access-vpc-only "studio-notebooks-and-internet-access.md#studio-notebooks-and-internet-access-vpc-only").

###### Note

To connect to Snowflake, the VPC of the Studio domain must have internet
access.

The first two sections describe how to ensure communication between your Studio
domain and your data store in VPCs without public internet access. The last section
covers how to ensure communication between Studio and your data store using an internet
connection. Prior to connecting Studio and your data store without internet access, make
sure to establish endpoints for Amazon Simple Storage Service, Amazon Redshift or Athena, SageMaker AI, and for Amazon CloudWatch and AWS CloudTrail
(logging and monitoring).

- If Studio and the data store are in different VPCs, either in the same
  AWS account or in separate accounts, see [Studio and the data store are deployed in separate VPCs](#sagemaker-sql-extension-networking-cross-vpc "#sagemaker-sql-extension-networking-cross-vpc").
- If Studio and the data store are in the same VPC, see [Studio and the data store are deployed in the same VPC](#sagemaker-sql-extension-networking-same-vpc "#sagemaker-sql-extension-networking-same-vpc").
- If you chose to connect Studio and the data store over the public internet, see
  [Studio and the data store communicate over public internet](#sagemaker-sql-extension-networking-internet "#sagemaker-sql-extension-networking-internet").

## Studio and the data store are deployed in separate VPCs

To allow communication between Studio and a data store deployed in different
VPCs:

1. Start by connecting your VPCs through a VPC peering connection.
2. Update the routing tables in each VPC to allow bidirectional network traffic
   between Studio subnets and the data store subnets.
3. Configure your security groups to allow inbound and outbound traffic.

The configuration steps are the same whether Studio and the data store are deployed
in a single AWS account or across different AWS accounts.

1. ###### VPC peering

Create a [VPC peering
connection](../../../vpc/latest/peering/working-with-vpc-peering.md "../../../vpc/latest/peering/working-with-vpc-peering.md") to facilitate the networking between the two VPCs
(Studio and the data store).

    1. From the Studio account, on the VPC dashboard, choose
     **Peering connections**, then **Create peering
     connection**.
    2. Create your request to peer the Studio VPC with the data store
     VPC. When requesting peering in another AWS account, choose
     **Another account** in **Select another VPC to peer
     with**.


    For cross-account peering, the administrator must accept the request from the SQL
     engine account.


    When peering private subnets, you should enable private IP DNS resolution at the
     VPC peering connection level.

2. ###### Routing tables

Configure the routing to allow network traffic between Studio and data store
VPC subnets in both directions.

After you establish the peering connection, the administrator (on each account for
cross account access) can add routes to the private subnet route tables to route the
traffic between Studio and the data store VPCs' subnets. You can define those
routes by going to the **Route Tables** section of each VPC in
the VPC dashboard. 3. ###### Security groups

Lastly, the security group of Studio's domain VPC must allow outbound
traffic, and the security group of the data store's VPC must allow inbound traffic
on your data store port from Studio's VPC security group.

## Studio and the data store are deployed in the same VPC

If Studio and the data store are in different private subnets in the same VPC, add
routes in each private subnet's route table. The routes should allow traffic to flow between
the Studio subnets and the data store subnets. You can define those routes by going to
the **Route Tables** section of each VPC in the VPC
dashboard. If you deployed Studio and the data store in the same VPC and the same
subnet, you do not need to route the traffic.

Regardless of any routing table updates, the security group of Studio's domain
VPC must allow outbound traffic, and the security group of the data store's
VPC must allow inbound traffic on its port from Studio's VPC security
group.

## Studio and the data store communicate over public internet

By default, Studio provides a network interface that allows communication with the
internet through an internet gateway in the VPC associated with the Studio
domain. If you choose to connect to your data store through the public internet, your data
store needs to accept inbound traffic on its port.

A [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-working-with "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-working-with")
must be used to allow instances in private subnets of multiple VPCs to share a single public
IP address provided by the [internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") when accessing
the internet.

###### Note

Each port opened for inbound traffic represents a potential security risk. Carefully
review custom security groups to ensure that you minimize vulnerabilities.
