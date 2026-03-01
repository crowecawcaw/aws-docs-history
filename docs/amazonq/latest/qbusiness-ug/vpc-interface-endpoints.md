# Amazon Q Business and interface Amazon VPC endpoints (AWS PrivateLink)

You can establish a private connection between your Amazon VPC and Amazon Q Business by
creating an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink, a
technology that allows you to privately access Amazon Q Business APIs without an
internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances
in your VPC don't need public IP addresses to communicate with Amazon Q Business APIs.
Traffic between your VPC and Amazon Q Business doesn't leave the Amazon
network.

Before you set up an interface VPC endpoint for Amazon Q Business, make sure that
you review the [prerequisites](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
_Amazon VPC User Guide_.

Amazon Q Business currently only supports making API calls from your VPC for Amazon Q Business APIs only. Using your VPC for the web experience user interface is not
supported.

## Creating an interface VPC endpoint for Amazon Q Business

You can create an interface endpoint for Amazon Q Business using either the
Amazon VPC console or the AWS Command Line Interface (AWS CLI).

Create an interface endpoint for Amazon Q Business using the following service
name:

```
aws.api.`region`.qbusiness
```

After you create a VPC endpoint, you can use the following example AWS CLI command that
uses the `endpoint-url` parameter to specify an interface endpoint to the
Amazon Q Business API:

```
aws qbusiness list-applications --endpoint-url https://`VPC endpoint`
```

`VPC endpoint` is the DNS name generated when the interface
endpoint is created. This name includes the VPC endpoint ID and the Amazon Q Business service name, which includes the region. For example,
`vpce-1234-adbcdef-us-west-2a.qbusiness.us-west-2.vpce.amazonaws.com`.

If you enable private DNS for the endpoint, you can make API requests to Amazon Q Business using its default DNS name for the region. For example,
`qbusiness.us-west-2.api.aws`.

For more information, see [Creating an interface
endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _Amazon VPC User Guide_.

## Creating a VPC endpoint policy for Amazon Q Business

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to Amazon Q Business through the
interface endpoint. To control the access allowed to Amazon Q Business from your
VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals/authorized users who can perform actions (AWS accounts,
  IAM users, and IAM roles)
- The actions that can be performed
- The resources on which the actions can be performed.

For more information, see [Controlling access to
services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User
Guide_.

###### Example: VPC endpoint policy for Amazon Q Business actions

The following is an example of an endpoint policy for Amazon Q Business.
When attached to an endpoint, this policy grants access to all available Amazon Q Business actions for all principals/authorized users on all
resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "qbusiness:*"
         ],
         "Resource":"*"
      }
   ]
}
```
