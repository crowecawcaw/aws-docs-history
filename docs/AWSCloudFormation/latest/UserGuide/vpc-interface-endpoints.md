# Access CloudFormation using an interface endpoint

(AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and CloudFormation.
You can access CloudFormation as if it were in your VPC, without the use of an internet gateway,
NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public
IP addresses to access CloudFormation.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface
in each subnet that you enable for the interface endpoint. These are requester-managed
network interfaces that serve as the entry point for traffic destined for CloudFormation.

CloudFormation supports making calls to all of its API actions through the interface
endpoint.

## Considerations for CloudFormation VPC

endpoints

Before you set up an interface endpoint, first make sure you have met the
prerequisites in the [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") topic in the
_AWS PrivateLink Guide_.

The following additional prerequisites and considerations apply when setting up an
interface endpoint for CloudFormation:

- If you have resources within your VPC that must respond to a custom resource
  request or a wait condition, make sure that they have access to the required
  CloudFormation-specific Amazon S3 buckets. CloudFormation has S3 buckets in each Region to
  monitor responses to a [custom
  resource](template-custom-resources.md "template-custom-resources.md") request or a [wait
  condition](using-cfn-waitcondition.md "using-cfn-waitcondition.md"). If a template includes custom resources or wait conditions
  in a VPC, the VPC endpoint policy must allow users to send responses to the
  following buckets:

      + For custom resources, permit traffic to the
       `cloudformation-custom-resource-response-`region``
       bucket. When using custom resources, AWS Region names don't contain
       dashes. For example, `uswest2`.
      + For wait conditions, permit traffic to the
       `cloudformation-waitcondition-`region``
       bucket. When using wait conditions, AWS Region names do contain
       dashes. For example, `us-west-2`.

  If the endpoint policy blocks traffic to these buckets, CloudFormation won't
  receive responses and the stack operation fails. For example, if you have a
  resource in a VPC in the `us-west-2` Region that must respond to a
  wait condition, the resource must be able to send a response to the
  `cloudformation-waitcondition-us-west-2` bucket.

For a list of AWS Regions where CloudFormation is currently available, see the
[AWS CloudFormation endpoints and quotas](../../../general/latest/gr/cfn.md "../../../general/latest/gr/cfn.md") page
in the _Amazon Web Services General Reference_.

- VPC endpoints currently don't support cross-Region requests — ensure
  that you create your endpoint in the same Region in which you plan to issue your
  API calls to CloudFormation.
- VPC endpoints only support Amazon-provided DNS through Route 53. If you want to
  use your own DNS, you can use conditional DNS forwarding. For more information,
  see [DHCP options sets in
  Amazon VPC](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the Amazon VPC User Guide.
- The security group attached to the VPC endpoint must allow incoming
  connections on port 443 from the private subnet of the VPC.

## Creating an interface VPC endpoint for

CloudFormation

You can create a VPC endpoint for CloudFormation using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

Create an interface endpoint for CloudFormation using the following service name:

- com.amazonaws.`region`.cloudformation
  – Creates an endpoint for CloudFormation API operations.

If you enable private DNS for the interface endpoint, you can make API requests to
CloudFormation using its default Regional DNS name. For example,
`cloudformation.us-east-1.amazonaws.com`.

In AWS Regions where FIPS-specific endpoints are supported, you can also create an
interface endpoint for CloudFormation using the following service name:

- com.amazonaws.`region`.cloudformation-fips
  – Creates an endpoint for the CloudFormation API that complies with [Federal Information Processing
  Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

For a complete list of CloudFormation endpoints, see [AWS CloudFormation endpoints and quotas](../../../general/latest/gr/cfn.md "../../../general/latest/gr/cfn.md") in the
_Amazon Web Services General Reference_.

## Creating a VPC endpoint policy for

CloudFormation

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to CloudFormation through the interface
endpoint. To control the access allowed to CloudFormation from your VPC, attach a custom
endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for CloudFormation

actions

The following is an example of an endpoint policy for CloudFormation. When attached to
an endpoint, this policy grants access to the listed CloudFormation actions for all
principals on all resources. The following example denies all users the permission
to create stacks through the VPC endpoint, and allows full access to all other
actions on the CloudFormation service.

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
      "Action": "cloudformation:CreateStack",
      "Effect": "Deny",
      "Principal": "*",
      "Resource": "*"
    }
  ]
}
```
