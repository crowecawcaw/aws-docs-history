# Cloud Control API and interface VPC endpoints

(AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and AWS Cloud Control API.
You can access Cloud Control API as if it were in your VPC, without the use of an internet gateway,
NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP
addresses to access Cloud Control API.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in each
subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for Cloud Control API.

Cloud Control API supports making calls to all of its API actions through the interface
endpoint.

## Considerations for Cloud Control API VPC endpoints

Before you set up an interface VPC endpoint for Cloud Control API, first make sure you have met
the prerequisites in the [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") topic in the
_AWS PrivateLink Guide_.

## Creating an interface VPC endpoint for

Cloud Control API

You can create a VPC endpoint for Cloud Control API using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

Create an interface endpoint for Cloud Control API using the following service name:

- com.amazonaws.`region`.cloudcontrolapi

If you enable private DNS for the endpoint, you can make API requests to
Cloud Control API using its default DNS name for the Region, for example,
`cloudcontrolapi.us-east-1.amazonaws.com`.

For more information, see [Access an
AWS service using an interface VPC endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for Cloud Control API

You can attach an endpoint policy to your VPC endpoint that controls access to Cloud Control API.
The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Important

VPCE endpoint policy details are not passed to any downstream services invoked by
Cloud Control API for evaluation. Because of this, policies specifying actions or resources that
belong to downstream services are not enforced.

For example, suppose you created an Amazon EC2 instance in a VPC instance with a VPC endpoint
for Cloud Control API in a subnet with no Internet access. Next, you attach the following VPC endpoint
policy to the VPCE:

```
{
  "Statement": [
    {
      "Action": [
        "cloudformation:*",
        "ec2:*",
        "lambda:*"
      ]
      "Effect": "Allow",
      "Principal": "*",
      "Resource": "*"
    }
  ]
}
```

If a user with administrator access then sends a request to access an Amazon S3 bucket in the
instance, no service error would be returned, even though Amazon S3 access is not granted in the
VPCE policy.

###### Example: VPC endpoint policy for Cloud Control API actions

The following is an example of an endpoint policy for Cloud Control API. When attached to an
endpoint, this policy grants access to the listed Cloud Control API actions for all principals on all
resources. The following example denies all users the permission to create resources through
the VPC endpoint, and allows full access to all other actions on the Cloud Control API service.

```
{
  "Statement": [
    {
      "Action": "cloudformation:*",
      "Effect": "Allow",
      "Principal": "*",
      "Resource": "*"
    },
    {
      "Action": "cloudformation:CreateResource",
      "Effect": "Deny",
      "Principal": "*",
      "Resource": "*"
    }
  ]
}
```

## See also

- [AWS services that
  integrate with AWS PrivateLink](../../../vpc/latest/privatelink/aws-services-privatelink-support.md "../../../vpc/latest/privatelink/aws-services-privatelink-support.md")
