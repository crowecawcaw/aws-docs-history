# Connect to Amazon Athena using an interface VPC endpoint

You can improve the security posture of your VPC by using an [interface VPC endpoint
(AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") and an [AWS Glue VPC endpoint](../../../glue/latest/dg/vpc-endpoint.md "../../../glue/latest/dg/vpc-endpoint.md") in your Virtual
Private Cloud (VPC). An interface VPC endpoint improves security by giving you control
over what destinations can be reached from inside your VPC. Each VPC endpoint is
represented by one or more [Elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") (ENIs) with private IP addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to Athena without an internet
gateway, NAT device, VPN connection, or Direct Connect connection. The instances in your VPC
don't need public IP addresses to communicate with the Athena API.

To use Athena through your VPC, you must connect from an instance that is inside the
VPC or connect your private network to your VPC by using an Amazon Virtual Private
Network (VPN) or Direct Connect. For information about Amazon VPN, see [VPN connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the
_Amazon Virtual Private Cloud User Guide_. For information about AWS Direct Connect, see
[Creating a connection](../../../directconnect/latest/UserGuide/create-connection.md "../../../directconnect/latest/UserGuide/create-connection.md")
in the _Direct Connect User Guide_.

Athena supports VPC endpoints in all AWS Regions where both [Amazon VPC](../../../general/latest/gr/rande.md#vpc_region "../../../general/latest/gr/rande.md#vpc_region") and [Athena](../../../general/latest/gr/rande.md#athena "../../../general/latest/gr/rande.md#athena") are available.

You can create an interface VPC endpoint to connect to Athena using the AWS Management Console or
AWS Command Line Interface (AWS CLI) commands. For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint").

After you create an interface VPC endpoint, if you enable [private DNS](../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns "../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns")
hostnames for the endpoint, the default Athena endpoint
(https://athena.`Region`.amazonaws.com) resolves to your
VPC endpoint.

If you do not enable private DNS hostnames, Amazon VPC provides a DNS endpoint name that
you can use in the following format:

```
`VPC_Endpoint_ID`.athena.`Region`.vpce.amazonaws.com
```

For more information, see [Interface VPC endpoints (AWS
PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.

Athena supports making calls to all of its [API actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") inside your
VPC.

## Create a VPC endpoint policy for Athena

You can create a policy for Amazon VPC endpoints for Athena to specify restrictions like
the following:

- Principal – The principal that can
  perform actions.
- Actions – The actions that can be
  performed.
- Resources – The resources on which
  actions can be performed.
- Only trusted identities – Use the
  `aws:PrincipalOrgId` condition to restrict access to only
  credentials that are part of your AWS organization. This can help prevent
  access by unintended principals.
- Only trusted resources – Use the
  `aws:ResourceOrgId` condition to prevent access to unintended
  resources.
- Only trusted identities and resources
  – Create a combined policy for a VPC endpoint that helps prevent
  access to unintended principals and resources.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the
_Amazon VPC User Guide_ and [Appendix 2 – VPC endpoint policy examples](../../../whitepapers/latest/building-a-data-perimeter-on-aws/appendix-2-vpc-endpoint-policy-examples.md "../../../whitepapers/latest/building-a-data-perimeter-on-aws/appendix-2-vpc-endpoint-policy-examples.md") in the AWS Whitepaper
_Building a data perimeter on AWS_.

###### Example– VPC endpoint policy

The following example allows requests by organization identities to
organization resources and allows requests by AWS service principals.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRequestsByOrgsIdentitiesToOrgsResources",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "`my-org-id`",
 "aws:ResourceOrgID": "`my-org-id`"
 }
 }
 },
 {
 "Sid": "AllowRequestsByAWSServicePrincipals",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "Bool": {
 "aws:PrincipalIsAWSService": "true"
 }
 }
 }
 ]
}`

```

Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## About VPC endpoints in shared subnets

You can't create, describe, modify, or delete VPC endpoints in subnets that are
shared with you. However, you can use the VPC endpoints in subnets that are shared
with you. For information about VPC sharing, see [Share your VPC with other
accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the _Amazon VPC User Guide_.
