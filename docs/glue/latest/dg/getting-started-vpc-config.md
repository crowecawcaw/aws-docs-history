# Configure a VPC for your ETL job

You can use Amazon Virtual Private Cloud (Amazon VPC) to define a virtual network in your own
logically isolated area within the AWS Cloud, known as a
_virtual private cloud (VPC)_. You can launch your
AWS resources, such as instances, into your VPC. Your VPC closely resembles a
traditional network that you might operate in your own data center, with the
benefits of using the scalable infrastructure of AWS. You can configure your VPC;
you can select its IP address range, create subnets, and configure route tables,
network gateways, and security settings. You can connect instances in your VPC
to the internet. You can connect your VPC to your own corporate data center,
making the AWS Cloud an extension of your data center. To protect the resources
in each subnet, you can use multiple layers of security, including security groups
and network access control lists. For more information, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

You can configure your AWS Glue ETL jobs to run within a VPC when using connectors. You
must configure your VPC for the following, as needed:

- Public network access for data stores not in AWS. All data stores that are
  accessed by the job must be available from the VPC subnet.
- If your job needs to access both VPC resources and the public internet, the
  VPC needs to have a network address translation (NAT) gateway inside the VPC.

For more information, see [Setting Up Your Environment to Access Data
Stores](start-connecting.md "start-connecting.md") in the _AWS Glue Developer Guide_.
