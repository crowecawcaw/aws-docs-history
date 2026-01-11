# AWS Transform custom and interface endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and AWS Transform custom by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access AWS Transform custom services without an internet gateway, NAT device, VPN connection, or
Direct Connect connection. Traffic between your VPC and AWS Transform custom does not leave the Amazon
network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

###### Note

- AWS PrivateLink integration with AWS Transform custom is only available in the US East (N. Virginia) region.
- You must enable AWS PrivateLink integration for Amazon S3 since AWS Transform custom makes S3 API calls. For detailed instructions, see the [AWS PrivateLink for Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md") documentation. If you encounter S3 access issues while using AWS Transform custom, refer to our [troubleshooting guide](custom-troubleshooting.md#custom-s3-access-issues "custom-troubleshooting.md#custom-s3-access-issues").
- If you are not using AWS PrivateLink Private DNS feature (see [Private DNS](../../../vpc/latest/privatelink/privatelink-access-aws-services.md#interface-endpoint-private-dns "../../../vpc/latest/privatelink/privatelink-access-aws-services.md#interface-endpoint-private-dns")), you must:
  - Configure routing to VPC interface endpoints (see the [Routing to VPC interface endpoints](../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md "../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md") documentation)
  - Set the `ATX_CUSTOM_ENDPOINT` environment variable to specify your custom domain, for example:

  ```
  ATX_CUSTOM_ENDPOINT=https://transform-custom.us-east-1.api.aws atx
  ```

## Considerations for AWS Transform custom VPC

endpoints

Before you set up an interface VPC endpoint for AWS Transform custom, ensure that you review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

AWS Transform custom supports making calls to all of its API actions through the interface
endpoint.

## Prerequisites

Before you begin any of the procedures below, ensure that you have the
following:

- An AWS account with appropriate permissions to create and configure
  resources.
- A VPC already created in your AWS account.
- Familiarity with AWS services, especially Amazon VPC and AWS Transform custom.

## Creating an interface VPC endpoint for AWS Transform custom

You can create a VPC endpoint for the AWS Transform custom service using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface
endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create the following VPC endpoints for AWS Transform custom using this service name:

- com.amazonaws.`region`.transform-custom

Replace `region` with AWS Region where you desire to use AWS Transform custom CLI,
for example, _com.amazonaws.us-east-1.transform-custom_.

For more information, see [Accessing a
service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

AWS Transform custom

You can attach an endpoint policy to your VPC endpoint that controls access to
AWS Transform custom. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for AWS Transform custom actions

The following is an example of an endpoint policy for AWS Transform custom. When attached to
an endpoint, this policy grants access to the listed AWS Transform custom actions for all
principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "transform-custom:*"
         ],
         "Resource":"*"
      }
   ]
}
```

## Using an on-premises computer to connect to a

AWS Transform custom endpoint

This section describes the process of using an on-premises computer to connect to
AWS Transform custom through a AWS PrivateLink endpoint in your AWS VPC.

1. [Create a VPN
   connection between your on-premises device and your VPC.](../../../vpn/latest/clientvpn-user/client-vpn-user-what-is.md "../../../vpn/latest/clientvpn-user/client-vpn-user-what-is.md")
2. [Create an interface VPC endpoint for
   AWS Transform custom.](#vpc-interface-endpoints-transform-custom-create "#vpc-interface-endpoints-transform-custom-create")
3. [Set up an inbound Amazon Route 53 endpoint.](../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md "../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md") This will enable you to use
   the DNS name of your AWS Transform custom endpoint from your on-premises device.
