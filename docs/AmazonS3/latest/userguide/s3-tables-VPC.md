

# VPC connectivity for S3 Tables
<a name="s3-tables-VPC"></a>

All tables in S3 Tables are in the Apache Iceberg format and are made up of two types of S3 objects. These two types of objects are data files which store the data and metadata files which track information about the data files at different points in time. All table bucket, namespace, and table operations (for example, `CreateNamespace`, `CreateTable`, and so on) are routed through an S3 Tables endpoint (`s3tables.region.amazonaws.com`) and all object-level operations that read or write the data and metadata files continue to be routed through an S3 service endpoint (`s3.region.amazonaws.com`). 

To access S3 Tables, Amazon S3 supports two types of VPC endpoints by using AWS PrivateLink: gateway endpoints and interface endpoints. A gateway endpoint is a gateway that you specify in your route table to access S3 from your VPC over the AWS network. Interface endpoints extend the functionality of gateway endpoints by using private IP addresses to route requests to Amazon S3 from within your VPC, on premises, or from a VPC in another AWS Region by using VPC peering or AWS Transit Gateway. 

To access S3 Tables from a VPC, we recommend creating two VPC endpoints (one for S3 and the other for S3 Tables). You can create either a gateway or an interface endpoint to route file (object) level operations to S3 and an interface endpoint to route bucket and table-level operations to S3 Tables. You can create and use VPC endpoints for file-level requests using S3. For more information, see [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) in the *AWS PrivateLink* User Guide. 

