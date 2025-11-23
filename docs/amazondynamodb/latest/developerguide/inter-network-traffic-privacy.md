# Securing DynamoDB connections using VPC endpoints and IAM policies"

Connections are protected both between Amazon DynamoDB and on-premises applications and between
DynamoDB and other AWS resources within the same AWS Region.

## Required policy for endpoints

Amazon DynamoDB provides a [DescribeEndpoints](../APIReference/API_DescribeEndpoints.md "../APIReference/API_DescribeEndpoints.md")
API that enables you to enumerate regional endpoint information. For requests to the public DynamoDB endpoints, the API responds regardless of the
configured DynamoDB IAM policy, even if there is an explicit or implicit deny in the IAM or VPC endpoint policy. This is because DynamoDB intentionally
skips authorization for the `DescribeEndpoints` API.

For requests from a VPC endpoint, both the IAM and Virtual Private Cloud (VPC)
endpoint policies must authorize the `DescribeEndpoints` API call for the requesting Identity and Access Management (IAM) principal(s)
using the IAM `dynamodb:DescribeEndpoints` action. Otherwise, access to the `DescribeEndpoints` API will be denied.

The following is an example of an endpoints policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "dynamodb:DescribeEndpoints",
 "Resource": "*"
 }
 ]
}`

```

## Traffic between service and

on-premises clients and applications

You have two connectivity options between your private network and AWS:

- An AWS Site-to-Site VPN connection. For more information, see
  [What is
  AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") in the _AWS Site-to-Site VPN User Guide_.
- An Direct Connect connection. For more information, see
  [What is
  Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") in the _Direct Connect User Guide_.

Access to DynamoDB via the network is through AWS published APIs. Clients must support
Transport Layer Security (TLS) 1.2. We recommend TLS 1.3. Clients must also
support cipher suites with Perfect Forward Secrecy (PFS), such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern
systems such as Java 7 and later support these modes. Additionally, you must sign
requests using an access key ID and a secret access key that are associated with an
IAM principal, or you can use the
[AWS Security Token Service (STS)](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") to generate temporary
security credentials to sign requests.

## Traffic between AWS

resources in the same Region

An Amazon Virtual Private Cloud (Amazon VPC) endpoint for DynamoDB is a logical entity within a VPC that allows
connectivity only to DynamoDB. The Amazon VPC routes requests to DynamoDB and routes responses back
to the VPC. For more information, see
[VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the
_Amazon VPC User Guide_. For example policies that you can use to
control access from VPC endpoints, see [Using IAM policies to control
access to DynamoDB](../../../vpc/latest/userguide/vpc-endpoints-ddb.md "../../../vpc/latest/userguide/vpc-endpoints-ddb.md").

###### Note

Amazon VPC endpoints are not accessible via AWS Site-to-Site VPN or Direct Connect.
