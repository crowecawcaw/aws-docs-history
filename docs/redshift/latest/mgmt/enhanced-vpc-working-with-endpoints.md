Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Controlling database traffic with VPC endpoints

You can use a VPC endpoint to create a managed connection between your Amazon Redshift cluster or Serverless workgroup in
a VPC and Amazon Simple Storage Service (Amazon S3). When you do, COPY and UNLOAD traffic between your database and
your data on Amazon S3 stays in your Amazon VPC. You can attach an endpoint policy to your
endpoint to more closely manage access to your data. For example, you can add a policy
to your VPC endpoint that permits unloading data only to a specific Amazon S3 bucket in your
account.

To use VPC endpoints, create a VPC endpoint for the VPC that your data warehouse is in and
then turn on enhanced VPC routing. You can turn on enhanced VPC routing
when you create your cluster or workgroup, or you can modify a cluster or workgroup in a VPC to use
enhanced VPC routing.

A VPC endpoint uses route tables to control the routing of traffic between a cluster or workgroup
in the VPC and Amazon S3. All clusters and workgroups in subnets associated with the specified route tables
automatically use that endpoint to access the service.

Your VPC uses the most specific, or most restrictive, route that matches your
traffic to determine how to route the traffic. For example, suppose that you
have a route in your route table for all internet traffic (0.0.0.0/0) that points to an
internet gateway and an Amazon S3 endpoint. In this case, the endpoint route takes precedence
for all traffic destined for Amazon S3. This is because the IP address range for the Amazon S3
service is more specific than 0.0.0.0/0. In this example, all other internet traffic
goes to your internet gateway, including traffic that's destined for Amazon S3 buckets
in other AWS Regions.

For more information about creating endpoints, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _Amazon VPC User Guide._

You use endpoint policies to control access from your cluster or workgroup to the Amazon S3 buckets that
hold your data files. For more specific control, you can optionally attach a custom endpoint policy. For more
information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide._

###### Note

AWS Database Migration Service (AWS DMS) is a cloud service that makes it possible to migrate relational databases, data warehouses, and other types of data
stores. It can connect to any AWS source or target database, including an Amazon Redshift database that's VPC enabled, with some configuration restrictions. Supporting Amazon VPC endpoints makes
it easier for AWS DMS to maintain end-to-end network security for replication tasks. For more information on
using Redshift with AWS DMS, see [Configuring VPC endpoints
as AWS DMS source and target endpoints](../../../dms/latest/userguide/CHAP_VPC_Endpoints.md "../../../dms/latest/userguide/CHAP_VPC_Endpoints.md") in the _AWS Database Migration Service User Guide_.

There is no additional charge for using endpoints. Standard charges for data transfer
and resource usage apply. For more information about pricing, see [Amazon EC2 Pricing](https://aws.amazon.com/redshift/pricing/#Data_Transfer "https://aws.amazon.com/redshift/pricing/#Data_Transfer").
