# Upgrade IAM policies to IPv6

AWS Resource Explorer customers use IAM policies to set an allowed range of IP addresses and
prevent any IP addresses outside the configured range from being able to access Resource Explorer
APIs.

The _resource-explorer-2.`region`.api.aws_
domain where Resource Explorer APIs are hosted is being upgraded to support IPv6 in addition to IPv4.

IP address filtering policies that are not updated to handle IPv6 addresses might result
in clients losing access to the resources on the Resource Explorer API domain.

## Customers impacted by upgrade from IPv4 to

IPv6

Customers who are using dual addressing with policies containing
_aws:sourceIp_ are impacted by this upgrade. Dual addressing
means that the network supports both IPv4 and IPv6.

If you are using dual addressing, you must update your IAM policies that are
currently configured with IPv4 format addresses to include IPv6 format addresses.

For help with access issues, contact [Support](https://support.console.aws.amazon.com/support/home/?nc1=f_dr#/case/create "https://support.console.aws.amazon.com/support/home/?nc1=f_dr#/case/create").

###### Note

The following customers are _not_ impacted by
this upgrade:

- Customers who are on _only_ IPv4
  networks.
- Customers who are on _only_ IPv6
  networks.

## What is IPv6?

IPv6 is the next generation IP standard intended to eventually replace IPv4. The
previous version, IPv4, uses a 32-bit addressing scheme to support 4.3 billion devices.
IPv6 instead uses 128-bit addressing to support approximately 340 trillion trillion
trillion (or 2 to the 128th power) devices.

```
2001:cdba:0000:0000:0000:0000:3257:9652
2001:cdba:0:0:0:0:3257:9652
2001:cdba::3257:965
```

## Updating an IAM policy for IPv6

IAM policies are currently used to set an allowed range of IP addresses using the
`aws:SourceIp` filter.

Dual addressing supports both IPv4 and IPV6 traffic. If your network uses dual
addressing, you must ensure that any IAM polices that are used for IP address
filtering are updated to include IPv6 address ranges.

For example, this Amazon S3 bucket policy identifies allowed IPv4 address ranges
`192.0.2.0.*` and `203.0.113.0.*` in the
`Condition` element.

To update this policy, the policy's `Condition` element is updated to
include IPv6 address ranges `2001:DB8:1234:5678::/64` and
`2001:cdba:3257:8593::/64`.

###### Note

DO NOT REMOVE the existing IPv4 addresses because they are needed for backward
compatibility.

```
"Condition": {
            "NotIpAddress": {
                "*aws:SourceIp*": [
                    "*192.0.2.0/24*", <<DO NOT REMOVE existing IPv4 address>>
                    "*203.0.113.0/24*", <<DO NOT REMOVE existing IPv4 address>>
                    "`*2001:DB8:1234:5678::/64*`", <<New IPv6 IP address>>
                    "`*2001:cdba:3257:8593::/64*`" <<New IPv6 IP address>>
                ]
            },
            "Bool": {
                "aws:ViaAWSService": "false"
            }
        }
```

For more information about managing access permissions with IAM, see [Managed policies
and inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _AWS Identity and Access Management User
Guide_.

## Verify your client can support IPv6

Customers using the _resource-explorer-2.{region}.api.aws_ endpoint
are advised to verify if their clients can access other AWS service Endpoints that are
already IPv6 enabled. The following steps describe how to verify those endpoints.

This examples uses Linux and curl version 8.6.0 and uses the [Amazon Athena service
endpoints](../../../general/latest/gr/athena.md "../../../general/latest/gr/athena.md") which has IPv6 enabled endpoints located at the _api.aws
domain_.

###### Note

Switch the AWS Region to the same Region where the client is
located. In this example, we use the US East (N. Virginia) – `us-east-1`
endpoint.

1. Determine if the endpoint resolves with an IPv6 address using the following
   curl command.

```
dig +short AAAA athena.us-east-1.api.aws
2600:1f18:e2f:4e05:1a8a:948e:7c08:d2d6
2600:1f18:e2f:4e03:4a1e:83b0:8823:4ce5
2600:1f18:e2f:4e04:34c3:6e9a:2b0d:dc79
```

2. Determine if the client network can make a connection using IPv6 using the
   following curl command.

```
curl --ipv6 -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: %{response_code}\n" https://athena.us-east-1.api.aws

remote ip: 2600:1f18:e2f:4e05:1a8a:948e:7c08:d2d6
response code: 404
```

If a remote IP was identified **and** the
response code is not `0`, a network connection was successfully made
to the endpoint using IPv6.

If the remote IP is blank or the response code is `0`, the client network
or the network path to the endpoint is IPv4-only. You can verify this configuration with
the following curl command.

```
curl -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: %{response_code}\n" https://athena.us-east-1.api.aws

remote ip: 3.210.103.49
response code: 404
```

If a remote IP was identified **and** the response code
is not `0`, a network connection was successfully made to the endpoint using
IPv4. The remote IP should be an IPv4 address because the operating system should select
the protocol that is valid for the client. If the remote IP is not an IPv4 address, use
the following command to force curl to use IPv4.

```
curl --ipv4 -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: %{response_code}\n" https://athena.us-east-1.api.aws

remote ip: 35.170.237.34
response code: 404
```
