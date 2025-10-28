# Accessing Macie with an interface endpoint

(AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your virtual private
cloud (VPC) and Amazon Macie. You can access Macie as if it were in your VPC, without the use
of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in
your VPC don't need public IP addresses to access Macie.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface
in each subnet that you enable for the interface endpoint. These are requester-managed
network interfaces that serve as the entry point for traffic destined for Macie.

For more information, see [Access AWS services
through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the
_AWS PrivateLink Guide_.

###### Topics

- [Considerations for Macie interface endpoints](#vpc-endpoint-considerations "#vpc-endpoint-considerations")
- [Creating an interface endpoint for Macie](#vpc-endpoint-create "#vpc-endpoint-create")
- [Creating an endpoint policy for Macie](#vpc-endpoint-policy "#vpc-endpoint-policy")

## Considerations for Macie interface

endpoints

Amazon Macie supports interface endpoints in all the AWS Regions where it's currently
available. For a list of these Regions, see [Amazon Macie endpoints and quotas](../../../general/latest/gr/macie.md "../../../general/latest/gr/macie.md") in the _AWS General Reference_. Macie supports making calls to all of its API operations
through interface endpoints.

If you create an interface endpoint for Macie, consider doing the same for other
AWS services that integrate with Macie and with AWS PrivateLink, such as Amazon EventBridge and
AWS Security Hub. Macie and those services can then use the interface endpoints for the
integration. For example, if you create an interface endpoint for Macie and an interface
endpoint for Security Hub, Macie can use its interface endpoint when it publishes findings to
Security Hub. Security Hub can use its interface endpoint when it receives the findings. For
information about supported services, see [AWS services
that integrate with AWS PrivateLink](../../../vpc/latest/privatelink/aws-services-privatelink-support.md "../../../vpc/latest/privatelink/aws-services-privatelink-support.md") in the
_AWS PrivateLink Guide_.

## Creating an interface endpoint for Macie

You can create an interface endpoint for Amazon Macie by using the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

When you create an interface endpoint for Macie, use the following service
name:

`com.amazonaws.`region`.macie2`

Where `region` is the Region code for the applicable
AWS Region.

If you enable private DNS for the interface endpoint, you can make API requests to
Macie using its default Regional DNS name, for example,
`macie2.us-east-1.amazonaws.com` for the US East (N. Virginia) Region.

## Creating an endpoint policy for Macie

An _endpoint policy_ is an AWS Identity and Access Management (IAM) resource that
you can attach to an interface endpoint. The default endpoint policy allows full access
to Amazon Macie through the interface endpoint. To control the access allowed to Macie from
your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

It's a separate policy for controlling access from the endpoint to the specified service.
For more information, see [Control
access to VPC endpoints using endpoint policies](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for Macie actions

The following is an example of a custom endpoint policy for Macie. If you attach this
policy to your interface endpoint, it grants access to the listed Macie actions for
all principals on all resources. It allows users connecting to Macie through the VPC
to access findings data by using the Amazon Macie API.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "macie2:GetFindings",
            "macie2:GetFindingStatistics",
            "macie2:ListFindings"
         ],
         "Resource": "*"
      }
   ]
}
```

To also allow users to access findings data or perform other actions by using the Amazon Macie
console, the policy should also grant access to the `macie2:GetMacieSession`
action, for example:

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "macie2:GetMacieSession",
            "macie2:GetFindings",
            "macie2:GetFindingStatistics",
            "macie2:ListFindings"
         ],
         "Resource": "*"
      }
   ]
}
```
