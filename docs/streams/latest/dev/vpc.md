# Use Amazon Kinesis Data Streams with interface VPC endpoints

You can use an interface VPC endpoint to prevent traffic between your Amazon VPC and Kinesis Data Streams from
leaving the Amazon network. Interface VPC endpoints don't require an internet gateway, NAT
device, VPN connection, or AWS Direct Connect connection. Interface VPC endpoints are powered by AWS
PrivateLink, an AWS technology that enables private communication between AWS services
using an elastic network interface with private IPs in your Amazon VPC. For more information, see
[Amazon Virtual Private Cloud](../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md "../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md") and [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint").

###### Topics

- [Use interface VPC endpoints for
  Kinesis Data Streams](#using-interface-vpc-endpoints "#using-interface-vpc-endpoints")
- [Control access to VPC endpoints for
  Kinesis Data Streams](#interface-vpc-endpoints-policies "#interface-vpc-endpoints-policies")
- [Availability of VPC endpoint policies for Kinesis Data Streams](#availability "#availability")

## Use interface VPC endpoints for

Kinesis Data Streams

To get started, you do not need to change the settings for your streams, producers, or
consumers. Create an interface VPC endpoint for your Kinesis Data Streams to start traffic flowing from
and to your Amazon VPC resources through the interface VPC endpoint. FIPS-enabled interface
VPC endpoints are available for US Regions. For more information, see [Creating an Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint").

The Amazon Kinesis Producer Library (KPL) and Kinesis Consumer Library
(KCL) call AWS services like Amazon CloudWatch and Amazon DynamoDB using either public
endpoints or private interface VPC endpoints, whichever are in use. For example, if your
KCL application is running in a VPC with DynamoDB interface with VPC endpoints
enabled, calls between DynamoDB and your KCL application flow through the
interface VPC endpoint.

## Control access to VPC endpoints for

Kinesis Data Streams

VPC endpoint policies let you control access by either attaching a policy to a VPC
endpoint or by using additional fields in a policy that is attached to an IAM user,
group, or role to restrict access to occur only through the specified VPC endpoint. Use
these policies to restrict access to specific streams to a specified VPC endpoint when
using them together with the IAM policies to grant only access to Kinesis data stream
actions through the specified VPC endpoint.

The following are example endpoint policies for accessing Kinesis data streams.

- **VPC policy example: read-only access** - this
  sample policy can be attached to a VPC endpoint. (For more information, see
  [Controlling Access to Amazon VPC Resources](../../../vpc/latest/userguide/VPC_IAM.md "../../../vpc/latest/userguide/VPC_IAM.md")). It restricts actions
  to only listing and describing a Kinesis data stream through the VPC endpoint to
  which it is attached.

```

{
  "Statement": [
    {
      "Sid": "ReadOnly",
      "Principal": "*",
      "Action": [
        "kinesis:List*",
        "kinesis:Describe*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}

```

- **VPC policy example: restrict access to a specific Kinesis
  data stream** - this sample policy can be attached to a VPC
  endpoint. It restricts access to a specific data stream through the VPC endpoint
  to which it is attached.

```

{
  "Statement": [
    {
      "Sid": "AccessToSpecificDataStream",
      "Principal": "*",
      "Action": "kinesis:*",
      "Effect": "Allow",
      "Resource": "arn:aws:kinesis:us-east-1:123456789012:stream/MyStream"
    }
  ]
}

```

- **IAM policy example: restrict access to a specific stream
  from a specific VPC endpoint only** - this sample policy can be
  attached to an IAM user, role, or group. It restricts access to a specified
  Kinesis data stream to occur only from a specified VPC endpoint.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessFromSpecificEndpoint",
 "Action": "kinesis:*",
 "Effect": "Deny",
 "Resource": "arn:aws:kinesis:us-east-1:123456789012:stream/MyStream",
 "Condition": { "StringNotEquals" : { "aws:sourceVpce": "vpce-11aa22bb" } }
 }
 ]
}`

```

## Availability of VPC endpoint policies for Kinesis Data Streams

Kinesis Data Streams interface VPC endpoints with policies are supported in the following Regions:

- Europe (Paris)
- Europe (Ireland)
- US East (N. Virginia)
- Europe (Stockholm)
- US East (Ohio)
- Europe (Frankfurt)
- South America (São Paulo)
- Europe (London)
- Asia Pacific (Tokyo)
- US West (N. California)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- China (Beijing)
- China (Ningxia)
- Asia Pacific (Hong Kong)
- Middle East (Bahrain)
- Middle East (UAE)
- Europe (Milan)
- Africa (Cape Town)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Canada (Central)
- US West (Oregon) except usw2-az4
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
- Asia Pacific (Osaka)
- Europe (Zurich)
- Asia Pacific (Hyderabad)
