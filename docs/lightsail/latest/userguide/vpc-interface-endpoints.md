# Access Amazon Lightsail using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
Amazon Lightsail. You can access Amazon Lightsail as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or Direct Connect connection.
Instances in your VPC don't need public IP addresses to access Amazon Lightsail.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in
each subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for Amazon Lightsail.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for Amazon Lightsail

Before you set up an interface endpoint for Amazon Lightsail, you must have a virtual private
cloud (VPC) created. For more information, see [Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") in the
_Amazon Virtual Private Cloud User Guide_. Additionally, review the [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

Amazon Lightsail supports making calls to all of its API actions through the interface
endpoint. For more information on the API actions available for Lightsail, see the
[Amazon Lightsail API
reference](../../2016-11-28/api-reference/API_Operations.md "../../2016-11-28/api-reference/API_Operations.md").

## Create an interface endpoint for Amazon Lightsail

You can create an interface endpoint for Amazon Lightsail using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for Amazon Lightsail using the following service name:

```
com.amazonaws.`region`.lightsail
```

If you enable private DNS for the interface endpoint, you can make API requests to
Amazon Lightsail using its default Regional DNS name. For example,
`lightsail.us-east-1.amazonaws.com`. For the Region codes that you can
use, see [Regions and
Availability Zones for Lightsail](understanding-regions-and-availability-zones-in-amazon-lightsail.md "understanding-regions-and-availability-zones-in-amazon-lightsail.md").

## AWS CLI examples

To access Lightsail using the interface endpoints, use the `--region` and
`--endpoint-url` parameters with your AWS CLI commands. For a list of
operations that you can perform in Lightsail, see [Actions](../../2016-11-28/api-reference/API_Operations.md "../../2016-11-28/api-reference/API_Operations.md") in the
_Amazon Lightsail API Reference_.

In the following examples, replace AWS Region
`us-east-1` and DNS name of the VPC endpoint
ID
`vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com`
with your own information.

###### Example: Use an endpoint URL to list Lightsail instances

The following example lists your instances using an interface endpoint.

```
aws lightsail get-instances --region `us-east-1` --endpoint-url https://`vpce-1a2b3c4d-5e6f`.lightsail.`us-east-1`.vpce.amazonaws.com
```

###### Example: Use an endpoint URL to list Lightsail disks

The following example lists your disks using an interface endpoint.

```
aws lightsail get-disks --region `us-east-1` --endpoint-url https://`vpce-1a2b3c4d-5e6f`.lightsail.`us-east-1`.vpce.amazonaws.com
```

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to Amazon Lightsail through the interface endpoint.
To control the access allowed to Amazon Lightsail from your VPC, attach a custom endpoint policy
to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for Amazon Lightsail actions

The following is an example of a custom endpoint policy. When you attach this
policy to your interface endpoint, it denies everyone permission to delete block
storage disks in Lightsail through the endpoint and grants everyone permission to
perform all other Lightsail actions.

```
{
  "Statement": [
    {
      "Action": "lightsail:*",
      "Effect": "Allow",
      "Principal": "*",
      "Resource": "*"
    },
    {
      "Action": "lightsail:DeleteDisk",
      "Effect": "Deny",
      "Principal": "*",
      "Resource": "*"
    }
  ]
}
```
