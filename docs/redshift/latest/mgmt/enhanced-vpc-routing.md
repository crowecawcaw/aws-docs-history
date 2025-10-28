Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Controlling network traffic with Redshift enhanced VPC routing

When you use Amazon Redshift enhanced VPC routing, Amazon Redshift forces all [COPY](../dg/r_COPY.md "../dg/r_COPY.md") and [UNLOAD](../dg/r_UNLOAD.md "../dg/r_UNLOAD.md") traffic between your cluster and your data repositories through your
virtual private cloud (VPC) based on the Amazon VPC service. By using enhanced VPC routing, you
can use standard VPC features, such as [VPC security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md"), [network access
control lists (ACLs)](../../../vpc/latest/userguide/VPC_ACLs.md "../../../vpc/latest/userguide/VPC_ACLs.md"), [VPC
endpoints](../../../vpc/latest/userguide/vpc-endpoints-s3.md "../../../vpc/latest/userguide/vpc-endpoints-s3.md"), [VPC endpoint
policies](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3"), [internet
gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md"), and [Domain Name System
(DNS)](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") servers, as described in the _Amazon VPC User Guide._ You use these features to control the flow of data
between your Amazon Redshift cluster and other resources. When you use enhanced VPC routing to route
traffic through your VPC, you can also use [VPC
flow logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") to monitor COPY and UNLOAD traffic.

Amazon Redshift clusters and Amazon Redshift Serverless workgroups both support enhanced VPC routing. You can't use enhanced VPC routing with Redshift Spectrum.
For more information, see [Accessing Amazon S3 buckets with Redshift Spectrum](spectrum-enhanced-vpc.md "spectrum-enhanced-vpc.md").

If enhanced VPC routing is not turned on, Amazon Redshift routes traffic through the internet,
including traffic to other services within the AWS network.

###### Important

Because enhanced VPC routing affects the way that Amazon Redshift accesses other resources, COPY
and UNLOAD commands might fail unless you configure your VPC correctly. You must
specifically create a network path between your cluster's VPC and your data
resources, as described following.

When you run a COPY or UNLOAD command on a cluster with enhanced VPC routing turned on,
your VPC routes the traffic to the specified resource using the
_strictest_, or most specific, network path available.

For example, you can configure the following pathways in your VPC:

- **VPC endpoints** – For traffic to an Amazon S3
  bucket in the same AWS Region as your cluster or workgroup, you can create a VPC endpoint to
  direct traffic directly to the bucket. When you use VPC endpoints, you can attach an
  endpoint policy to manage access to Amazon S3. For more information about using endpoints
  with Redshift, see [Controlling database traffic with VPC endpoints](enhanced-vpc-working-with-endpoints.md "enhanced-vpc-working-with-endpoints.md"). If you use Lake Formation, you can find more information about
  establishing a private connection between your VPC and AWS Lake Formation at [AWS Lake Formation and
  interface VPC endpoints (AWS PrivateLink)](../../../lake-formation/latest/dg/privatelink.md "../../../lake-formation/latest/dg/privatelink.md").

###### Note

When you use Redshift VPC endpoints with Amazon S3 VPC Gateway endpoints, you must enable enhanced VPC routing
in Redshift. For more information,
see [Gateway endpoints for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md").

- **NAT gateway** – You can connect to an Amazon S3
  bucket in another AWS Region, and you can connect to another service within the AWS
  network. You can also access a host instance outside the AWS network. To do so,
  configure a [network address
  translation (NAT) gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md"), as described in the _Amazon VPC User Guide._
- **Internet gateway** – To connect to AWS
  services outside your VPC, you can attach an [internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") to your
  VPC subnet, as described in the _Amazon VPC User Guide._
  To use an internet gateway, your cluster or workgroup must be publicly accessible to allow other
  services to communicate it.
  For more information, see [VPC
  Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the Amazon VPC User Guide.

There is no additional charge for using enhanced VPC routing. You might incur additional
data transfer charges for certain operations. These include such operations as UNLOAD to
Amazon S3 in a different AWS Region. COPY from Amazon EMR, or Secure Shell (SSH) with public IP
addresses. For more information about pricing, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

###### Topics

- [Controlling database traffic with VPC endpoints](enhanced-vpc-working-with-endpoints.md "enhanced-vpc-working-with-endpoints.md")
- [Turning on enhanced VPC routing](enhanced-vpc-enabling-cluster.md "enhanced-vpc-enabling-cluster.md")
- [Accessing Amazon S3 buckets with Redshift Spectrum](spectrum-enhanced-vpc.md "spectrum-enhanced-vpc.md")
