# VPC connectivity for S3 Tables

All tables in S3 Tables are in the Apache Iceberg format and are made up of two types of S3 objects. These two types of objects are
 data files which store the data and metadata files which track information about the data files at different points in time. 
 All table bucket, namespace, and table operations (for example, `CreateNamespace`, `CreateTable`, and so on) are routed through 
 an S3 Tables endpoint (`s3tables.region.amazonaws.com`) and all object-level operations that read or write the data and metadata files continue 
 to be routed through an S3 service endpoint (`s3.region.amazonaws.com`). 

To access S3 Tables, Amazon S3 supports two types of VPC endpoints by using AWS PrivateLink: gateway endpoints and
 interface endpoints. A gateway endpoint is a gateway that you
 specify in your route table to access S3 from your VPC over the AWS network. Interface
 endpoints extend the functionality of gateway endpoints by using private IP addresses to
 route requests to Amazon S3 from within your VPC, on premises, or from a VPC in another
 AWS Region by using VPC peering or AWS Transit Gateway. 

To access S3 Tables from a VPC, we recommend creating two VPC endpoints (one for
 S3 and the other for S3 Tables). You can create either a gateway or an interface endpoint to
 route file (object) level operations to S3 and an interface endpoint to route bucket and
 table-level operations to S3 Tables. You can create and use VPC endpoints for file-level
 requests using S3. For more information, see [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html "https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html") in the
 *AWS PrivateLink* User Guide. 

To learn more about using AWS PrivateLink to create and work with endpoints for
 S3 Tables, see the following topics. To create a VPC interface endpoint, see
 [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws "https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws") in the *AWS PrivateLink Guide*.

###### Topics

* [Creating VPC endpoints for S3 Tables](#s3-tables-endpoints "#s3-tables-endpoints")
* [Accessing table buckets and tables
 through endpoints using the AWS CLI](#s3-tables-endpoints-cli-sdks "#s3-tables-endpoints-cli-sdks")
* [Configuring a VPC network when using query engines](#s3-tables-query-engine "#s3-tables-query-engine")
* [Restricting access to S3 Tables within the VPC
 network](#s3-tables-VPC-policy "#s3-tables-VPC-policy")

## Creating VPC endpoints for S3 Tables


When you create a VPC endpoint, S3 Tables generates two types of endpoint-specific DNS names: Regional and Zonal. 



* A Regional DNS name is of the following format:
 `VPCendpointID.s3tables.AWSregion.vpce.amazonaws.com`. For
 example, for the VPC endpoint ID `vpce-1a2b3c4d`, the DNS name
 generated will be similar to
 `vpce-1a2b3c4d-5e6f.s3tables.us-east-1.vpce.amazonaws.com`
* A Zonal DNS name is of the following format: `VPCendpointID-AvailabilityZone.s3tables.AWSregion.vpce.amazonaws.com`.
 
 For example, For the VPC endpoint ID `vpce-1a2b3c4d-5e6f.`, the DNS name generated will be similar to 
 `vpce-1a2b3c4d-5e6f-us-east-1a.s3tables.us-east-1.vpce.amazonaws.com`



 A Zonal DNS name includes your Availability Zone. You might use Zonal DNS names if your
 architecture isolates Availability Zones. Endpoint specific S3 DNS names can be
 resolved from the S3 public DNS domain.

You can also use Private DNS options to simplify routing S3 traffic over VPC endpoints
 and help you take advantage of the lowest-cost network path available to your
 application. Private DNS maps the public endpoint of S3 Tables, for instance,
 `s3tables.region.amazonaws.com`, to a private IP in your VPC. You can
 use private DNS options to route Regional S3 traffic without updating your S3 clients to
 use the endpoint-specific DNS names of your interface endpoints.


###### Note

AWS PrivateLink for Amazon S3 doesn't support using Amazon S3 dual-stack endpoints. For more information,
 see [Using Amazon S3 dual-stack endpoints](../API/dual-stack-endpoints.md "../API/dual-stack-endpoints.md") in the *Amazon S3 API
 Reference*.


## Accessing table buckets and tables
 through endpoints using the AWS CLI


You can use the AWS Command Line Interface (AWS CLI) to access table buckets and tables through the
 interface endpoints. With the AWS CLI, `aws s3` commands route traffic through
 the Amazon S3 endpoint. The `aws s3tables` AWS CLI commands use the Amazon
 S3 Tables endpoint. 


An example of an `s3tables` VPC endpoint is
 `vpce-0123456afghjipljw-nmopsqea.s3tables.region.vpce.amazonaws.com`


An `s3tables` VPC endpoint doesn't include a bucket name. You can
 access the `s3tables` VPC endpoint using the `aws s3tables`
 AWS CLI commands.


An example of an `s3` VPC endpoint is `amzn-s3-demo-bucket.vpce-0123456afghjipljw-nmopsqea.s3.region.vpce.amazonaws.com`


You can access the `s3` VPC endpoint using the `aws s3`
 AWS CLI commands.


To access table buckets and tables through interface endpoints using the AWS CLI,
 use the `-region`- and `--endpoint-url` parameters. To
 perform table bucket and table level actions, use the S3 Tables endpoint URL.
 To perform object level actions, use the Amazon S3 endpoint URL.

In the following examples, replace the `user input
 placeholders` with your own information.

**Example 1: Use an endpoint URL to list table buckets in your account**


```
aws s3tables list-table-buckets --endpoint https://`vpce-0123456afghjipljb-aac`.s3tables.`us-east-1`.vpce.amazonaws.com —region `us-east-1`
```
**Example 2: Use an endpoint URL to list tables in your
 bucket**


```
aws s3tables list-tables --table-bucket-arn arn:aws:s3tables:`us-east-1`:`123456789301`:bucket/`amzn-s3-demo-bucket` --endpoint https://`vpce-0123456afghjipljb-aac`.s3tables.`us-east-1`.vpce.amazonaws.com --region `us-east-1`
```

## Configuring a VPC network when using query engines


Use the following steps to configure a VPC network when using query engines. 



1. To get started, you can create or update a VPC. For more information, see
 [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-and-other-resources "https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-and-other-resources").
2. For table and table bucket level operations that route to S3 Tables, create a new interface endpoint. For more information, 
 see 
 [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws "https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws").
3. For all object level operations that route to Amazon S3, create a gateway endpoint or a interface endpoint. 
 For more information on gateway endpoints, see 
 [Create a gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3 "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3").
4. Next, configure your data resources and launch an Amazon EMR cluster. For more information, see 
 
 [Getting started with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html "https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html").
5. You can then submit a Spark application with an additional configuration by
 selecting your DNS names from the VPC endpoint. For example,
 `spark.sql.catalog.ice_catalog.s3tables.endpoint` and
 `https://interface-endpoint.s3tables.`us-east-1`.vpce.amazonaws.com`
 For more information, see [Submit work to your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html#emr-getting-started-manage "https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html#emr-getting-started-manage").

## Restricting access to S3 Tables within the VPC
 network


Similar to resource-based policies, you can attach an endpoint policy to your VPC endpoint
 that controls the access to tables and table buckets. In the following example, the
 interface endpoint policy restricts access to only specific table buckets.



JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "Policy141511512309",
 "Statement": [
 {
 "Sid": "Access-to-specific-bucket-only",
 "Principal": "*",
 "Action": "s3tables:*",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket`",
 "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```
