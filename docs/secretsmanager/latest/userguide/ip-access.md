# Control API access with IAM policies

If you use IAM policies to control access to AWS services based on IP addresses, you
might need to update your policies to include IPv6 address ranges. This guide explains the
differences between IPv4 and IPv6 and describes how to update your IAM policies to support
both protocols. Implementing these changes helps you maintain secure access to your AWS
resources while supporting IPv6.

## What is IPv6?

IPv6 is the next generation IP standard intended to eventually replace IPv4. The
previous version, IPv4, uses a 32-bit addressing scheme to support 4.3 billion devices.
IPv6 instead uses 128-bit addressing to support approximately 340 trillion trillion
trillion (or 2 to the 128th power) devices.

For more information, see the [VPC IPv6
web page](https://aws.amazon.com/vpc/ipv6/ "https://aws.amazon.com/vpc/ipv6/").

These are examples of IPv6 addresses:

```
2001:cdba:0000:0000:0000:0000:3257:9652 # This is a full, unabbreviated IPv6 address.
2001:cdba:0:0:0:0:3257:9652             # The same address with leading zeros in each group omitted
2001:cdba::3257:965                     # A compressed version of the same address.
```

## IAM dual-stack (IPv4 and IPv6) policies

You can use IAM policies to control access to Secrets Manager APIs and prevent IP
addresses outside the configured range from accessing Secrets Manager APIs.

The _secretsmanager.{region}.amazonaws.com_ dual-stack endpoint for
Secrets Manager APIs supports both IPv6 and IPv4.

If you need to support both IPv4 and IPv6, update your IP address filtering policies
to handle IPv6 addresses. Otherwise, you might not be able to connect to Secrets Manager over
IPv6.

### Who should make this change?

This change affects you if you use dual addressing with policies that contain
`aws:sourceIp`. _Dual addressing_
means that the network supports both IPv4 and IPv6.

If you use dual addressing, update your IAM policies that currently use IPv4
format addresses to include IPv6 format addresses.

### Who should not make this change?

This change doesn't affect you if you _only_ use
IPv4 networks.

## Adding IPv6 to an IAM policy

IAM policies use the `aws:SourceIp` condition key to control access from
specific IP addresses. If your network uses dual addressing (IPv4 and IPv6), update your
IAM policies to include IPv6 address ranges.

In the `Condition` element of your policies, use the `IpAddress`
and `NotIpAddress` operators for IP address conditions. Don't use string
operators, as they can't handle the various valid IPv6 address formats.

These examples use `aws:SourceIp`. For VPCs, use
`aws:VpcSourceIp` instead.

The following is the [Denies
access to AWS based on the source IP](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md") reference policy from the
_IAM User Guide_. The `NotIpAddress` in the `Condition` element to lists two IPv4 address ranges, `192.0.2.0/24`
and `203.0.113.0/24`, which will be denied access to the API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "NotIpAddress": {
 "aws:SourceIp": [
 "`192.0.2.0/24`",
 "`203.0.113.0/24`"
 ]
 },
 "Bool": {
 "aws:ViaAWSService": "false"
 }
 }
 }
}`

```

To update this policy, change the `Condition` element to include the IPv6
address ranges `2001:DB8:1234:5678::/64` and
`2001:cdba:3257:8593::/64`.

###### Note

Don't remove the existing IPv4 addresses. They're needed for backward
compatibility.

```
"Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": [
                        "192.0.2.0/24", <<DO NOT REMOVE existing IPv4 address>>
                        "203.0.113.0/24", <<DO NOT REMOVE existing IPv4 address>>
                        `"2001:DB8:1234:5678::/64", <<New IPv6 IP address>>
 "2001:cdba:3257:8593::/64" <<New IPv6 IP address>>`
                    ]
                },
                "Bool": {
                    "aws:ViaAWSService": "false"
                }
            }
```

To update this policy for a VPC, use `aws:VpcSourceIp` instead of `aws:SourceIp`:

```
"Condition": {
                "NotIpAddress": {
                    "aws:VpcSourceIp": [
                        "10.0.2.0/24", <<DO NOT REMOVE existing IPv4 address>>
                        "10.0.113.0/24", <<DO NOT REMOVE existing IPv4 address>>
                        `"fc00:DB8:1234:5678::/64", <<New IPv6 IP address>>
 "fc00:cdba:3257:8593::/64" <<New IPv6 IP address>>`
                    ]
                },
                "Bool": {
                    "aws:ViaAWSService": "false"
                }
            }
```

## Verifying your client supports IPv6

If you use the _secretsmanager.{region}.amazonaws.com_ endpoint, verify
that you can connect to it. The following steps describe how to perform the
verification.

This examples uses Linux and curl version 8.6.0 and uses the [AWS Secrets Manager
service](../../../general/latest/gr/secretsmanager.md "../../../general/latest/gr/secretsmanager.md") which has IPv6 enabled endpoints located at the
**amazonaws.com** endpoint.

###### Note

The **secretsmanager.{region}.amazonaws.com** differs from the [typical dual-stack naming convention](../../../general/latest/gr/rande.md#dual-stack-endpoints "../../../general/latest/gr/rande.md#dual-stack-endpoints"). For a full list of Secrets Manager endpoints, see [AWS Secrets Manager endpoints](asm_access.md#endpoints "asm_access.md#endpoints").

Change the AWS Region to the same Region where your service is located. In this example, we use the US East (N. Virginia) – `us-east-1` endpoint.

1. Determine if the endpoint resolves with an IPv6 address using the following
   `dig` command.

```
`$` dig +short AAAA secretsmanager.us-east-1.amazonaws.com

> 2600:1f18:e2f:4e05:1a8a:948e:7c08:c1c3
```

2. Determine if the client network can make an IPv6 connection using the
   following `curl` command. A 404 response code means the connection
   succeeded, while a 0 response code means the connection failed.

```
`$` curl --ipv6 -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: %{response_code}\n" https://secretsmanager.us-east-1.amazonaws.com

> remote ip: 2600:1f18:e2f:4e05:1a8a:948e:7c08:c1c3
> response code: 404
```

If a remote IP was identified **and** the response code
is not `0`, a network connection was successfully made to the endpoint using
IPv6. The remote IP should be an IPv6 address because the operating system should select
the protocol that is valid for the client.

If the remote IP is blank or the response code is `0`, the client network
or the network path to the endpoint is IPv4-only. You can verify this configuration with
the following `curl` command.

```
`$` curl -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: %{response_code}\n" https://secretsmanager.us-east-1.amazonaws.com

> remote ip: 3.123.154.250
> response code: 404
```