To learn more about using AWS PrivateLink to create and work with endpoints for S3 Tables, see the following topics. To create a VPC interface endpoint, see [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

**Topics**
+ [Creating VPC endpoints for S3 Tables](#s3-tables-endpoints)
+ [Accessing table buckets and tables through endpoints using the AWS CLI](#s3-tables-endpoints-cli-sdks)
+ [Configuring a VPC network when using query engines](#s3-tables-query-engine)
+ [Using the dual-stack endpoints to access tables and table buckets](#s3-tables-dual-stack-endpoints)
+ [Using VPC endpoint policy conditions with table bucket policies](#s3-tables-vpc-endpoint-policies)
+ [Restricting access to S3 Tables within the VPC network](#s3-tables-VPC-policy)

## Creating VPC endpoints for S3 Tables
<a name="s3-tables-endpoints"></a>

When you create a VPC endpoint, S3 Tables generates two types of endpoint-specific DNS names: Regional and Zonal. 
+ A Regional DNS name is of the following format: `VPCendpointID.s3tables.AWSregion.vpce.amazonaws.com`. For example, for the VPC endpoint ID `vpce-1a2b3c4d`, the DNS name generated will be similar to `vpce-1a2b3c4d-5e6f.s3tables.us-east-1.vpce.amazonaws.com` 
+ A Zonal DNS name is of the following format: `VPCendpointID-AvailabilityZone.s3tables.AWSregion.vpce.amazonaws.com`. For example, For the VPC endpoint ID `vpce-1a2b3c4d-5e6f.`, the DNS name generated will be similar to `vpce-1a2b3c4d-5e6f-us-east-1a.s3tables.us-east-1.vpce.amazonaws.com` 

   A Zonal DNS name includes your Availability Zone. You might use Zonal DNS names if your architecture isolates Availability Zones. Endpoint specific S3 DNS names can be resolved from the S3 public DNS domain. 

You can also use Private DNS options to simplify routing S3 traffic over VPC endpoints and help you take advantage of the lowest-cost network path available to your application. Private DNS maps the public endpoint of S3 Tables, for instance, `s3tables.region.amazonaws.com`, to a private IP in your VPC. You can use private DNS options to route Regional S3 traffic without updating your S3 clients to use the endpoint-specific DNS names of your interface endpoints.

## Accessing table buckets and tables through endpoints using the AWS CLI
<a name="s3-tables-endpoints-cli-sdks"></a>

You can use the AWS Command Line Interface (AWS CLI) to access table buckets and tables through the interface endpoints. With the AWS CLI, `aws s3` commands route traffic through the Amazon S3 endpoint. The `aws s3tables` AWS CLI commands use the Amazon S3 Tables endpoint. 

An example of an `s3tables` VPC endpoint is `vpce-0123456afghjipljw-nmopsqea.s3tables.region.vpce.amazonaws.com`

An `s3tables` VPC endpoint doesn't include a bucket name. You can access the `s3tables` VPC endpoint using the `aws s3tables` AWS CLI commands.

An example of an `s3` VPC endpoint is `amzn-s3-demo-bucket.vpce-0123456afghjipljw-nmopsqea.s3.region.vpce.amazonaws.com`

You can access the `s3` VPC endpoint using the `aws s3` AWS CLI commands.

### Using the AWS CLI
<a name="set-s3tables-vpc-cli"></a>

To access table buckets and tables through interface endpoints using the AWS CLI, use the `-region`- and `--endpoint-url` parameters. To perform table bucket and table level actions, use the S3 Tables endpoint URL. To perform object level actions, use the Amazon S3 endpoint URL.

In the following examples, replace the {{user input placeholders}} with your own information.

**Example 1: Use an endpoint URL to list table buckets in your account**

```
aws s3tables list-table-buckets --endpoint https://{{vpce-0123456afghjipljb-aac}}.s3tables.{{us-east-1}}.vpce.amazonaws.com —region {{us-east-1}}
```

**Example 2: Use an endpoint URL to list tables in your bucket**

```
aws s3tables list-tables --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{123456789301}}:bucket/{{amzn-s3-demo-bucket}} --endpoint https://{{vpce-0123456afghjipljb-aac}}.s3tables.{{us-east-1}}.vpce.amazonaws.com --region {{us-east-1}}
```

## Configuring a VPC network when using query engines
<a name="s3-tables-query-engine"></a>

Use the following steps to configure a VPC network when using query engines. 

1. To get started, you can create or update a VPC. For more information, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-and-other-resources).

1.  For table and table bucket level operations that route to S3 Tables, create a new interface endpoint. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws).

1.  For all object level operations that route to Amazon S3, create a gateway endpoint or a interface endpoint. For more information on gateway endpoints, see [Create a gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3).

1.  Next, configure your data resources and launch an Amazon EMR cluster. For more information, see [Getting started with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html).

1. You can then submit a Spark application with an additional configuration by selecting your DNS names from the VPC endpoint. For example, `spark.sql.catalog.ice_catalog.s3tables.endpoint` and `https://interface-endpoint.s3tables.{{us-east-1}}.vpce.amazonaws.com` For more information, see [Submit work to your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html#emr-getting-started-manage).

## Using the dual-stack endpoints to access tables and table buckets
<a name="s3-tables-dual-stack-endpoints"></a>

S3 Tables supports dual-stack connectivity for AWS PrivateLink. Dual-stack endpoints allow you to access S3 tables buckets using the Internet Protocol version 6 (IPv6), in addition to the IPv4 protocol, depending on what your network supports. You can access an S3 bucket through a dual-stack endpoint using the following naming convention: 

```
s3tables.<region>.api.aws
```

The following are some things you should know before trying to access S3 tables and table buckets over IPv6 in your VPC:
+ The client you use to access tables and your S3 client must both have dual-stack enabled.
+ IPv6 inbound is not enabled by default for VPC security groups. To allow IPv6 access you will need to add a new rule allowing HTTPS (TCP port 443) to your security group. For more information, see [*Configure security group rules*](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html#add-remove-security-group-rules) in the *Amazon EC2user guide*
+ If your VPC doesn't have IPv6 CIDRs assigned, you will need to manually add an IPv6 CIDR block to your VPC. For more info, see [*Add IPv6 support for your VPC*](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-add.html) in the *AWS PrivateLink user guide*
+ If you use IP address filtering IAM policies they must be updated to handle IPv6 addresses. For more information about managing access permissions with IAM, see [Identity and Access Management for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-iam.html).

To create a new VPC endpoint that uses the dual-stack endpoint for S3 Tables use example CLI command:

```
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-id \
  --service-name com.amazonaws.{{aws-region}}.s3tables \
  --subnet-ids subnet-1 subnet-2 \
  --vpc-endpoint-type Interface \
  --ip-address-type dualstack \
  --dns-options "DnsRecordIpType=dualstack" \
  --security-group-ids sg-id \
  --region {{aws-region}}
```

For more information on creating VPC endpoints see [*Create an interface endpoint*](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the VPC user guide.

If your network supports IPv6 and you want to update your VPC to enable IPv6 you can use the following CLI command:

```
aws ec2 modify-vpc-endpoint \
  --vpc-endpoint-id vpce-id \
  --ip-address-type dualstack \
  --dns-options "DnsRecordIpType=dualstack" \
  --region {{aws-region}}
```

## Using VPC endpoint policy conditions with table bucket policies
<a name="s3-tables-vpc-endpoint-policies"></a>

You can use the `aws:SourceVpce`, `aws:SourceVpc`, and `aws:VpcSourceIp` condition keys in a table bucket policy to restrict access to table bucket resources from a specific VPC or VPC endpoint. For more information about these condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

When using the [Iceberg REST APIs](s3-tables-integrating-open-source.md), S3 Tables makes requests to Amazon S3 on your behalf to read and write table metadata. When an Iceberg REST API request is made through a VPC endpoint, the source VPC of the initial request is not preserved in the table metadata requests to Amazon S3. If your table bucket policy restricts access using these condition keys, you must also add a condition for `aws:CalledVia` to allow these table metadata requests from S3 Tables.

The following example table bucket policy denies all S3 Tables actions unless the request comes from the specified VPC endpoint or is a request made by the Amazon S3 Tables Iceberg REST endpoint on your behalf.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "RestrictToVPCe",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3tables:*",
            "Resource": [
                "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-bucket}}",
                "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-bucket}}/*"
            ],
            "Condition": {
                "StringNotEqualsIfExists": {
                    "aws:SourceVpce": "{{vpce-1a2b3c4d}}",
                    "aws:CalledViaLast": "s3tables.amazonaws.com"
                }
            }
        }
    ]
}
```

------

## Restricting access to S3 Tables within the VPC network
<a name="s3-tables-VPC-policy"></a>

Similar to resource-based policies, you can attach an endpoint policy to your VPC endpoint that controls the access to tables and table buckets. In the following example, the interface endpoint policy restricts access to only specific table buckets.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "Policy141511512309",
    "Statement": [
        {
            "Sid": "Access-to-specific-bucket-only",
            "Principal": "*",
            "Action": "s3tables:*",
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-bucket}}",
                "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-bucket}}/*"
            ]
        }
    ]
}
```

------