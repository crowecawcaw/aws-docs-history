Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Configure Managed Service for Apache Flink to access resources in an Amazon VPC

You can configure a Managed Service for Apache Flink application to connect to private subnets in a virtual private cloud (VPC) in your account.
Use Amazon Virtual Private Cloud (Amazon VPC) to create a private network for resources such as databases, cache instances, or internal services.
Connect your application to the VPC to access private resources during execution.

###### This topic contains the following sections:

- [Amazon VPC concepts](#vpc-concepts "#vpc-concepts")
- [VPC application permissions](vpc-permissions.md "vpc-permissions.md")
- [Internet and service access for a VPC-connected Managed Service for Apache Flink application](vpc-internet.md "vpc-internet.md")
- [Use the Managed Service for Apache Flink VPC API](vpc-api.md "vpc-api.md")
- [Example: Use a VPC to access data in an Amazon MSK cluster](vpc-example.md "vpc-example.md")

## Amazon VPC concepts

Amazon VPC is the networking layer for Amazon EC2. If you're new to Amazon EC2, see
[What is Amazon EC2?](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md")
in the _Amazon EC2 User Guide for Linux Instances_ to get a brief overview.

The following are the key concepts for VPCs:

- A _virtual private cloud_ (VPC) is a virtual network dedicated to your AWS account.
- A _subnet_ is a range of IP addresses in your VPC.
- A _route table_ contains a set of rules, called routes, that are used to determine where
  network traffic is directed.
- An _internet gateway_ is a horizontally scaled, redundant, and highly available
  VPC component that allows communication between instances in your VPC and the internet. It therefore imposes no
  availability risks or bandwidth constraints on your network traffic.
- A _VPC endpoint_ enables you to privately connect your VPC to supported
  AWS services and VPC endpoint services powered by PrivateLink without requiring an internet gateway,
  NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses
  to communicate with resources in the service. Traffic between your VPC and the other service does not leave the
  Amazon network.

For more information about the Amazon VPC service, see the
[Amazon Virtual Private Cloud
User Guide](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

Managed Service for Apache Flink creates [elastic network interfaces](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md") in one of the subnets provided in your VPC configuration for the application.
The number of elastic network interfaces created in your VPC subnets may vary, depending on the parallelism and
parallelism per KPU of the application. For more information about application scaling, see
[Implement application scaling](how-scaling.md "how-scaling.md").

###### Note

VPC configurations are not supported for SQL applications.

###### Note

The Managed Service for Apache Flink service manages the checkpoint and snapshot state for applications that have a VPC configuration.
