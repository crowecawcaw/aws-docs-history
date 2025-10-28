For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Connecting to Timestream for InfluxDB through a VPC endpoint

You can connect directly to Timestream for InfluxDB through a private interface endpoint in your virtual
private cloud (VPC). When you use an interface VPC endpoint, communication between your VPC and
Timestream for InfluxDB is conducted entirely within the AWS network.

Timestream for InfluxDB supports Amazon Virtual Private Cloud (Amazon VPC) endpoints powered by [AWS PrivateLink](../../../vpc/latest/privatelink.md "../../../vpc/latest/privatelink.md"). Each VPC endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") (ENIs) with private IP
addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to Timestream for InfluxDB without an internet gateway,
NAT device, VPN connection, or AWS Direct Connect connection. The instances in your VPC do not need
public IP addresses to communicate with Timestream for InfluxDB.

###### Regions

Timestream for InfluxDB supports VPC endpoints and VPC endpoint policies in all AWS Regions in which
Timestream for InfluxDB is supported.

###### Topics

- [Considerations for Timestream for InfluxDB VPC endpoints](#vpce-considerations "#vpce-considerations")
- [Creating a VPC endpoint for Timestream for InfluxDB](#vpce-create-endpoint "#vpce-create-endpoint")
- [Connecting to an Timestream for InfluxDB VPC endpoint](#vpce-connect "#vpce-connect")
- [Controlling access to a VPC endpoint](#vpce-policy "#vpce-policy")
- [Using a VPC endpoint in a policy statement](#vpce-policy-condition "#vpce-policy-condition")
- [Logging your VPC endpoint](#vpce-logging "#vpce-logging")

## Considerations for Timestream for InfluxDB VPC endpoints

Before you set up an interface VPC endpoint for Timestream for InfluxDB, review the [Interface endpoint
properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") topic in the _AWS PrivateLink Guide_.

Timestream for InfluxDB support for a VPC endpoint includes the following.

- You can use your VPC endpoint to call all [Timestream for InfluxDB API operations](../../../ts-influxdb/latest/ts-influxdb-api/API_Operations.md "../../../ts-influxdb/latest/ts-influxdb-api/API_Operations.md") from your
  VPC.
- You can use AWS CloudTrail logs to audit your use of Timestream for InfluxDB resources through the VPC endpoint.
  For details, see [Logging your VPC endpoint](#vpce-logging "#vpce-logging").

## Creating a VPC endpoint for Timestream for InfluxDB

You can create a VPC endpoint for Timestream for InfluxDB by using the Amazon VPC console or the Amazon VPC API. For
more information, see [Create an interface
endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _AWS PrivateLink Guide_.

- To create a VPC endpoint for Timestream for InfluxDB, use the following service name:

```
com.amazonaws.`region`.timestream-influxdb
```

For example, in the US West (Oregon) Region (`us-west-2`), the service
name would be:

```
com.amazonaws.us-west-2.timestream-influxdb
```

To make it easier to use the VPC endpoint, you can enable a [private DNS name](../../../vpc/latest/privatelink/verify-domains.md "../../../vpc/latest/privatelink/verify-domains.md") for your VPC
endpoint. If you select the **Enable DNS Name** option, the standard Timestream for InfluxDB
DNS hostname resolves to your VPC endpoint. For example,
`https://timestream-influxdb.us-west-2.amazonaws.com` would resolve to a VPC endpoint connected
to service name `com.amazonaws.us-west-2.timestream-influxdb`.

This option makes it easier to use the VPC endpoint. The AWS SDKs and AWS CLI use the
standard Timestream for InfluxDB DNS hostname by default, so you do not need to specify the VPC endpoint URL in
applications and commands.

For more information, see [Accessing a
service through an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint") in the
_AWS PrivateLink Guide_.

## Connecting to an Timestream for InfluxDB VPC endpoint

You can connect to Timestream for InfluxDB through the VPC endpoint by using an AWS SDK, the AWS CLI or
AWS Tools for PowerShell. To specify the VPC endpoint, use its DNS name.

If you enabled private hostnames when you created your VPC endpoint, you do not need to
specify the VPC endpoint URL in your CLI commands or application configuration. The standard
Timestream for InfluxDB DNS hostname resolves to your VPC endpoint. The AWS CLI and SDKs use this hostname by
default, so you can begin using the VPC endpoint to connect to an Timestream for InfluxDB regional endpoint
without changing anything in your scripts and applications.

To use private hostnames, the `enableDnsHostnames` and
`enableDnsSupport` attributes of your VPC must be set to `true`. To
set these attributes, use the [ModifyVpcAttribute](../../../AWSEC2/latest/APIReference/API_ModifyVpcAttribute.md "../../../AWSEC2/latest/APIReference/API_ModifyVpcAttribute.md") operation. For details, see [View and update DNS attributes for your
VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating") in the _Amazon VPC User Guide_.

## Controlling access to a VPC endpoint

To control access to your VPC endpoint for Timestream for InfluxDB, attach a _VPC
endpoint policy_ to your VPC endpoint. The endpoint policy determines whether
principals can use the VPC endpoint to call Timestream for InfluxDB operations on Timestream for InfluxDB resources.

You can create a VPC endpoint policy when you create your endpoint, and you can change the
VPC endpoint policy at any time. Use the VPC management console, or the [CreateVpcEndpoint](../../../AWSEC2/latest/APIReference/API_CreateVpcEndpoint.md "../../../AWSEC2/latest/APIReference/API_CreateVpcEndpoint.md") or [ModifyVpcEndpoint](../../../AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.md "../../../AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.md") operations. You can
also create and change a VPC endpoint policy by [using an AWS CloudFormation template](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md").
For help using the VPC management console, see [Create an interface
endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") and [Modifying an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#modify-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#modify-interface-endpoint") in the _AWS PrivateLink Guide_.

###### Note

Timestream for InfluxDB supports VPC endpoint policies beginning in July 2020. VPC endpoints for Timestream for InfluxDB
that were created before that date have the [default VPC
endpoint policy](#vpce-default-policy "#vpce-default-policy"), but you can change it at any time.

###### Topics

- [About VPC endpoint policies](#vpce-policy-about "#vpce-policy-about")
- [Default VPC endpoint policy](#vpce-default-policy "#vpce-default-policy")
- [Creating a VPC endpoint policy](#vpce-policy-create "#vpce-policy-create")
- [Viewing a VPC endpoint policy](#vpce-policy-get "#vpce-policy-get")

### About VPC endpoint policies

For an Timestream for InfluxDB request that uses a VPC endpoint to be successful, the principal requires
permissions from two sources:

- A [IAM
  policy](security-iam-for-influxdb.md "security-iam-for-influxdb.md") must give principal permission
  to call the operation on the resource.
- A VPC endpoint policy must give the principal permission to use the endpoint to make
  the request.

### Default VPC endpoint policy

Every VPC endpoint has a VPC endpoint policy, but you are not required to specify the
policy. If you don't specify a policy, the default endpoint policy allows all operations by
all principals on all resources over the endpoint.

However, for Timestream for InfluxDB resources, the principal must also have permission to call the
operation from an [IAM policy](security-iam-for-influxdb.md "security-iam-for-influxdb.md")
Therefore, in practice, the default policy says that if a principal has permission to call
an operation on a resource, they can also call it by using the endpoint.

```
{
  "Statement": [
    {
      "Action": "*",
      "Effect": "Allow",
      "Principal": "*",
      "Resource": "*"
    }
  ]
}
```

To allow principals to use the VPC endpoint for only a subset of their permitted
operations, [create or update the VPC endpoint
policy](#vpce-policy-create "#vpce-policy-create").

### Creating a VPC endpoint policy

A VPC endpoint policy determines whether a principal has permission to use the VPC
endpoint to perform operations on a resource. For Timestream for InfluxDB resources, the principal must also
have permission to perform the operations from a [IAM policy](security-iam-for-influxdb.md "security-iam-for-influxdb.md"),

Each VPC endpoint policy statement requires the following elements:

- The principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

The policy statement doesn't specify the VPC endpoint. Instead, it applies to any VPC
endpoint to which the policy is attached. For more information, see [Controlling access to services with VPC
endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

AWS CloudTrail logs all operations that use the VPC endpoint.

### Viewing a VPC endpoint policy

To view the VPC endpoint policy for an endpoint, use the [VPC management console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/") or the [DescribeVpcEndpoints](../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.md")
operation.

The following AWS CLI command gets the policy for the endpoint with the specified VPC
endpoint ID.

Before using this command, replace the example endpoint ID with a valid one from your
account.

```
`$` `aws ec2 describe-vpc-endpoints \

--query 'VpcEndpoints[?VpcEndpointId==``vpc-endpoint-id``].[PolicyDocument]'

--output text`
```

## Using a VPC endpoint in a policy statement

You can control access to Timestream for InfluxDB resources and operations when the request comes from VPC
or uses a VPC endpoint. To do so, use one of the following [global condition
keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys") in a [IAM policy](security-iam-for-influxdb.md "security-iam-for-influxdb.md").

- Use the `aws:sourceVpce` condition key to grant or restrict access based on
  the VPC endpoint.
- Use the `aws:sourceVpc` condition key to grant or restrict access based on
  the VPC that hosts the private endpoint.

###### Note

Use caution when creating key policies and IAM policies based on your VPC endpoint. If
a policy statement requires that requests come from a particular VPC or VPC endpoint,
requests from integrated AWS services that use an Timestream for InfluxDB resource on your behalf might
fail.

Also, the `aws:sourceIP` condition key is not effective when the request
comes from an [Amazon VPC endpoint](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md"). To
restrict requests to a VPC endpoint, use the `aws:sourceVpce` or
`aws:sourceVpc` condition keys. For more information, see [Identity and access management for VPC
endpoints and VPC endpoint services](../../../vpc/latest/privatelink/vpc-endpoints-iam.md "../../../vpc/latest/privatelink/vpc-endpoints-iam.md") in the _AWS PrivateLink Guide_.

You can use these global condition keys to control access to operations like [CreateDbInstance](../../../ts-influxdb/latest/ts-influxdb-api/API_CreateDbInstance.md "../../../ts-influxdb/latest/ts-influxdb-api/API_CreateDbInstance.md")
that don't depend on any particular resource.

## Logging your VPC endpoint

AWS CloudTrail logs all operations that use the VPC endpoint. When a request to Timestream for InfluxDB uses a VPC
endpoint, the VPC endpoint ID appears in the [AWS CloudTrail
log](logging-using-cloudtrail.md "logging-using-cloudtrail.md") entry that records the request. You can use the endpoint ID to audit the use of
your Timestream for InfluxDB VPC endpoint.

However, your CloudTrail logs don't include operations requested by principals in other accounts
or requests for Timestream for InfluxDB operations on Timestream for InfluxDB resources and aliases in other accounts. Also, to protect
your VPC, requests that are denied by a [VPC endpoint
policy](#vpce-policy "#vpce-policy"), but otherwise would have been allowed, are not recorded in [AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
