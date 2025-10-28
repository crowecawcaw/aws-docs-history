# Upgrading IAM policies to IPv6

AWS Marketplace customers use IAM policies to set an allowed range of IP addresses and prevent any
IP addresses outside the configured range from being able to access AWS Marketplace resources.

The AWS Marketplace website domain is being upgraded to the IPv6 protocol.

IP address filtering policies that are not updated to handle IPv6 addresses might result in
clients losing access to the resources on AWS Marketplace website.

## Customers impacted by upgrade from IPv4 to IPv6

Customers who are using dual addressing are impacted by this upgrade. Dual addressing
means that the network supports both IPv4 and IPv6.

If you are using dual addressing, you must update your IAM policies that are currently
configured with IPv4 format addresses to include IPv6 format addresses.

For help with access issues, contact [Support](https://support.console.aws.amazon.com/support/home/?nc1=f_dr#/case/create "https://support.console.aws.amazon.com/support/home/?nc1=f_dr#/case/create").

###### Note

The following customers are _not_ impacted by this
upgrade:

- Customers who are on _only_ IPv4 networks.
- Customers who are on _only_ IPv6 networks.

## What is IPv6?

IPv6 is the next generation IP standard intended to eventually replace IPv4. The previous
version, IPv4, uses a 32-bit addressing scheme to support 4.3 billion devices. IPv6 instead
uses 128-bit addressing to support approximately 340 trillion trillion trillion (or 2 to the
128th power) devices.

```
2001:cdba:0000:0000:0000:0000:3257:9652
2001:cdba:0:0:0:0:3257:9652
2001:cdba::3257:965
```

## Updating an IAM policy for IPv6

IAM policies are currently used to set an allowed range of IP addresses using the
`aws:SourceIp` filter.

Dual addressing supports both IPv4 and IPV6 traffic. If your network uses dual addressing,
you must ensure that any IAM polices that are used for IP address filtering are updated to
include IPv6 address ranges.

For example, this IAM identity-based policy identifies allowed IPv4 address CIDR ranges
192.0.2.0/24 and 203.0.113.0/24 in the Condition element.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": "aws-marketplace:*",
 "Resource": "*",
 "Condition": {
 "NotIpAddress": {
 "aws:SourceIp": [
 "192.0.2.0/24",
 "203.0.113.0/24"
 ]
 },
 "Bool": {
 "aws:ViaAWSService": "false"
 }
 }
 }
}`

```

For more information about the IAM identity-based policy example, see [AWS: Denies access to AWS based on the source IP](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md") in the _AWS Identity and Access Management
User Guide_.

To update this policy, the policy's `Condition` element is updated to include
IPv6 address ranges `2001:DB8:1234:5678::/64` and
`2001:cdba:3257:8593::/64`.

###### Note

DO NOT REMOVE the existing IPv4 addresses because they are needed for backward
compatibility.

```
"Condition": {
            "NotIpAddress": {
                "aws:SourceIp": [
                    "192.0.2.0/24", <<DO NOT remove existing IPv4 address>>
                    "203.0.113.0/24", <<DO NOT remove existing IPv4 address>>
                    "`2001:DB8:1234:5678::/64`", <<New IPv6 IP address>>
                    "`2001:cdba:3257:8593::/64`" <<New IPv6 IP address>>
                ]
            },
            "Bool": {
                "aws:ViaAWSService": "false"
            }
        }
```

For more information about managing access permissions with IAM, see [Managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _AWS Identity and Access Management User
Guide_.

## Testing network after update from IPv4 to IPv6

After you update your IAM policies to the IPv6 format, you can test whether your network
is accessing the IPv6 endpoint and the AWS Marketplace website functionality.

###### Topics

- [Testing network with Linux/Unix or Mac OS X](#testing-linux "#testing-linux")
- [Testing network with Windows 7 or Windows 10](#testing-widows "#testing-widows")
- [Testing the AWS Marketplace website](#testing-website "#testing-website")

### Testing network with Linux/Unix or Mac OS X

If you are using Linux/Unix or Mac OS X, you can test whether your network is accessing
the IPv6 endpoint by using the following curl command.

```
curl -v -s -o /dev/null http://ipv6.ec2-reachability.amazonaws.com/
```

For example, if you are connected over IPv6, the connected IP address displays the
following information.

```

* About to connect() to aws.amazon.com port 443 (#0)
*   Trying IPv6 address... connected
* Connected to aws.amazon.com (IPv6 address) port 443 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.18.1 (x86_64-unknown-linux-gnu) libcurl/7.18.1 OpenSSL/1.0.1t zlib/1.2.3
> Host: aws.amazon.com
```

### Testing network with Windows 7 or Windows 10

If you are using Windows 7 or Windows 10, you can test whether your network can access a
dual-stack endpoint over IPv6 or IPv4. Use the `ping` command as shown in the
following example.

```
ping aws.amazon.com
```

This command returns IPv6 addresses if you are accessing an endpoint over IPv6.

### Testing the AWS Marketplace website

Testing the AWS Marketplace website functionality after the update depends primarily on how your
policy is written and what it is used for. In general, you should verify that the
functionality specified in the policy works as intended.

The following scenarios can help you get started with testing the AWS Marketplace website
functionality.

As a buyer on the AWS Marketplace website, test whether you can do the following tasks:

- Subscribe to an AWS Marketplace product.
- Configure an AWS Marketplace product.
- Launch or fulfill an AWS Marketplace product.

As a seller on the AWS Marketplace website, test whether you can do the following tasks:

- Manage your existing AWS Marketplace products.
- Create an AWS Marketplace product.
