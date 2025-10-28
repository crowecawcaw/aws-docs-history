# Access AWS Cloud Map using an interface endpoint

(AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and AWS Cloud Map.
You can access AWS Cloud Map as if it were in your VPC, without the use of an internet gateway, NAT
device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to access AWS Cloud Map.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface
in each subnet that you enable for the interface endpoint. These are requester-managed
network interfaces that serve as the entry point for traffic destined for AWS Cloud Map.

For more information, see [Access AWS services
through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the
_AWS PrivateLink Guide_.

## Considerations for AWS Cloud Map

Before you set up an interface endpoint for AWS Cloud Map, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

If your Amazon VPC doesn’t have an internet gateway and your tasks use the
`awslogs` log driver to send log information to CloudWatch Logs, you must create an
interface VPC endpoint for CloudWatch Logs. For more information, see [Using
CloudWatch Logs with Interface VPC Endpoints](../../../AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.md "../../../AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.md") in the Amazon CloudWatch Logs User Guide.

VPC endpoints don’t support AWS cross-Region requests. Ensure that
you create your endpoint in the same Region where you plan to issue your
API calls to AWS Cloud Map.

VPC endpoints only support Amazon-provided DNS through Amazon Route 53. If you want to use
your own DNS, you can use conditional DNS forwarding. For more information, see [DHCP Options
Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the Amazon VPC User Guide.

The security group attached to the VPC endpoint must allow incoming connections on
port 443 from the private subnet of the Amazon VPC.

## Create an interface endpoint for AWS Cloud Map

You can create an interface endpoint for AWS Cloud Map using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

Create an interface endpoint for AWS Cloud Map using the following service names:

###### Note

`DiscoverInstances` API won't be available over these two
endpoints.

```
com.amazonaws.`region`.servicediscovery
```

```
com.amazonaws.`region`.servicediscovery-fips
```

Create an interface endpoint for AWS Cloud Map data plane to access the
`DiscoverInstances` API using the following service names:

```
com.amazonaws.`region`.data-servicediscovery
```

```
com.amazonaws.`region`.data-servicediscovery-fips
```

###### Note

You'll need to disable host prefix injection when you call
`DiscoverInstances` with the regional or zonal VPCE DNS names for
data plane endpoints. The AWS CLI and AWS SDKs prepend the service endpoint with
various host prefixes when you call each API operation, which produces invalid URLS
when you specify a VPC endpoint.

If you enable private DNS for the interface endpoint, you can make API requests to
AWS Cloud Map using its default Regional DNS name. For example,
`servicediscovery.us-east-1.amazonaws.com`.

VPCE AWS PrivateLink connection is supported in any Region where AWS Cloud Map
is supported; however, a customer needs to check which Availability Zones support VPCE
before defining an endpoint. To find out which Availability Zones are supported with
interface VPC endpoints in a Region, use the [describe-vpc-endpoint-services](../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md "../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md") command or use the AWS Management Console. For example,
the following commands return the availability zones to which you can deploy an AWS Cloud Map
interface VPC endpoints within the US East (Ohio) Region:

```
`aws --region `us-east-2` ec2 describe-vpc-endpoint-services --query 'ServiceDetails[?ServiceName==`com.amazonaws.`us-east-2`.servicediscovery`].AvailabilityZones[]'`
```
